using System;
using System.Web.Services;
using System.Data;
using System.Data.OracleClient;
using System.Configuration;
using System.IO;
using System.IO.Compression;
using System.Runtime.Serialization.Formatters.Binary;
using System.Windows.Forms;
using Class1;
using outlook = Microsoft.Office.Interop.Outlook;
using CompressDataSet;

namespace WebApplication2
{
    /// <summary>
    /// WebService1 的摘要说明
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // 若要允许使用 ASP.NET AJAX 从脚本中调用此 Web 服务，请取消注释以下行。 
    // [System.Web.Script.Services.ScriptService]
    public class WebService1 : System.Web.Services.WebService
    {


        // 定义一个sqlconnection连接成员
       // OracleConnection sqler = new OracleConnection("Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=10.0.10.17)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=MESDB)));User Id=sajet;Password=tech;");

        public WebService1()
        {

            // 如果使用设计的组件，请取消注释以下行 
            //InitializeComponent();
        }

        [WebMethod]
        public String getValue(String name)
        {
            return "欢迎你！ " + name;
        }

        [WebMethod]
        public  void Sendmail(string textBox4, string textBox5, string textBox6, string richTextBox1, string textBox7)
        {
            outlook.Application myapp = new outlook.Application();
            outlook.MAPIFolder myFolder = myapp.GetNamespace("MAPI").GetDefaultFolder(outlook.OlDefaultFolders.olFolderTasks);
            outlook.MailItem myItem = (outlook.MailItem)myFolder.Items.Add(outlook.OlItemType.olMailItem);



           myItem.Attachments.Add(textBox7, outlook.OlItemType.olMailItem, 1, "emal");

            myItem.Subject = textBox5;
            myItem.To = textBox4;
            myItem.Body = richTextBox1;
            myItem.Send();
            MessageBox.Show("发送成功");
        }




        [WebMethod(Description = "条件查询表G_SN_COUNT直接返回DataSet对象")]
        public DataSet shujuchaxun(string work_order, string startime, string endtiem)
        {
           // sqler.Open();
            OraOprater();
            DataSet ds = new DataSet();
            string sql = "select * from G_SN_COUNT WHERE WORK_ORDER = '" + work_order + "' AND CREATE_TIME between to_date('" + startime + "','yyyy/mm/dd hh24:mi:ss')and to_date('" + endtiem + "','yyyy/mm/dd hh24:mi:ss') ";

            OracleDataAdapter dt = new OracleDataAdapter(sql, conn);


            dt.Fill(ds);
            conn.Close();
            return ds;

        }

        [WebMethod(Description = "字段，表，条件，查询直接返回DataSet对象")]
        public DataSet ziduantiaojian(string ziduan,string biaoming, string tiaojian)
        {
           // sqler.Open();
            OraOprater();
            DataSet ds = new DataSet();
            string sql = "select " + ziduan + " from " + biaoming + " WHERE  " + tiaojian + "";

            OracleDataAdapter dt = new OracleDataAdapter(sql, conn);


            dt.Fill(ds);
            conn.Close();
            return ds;

        }


        [WebMethod(Description = "返回DataSet对象用Binary序列化后的字节数组")]
        public byte[] GetDataSetBytes(string vCmd)
        {
            DataSet DS = GetData(vCmd);
            BinaryFormatter ser = new BinaryFormatter();
            MemoryStream ms = new MemoryStream();
            ser.Serialize(ms, DS);
            byte[] buffer = ms.ToArray();
            return buffer;
        }



        [WebMethod(Description = "SQL查询，直接返回DataSet对象")]
        public DataSet GetData(string vCmd)
        {
          // sqler.Open();
            OraOprater();        
            string sql =""+vCmd+"";         
            OraOprater();
            DataSet ds = new DataSet();
            System.Data.OracleClient.OracleDataAdapter adp = new System.Data.OracleClient.OracleDataAdapter(sql, conn);
            adp.Fill(ds);
            conn.Close();
            return ds;
        }


        [WebMethod(Description = "返回DataSetSurrogate对象用Binary序列化并ZIP压缩后的字节数组")]
        public byte[] GetDataSetSurrogateZipBytes(string vCmd)
        {
            DataSet dataSet = GetData(vCmd);
            DataSetSurrogate dss = new DataSetSurrogate(dataSet);
            BinaryFormatter ser = new BinaryFormatter();
            MemoryStream ms = new MemoryStream();
            ser.Serialize(ms, dss);
            byte[] buffer = ms.ToArray();
            byte[] zipBuffer = Compress(buffer);
            return zipBuffer;
        }

        public byte[] Compress(byte[] data)
        {
            MemoryStream ms = new MemoryStream();
            Stream zipStream = null;
            zipStream = new GZipStream(ms, CompressionMode.Compress, true);
            zipStream.Write(data, 0, data.Length);
            zipStream.Close();
            ms.Position = 0;
            byte[] compressed_data = new byte[ms.Length];
            ms.Read(compressed_data, 0, int.Parse(ms.Length.ToString()));
            return compressed_data;
        }




        // [WebMethod]
        // public string HelloStus(string fileName, DataGridView myDGV)
        // {
        //  WebService1 cls = new WebService1();
        //   cls.ExportExcels(fileName, myDGV);

        //  return fileName;
        // }


        private OracleConnection conn = null;
        private void OraOprater()
        {
            ConnectionStringSettings settings = ConfigurationManager.ConnectionStrings["SFC"];
            string connString = settings.ConnectionString;
            conn = new OracleConnection(connString);
            try
            {
                conn.Open();
            }
            catch (Exception e)
            {
                conn.Close();
                throw e;
            }
        }


     

       



    }

}

        
