using System;
using System.Data;
using System.Windows.Forms;
using System.Data.OleDb;
using System.Data.OracleClient;

namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }
        public DataSet LoadDataFromExcel(string filePath)
        {
            try
            {
                string strConn;
                strConn = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + filePath + ";Extended Properties='Excel 8.0;HDR=False;IMEX=1'";
                OleDbConnection OleConn = new OleDbConnection(string.Format(strConn));
                OleConn.Open();
                String sql = "SELECT * FROM  [Sheet1$]";

                OleDbDataAdapter OleDaExcel = new OleDbDataAdapter(sql, OleConn);
                DataSet OleDsExcle = new DataSet();
                OleDaExcel.Fill(OleDsExcle, "Sheet1");
                OleConn.Close();
                return OleDsExcle;
            }
            catch (Exception err)
            {
                MessageBox.Show("数据绑定Excel失败!失败原因：" + err.Message, "提示信息",
                    MessageBoxButtons.OK, MessageBoxIcon.Information);
                return null;
            }
        }

        public void addData(DataSet obj)
        {
            try
            {
                string strConnect = "Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=172.22.10.246)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=XE)));User Id=用户名;Password=密码;";
                
                OracleConnection dbConn = new OracleConnection(strConnect);
                dbConn.Open();

                foreach (DataTable dt in obj.Tables) 
                {
                    foreach (DataRow dr in dt.Rows) 
                    {
                        string sql = string.Format("INSERT INTO G_SN_COUNT(WORK_ORDER,PART_ID,PDLINE_ID,STAGE_ID,PROCESS_ID,SHIFT_NAME,WORK_DATE,WORK_TAME,PASS_QTY,FAIL_QTY,REPASS_QTY,REFAIL_QTY,OUTPUT_QTY,MACHINE_ID,TIMES,SHIFT_ID,CREATE_TIME) VALUES(seq_aml_blacklist_new.nextval," + Convert.ToInt32(dr["工单号码"]) + ",'" + dr["机种"] + "','" + dr["线别"] + "','" + dr["区段别"] + "','" + dr["制程别"] + "','" + dr["班别"] + "','" + dr["日期"] + "'','" + dr["时间"] + "'','" + dr["良品数"] + "'','" + dr["不良品数"] + "'','" + dr["重流良品数"] + "'','" + dr["重流不良品数"] + "'','" + dr["产出数"] + "'','" + dr["机台"] + "'','" + dr["设备运行时间"] + "'','" + dr["？？"] + "'','" + dr["  "] + "')");
                        MessageBox.Show(sql);
                        OracleCommand aCommand = new OracleCommand(sql, dbConn);
                        aCommand.ExecuteNonQuery();
                    }
                }
                MessageBox.Show("数据上传成功！");
                dbConn.Close();
            }
            catch (Exception e)
            {
                MessageBox.Show(e.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            DataSet dts = LoadDataFromExcel(textBox1.Text);
            if (dts == null)
            {
                MessageBox.Show("数据为空！");
            }
            else
            {
                MessageBox.Show("数据不为空!");
                addData(dts);
            }

        }

        private static void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFiledialog1 = new OpenFileDialog();
            openFiledialog1.Filter = "Excel文件|*.xls";
            openFiledialog1.ShowDialog();
            textBox1.Text = openFiledialog1.FileName;

        }

       
    }
}
