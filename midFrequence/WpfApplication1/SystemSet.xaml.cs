using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.Xml.Linq;

namespace midFrequence
{
    /// <summary>
    /// SystemSet.xaml 的交互逻辑
    /// </summary>
    public partial class SystemSet : Window
    {
        MainWindow m = (MainWindow)Application.Current.MainWindow;
        private XDocument xdoc;//config.xml
        private System.Windows.Controls.TextBox selText = new TextBox();

        public SystemSet()
        {
            InitializeComponent();
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            xdoc = XDocument.Load(Environment.CurrentDirectory + "\\Config.xml");
            XElement xroot = xdoc.Element("root");
            string GetPara = xroot.Element("Config").Element("SaveLogMonth").Value;
            cmbPeriod.Text = GetPara;
            GetPara = xroot.Element("Config").Element("CmdInterval").Value;
                txtcmdInterval.Text = GetPara;
            GetPara = xroot.Element("Config").Element("OptLogInterval").Value;
                txtlogInterval.Text = GetPara;
            GetPara = xroot.Element("Port").Element("PortName").Value;
                cmbPORT.Text = GetPara;
            GetPara = xroot.Element("Port").Element("BaudRate").Value;
                cmbBAUT.Text = GetPara; 
            GetPara = xroot.Element("PARAMN").Element("RS").Value;
                txtRS.Text = GetPara;
            GetPara = xroot.Element("PARAMN").Element("FS").Value;
                txtFS.Text = GetPara;
            GetPara = xroot.Element("PARAMN").Element("ZDL").Value;
                txtZDL.Text = GetPara;
            GetPara = xroot.Element("PARAMN").Element("ZDY").Value;
                txtZDY.Text = GetPara;
            GetPara = xroot.Element("PARAMN").Element("TX").Value;
                txtTXZBB.Text = GetPara;
            GetPara = xroot.Element("PARAMN").Element("DT").Value;
                txtDTZBB.Text = GetPara;
            GetPara = xroot.Element("PARAMN").Element("TFD").Value;
                txtTFD.Text = GetPara;
            GetPara = xroot.Element("PARAMN").Element("Z22").Value;
                txtZ22V.Text = GetPara;
            GetPara = xroot.Element("PARAMN").Element("F22").Value;
                txtF22V.Text = GetPara;
            GetPara = xroot.Element("PARAMN").Element("Z8").Value;
                txtZ8V.Text = GetPara;
            GetPara = xroot.Element("PARAMN").Element("F8").Value;
                txtF8V.Text = GetPara;
            GetPara = xroot.Element("PARAMN").Element("SPTD").Value;
                txtSPTD.Text = GetPara;
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {
            //Single sel_ProgV;

            //if (selText.Tag == null) return;
            if (selText.Text == "") selText.Text = "0";

            //屏蔽中文输入和非法字符粘贴输入
            TextBox textBox = sender as TextBox;
            TextChange[] change = new TextChange[e.Changes.Count];
            e.Changes.CopyTo(change, 0);
            int offset = change[0].Offset;
            if (change[0].AddedLength > 0)
            {
                float num = 0;
                if (!float.TryParse(textBox.Text, out num))
                {
                    textBox.Text = textBox.Text.Remove(offset, change[0].AddedLength);
                    textBox.Select(offset, 0);
                }
            }
        }

        private void TextBox_GotFocus(object sender, RoutedEventArgs e)
        {
            selText.SelectAll();
            selText.PreviewMouseDown -= new System.Windows.Input.MouseButtonEventHandler(TextBox_PreviewMouseDown);
        }
        private void TextBox_PreviewMouseDown(object sender, System.Windows.Input.MouseButtonEventArgs e)
        {
            //if (selText.Tag != null)
            selText.PreviewMouseDown += new System.Windows.Input.MouseButtonEventHandler(TextBox_PreviewMouseDown);

            SolidColorBrush sb1 = new SolidColorBrush(Colors.Black);
            selText.Background = sb1;
            SolidColorBrush sb2 = new SolidColorBrush(Colors.Lime);
            selText.Foreground = sb2;
            selText = (TextBox)sender;
            //selValue = Single.Parse(selText.Text);
            SolidColorBrush sb3 = new SolidColorBrush(Colors.White);
            selText.Background = sb3;
            SolidColorBrush sb4 = new SolidColorBrush(Colors.Black);
            selText.Foreground = sb4;

            selText.Focus();
            e.Handled = true;
        }

        private void TextBox_PreviewTextInput(object sender, System.Windows.Input.TextCompositionEventArgs e)
        {
            char x = Convert.ToChar(e.Text.Substring(0, 1));
            int m = Convert.ToInt32(x);
            if ((m > 57) || (m < 48)) { e.Handled = true; return; }
            string xx = x.ToString();

            Single k;
            if (selText.SelectionLength > 0)
                k = Single.Parse(xx);
            else
            {
                string p = selText.Text.Insert(selText.SelectionStart, xx);
                k = Single.Parse(p);
            }

            //selValue = k;
            selText.SelectionStart = selText.Text.Length;
            e.Handled = true;
        }

        private void btnNUM_Click(object sender, RoutedEventArgs e)
        {
            //if (selText.Tag == null) return;
            string num = "";

            Button btn = sender as Button;
            if (btn == btnOne) num = "1";
            if (btn == btnTwo) num = "2";
            if (btn == btnThree) num = "3";
            if (btn == btnFour) num = "4";
            if (btn == btnFive) num = "5";
            if (btn == btnSix) num = "6";
            if (btn == btnSeven) num = "7";
            if (btn == btnEight) num = "8";
            if (btn == btnNine) num = "9";
            if (btn == btnZero) num = "0";
            if (btn == btnClear)
            {
                selText.Clear();
                return;
            }

            Single k;
            if (selText.SelectionLength > 0)
                k = Single.Parse(num);
            else
                k = Single.Parse(selText.Text + num);

            selText.Text = k.ToString();
            //selValue = k;
        }

        private void btnOK_Click(object sender, RoutedEventArgs e)
        {
            XElement xroot = xdoc.Element("root");
            xroot.Element("Config").Element("SaveLogMonth").Value = cmbPeriod.Text;
            xroot.Element("Config").Element("CmdInterval").Value = txtcmdInterval.Text;
            xroot.Element("Config").Element("OptLogInterval").Value = txtlogInterval.Text;
            xroot.Element("Port").Element("PortName").Value = cmbPORT.Text;
            xroot.Element("Port").Element("BaudRate").Value = cmbBAUT.Text;
            //xroot.Element("PARATX").Element("RS").Value = Global.paraTX[0].ToString();
            xroot.Element("PARAMN").Element("RS").Value = txtRS.Text;
            xroot.Element("PARAMN").Element("FS").Value = txtFS.Text;
            xroot.Element("PARAMN").Element("ZDL").Value = txtZDL.Text;
            xroot.Element("PARAMN").Element("ZDY").Value = txtZDY.Text;
            xroot.Element("PARAMN").Element("TX").Value = txtTXZBB.Text;
            xroot.Element("PARAMN").Element("DT").Value = txtDTZBB.Text;
            xroot.Element("PARAMN").Element("TFD").Value = txtTFD.Text;
            xroot.Element("PARAMN").Element("Z22").Value = txtZ22V.Text;
            xroot.Element("PARAMN").Element("F22").Value = txtF22V.Text;
            xroot.Element("PARAMN").Element("Z8").Value = txtZ8V.Text;
            xroot.Element("PARAMN").Element("F8").Value = txtF8V.Text;
            xroot.Element("PARAMN").Element("SPTD").Value = txtSPTD.Text;
            xdoc.Save(Environment.CurrentDirectory + "\\Config.xml", SaveOptions.None);
            m.comm.Close();
            m.portName = cmbPORT.Text;
            m.bautRate = int.Parse(cmbBAUT.Text);
            m.initPort();
            MessageBox.Show("保存成功,请重新启动程序");
            this.Close();
        }

        private void default_Click(object sender, RoutedEventArgs e)
        {
            XElement xroot = xdoc.Element("root");
            string GetDefault = xroot.Element("Config").Element("DefaultSaveLogMonth").Value;
            cmbPeriod.Text = GetDefault;
            GetDefault = xroot.Element("Config").Element("DefaultCmdInterval").Value;
            txtcmdInterval.Text = GetDefault;
            GetDefault = xroot.Element("Config").Element("DefaultOptLogInterval").Value;
            txtlogInterval.Text = GetDefault;
            GetDefault = xroot.Element("Port").Element("DefaultPortName").Value;
            cmbPORT.Text = GetDefault;
            GetDefault = xroot.Element("Port").Element("DefaultBaudRate").Value;
            cmbBAUT.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultRS").Value;
            txtRS.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultFS").Value;
            txtFS.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultZDL").Value;
            txtZDL.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultZDY").Value;
            txtZDY.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultTX").Value;
            txtTXZBB.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultDT").Value;
            txtDTZBB.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultTFD").Value;
            txtTFD.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultZ22").Value;
            txtZ22V.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultF22").Value;
            txtF22V.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultZ8").Value;
            txtZ8V.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultF8").Value;
            txtF8V.Text = GetDefault;
            GetDefault = xroot.Element("PARAMN").Element("DefaultSPTD").Value;
            txtSPTD.Text = GetDefault;

            xroot.Element("Config").Element("SaveLogMonth").Value = cmbPeriod.Text;
            xroot.Element("Config").Element("CmdInterval").Value = txtcmdInterval.Text;
            xroot.Element("Config").Element("OptLogInterval").Value = txtlogInterval.Text;
            xroot.Element("Port").Element("PortName").Value = cmbPORT.Text;
            xroot.Element("Port").Element("BaudRate").Value = cmbBAUT.Text;
            //xroot.Element("PARATX").Element("RS").Value = Global.paraTX[0].ToString();
            xroot.Element("PARAMN").Element("RS").Value = txtRS.Text;
            xroot.Element("PARAMN").Element("FS").Value = txtFS.Text;
            xroot.Element("PARAMN").Element("ZDL").Value = txtZDL.Text;
            xroot.Element("PARAMN").Element("ZDY").Value = txtZDY.Text;
            xroot.Element("PARAMN").Element("TX").Value = txtTXZBB.Text;
            xroot.Element("PARAMN").Element("DT").Value = txtDTZBB.Text;
            xroot.Element("PARAMN").Element("TFD").Value = txtTFD.Text;
            xroot.Element("PARAMN").Element("Z22").Value = txtZ22V.Text;
            xroot.Element("PARAMN").Element("F22").Value = txtF22V.Text;
            xroot.Element("PARAMN").Element("Z8").Value = txtZ8V.Text;
            xroot.Element("PARAMN").Element("F8").Value = txtF8V.Text;
            xroot.Element("PARAMN").Element("SPTD").Value = txtSPTD.Text;
            xdoc.Save(Environment.CurrentDirectory + "\\Config.xml", SaveOptions.None);
            m.comm.Close();
            m.portName = cmbPORT.Text;
            m.bautRate = int.Parse(cmbBAUT.Text);
            m.initPort();
            MessageBox.Show("恢复默认成功,请重新启动程序");
        }
        //public void initPort()
        //{
        //    //注册串口
        //    comm = new Comm();
        //    comm.serialPort.PortName = portName;
        //    //波特率
        //    comm.serialPort.BaudRate = bautRate;
        //    //数据位
        //    comm.serialPort.DataBits = 8;
        //    //两个停止位
        //    comm.serialPort.StopBits = System.IO.Ports.StopBits.One;
        //    //无奇偶校验位
        //    comm.serialPort.Parity = System.IO.Ports.Parity.None;
        //    comm.serialPort.ReadTimeout = 1000;
        //    comm.serialPort.WriteTimeout = -1;
        //    comm.Open();
        //    if (comm.IsOpen)
        //    {
        //        comm.DataReceived += new Comm.EventHandle(comm_DataReceived);
        //    }
        //}
    }
}
