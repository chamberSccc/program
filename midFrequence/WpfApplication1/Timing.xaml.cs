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
    /// Timing.xaml 的交互逻辑
    /// </summary>
    public partial class Timing : Window
    {
        private XDocument xdoc;//config.xml
        private System.Windows.Controls.TextBox selText = new TextBox();

        public Timing()
        {
            InitializeComponent();
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            xdoc = XDocument.Load(Environment.CurrentDirectory + "\\Config.xml");
            XElement xroot = xdoc.Element("root");

            chkTimeEnable.IsChecked = xroot.Element("TIMING").Element("TimingOnOff").Value == "1";
            string GetTiming = xroot.Element("TIMING").Element("Timing1").Value;
            chkTime1.IsChecked = GetTiming.Substring(0, 1) == "1";
            txtONH1.Text = GetTiming.Substring(2, 2);
            txtONM1.Text = GetTiming.Substring(5, 2);
            txtOFFH1.Text = GetTiming.Substring(8, 2);
            txtOFFM1.Text = GetTiming.Substring(11, 2);
            GetTiming = xroot.Element("TIMING").Element("Timing2").Value;
            chkTime2.IsChecked = GetTiming.Substring(0, 1) == "1";
            txtONH2.Text = GetTiming.Substring(2, 2);
            txtONM2.Text = GetTiming.Substring(5, 2);
            txtOFFH2.Text = GetTiming.Substring(8, 2);
            txtOFFM2.Text = GetTiming.Substring(11, 2);
            GetTiming = xroot.Element("TIMING").Element("Timing3").Value;
            chkTime3.IsChecked = GetTiming.Substring(0, 1) == "1";
            txtONH3.Text = GetTiming.Substring(2, 2);
            txtONM3.Text = GetTiming.Substring(5, 2);
            txtOFFH3.Text = GetTiming.Substring(8, 2);
            txtOFFM3.Text = GetTiming.Substring(11, 2);
            GetTiming = xroot.Element("TIMING").Element("Timing4").Value;
            chkTime4.IsChecked = GetTiming.Substring(0, 1) == "1";
            txtONH4.Text = GetTiming.Substring(2, 2);
            txtONM4.Text = GetTiming.Substring(5, 2);
            txtOFFH4.Text = GetTiming.Substring(8, 2);
            txtOFFM4.Text = GetTiming.Substring(11, 2);
            //GetTiming = xroot.Element("TIMING").Element("Timing5").Value;
            //chkTime5.IsChecked = GetTiming.Substring(0, 1) == "1";
            //txtONH5.Text = GetTiming.Substring(2, 2);
            //txtONM5.Text = GetTiming.Substring(5, 2);
            //txtOFFH5.Text = GetTiming.Substring(8, 2);
            //txtOFFM5.Text = GetTiming.Substring(11, 2);
            //GetTiming = xroot.Element("TIMING").Element("Timing6").Value;
            //chkTime6.IsChecked = GetTiming.Substring(0, 1) == "1";
            //txtONH6.Text = GetTiming.Substring(2, 2);
            //txtONM6.Text = GetTiming.Substring(5, 2);
            //txtOFFH6.Text = GetTiming.Substring(8, 2);
            //txtOFFM6.Text = GetTiming.Substring(11, 2);           
            GetTiming = xroot.Element("TIMING").Element("Timing5").Value;
            tueTime1.IsChecked = GetTiming.Substring(0, 1) == "1";
            tuetxtONH1.Text = GetTiming.Substring(2, 2);
            tuetxtONM1.Text = GetTiming.Substring(5, 2);
            tuetxtOFFH1.Text = GetTiming.Substring(8, 2);
            tuetxtOFFM1.Text = GetTiming.Substring(11, 2);
            GetTiming = xroot.Element("TIMING").Element("Timing6").Value; //cmbPeriod1
            tueTime2.IsChecked = GetTiming.Substring(0, 1) == "1";
            tuetxtONH2.Text = GetTiming.Substring(2, 2);
            tuetxtONM2.Text = GetTiming.Substring(5, 2);
            tuetxtOFFH2.Text = GetTiming.Substring(8, 2);
            tuetxtOFFM2.Text = GetTiming.Substring(11, 2);
            GetTiming = xroot.Element("TIMING").Element("Timing7").Value;
            tueTime3.IsChecked = GetTiming.Substring(0, 1) == "1";
            tuetxtONH3.Text = GetTiming.Substring(2, 2);
            tuetxtONM3.Text = GetTiming.Substring(5, 2);
            tuetxtOFFH3.Text = GetTiming.Substring(8, 2);
            tuetxtOFFM3.Text = GetTiming.Substring(11, 2);
            GetTiming = xroot.Element("TIMING").Element("Timing8").Value; //cmbPeriod1
            tueTime4.IsChecked = GetTiming.Substring(0, 1) == "1";
            tuetxtONH4.Text = GetTiming.Substring(2, 2);
            tuetxtONM4.Text = GetTiming.Substring(5, 2);
            tuetxtOFFH4.Text = GetTiming.Substring(8, 2);
            tuetxtOFFM4.Text = GetTiming.Substring(11, 2);
            cmbPeriod1.Text = xroot.Element("TIMING").Element("OnType1").Value;
            cmbPeriod2.Text = xroot.Element("TIMING").Element("OnType2").Value;
            cmbPeriod3.Text = xroot.Element("TIMING").Element("OnType3").Value;
            cmbPeriod4.Text = xroot.Element("TIMING").Element("OnType4").Value;
            //cmbPeriod5.Text = xroot.Element("TIMING").Element("OnType5").Value;
            //cmbPeriod6.Text = xroot.Element("TIMING").Element("OnType6").Value;
            tueCmbPeriod1.Text = xroot.Element("TIMING").Element("OnType5").Value;
            tueCmbPeriod2.Text = xroot.Element("TIMING").Element("OnType6").Value;
            tueCmbPeriod3.Text = xroot.Element("TIMING").Element("OnType7").Value;
            tueCmbPeriod4.Text = xroot.Element("TIMING").Element("OnType8").Value;
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {
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
            int v = int.Parse(textBox.Text);
            if ((string)textBox.Tag == "H")
            {
                if (v > 23) textBox.Text = "23";
            }
            else
            {
                if (v > 59) textBox.Text = "59";
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
            Global.TimingEnable = (bool)chkTimeEnable.IsChecked;
            XElement xroot = xdoc.Element("root");
            string t = (bool)chkTime1.IsChecked ? "1" : "0";
            t = t + "," + txtONH1.Text.PadLeft(2, '0') + ":" + txtONM1.Text.PadLeft(2, '0') + "," + txtOFFH1.Text.PadLeft(2, '0') + ":" + txtOFFM1.Text.PadLeft(2, '0');
            xroot.Element("TIMING").Element("Timing1").Value = t;
            t = (bool)chkTime2.IsChecked ? "1" : "0";
            t = t + "," + txtONH2.Text.PadLeft(2, '0') + ":" + txtONM2.Text.PadLeft(2, '0') + "," + txtOFFH2.Text.PadLeft(2, '0') + ":" + txtOFFM2.Text.PadLeft(2, '0');
            xroot.Element("TIMING").Element("Timing2").Value = t;
            t = (bool)chkTime3.IsChecked ? "1" : "0";
            t = t + "," + txtONH3.Text.PadLeft(2, '0') + ":" + txtONM3.Text.PadLeft(2, '0') + "," + txtOFFH3.Text.PadLeft(2, '0') + ":" + txtOFFM3.Text.PadLeft(2, '0');
            xroot.Element("TIMING").Element("Timing3").Value = t;
            t = (bool)chkTime4.IsChecked ? "1" : "0";
            t = t + "," + txtONH4.Text.PadLeft(2, '0') + ":" + txtONM4.Text.PadLeft(2, '0') + "," + txtOFFH4.Text.PadLeft(2, '0') + ":" + txtOFFM4.Text.PadLeft(2, '0');
            xroot.Element("TIMING").Element("Timing4").Value = t;
            //t = (bool)chkTime5.IsChecked ? "1" : "0";
            //t = t + "," + txtONH5.Text.PadLeft(2, '0') + ":" + txtONM5.Text.PadLeft(2, '0') + "," + txtOFFH5.Text.PadLeft(2, '0') + ":" + txtOFFM5.Text.PadLeft(2, '0');
            //xroot.Element("TIMING").Element("Timing5").Value = t;
            //t = (bool)chkTime6.IsChecked ? "1" : "0";
            //t = t + "," + txtONH6.Text.PadLeft(2, '0') + ":" + txtONM6.Text.PadLeft(2, '0') + "," + txtOFFH6.Text.PadLeft(2, '0') + ":" + txtOFFM6.Text.PadLeft(2, '0');
            string timingOnOff = (bool)chkTime1.IsChecked ? "1" : "0";
            xroot.Element("TIMING").Element("TimingOnOff").Value = timingOnOff;
            //xroot.Element("TIMING").Element("Timing6").Value = t;
            t = (bool)tueTime1.IsChecked ? "1" : "0";
            t = t + "," + tuetxtONH1.Text.PadLeft(2, '0') + ":" + tuetxtONM1.Text.PadLeft(2, '0') + "," + tuetxtOFFH1.Text.PadLeft(2, '0') + ":" + tuetxtOFFM1.Text.PadLeft(2, '0');
            xroot.Element("TIMING").Element("Timing5").Value = t;
            t = (bool)tueTime2.IsChecked ? "1" : "0";
            t = t + "," + tuetxtONH2.Text.PadLeft(2, '0') + ":" + tuetxtONM2.Text.PadLeft(2, '0') + "," + tuetxtOFFH2.Text.PadLeft(2, '0') + ":" + tuetxtOFFM2.Text.PadLeft(2, '0');
            xroot.Element("TIMING").Element("Timing6").Value = t;
            t = (bool)tueTime2.IsChecked ? "1" : "0";
            t = t + "," + tuetxtONH3.Text.PadLeft(2, '0') + ":" + tuetxtONM3.Text.PadLeft(2, '0') + "," + tuetxtOFFH3.Text.PadLeft(2, '0') + ":" + tuetxtOFFM3.Text.PadLeft(2, '0');
            xroot.Element("TIMING").Element("Timing7").Value = t;
            t = (bool)tueTime2.IsChecked ? "1" : "0";
            t = t + "," + tuetxtONH4.Text.PadLeft(2, '0') + ":" + tuetxtONM4.Text.PadLeft(2, '0') + "," + tuetxtOFFH4.Text.PadLeft(2, '0') + ":" + tuetxtOFFM4.Text.PadLeft(2, '0');
            xroot.Element("TIMING").Element("Timing8").Value = t;
            xroot.Element("TIMING").Element("OnType1").Value = cmbPeriod1.Text;
            xroot.Element("TIMING").Element("OnType2").Value = cmbPeriod2.Text;
            xroot.Element("TIMING").Element("OnType3").Value = cmbPeriod3.Text;
            xroot.Element("TIMING").Element("OnType4").Value = cmbPeriod4.Text;
            xroot.Element("TIMING").Element("OnType5").Value = tueCmbPeriod1.Text;
            xroot.Element("TIMING").Element("OnType6").Value = tueCmbPeriod2.Text;
            xroot.Element("TIMING").Element("OnType7").Value = tueCmbPeriod3.Text;
            xroot.Element("TIMING").Element("OnType8").Value = tueCmbPeriod4.Text;
            xdoc.Save(Environment.CurrentDirectory + "\\Config.xml", SaveOptions.None);
            Global.ExeTimingSet = Global.GetNewTimingSet();
            MessageBox.Show("保存成功");
            this.Close();
        }
    }
}
