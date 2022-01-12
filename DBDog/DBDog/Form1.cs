using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using DBDog.BLL;
using System.Collections;

namespace DBDog
{

    public partial class Form1 : Form
    {
        DBStatusAccess dba;
        DataTable dtDBStatus;
        DataTable dtCfg;
        DataTable dtCalc;
        Dictionary<string, FreeMBRecord> ListRecord = new System.Collections.Generic.Dictionary<string, FreeMBRecord>();
        ReadCfg cfg;
        MailHelper mail;
        bool disableDeclear = false;
        DateTime tmLastDeclare = new DateTime();
        DateTime tmLastAlarmDBDisconn =DateTime.MinValue;
        public Form1()
        {
            InitializeComponent();
            dba = new DBStatusAccess();
            btnReadcfg_Click(null, null);
            mail = new MailHelper(cfg.Mailscfg.smtp, cfg.Mailscfg.fromName, cfg.Mailscfg.from);
            timerRepeat_Tick(null, null);
            timerRepeat.Interval = 1000 * cfg.FreshDataTableTime;
            timerRepeat.Start();
        }

        private void btnFresh_Click(object sender, EventArgs e)
        {
            try
            {
                dtDBStatus = dba.GetDBTableStatus();
                dgvDBStatus.DataSource = dtDBStatus;
            }
            catch (Oracle.ManagedDataAccess.Client.OracleException ex)
            {
            string rst=    dba.ReOpenDB();
                this.DBShutdownAlarm(rst+ex.Message);
            }
        }

        private void btnReadcfg_Click(object sender, EventArgs e)
        {
            ReadConfig();
        }


        private void btnCalc_Click(object sender, EventArgs e)
        {
            CreateDtCalc();
            CalcDtCalc();
            dgvCalc.DataSource = dtCalc;
        }
        private void btnAliveDeclare_Click(object sender, EventArgs e)
        {
            AliveDeclare();
        }

