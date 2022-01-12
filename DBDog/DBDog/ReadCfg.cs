using System;
using System.Collections.Generic;
using System.Linq;
using System.Text; 
using System.Xml;
using System.Collections;
using System.Data;

namespace DBDog
{
    class ReadCfg
    {
        XmlDocument xml;
        MAILSCFG mailscfg;

        internal MAILSCFG Mailscfg
        {
            get { return mailscfg; }
            set { mailscfg = value; }
        }
        int freshDataTableTime;

        public int FreshDataTableTime
        {
            get { return freshDataTableTime; }
            set { freshDataTableTime = value; }
        }
        string alive_declare_time;

        public string Alive_declare_time
        {
            get { return alive_declare_time; }
            set { alive_declare_time = value; }
        }
        int alarm_interval;

        public int Alarm_interval
        {
            get { return alarm_interval; }
            set { alarm_interval = value; }
        }
        public DataTable dtMonitor;
        public ReadCfg(string xmlFilePath = "")
        {
            xml = new XmlDocument();
            if (xmlFilePath == "")
                xmlFilePath = "DBDogCfg.xml";
            xml.Load(xmlFilePath);
            mailscfg = new MAILSCFG();
            ReadToCache();
        }
        private int alarm_db_disconn;

public int Alarm_db_disconn
{
  get { return alarm_db_disconn; }
  set { alarm_db_disconn = value; }
}
            
         

        void ReadToCache()
        {
            dtMonitor = new DataTable();
            dtMonitor.Columns.Add("TABLESPACE_NAME", typeof(string));
            dtMonitor.Columns.Add("USING_SPEED", typeof(double));
            dtMonitor.Columns.Add("MAX_CALC_SPEED",typeof(double));
            dtMonitor.Columns.Add("FREE_MB_THRESHOLD", typeof(double));
            dtMonitor.Columns.Add("MAX_BYTES_THRESHOLD", typeof(double));
            foreach (XmlNode node in xml.SelectNodes("CFG/MONITOR/TABLESPACE"))
            {
                DataRow s = dtMonitor.NewRow();
                s["TABLESPACE_NAME"] = node["TABLESPACE_NAME"].InnerText;
                s["USING_SPEED"] = Double.Parse( node["USING_SPEED"].InnerText);
                s["MAX_CALC_SPEED"] = Double.Parse(node["MAX_CALC_SPEED"].InnerText);
                s["FREE_MB_THRESHOLD"] =Double.Parse( node["FREE_MB_THRESHOLD"].InnerText);
                s["MAX_BYTES_THRESHOLD"] =Double.Parse( node["MAX_BYTES_THRESHOLD"].InnerText);
                dtMonitor.Rows.Add(s);
            }

            XmlNode n;
            n = xml.SelectSingleNode("CFG/MAILSCFG");
            mailscfg.smtp = n["SMTP"].InnerText;
            mailscfg.from = n["FROM"].InnerText;
            mailscfg.fromName = n["FROM_NAME"].InnerText;
            mailscfg.aliveto = n["ALIVETO"].InnerText;
            mailscfg.alarmto = n["ALARMTO"].InnerText;

            n = xml.SelectSingleNode("CFG");
            freshDataTableTime = Int32.Parse(n["FRESH_DATA_TABLE_TIME"].InnerText);
            alarm_db_disconn = Int32.Parse(n["ALARM_DB_DISCONN"].InnerText);
            alive_declare_time = n["ALIVE_DECLARE_TIME"].InnerText ;
            alarm_interval = Int32.Parse(n["ALARM_INTERVAL"].InnerText);
        }
    }
    struct MAILSCFG
    {
        public string smtp;
        public string from;
        public string fromName;
        public string aliveto;
        public string alarmto;
    }

}
