using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace midFrequence
{
    /// <summary>
    /// UserControl1.xaml 的交互逻辑
    /// </summary>
    public partial class bargraph : UserControl
    {
        public bargraph()
        {
            InitializeComponent();
            BatteryProgressBarBig.IsEnabled = true;
        }
        public double ChargingProgress
        {
            get
            {
                return ChargingProgress;
            }
            set
            {
                //A：透明度，R：红色值。G：绿色值。B：蓝色值
                //FF0000-FFFF00 红到黄 FFFF00-00FF00黄到绿
                //if (value <= 75)
                //{

                //    GS_0.Color = Color.FromArgb(192, 255, Convert.ToByte((255 - 225) * (value / 75) + 225), 225);
                //    GS_1.Color = Color.FromArgb(192, 255, Convert.ToByte((255 - 96) * (value / 75) + 96), 96);
                //    GS_2.Color = Color.FromArgb(192, 192, Convert.ToByte((192 - 0) * (value / 75) + 0), 0);
                //    GS_3.Color = Color.FromArgb(192, 128, Convert.ToByte((128 - 0) * (value / 75) + 0), 0);
                //}
                //else
                //{

                //    GS_0.Color = Color.FromArgb(192, Convert.ToByte(225 + (255 - 225) * ((100 - value) / 25)), 255, 225);
                //    GS_1.Color = Color.FromArgb(192, Convert.ToByte(96 + (255 - 96) * ((100 - value) / 25)), 255, 96);
                //    GS_2.Color = Color.FromArgb(192, Convert.ToByte(0 + (192 - 0) * ((100 - value) / 25)), 192, 0);
                //    GS_3.Color = Color.FromArgb(192, Convert.ToByte(0 + (128 - 0) * ((100 - value) / 25)), 128, 0);
                //}

                GS_0.Color = Color.FromArgb(192, 50, 255, 20);
                GS_1.Color = Color.FromArgb(192, 30, 255, 20);
                GS_2.Color = Color.FromArgb(192, 10, 255, 20);
                GS_3.Color = Color.FromArgb(192, 0, 255, 20);
                //TextBlockProgressBig.Text = Convert.ToString(Convert.ToInt16(Math.Floor(value)));
                BatteryProgressBarBig.Value = value;
            }
        }
    }
}
