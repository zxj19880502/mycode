
using System;
using System.Collections;
using System.Data;
using System.Configuration;
using Oracle.ManagedDataAccess.Client;
using System.Windows.Forms;
using System.IO.Compression;
using System.IO;

namespace Class1
{
    /// <summary>
    /// 类，用于数据访问的类。
    /// </summary>
    public class OraDatabase : IDisposable
    {
        /// <summary>
        /// the count of selected results
        /// </summary>
        int _count;
        public static string SFC = "Data Source=MESDB;User Id=sajet;Password=tech;";
        public int Count
        {
            get { return _count; }
            set { _count = value; }
        }

        /// <summary>
        /// 保护变量，数据库连接。
        /// </summary>
        OracleConnection Connection;

        /// <summary>
        /// 保护变量，数据库连接串。
        /// </summary>
        protected String ConnectionString;

        OracleCommand cmd;



        public OraDatabase()
        {
            ConnectionStringSettings settings = ConfigurationManager.ConnectionStrings["SFC"];
            ConnectionString = settings.ConnectionString;
            Open();
        }

        /// <summary>
        /// 执行查询语句，返回OleDbDataReader
        /// </summary>
        /// <param name="strSQL">查询语句</param>
        /// <returns>OleDbDataReader</returns>
        public IDataReader ExecuteReader(string strSQL)
        {
            OracleConnection connection = new OracleConnection(ConnectionString);
            OracleCommand cmd = new OracleCommand(strSQL, connection);
            cmd.CommandTimeout = 10000;
            try
            {
                connection.Open();
                OracleDataReader myReader = cmd.ExecuteReader();
                return myReader;
            }
            catch (System.Data.DataException e)
            {
                throw new Exception(e.Message);
            }

        }

        public static OracleDataReader ExecuteQueryReturnReader(string sql, string connStr)
        {
            OracleConnection conn = new OracleConnection();
            OracleDataReader reader = null;

            try
            {
                conn = new OracleConnection(connStr);
                conn.Open();

                OracleCommand command = conn.CreateCommand();
                command.CommandText = sql;
                reader = command.ExecuteReader();
            }
            catch
            {
            }
            finally
            {
                if (conn != null)
                    conn.Close();
            }
            return reader;
        }

        /// <summary>
        /// 構造函數,自定義連接字符串
        /// </summary>
        /// <param name="argConnectionString"></param>
        public OraDatabase(string argConnectionString)
        {
            ConnectionString = argConnectionString;
            Open();
        }

        /// <summary>
        /// 析构函数，释放非托管资源
        /// </summary>
        ~OraDatabase()
        {
            Connection.Dispose();
        }

        /// <summary>
        /// 保护方法，打开数据库连接。
        /// </summary>
        public void Open()
        {

            if (Connection == null)
            {
                Connection = new OracleConnection(ConnectionString);
            }
            if (Connection.State.Equals(ConnectionState.Closed))
            {
                Connection.Open();
            }

            cmd = Connection.CreateCommand();

        }

        /// <summary>
        /// 公有方法，关闭数据库连接。
        /// </summary>
        public void Close()
        {
            if (Connection != null)
                Connection.Close();
        }


        /// <summary>
        /// 公有方法，释放资源。
        /// </summary>
        public void Dispose()
        {
            Close();
            // 确保连接被关闭
            if (Connection != null)
            {
                Connection.Dispose();
                Connection = null;
            }
            if (cmd != null)
            {
                cmd.Dispose();
                cmd = null;
            }
        }

        /// <summary>
        /// 查询结果行数,此函数可能造成性能的损失
        /// </summary>
        /// <param name="cmd"></param>
        /// <returns></returns>
        public int QueryResultQty(OracleCommand cmd)
        {
            string cmdSqlRecover = cmd.CommandText;
            cmd.CommandText = string.Format("select count(*) from ({0})", cmd.CommandText);
            int rst = QueryInt(cmd);
            cmd.CommandText = cmdSqlRecover;
            return rst;
        }

