using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Threading;
using System.Xml.Linq;

namespace midFrequence
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    /// 

   
     public partial class MainWindow : Window
    {
         Game game1, game2, game3, game4, game5, game6;
        private XDocument xdoc;//set.xml
        private DispatcherTimer ShowTimer,QueryTimer,AddOptLogTimer;
        private MineLog mineLog;
        public Comm comm = null;
        //定时发送查询指令,存储模拟数据记录
        private int queryInterval, AddOptLogInterval;
        public string portName;
        public int bautRate;
        public string btnColorCompare1;
        public string btnColorCompare2; 
        //创建一个数组用于辨别每次设备返回数据,如果一样,则此次返回数据不处理
        byte[] compareBuff = null;
        public MainWindow()
        {
            InitializeComponent();          
          }      
        //页面显示当前时间,定时开关机
        public void ShowCurTimer(object sender, EventArgs e)
        {
            //"星期"+DateTime.Now.DayOfWeek.ToString(("d"))
            //获得年月日
            this.lblDate.Content = DateTime.Now.ToString("yyyy年MM月dd日");   //yyyy年MM月dd日
            //获得星期几
            this.lblDate1.Content = DateTime.Now.ToString("dddd", new System.Globalization.CultureInfo("zh-cn"));
            this.lblDate1.Content += " ";
            //获得时分秒
            this.lblDate1.Content += DateTime.Now.ToString("HH:mm:ss");
            if (comm.IsOpen)
            {
                portTip.Foreground = Brushes.Lime;
                portTip.Content = "串口通讯正常";
                btnColorCompare1 = portTip.Content.ToString();
            }
            else
            {
                portTip.Foreground = Brushes.Red;
                portTip.Content = "串口通讯出错";
                btnColorCompare2 = portTip.Content.ToString();
                btnInvalid();
            }
            if (!btnColorCompare1.Equals(btnColorCompare2) && portTip.Content.ToString().Equals("串口通讯正常"))
            {
                btnColBack();
                btnColorCompare2 = "串口通讯正常";
            }
            AutoOnOff();
        }
        private void btnControl_Click(object sender, RoutedEventArgs e)
        {
            btnColBack();
            Button selBtn = sender as Button;
            if (selBtn == low_power)
            {
                CombineCMD(0x0b, "低功率开机");
                CombineDB.AddSyslog("低功率开机");
            }
            //中功率开机
            if (selBtn == mid_power)
            {
                CombineCMD(0x0a,"中功率开机");
                CombineDB.AddSyslog("中功率开机");
            }
            //高功率开机
            else if (selBtn == high_power)
            {
                CombineCMD(0x0c, "高功率开机");
                CombineDB.AddSyslog("高功率开机");
            }
            //复位
            else if (selBtn == reset)
            {
                CombineCMD(0x0f, "复位");
                CombineDB.AddSyslog("复位");
            }
            //关机
            else if (selBtn == off)
            {
                CombineCMD(0x09, "关机");
                CombineDB.AddSyslog("关机");
            }
            else if (selBtn == exit)
            {
                Environment.Exit(0);
            }
            else if (selBtn == time)
            {
                Timing timeForm = new Timing();
                timeForm.ShowDialog();
            }
            else if (selBtn == set)
            {
                SystemSet setForm = new SystemSet();
                setForm.ShowDialog();
            }
            else if (selBtn == exit)
            {
                Environment.Exit(0);
            }
            else if (selBtn == log)
            {
                Log logForm = new Log();
                logForm.ShowDialog();
            }  
        }
        //PC发指令合并,9关机、10中功率开机、11低功率开机、12高功率开机
        //13升功率开始、20升功率结束、14降功率开始、21降功率结束、15故障复位
        public void CombineCMD(byte cmd ,string cmdMsg)
        {            
            byte[] buff = new byte[7];           
            buff[0] = 0x7E;//帧头
            buff[1] = 0xE7;
            buff[2] = 0x04;//长度
            buff[3] = 0x00;//设备号
            buff[4] = cmd;//指令
            buff[5] = 0x00;//数据
            buff[6] = bccVerify(buff);//校验位
            comm.WritePort(buff, 0, 7);
            mineLog.WriteLogFile(cmdMsg + ",指令为：" + stringCmd(buff));
        }
        // 把指令拼接成16进制字符串,方便输出
        public string stringCmd(byte[] cmd)
        {
            string a = "";
            for (int i = 0; i < cmd.Length; i++)
            {
                a += Convert.ToString(cmd[i] ,16) + " ";
            }
            return a;
        }
        //bbc校验,得到校验位
        public byte bccVerify(byte[] protocol)
        {
            byte bccData =0x00;
            for (int i = 0; i < protocol.Length; i++)
            {
                bccData ^= protocol[i];
            }
            return bccData;
        }

        //按钮颜色归位
        private void btnColBack()
        {
            foreach (var control in forth_grid.Children)
            {
                if (control.GetType().Name == "Button")
                {
                    Button btn = control as Button;
                    btn.Template = (ControlTemplate)this.Resources["CornerButton"];
                }
            }
        }
        //通讯不正常,按钮变灰
        private void btnInvalid()
        {
            foreach (var control in forth_grid.Children)
            {
                if (control.GetType().Name == "Button")
                {
                    Button btn = control as Button;
                    btn.Template = (ControlTemplate)this.Resources["CornerButtonGray"];
                }
            }
        }
        //仪表盘控件类
        public class Game : INotifyPropertyChanged
        {
            private double score;

            public double Score
            {
                get { return score; }
                set
                {
                    score = value;
                    if (PropertyChanged != null)
                    {
                        PropertyChanged(this, new PropertyChangedEventArgs("Score"));
                    }
                }
            }

            public Game(double scr)
            {
                this.Score = scr;
            }
            public event PropertyChangedEventHandler PropertyChanged;
        }

        //串口线程不能直接访问主界面,定义委托
        private delegate void DelegateShowMessage(byte[] msg);
        public void queryStateOrAnalog(object sender, EventArgs e)
        {
                CombineCMD(0x03, "查询模拟量+状态量");
        }
        public void AddOperateLog(object sender, EventArgs e)
        {
            string[] MnRecord = new string[14];
            if (compareBuff != null)
            {
                MnRecord[0] = game3.Score.ToString();
                MnRecord[1] = game4.Score.ToString();
                MnRecord[2] = game2.Score.ToString();
                MnRecord[3] = game1.Score.ToString();
                MnRecord[4] = game5.Score.ToString();
                MnRecord[5] = game6.Score.ToString();
                MnRecord[6] = compareBuff[17].ToString();
                MnRecord[7] = compareBuff[18].ToString();
                MnRecord[8] = compareBuff[19].ToString();
                MnRecord[9] = compareBuff[20].ToString();
                MnRecord[10] = compareBuff[21].ToString();
                MnRecord[11] = compareBuff[22].ToString();
                MnRecord[12] = compareBuff[23].ToString();
                MnRecord[13] = compareBuff[24].ToString();
                CombineDB.AddOptlog(MnRecord);
            }
        }
        
        //委托访问接口
        private void ChangeMainInvoke(byte[] msg)                                      
        {
            DelegateShowMessage changeMainWindow = ChangeMainWindow;
            //this.Dispatcher.Invoke(changeMainWindow,new object[] {msg});
            this.Dispatcher.Invoke(changeMainWindow,msg);
        }
        //串口实时接收数据,只接收,不处理
        void comm_DataReceived(byte[] readBufferTemp)
        {
            ChangeMainInvoke(readBufferTemp);
            //comm.DataReceived += new Comm.EventHandle(comm__DataReceived);
        }
        //要让主线程完成的事情
        private void ChangeMainWindow(byte[] getMsg)                                                 
        {
            int msgLength = getMsg.Length;
            //空闲查询
            if(msgLength == 7 && getMsg[6] ==255 ){

            }
            //状态量查询
            else if (msgLength == 12 && getMsg[11] == 255)
            {
            }
            //模拟量查询
            else if (msgLength == 20 && getMsg[19] == 255)
            {

            }
            //模拟量加状态量
            else if (msgLength == 26 && getMsg[25] == 255)
            {
                if (compareBuff == getMsg)
                {
                    return;
                }
                if (getMsg[25] == 254)
                {
                    return;
                }
                else
                {
                    foreach (var childBorder in statusPicture.Children)
                    {
                        if (childBorder.GetType().Name == "Border")
                        {
                            Border bor = childBorder as Border;
                            bor.Background = Brushes.Gray;
                        }
                    }
                    //模拟量 11-24 字节顺序(0是第一位)  11:输出功率 12:反射功率 13:主电流 14:主电压 15:天线驻波比 16:带通驻波比 17:调幅度    
                    // 页面仪表盘  1:电压 2:电流 3:入射功率 4:反射功率   barControl 入射功率  barControl1 调幅度
                    game1.Score = Math.Round(Convert.ToDouble(getMsg[14]) * gauge1.MaxValue / 255.0,1);
                    game2.Score = Math.Round(Convert.ToDouble(getMsg[13]) * gauge2.MaxValue / 255.0, 1);
                    game3.Score = Math.Round((Convert.ToDouble(getMsg[11] * getMsg[11]) / 65025.0) * gauge3.MaxValue, 1);
                    game4.Score = Math.Round( (Convert.ToDouble(getMsg[12] * getMsg[12])/ 65025.0) * gauge4.MaxValue, 1);
                    game5.Score = Math.Round(Convert.ToDouble(getMsg[15]) * gauge5.MaxValue / 255.0, 1);
                    game6.Score = Math.Round(Convert.ToDouble(getMsg[16]) * gauge6.MaxValue / 255.0, 1);
                    barControl.ChargingProgress = Math.Round(game3.Score / gauge3.MaxValue * 100,1);
                    labelrsgl.Content = game3.Score.ToString()+"KW";
                    barControl1.ChargingProgress = getMsg[17];
                    labeltfd.Content = getMsg[17].ToString() + "%";
                    gaugelable1.Content = Math.Round(game1.Score, 1).ToString();
                    gaugelable2.Content = Math.Round(game2.Score, 1).ToString();
                    gaugelable3.Content = Math.Round(game3.Score, 1).ToString();
                    gaugelable4.Content = Math.Round(game4.Score, 1).ToString();
                    gaugelable5.Content = Math.Round(game5.Score, 1).ToString();
                    gaugelable6.Content = Math.Round(game6.Score, 1).ToString();
                    //状态量
                    for (int j = 5; j <= 10; j++ )
                    {
                        string borderName = "";
                        int msgStateOrder = j - 4;
                        string binaryNum = Convert.ToString(getMsg[j], 2);
                        int numLength = binaryNum.Length;
                        if(numLength<8){
                            for (int k = 0; k < 8 - numLength; k++)
                            {
                                binaryNum = "0" + binaryNum;
                            }
                        }
                        char[] binaryNumArray = binaryNum.ToCharArray();
                        for(int n = 0 ;n < binaryNumArray.Length;n++) 
                        {
                            borderName = "a" + msgStateOrder.ToString() + "0" + n.ToString() + "a";
                            Border border = this.FindName(borderName) as Border;
                            if (binaryNumArray[n].ToString().Equals("1"))
                            {
                                if (border != null)
                                {
                                    border.Background = Brushes.Lime;
                                }
                            }
                            else if(binaryNumArray[n].ToString().Equals("0")){
                                if (border != null)
                                {
                                    border.Background = Brushes.Red;
                                }
                            }
                            else
                            {
                                if (borderName.Equals("a300a"))
                                {
                                    mid_power.Template = (ControlTemplate)this.Resources["CornerButtonGray"];
                                }
                                else if (borderName.Equals("a302a"))
                                {
                                    high_power.Template = (ControlTemplate)this.Resources["CornerButtonGray"];
                                }
                                else if (borderName.Equals("a207a"))
                                {
                                    //low_power.Template = (ControlTemplate)this.Resources["CornerButtonGray"];
                                }
                                else if (borderName.Equals("a402a"))
                                {
                                    off.Template = (ControlTemplate)this.Resources["CornerButtonRed"];
                                }
                                else
                                {
                                    //MessageBox.Show("设备返回状态量数据第" + msgStateOrder.ToString() + "个字节数有误,系统未找到状态灯,错误字节编号:" + borderName.Replace("a", ""));
                                }

                            }
                        }
                        //IsDataOff = true;
                    }
                    //数组赋值
                    compareBuff = getMsg;
                }
            }
            else
            {
                MessageBox.Show("发射机返回数据有误");
            }                        
        }
        private void Window_Initialized(object sender, EventArgs e)
        {
            GetConfig();
            CombineDB.Connectstring = "Data Source=" + Environment.CurrentDirectory + "\\midFrequence.db";
            CombineDB.ClearOldRecord();
            initPort();
            mineLog = new MineLog();
            InitGauge();

        }
        public void Window_Loaded(object sender, RoutedEventArgs e)
        {
            queryTimer(queryInterval, AddOptLogInterval);
        }
        //定时器
        public void queryTimer(int interval, int interval2)
        {
            ////定时发指令，毫秒
            //QueryTimer = new System.Windows.Threading.DispatcherTimer();
            //QueryTimer.Tick += new EventHandler(queryStateOrAnalog);
            //QueryTimer.Interval = new TimeSpan(0, 0, 0, 0, interval);
            //QueryTimer.Start();
            //显示时间,定时开关机
            ShowTimer = new System.Windows.Threading.DispatcherTimer();
            ShowTimer.Tick += new EventHandler(ShowCurTimer);
            ShowTimer.Interval = new TimeSpan(0, 0, 0, 1, 0);
            ShowTimer.Start();
            //定时存储操作记录，分钟
            AddOptLogTimer = new System.Windows.Threading.DispatcherTimer();
            AddOptLogTimer.Tick += new EventHandler(AddOperateLog);
            AddOptLogTimer.Interval = new TimeSpan(0, 0, interval2, 0, 0);
            AddOptLogTimer.Start();
        }

         //初始化端口
        public void initPort()
        {
            //注册串口
            comm = new Comm();
            comm.serialPort.PortName = portName;
            //波特率
            comm.serialPort.BaudRate = bautRate;
            //数据位
            comm.serialPort.DataBits = 8;
            //两个停止位
            comm.serialPort.StopBits = System.IO.Ports.StopBits.One;
            //无奇偶校验位
            comm.serialPort.Parity = System.IO.Ports.Parity.None;
            comm.serialPort.ReadTimeout = 1000;
            comm.serialPort.WriteTimeout = -1;
            comm.Open();
            if (comm.IsOpen)
            {                
                comm.DataReceived += new Comm.EventHandle(comm_DataReceived);
            }
        }
        //初始化仪表盘
        public void InitGauge()
        {
            game1 = new Game(0);
            game2 = new Game(0);
            game3 = new Game(0);
            game4 = new Game(0);
            game5 = new Game(0);
            game6 = new Game(0);
            this.gauge1.DataContext = game1;
            this.gauge2.DataContext = game2;
            this.gauge3.DataContext = game3;
            this.gauge4.DataContext = game4;
            this.gauge5.DataContext = game5;
            this.gauge6.DataContext = game5;
        }
        private void GetConfig()
        {
            xdoc = XDocument.Load(Environment.CurrentDirectory + "\\Config.xml");
            XElement xroot = xdoc.Element("root");
            Global.TimingEnable = xroot.Element("TIMING").Element("TimingOnOff").Value == "1";
            Global.ExeTimingSet = Global.GetNewTimingSet();
            CombineDB.SaveLogMonth = int.Parse(xroot.Element("Config").Element("SaveLogMonth").Value);
            queryInterval = int.Parse(xroot.Element("Config").Element("CmdInterval").Value);
            AddOptLogInterval = int.Parse(xroot.Element("Config").Element("OptLogInterval").Value);
            portName = xroot.Element("Port").Element("PortName").Value;//
            bautRate = int.Parse(xroot.Element("Port").Element("BaudRate").Value);
            gauge2.MaxValue = double.Parse(xroot.Element("PARAMN").Element("ZDL").Value);
            gauge1.MaxValue = double.Parse(xroot.Element("PARAMN").Element("ZDY").Value);
            gauge3.MaxValue = double.Parse(xroot.Element("PARAMN").Element("RS").Value);
            gauge4.MaxValue = double.Parse(xroot.Element("PARAMN").Element("FS").Value);
            gauge5.MaxValue = double.Parse(xroot.Element("PARAMN").Element("TX").Value);
            gauge6.MaxValue = double.Parse(xroot.Element("PARAMN").Element("TFD").Value);
        }
         //定时开关机
        private void AutoOnOff()
        {            
            if (Global.TimingEnable)
            {
                if (Global.ExeTimingSet.Enable)
                {
                    if ((Global.ExeTimingSet.Hour == DateTime.Now.Hour) && (Global.ExeTimingSet.Minute == DateTime.Now.Minute))
                    {
                        if (Global.ExeTimingSet.OnOff)
                        {
                            if(Global.ExeTimingSet.OnCmd.Equals("低功率")){
                                CombineCMD(0x0b, "定时低功率开机");
                            }
                            else if (Global.ExeTimingSet.OnCmd.Equals("中功率"))
                            {
                                CombineCMD(0x0a, "定时中功率开机");
                            }
                            else if (Global.ExeTimingSet.OnCmd.Equals("高功率"))
                            {
                                CombineCMD(0x0c, "定时高功率开机");//高功率开机
                            }
                        }
                        else
                        {
                            CombineCMD(0x09, "定时关机");//关机
                        }
                        Global.ExeTimingSet = Global.GetNewTimingSet();
                    }
                }
            }
        }
        //系统关闭时,关闭端口
        private void Window_Closed(object sender, EventArgs e)
        {
            comm.Close();
        }
        private void btn_MouseDown(object sender, MouseButtonEventArgs e)
        {
            Button btn = sender as Button;
            //升功率开始
            if (btn == raise_power)
            {
                // MessageBox.Show("升功率开始");
                raise_power.Template = (ControlTemplate)this.Resources["CornerButtonGreen"];
                CombineCMD(0x0d, "升功率开始");               
                
            }
            //降功率开始
            else if (btn == descend_power)
            {
                //MessageBox.Show("降功率开始");
                descend_power.Template = (ControlTemplate)this.Resources["CornerButtonGreen"];
                CombineCMD(0x0e, "降功率开始");

            }
        }
        private void btn_MouseUp(object sender, MouseButtonEventArgs e)
        {
            Button btn = sender as Button;
            MessageBox.Show("升功率结束");
            //升功率结束
            if (btn == raise_power)
            {
                raise_power.Template = (ControlTemplate)this.Resources["CornerButton"];
                CombineCMD(0x14,"升功率结束");
                CombineCMD(0x14, "升功率结束");
                CombineCMD(0x14, "升功率结束");

            }
            //降功率结束
            else if (btn == descend_power)
            {
                descend_power.Template = (ControlTemplate)this.Resources["CornerButton"];
                CombineCMD(0x15,"降功率结束");
                CombineCMD(0x14, "升功率结束");
                CombineCMD(0x14, "升功率结束");
            }
        }

         //去掉系统边框后,可以拖动窗口,仅测试
        //private void Window_MouseLeftButtonDown(object sender, MouseButtonEventArgs e)
        //{
        //    this.DragMove();
        //}

    }
}