        private void btnCheckThreshold_Click(object sender, EventArgs e)
        {
            CheckTHRESHOLD();
        }
        private void timerResetDeclareFlag_Tick(object sender, EventArgs e)
        {
            string strDeclare = DateTime.Now.ToString("yyyy-MM-dd ");
            strDeclare += cfg.Alive_declare_time;
            DateTime tmNeedDelare = DateTime.ParseExact(strDeclare, "yyyy-MM-dd HH:mm:ss", null);

            if (DateTime.Now > tmNeedDelare && tmLastDeclare.ToString("yyyy-MM-dd") != DateTime.Now.ToString("yyyy-MM-dd"))
            {
                disableDeclear = false;
            }

        }
        private void timerRepeat_Tick(object sender, EventArgs e)
        {
            Console.WriteLine(System.DateTime.Now.ToString()+":timerRepeat_Tick(object sender, EventArgs e)");
            btnFresh_Click(null, null);
            btnCalc_Click(null, null);
            btnCheckThreshold_Click(null, null);
            if (!disableDeclear)
            {
                AliveDeclare();
            }
        }
        void CreateDtCalc()
        {
            dtCalc = new DataTable();
            dtCalc.Columns.Add("USEING_DAY");
            dtCalc.Columns.Add("MIN_USEING_DAY");
            dtCalc.Merge(dtDBStatus.Clone());
            dtCalc.Merge(dtCfg.Clone());
            dtCalc.Columns.Add("LAST_RECORD_FREE_MB");
            dtCalc.Columns.Add("LAST_RECORD_TIME");
        }
        void ReadConfig()
        {
            cfg = new ReadCfg();
            dtCfg = cfg.dtMonitor;
            dgvCfg.DataSource = dtCfg;
            lblMailSmtp.Text = cfg.Mailscfg.smtp;
            lblMailFrom.Text = cfg.Mailscfg.from;
            lblMailFromName.Text = cfg.Mailscfg.fromName;
            lblMailAliveTo.Text = cfg.Mailscfg.aliveto;
            lblMailAlarmTo.Text = cfg.Mailscfg.alarmto;
            lblFreshDataTableTime.Text = cfg.FreshDataTableTime.ToString();
            lblAliveDeclareTime.Text = cfg.Alive_declare_time.ToString();
            lblAlarmInterval.Text = cfg.Alarm_interval.ToString();

            initListRecord();
        }
        void initListRecord()
        {
            foreach (DataRow dr in dtCfg.Rows)
            {
                string tabName = dr["TABLESPACE_NAME"].ToString();
                ListRecord[tabName] = new FreeMBRecord();
                ListRecord[tabName].MAX_CALC_SPEED = double.Parse(dr["MAX_CALC_SPEED"].ToString());
            }
        }
        void CalcDtCalc()
        {
            dtCalc.Clear();

            foreach (DataRow dr in dtCfg.Rows)
            {
                DataRow newdr = dtCalc.NewRow();
                foreach (DataColumn dc in dtCfg.Columns)
                {
                    newdr[dc.ColumnName] = dr[dc.ColumnName];
                }
                dr["MAX_CALC_SPEED"] = ListRecord[dr["TABLESPACE_NAME"].ToString()].MAX_CALC_SPEED;

                var rst = dtDBStatus.Select("TABLESPACE_NAME='" + dr["TABLESPACE_NAME"] + "'");
                if (rst.Count() != 1)
                {
                    MessageBox.Show("Could not find the tablespace name:" + dr["TABLESPACE_NAME"].ToString());
                    continue;
                }
                foreach (DataColumn dc in dtDBStatus.Columns)
                {
                    newdr[dc.ColumnName] = rst[0][dc.ColumnName];
                }
                newdr["USEING_DAY"] = Math.Floor(double.Parse(newdr["FREE_MB"].ToString()) / double.Parse(newdr["USING_SPEED"].ToString()));
                newdr["MIN_USEING_DAY"] = Math.Floor(double.Parse(newdr["FREE_MB"].ToString()) / double.Parse(newdr["MAX_CALC_SPEED"].ToString()));
                newdr["LAST_RECORD_FREE_MB"] = ListRecord[dr["TABLESPACE_NAME"].ToString()].Free_MB;
                newdr["LAST_RECORD_TIME"] = ListRecord[dr["TABLESPACE_NAME"].ToString()].recordTime;
                dtCalc.Rows.Add(newdr);
            }
        }
        void AliveDeclare()
        {
            string rst;
            rst = DatatableToHtml.GetHtmlString(dtCalc);
            rst += "请检查每天早上8:00必须叫,不叫就是死狗!";
            mail.SendMailWithIPAddr(cfg.Mailscfg.aliveto, "汪~汪~汪汪汪!!", rst);
            disableDeclear = true;
            RecordFreeMBandCalcMaxSpeed();
            tmLastDeclare = DateTime.Now;
        }
        void RecordFreeMBandCalcMaxSpeed()
        {

            foreach (DataRow dr in dtCalc.Rows)
            {
                string tabName = dr["TABLESPACE_NAME"].ToString();
                if (ListRecord[tabName].Free_MB >= 0)
                {
                    //  double recordFreeMB = ListRecord[tabName].Free_MB;
                    double span = (DateTime.Now - ListRecord[tabName].recordTime).TotalDays;
                    if (span < 0.8)
                    {//the length of time span must be enough; 
                        continue;// the effect is the same as break or return;
                    }
                    double speed = (ListRecord[tabName].Free_MB - double.Parse(dr["FREE_MB"].ToString())) / span;
                    if (speed > ListRecord[tabName].MAX_CALC_SPEED)
                    {
                        ListRecord[tabName].MAX_CALC_SPEED = speed;
                    }
                }
                ListRecord[tabName].Free_MB = double.Parse(dr["FREE_MB"].ToString());
                ListRecord[tabName].recordTime = DateTime.Now;
            }

            CalcDtCalc();

        }
        void CheckTHRESHOLD()
        {
            foreach (DataRow dr in dtCalc.Rows)
            {
                double freeMB = double.Parse(dr["FREE_MB"].ToString());
                double freeMBThreshold = double.Parse(dr["FREE_MB_THRESHOLD"].ToString());
                double maxBytes = double.Parse(dr["MAX_BYTES_MB"].ToString());
                double maxBytesThreshold = double.Parse(dr["MAX_BYTES_THRESHOLD"].ToString());
                if (freeMB < freeMBThreshold)
                {
                    string msg = string.Format("freeMB < freeMBThreshold <br> {0}<{1} <br> tablespace:{2}", freeMB, freeMBThreshold, dr["TABLESPACE_NAME"]);
                    ThresholdAlarm(msg);
                    continue;
                }
                if (maxBytes < maxBytesThreshold)
                {
                    string msg = string.Format("maxBytes < maxBytesThreshold<br> {0}<{1} <br> tablespace:{2}", maxBytes, maxBytesThreshold, dr["TABLESPACE_NAME"]);
                    ThresholdAlarm(msg);
                }
            }
        }
        void ThresholdAlarm(string msg)
        {
            double lastSpan = (DateTime.Now - tmLastDeclare).TotalSeconds;
            if (lastSpan < cfg.Alarm_interval)
            {
                return;
            }
            msg += "<br>" + DatatableToHtml.GetHtmlString(dtCalc);
            mail.SendMailWithIPAddr(cfg.Mailscfg.alarmto, "严重警报:DB表空间不足阈值", msg);
            tmLastDeclare = DateTime.Now;
        }
        void DBShutdownAlarm(string msg)
        {
            if ((DateTime.Now - tmLastAlarmDBDisconn).TotalSeconds >= cfg.Alarm_db_disconn)
            {
                tmLastAlarmDBDisconn = DateTime.Now;
                mail.SendMailWithIPAddr(cfg.Mailscfg.alarmto, "不能查询DB,即将重新连接...", msg);
            }
        }


    }
    class FreeMBRecord
    {
        public double Free_MB = -1;
        public DateTime recordTime;
        public double MAX_CALC_SPEED;
    }
}