        public static DataSet GetDataSet(string sqlStr)
        {
            System.Data.OracleClient.OracleConnection conn = new System.Data.OracleClient.OracleConnection(SFC);
            conn.Open();
            DataSet ds = new DataSet();
            System.Data.OracleClient.OracleDataAdapter adp = new System.Data.OracleClient.OracleDataAdapter(sqlStr, conn);
            adp.Fill(ds);
            conn.Close();
            return ds;
        }

      //  public static DataSet shujuchaxun(string work_order,string startime,string endtime)
       // {
         //   System.Data.OracleClient.OracleConnection conn = new System.Data.OracleClient.OracleConnection(SFC);
         //   conn.Open();
         //   DataSet ds = new DataSet();
         //   string sql = "select * from G_SN_COUNT WHERE WORK_ORDER = '" + work_order + "' AND CREATE_TIME between to_date('" + startime + "','yyyy/mm/dd hh24:mi:ss')and to_date('" + endtime + "','yyyy/mm/dd hh24:mi:ss') ";

        //    System.Data.OracleClient.OracleDataAdapter dt = new System.Data.OracleClient.OracleDataAdapter(sql, conn);
            
           
       //     dt.Fill(ds);
       //     conn.Close();
       //     return ds;

      //  }


        public static string goData(string sql)
        {
            string DealResult = "";
            System.Data.OracleClient.OracleConnection conn = new System.Data.OracleClient.OracleConnection(SFC);
            conn.Open();
            System.Data.OracleClient.OracleCommand cmd = new System.Data.OracleClient.OracleCommand();
            cmd.Connection = conn;
            System.Data.OracleClient.OracleTransaction myTransaction = conn.BeginTransaction();
            cmd.Transaction = myTransaction;
            try
            {
                cmd.CommandText = sql;
                cmd.ExecuteNonQuery();
                myTransaction.Commit();
                DealResult = "ok";
            }
            catch (Exception ex)
            {
                myTransaction.Rollback();
                DealResult = ex.Message;
            }
            finally
            {
                conn.Close();
            }
            return DealResult;
        }


        /// <summary>
        /// 公有方法，获取数据，返回一个DataSet。
        /// </summary>
        /// <param name="sqlString">Sql语句</param>
        /// <returns>DataSet</returns>
        public DataSet QueryDataSet(OracleCommand cmd, int startRecord = -1, int maxRecord = 1)
        {
            OracleDataAdapter adapter = new OracleDataAdapter(cmd);
            DataSet dataset = new DataSet();
            if (startRecord == -1 || maxRecord == -1)
            {
                adapter.Fill(dataset);
            }
            else
            {
                adapter.Fill(dataset, startRecord, maxRecord, "dataset");
            }
            adapter.Dispose();
            return dataset;


        }



        /// <summary>
        /// 
        /// </summary>
        /// <param name="cmd">orale command type contain sql</param>
        /// <param name="startRecord">begin with 0</param>
        /// <param name="maxRecord"></param>
        /// <returns></returns>
        public DataTable QueryDataTable(OracleCommand cmd, int startRecord = -1, int maxRecord = 1)
        {
            DataSet dataset = QueryDataSet(cmd, startRecord, maxRecord);
            _count = dataset.Tables[0].Rows.Count;
            return dataset.Tables[0];
        }
        /// <summary>
        /// 公有方法，获取数据，返回一个DataRow。
        /// </summary>
        /// <param name="sqlString">Sql语句</param>
        /// <returns>DataRow</returns>
        public DataRow QueryDataRow(OracleCommand cmd)
        {
            DataSet dataset = QueryDataSet(cmd, 0, 0);
            if (dataset.Tables[0].Rows.Count > 0)
            {
                return dataset.Tables[0].Rows[0];
            }
            else
            {
                return null;
            }
        }
        /// <summary>
        /// Get one string from sql query. 
        /// </summary>
        /// <param name="sqlString"></param>
        /// <returns></returns>
        public string QueryString(OracleCommand cmd)
        {
            DataRow dr = QueryDataRow(cmd);
            if (dr != null)
            {
                object obj = dr[0];
                if (obj != null)
                {
                    return obj.ToString();
                }
            }

            return null;


        }
        /// <summary>
        /// 只適用于查詢數量的sql語句
        /// </summary>
        /// <param name="sqlcmd">select count(id) from t_emp where account='jack_wei'</param>
        /// <returns></returns>
        public int QueryInt(OracleCommand cmd)
        {
            int rst = Int32.Parse(QueryString(cmd));
            return rst;
        }



