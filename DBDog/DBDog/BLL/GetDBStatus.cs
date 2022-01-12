using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Data;
using System.Collections;

namespace DBDog.BLL
{
    class DBStatusAccess
    {
        OraDatabase db;
        public DBStatusAccess()
        {
            db = new OraDatabase();
        }
        public DataTable GetDBTableStatus()
        {
            string sql = @"SELECT UPPER(F.TABLESPACE_NAME) TABLESPACE_NAME,
       D.TOT_GROOTTE_MB TOT_MB,
       D.TOT_GROOTTE_MB - F.TOTAL_BYTES USED_MB,
       TO_CHAR(ROUND((D.TOT_GROOTTE_MB - F.TOTAL_BYTES) / D.TOT_GROOTTE_MB * 100,
                     2),
               '990.99') || '%' USED_RATE,
       F.TOTAL_BYTES FREE_MB,
       F.MAX_BYTES MAX_BYTES_MB
  FROM (SELECT TABLESPACE_NAME,
               ROUND(SUM(BYTES) / (1024 * 1024), 2) TOTAL_BYTES,
               ROUND(MAX(BYTES) / (1024 * 1024), 2) MAX_BYTES
          FROM SYS.DBA_FREE_SPACE
         GROUP BY TABLESPACE_NAME) F,
       (SELECT DD.TABLESPACE_NAME,
               ROUND(SUM(DD.BYTES) / (1024 * 1024), 2) TOT_GROOTTE_MB
          FROM SYS.DBA_DATA_FILES DD
         GROUP BY DD.TABLESPACE_NAME) D
 WHERE D.TABLESPACE_NAME = F.TABLESPACE_NAME
-- and F.TABLESPACE_NAME in ('SYSTRAVELIDX','SYSSNIDX','SYSTRAVEL','SYSSN')
 ORDER BY USED_RATE desc";
         return   db.QueryDataTable( db.CMD(sql));
        }
        public string ReOpenDB()
        {
            try
            {
                db.Close();
                db.Open();
                return "DB ReOpen OK";
            }
            catch (Exception ex)
            {
                return "DB ReOpen Fail " + ex.Message; 
            }
        }

    }
}
