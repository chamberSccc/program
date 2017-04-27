using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace midFrequence
{
    class Global
    {
        public static bool TimingEnable;
        public static int SaveLogMonth;
        public static int[] paraMN = new int[12];    //发射机模拟量参数
        public struct StrTiming
        {
            public bool Enable;
            public int Hour;
            public int Minute;
            public bool OnOff;//true:On,false:Off
            public string OnCmd;
        }
        public static StrTiming ExeTimingSet = new StrTiming();
        //查找最近的定时开关机设置
        public static StrTiming GetNewTimingSet()
        {
            StrTiming newTiming = new StrTiming();
            StrTiming BigTiming = new StrTiming();//当前时间到23:59分之间最近的时间
            StrTiming SmallTiming = new StrTiming();//0:0分到当前时间最远的时间

            XDocument xdoc = XDocument.Load(Environment.CurrentDirectory + "\\Config.xml");
            XElement xroot = xdoc.Element("root");

            try
            {
                newTiming.Enable = false;
                BigTiming.Hour = 23;
                BigTiming.Minute = 59;
                SmallTiming.Hour = DateTime.Now.Hour;
                SmallTiming.Minute = DateTime.Now.Minute;

                int tempH;
                int tempM;
                int a = 1;
                int b = 5;
                if (DateTime.Now.DayOfWeek.ToString().Equals("Tuesday"))
                {
                        a = 5;
                        b = 9;
                }
                for (int i = a; i < b; i++)
                {//1,00:00,00:00
                    //                    string GetTiming = RegKey.GetValue("Timing" + i.ToString()).ToString();
                    string GetTiming = xroot.Element("TIMING").Element("Timing" + i.ToString()).Value;
                    if (GetTiming.Substring(0, 1) == "1")
                    {
                        //开机
                        tempH = int.Parse(GetTiming.Substring(2, 2));
                        tempM = int.Parse(GetTiming.Substring(5, 2));
                        if ((tempH >= 0) && (tempM >= 0))
                        {
                            if ((tempH == DateTime.Now.Hour) && (tempM > DateTime.Now.Minute))
                            {
                                if (tempM <= BigTiming.Minute)
                                {
                                    BigTiming.Hour = tempH;
                                    BigTiming.Minute = tempM;
                                    BigTiming.Enable = true;
                                    BigTiming.OnOff = true;
                                    BigTiming.OnCmd = xroot.Element("TIMING").Element("OnType" + i.ToString()).Value; 
                                }
                            }
                            if (tempH > DateTime.Now.Hour)
                            {
                                if (tempH < BigTiming.Hour)
                                {
                                    BigTiming.Hour = tempH;
                                    BigTiming.Minute = tempM;
                                    BigTiming.Enable = true;
                                    BigTiming.OnOff = true;
                                    BigTiming.OnCmd = xroot.Element("TIMING").Element("OnType" + i.ToString()).Value; 
                                }
                                if ((tempH == BigTiming.Hour) && (tempM <= BigTiming.Minute))
                                {
                                    BigTiming.Hour = tempH;
                                    BigTiming.Minute = tempM;
                                    BigTiming.Enable = true;
                                    BigTiming.OnOff = true;
                                    BigTiming.OnCmd = xroot.Element("TIMING").Element("OnType" + i.ToString()).Value; 
                                }
                            }

                            if ((tempH == DateTime.Now.Hour) && (tempM < DateTime.Now.Minute))
                            {
                                if (tempM <= SmallTiming.Minute)
                                {
                                    SmallTiming.Hour = tempH;
                                    SmallTiming.Minute = tempM;
                                    SmallTiming.Enable = true;
                                    SmallTiming.OnOff = true;
                                    SmallTiming.OnCmd = xroot.Element("TIMING").Element("OnType" + i.ToString()).Value; 
                                }
                            }
                            if (tempH < DateTime.Now.Hour)
                            {
                                if (tempH < SmallTiming.Hour)
                                {
                                    SmallTiming.Hour = tempH;
                                    SmallTiming.Minute = tempM;
                                    SmallTiming.Enable = true;
                                    SmallTiming.OnOff = true;
                                    SmallTiming.OnCmd = xroot.Element("TIMING").Element("OnType" + i.ToString()).Value; 
                                }
                                if ((tempH == SmallTiming.Hour) && (tempM <= SmallTiming.Minute))
                                {
                                    SmallTiming.Hour = tempH;
                                    SmallTiming.Minute = tempM;
                                    SmallTiming.Enable = true;
                                    SmallTiming.OnOff = true;
                                    SmallTiming.OnCmd = xroot.Element("TIMING").Element("OnType" + i.ToString()).Value; 
                                }
                            }
                        }
                        //关机
                        tempH = int.Parse(GetTiming.Substring(8, 2));
                        tempM = int.Parse(GetTiming.Substring(11, 2));
                        if ((tempH >= 0) && (tempM >= 0))
                        {
                            if ((tempH == DateTime.Now.Hour) && (tempM > DateTime.Now.Minute))
                            {
                                if (tempM <= BigTiming.Minute)
                                {
                                    BigTiming.Hour = tempH;
                                    BigTiming.Minute = tempM;
                                    BigTiming.Enable = true;
                                    BigTiming.OnOff = false;
                                }
                            }
                            if (tempH > DateTime.Now.Hour)
                            {
                                if (tempH < BigTiming.Hour)
                                {
                                    BigTiming.Hour = tempH;
                                    BigTiming.Minute = tempM;
                                    BigTiming.Enable = true;
                                    BigTiming.OnOff = false;
                                }
                                if ((tempH == BigTiming.Hour) && (tempM <= BigTiming.Minute))
                                {
                                    BigTiming.Hour = tempH;
                                    BigTiming.Minute = tempM;
                                    BigTiming.Enable = true;
                                    BigTiming.OnOff = false;
                                }
                            }

                            if ((tempH == DateTime.Now.Hour) && (tempM < DateTime.Now.Minute))
                            {
                                if (tempM <= SmallTiming.Minute)
                                {
                                    SmallTiming.Hour = tempH;
                                    SmallTiming.Minute = tempM;
                                    SmallTiming.Enable = true;
                                    SmallTiming.OnOff = false;
                                }
                            }
                            if (tempH < DateTime.Now.Hour)
                            {
                                if (tempH < SmallTiming.Hour)
                                {
                                    SmallTiming.Hour = tempH;
                                    SmallTiming.Minute = tempM;
                                    SmallTiming.Enable = true;
                                    SmallTiming.OnOff = false;
                                }
                                if ((tempH == SmallTiming.Hour) && (tempM <= SmallTiming.Minute))
                                {
                                    SmallTiming.Hour = tempH;
                                    SmallTiming.Minute = tempM;
                                    SmallTiming.Enable = true;
                                    SmallTiming.OnOff = false;
                                }
                            }
                        }
                    }
                }
            }
            catch
            {
            }
            if (BigTiming.Enable)
                newTiming = BigTiming;
            else if (SmallTiming.Enable)
                newTiming = SmallTiming;
            return newTiming;
        }
    }
}