        public int ExecuteSQL(OracleCommand cmd)
        {
            int rowsUpdated;
            rowsUpdated = cmd.ExecuteNonQuery();
            return rowsUpdated;
        }



        public OracleCommand CMD(string sqlString)
        {
            cmd.CommandText = sqlString;
            return cmd;
        }


        public OracleCommand CMD(string sqlString, string key, object value)
        {
            //try add  oracle type
            cmd.CommandText = sqlString;
            cmd.Parameters.Clear();
            OracleParameter p = new OracleParameter();
            p.ParameterName = key;
            p.OracleDbType = GetOraType(value);
            p.Value = value;
            cmd.Parameters.Add(p);
            return cmd;
        }
        public OracleCommand CMD(string sqlString, string[] keys, object[] values)
        {
            cmd.CommandText = sqlString;
            cmd.Parameters.Clear();
            for (int i = 0; i < keys.Length; i++)
            {
                OracleParameter p = new OracleParameter();
                p.ParameterName = keys[i];
                p.OracleDbType = GetOraType(values[i]);
                p.Value = values[i];
                cmd.Parameters.Add(p);
            }
            return cmd;
        }
        public OracleCommand CMD(string sqlString, Hashtable parms)
        {
            cmd.CommandText = sqlString;
            cmd.Parameters.Clear();
            foreach (string k in parms.Keys)
            {
                object v = parms[k];

                OracleParameter p = new OracleParameter();
                p.ParameterName = k;
                p.OracleDbType = GetOraType(v);
                p.Value = v;
                cmd.Parameters.Add(p);

            }
            return cmd;
        }

        public OracleCommand CMD(string sqlString, PrcPam[] parms)
        {
            cmd.CommandText = sqlString;
            if (parms.Length > 0)
                cmd.ArrayBindCount = parms[0].ArrayBindCount;
            else
                cmd.ArrayBindCount = 0;

            cmd.Parameters.Clear();
            foreach (PrcPam p in parms)
            {
                OracleParameter parm = new OracleParameter(p.name, p.type, p.cache);
                parm.Direction = p.GetDirc();
                parm.Value = p.val;
                cmd.Parameters.Add(parm);
            }
            return cmd;
        }
        #region Run procedure
        /// <summary>
        ///             PrcPam p1 = new PrcPam("barcode", barcode, "INPUT");
        ///             PrcPam p2 = new PrcPam("rst", "", "OUTPUT", 80);
        ///             System.Collections.Hashtable ht = db.RunProcedure("SCN_CHKRULE", new PrcPam[] { p1, p2 });
        /// </summary>
        /// <param name="ProcedureName"></param>
        /// <param name="parms"></param>
        /// <returns></returns>
        public Hashtable RunProcedure(string ProcedureName, PrcPam[] parms = null)
        {
            OracleCommand cmd = new OracleCommand();
            int rows = 0;

            cmd.CommandType = CommandType.StoredProcedure;
            cmd.Connection = Connection;
            cmd.CommandText = ProcedureName;

            if (parms != null)
            {
                cmd.ArrayBindCount = parms[0].ArrayBindCount;

                foreach (PrcPam p in parms)
                {
                    OracleParameter parm = new OracleParameter(p.name, p.type, p.cache);
                    parm.Direction = p.GetDirc();
                    parm.Value = p.val;
                    cmd.Parameters.Add(parm);
                }
            }
            rows = cmd.ExecuteNonQuery();

            Hashtable ht = new Hashtable();
            foreach (OracleParameter p in cmd.Parameters)
            {
                if (p.Direction == ParameterDirection.Output || p.Direction == ParameterDirection.InputOutput)
                {
                    ht.Add(p.ParameterName, p.Value);
                }
            }

            return ht;
        }


