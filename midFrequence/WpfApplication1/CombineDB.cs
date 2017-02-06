using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SQLite;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace midFrequence
{
    class CombineDB
    {
        private static string mConnectstring;
        private static int mSaveLogMonth = 0;

        public static string Connectstring
        {
            set { mConnectstring = value; }
        }
        public static int SaveLogMonth
        {
            get { return mSaveLogMonth; }
            set { mSaveLogMonth = value; }
        }
        //增加记录
        public static void AddSyslog( string opt)
        {
            using (SQLiteConnection thisConnection = new SQLiteConnection(mConnectstring))
            {
                thisConnection.Open();
                string sqlcmd = "INSERT INTO Syslog (LOGDATE, " +
                                                       "LOGTIME, " +
                                                       "OPERATE)" +
                                "VALUES ('" + DateTime.Now.ToString("yyyy-MM-dd") + "', " +
                                        "'" + DateTime.Now.ToString("HH:mm:ss") + "', " +
                                        "'" + opt + "')";
                SQLiteCommand thiscmd = new SQLiteCommand(sqlcmd, thisConnection);
                thiscmd.ExecuteNonQuery();
            }
        }
        //查找记录
        public static DataTable GetSyslog(string date)
        {
            using (SQLiteConnection thisConnection = new SQLiteConnection(mConnectstring))
            {
                thisConnection.Open();
                SQLiteDataAdapter thisAdapter = new SQLiteDataAdapter();
                //string selcmd = "SELECT * FROM Syslog WHERE LOGDATE='" + date + "'";
                string selcmd = "SELECT * FROM Syslog ";
                thisAdapter.SelectCommand = new SQLiteCommand(selcmd, thisConnection);
                DataTable thisTable = new DataTable();
                thisAdapter.Fill(thisTable);
                //thisTable.Columns.Remove("ID");
                return thisTable;
            }
        }
        public static DataTable GetOptLog(string date)
        {
            using (SQLiteConnection thisConnection = new SQLiteConnection(mConnectstring))
            {
                thisConnection.Open();
                SQLiteDataAdapter thisAdapter = new SQLiteDataAdapter();
                //string selcmd = "SELECT * FROM Syslog WHERE LOGDATE='" + date + "'";
                string selcmd = "SELECT * FROM OptLog ";
                thisAdapter.SelectCommand = new SQLiteCommand(selcmd, thisConnection);
                DataTable thisTable = new DataTable();
                thisAdapter.Fill(thisTable);
                //thisTable.Columns.Remove("ID");
                return thisTable;
            }
        }
        //定期清除记录
        public static void ClearOldRecord()
        {
            //try
            //{
            DateTime thisDate = DateTime.Now.AddMonths(0 - SaveLogMonth);
            string date = thisDate.Date.ToString("yyyy-MM-dd");
            using (SQLiteConnection thisConnection = new SQLiteConnection(mConnectstring))
            {
                thisConnection.Open();
                string sqlcmd = "DELETE FROM Syslog WHERE LogDate<'" + date + "'";
                SQLiteCommand thisCmd = new SQLiteCommand(sqlcmd, thisConnection);
                thisCmd.ExecuteNonQuery();

                //string sqlcmd2 = "DELETE FROM TB_TransmitterA WHERE LogDate<'" + date + "'";
                //SQLiteCommand thisCmd2 = new SQLiteCommand(sqlcmd2, thisConnection);
                //thisCmd2.ExecuteNonQuery();

                //string sqlcmd3 = "DELETE FROM TB_TransmitterB WHERE LogDate<'" + date + "'";
                //SQLiteCommand thisCmd3 = new SQLiteCommand(sqlcmd3, thisConnection);
                //thisCmd3.ExecuteNonQuery();

                //string sqlcmd4 = "DELETE FROM TB_Combine WHERE LogDate<'" + date + "'";
                //SQLiteCommand thisCmd4 = new SQLiteCommand(sqlcmd4, thisConnection);
                //thisCmd4.ExecuteNonQuery();
            }
            //}
            //catch
            //{
            //}
        }
        //删除系统记录
        public static void DelSyslog(int index)
        {
            using (SQLiteConnection thisConnection = new SQLiteConnection(mConnectstring))
            {
                thisConnection.Open();
                string sqlcmd = "DELETE FROM Syslog WHERE id=" + index;
                SQLiteCommand thisCmd = new SQLiteCommand(sqlcmd, thisConnection);
                thisCmd.ExecuteNonQuery();
            }
        }
        //删除操作记录(发射机返回记录)
        public static void DelOptlog(int index)
        {
            using (SQLiteConnection thisConnection = new SQLiteConnection(mConnectstring))
            {
                thisConnection.Open();
                string sqlcmd = "DELETE FROM Optlog WHERE id=" + index;
                SQLiteCommand thisCmd = new SQLiteCommand(sqlcmd, thisConnection);
                thisCmd.ExecuteNonQuery();
            }
        }
        //发射机工作记录
        public static void AddOptlog(string[] thisRecord)
        {
            using (SQLiteConnection thisConnection = new SQLiteConnection(mConnectstring))
            {
                thisConnection.Open();
                string sqlcmd = "INSERT INTO OptLog" +" (LOGDATE, " +
                                                       "LOGTIME, " +
                                                       "RS, " +
                                                       "FS, " +
                                                       "ZDL, " +
                                                       "ZDY, " +
                                                       "TXZBB, " +
                                                       "DTZBB, " +
                                                       "TFD, " +
                                                       "Z22V, " +
                                                       "F22V, " +
                                                       "Z8V, " +
                                                       "F8V, " +
                                                       "SPTD, " +
                                                       "SPG, " +
                                                       "SPD)" +
                                "VALUES ('" + DateTime.Now.ToString("yyyy-MM-dd") + "', " +
                                        "'" + DateTime.Now.ToString("HH:mm:ss") + "', " +
                                        "'" + thisRecord[0] + "', " +
                                        "'" + thisRecord[1] + "', " +
                                        "'" + thisRecord[2] + "', " +
                                        "'" + thisRecord[3] + "', " +
                                        "'" + thisRecord[4] + "', " +
                                        "'" + thisRecord[5] + "', " +
                                        "'" + thisRecord[6] + "', " +
                                        "'" + thisRecord[7] + "', " +
                                        "'" + thisRecord[8] + "', " +
                                        "'" + thisRecord[9] + "', " +
                                        "'" + thisRecord[10] + "', " +
                                        "'" + thisRecord[11] + "', " +
                                        "'" + thisRecord[12] + "', " +
                                        "'" + thisRecord[13] + "')";
                SQLiteCommand thiscmd = new SQLiteCommand(sqlcmd, thisConnection);
                thiscmd.ExecuteNonQuery();
            }
        }
    }
}
