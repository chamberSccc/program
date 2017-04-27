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
using System.Data;

namespace midFrequence
{
    /// <summary>
    /// Log.xaml 的交互逻辑
    /// </summary>
    public partial class Log : Window
    {
        private DateTime SelDate = DateTime.Now;
        private DataTable SelTable;

        public Log()
        {
            InitializeComponent();
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            //GetLog(tabControl1.SelectedIndex);
            datePicker1.SelectedDate = SelDate;
        }

        private void tabControl1_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            //GetLog(tabControl1.SelectedIndex);
        }

        private void datePicker1_SelectedDateChanged(object sender, SelectionChangedEventArgs e)
        {
            SelDate = (DateTime)datePicker1.SelectedDate;
        }

        private void btnFind_Click(object sender, RoutedEventArgs e)
        {
            GetLog(tabControl1.SelectedIndex);
        }
        private void GetLog(int flag)
        {
            switch (flag)
            {
                case 0:
                    SelTable = CombineDB.GetSyslog(SelDate.ToString("yyyy-MM-dd"));
                    lblCount.Content = "--- 共" + SelTable.Rows.Count.ToString() + "条记录 ---";
                    dataGridSyslog.DataContext = SelTable;
                    break;
                case 1:
                    SelTable = CombineDB.GetOptLog(SelDate.ToString("yyyy-MM-dd"));
                    lblCount.Content = "--- 共" + SelTable.Rows.Count.ToString() + "条记录 ---";
                    dataGridOptlog.DataContext = SelTable;
                    break;
            }
        }
        private void DelLog(int flag1,int flag2)
        {
            switch (flag1)
            {
                case 0:
                    CombineDB.DelSyslog(flag2);
                    SelTable = CombineDB.GetSyslog(SelDate.ToString("yyyy-MM-dd"));
                    lblCount.Content = "--- 共" + SelTable.Rows.Count.ToString() + "条记录 ---";
                    dataGridSyslog.DataContext = SelTable;
                    break;
                case 1:
                    CombineDB.DelOptlog(flag2);
                    SelTable = CombineDB.GetOptLog(SelDate.ToString("yyyy-MM-dd"));
                    lblCount.Content = "--- 共" + SelTable.Rows.Count.ToString() + "条记录 ---";
                    dataGridOptlog.DataContext = SelTable;
                    break;
            }
        }
        private void btnDelete_Click(object sender, RoutedEventArgs e)
        {
            var a = dataGridSyslog.SelectedItem; 
            var b = a as DataRowView;
            string result = b.Row[0].ToString();
            int flag = int.Parse(result);
            DelLog(tabControl1.SelectedIndex, flag);
        }
        private void btnDelete1_Click(object sender, RoutedEventArgs e)
        {
            var a = dataGridOptlog.SelectedItem;  
            var b = a as DataRowView;
            string result = b.Row[0].ToString();
            int flag = int.Parse(result);
            DelLog(tabControl1.SelectedIndex, flag);
        }
    }
}