        #endregion

        public OracleDbType GetOraType(object o)
        {
            string t = o.GetType().ToString();

            OracleDbType type;
            switch (t)
            {
                case "System.String": type = OracleDbType.Varchar2; break;
                case "System.Int32": type = OracleDbType.Int32; break;
                case "System.Char": type = OracleDbType.Char; break;
                default: type = OracleDbType.Varchar2; break;
            }
            return type;
        }





        public class PrcPam
        {
            public int ArrayBindCount = 0;
            public string name { get; set; }
            private object _val;
            public object val
            {
                get { return _val; }
                set
                {
                    _val = value;
                    if (value == null)
                    {
                        type = OracleDbType.Varchar2;
                        return;
                    }
                    string t = value.GetType().ToString();
                    switch (t)
                    {
                        case "System.String":
                            {
                                ArrayBindCount = 0;
                                type = OracleDbType.Varchar2; break;
                            }
                        case "System.String[]":
                            {
                                ArrayBindCount = ((string[])value).Length;
                                type = OracleDbType.Varchar2; break;
                            }
                        case "System.Int32":
                            {
                                type = OracleDbType.Int32; break;
                            }
                        case "System.Int32[]":
                            {
                                ArrayBindCount = ((Int32[])value).Length;
                                type = OracleDbType.Int32; break;
                            }
                        case "System.Double":
                            {
                                ArrayBindCount = 0;
                                type = OracleDbType.Double; break;
                            }
                        case "System.Double[]":
                            {
                                ArrayBindCount = ((double[])value).Length;
                                type = OracleDbType.Double; break;
                            }
                        default:
                            {
                                ArrayBindCount = 0;
                                type = OracleDbType.Varchar2; break;
                            }
                    }


                }
            }
            public OracleDbType type { get; private set; }
            public int cache { get; set; }
            public string dirc { get; set; }

            public ParameterDirection GetDirc()
            {
                ParameterDirection rst;
                switch (dirc.ToUpper())
                {
                    case "INPUT": rst = ParameterDirection.Input; break;
                    case "OUTPUT": rst = ParameterDirection.Output; break;
                    default: rst = ParameterDirection.InputOutput; break;
                }
                return rst;
            }


            /// <summary>
            /// 
            /// </summary>
            /// <param name="argname"></param>
            /// <param name="argval"></param>
            /// <param name="argdirc">"INPUT"/"OUTPUT"</param>
            /// <param name="argcache">When dirc=input,the argcache can be 0, which is default</param>
            public PrcPam(string argname, object argval, string argdirc = "INPUT", int argcache = 0)
            {
                name = argname;
                val = argval;
                cache = argcache;
                dirc = argdirc;
            }

            public static byte[] Decompress(byte[] data)
            {
                try
                {
                    MemoryStream ms = new MemoryStream(data);
                    Stream zipStream = null;
                    zipStream = new GZipStream(ms, CompressionMode.Decompress);
                    byte[] dc_data = null;
                    dc_data = EtractBytesFormStream(zipStream, data.Length);
                    return dc_data;
                }
                catch
                {
                    return null;
                }


            }

            public static byte[] EtractBytesFormStream(Stream zipStream, int dataBlock)
            {
                try
                {
                    byte[] data = null;
                    int totalBytesRead = 0;
                    while (true)
                    {
                        Array.Resize(ref data, totalBytesRead + dataBlock + 1);
                        int bytesRead = zipStream.Read(data, totalBytesRead, dataBlock);
                        if (bytesRead == 0)
                        {
                            break;
                        }
                        totalBytesRead += bytesRead;
                    }
                    Array.Resize(ref data, totalBytesRead);
                    return data;
                }
                catch
                {
                    return null;
                }
            }


        }

    }
}




