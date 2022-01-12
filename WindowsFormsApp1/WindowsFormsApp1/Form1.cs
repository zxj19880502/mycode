using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Oracle.ManagedDataAccess.Client;
using Microsoft.Office.Interop.Excel;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            string parame1;
            parame1 = textBox1.Text.Trim();
            if (parame1 == "")
            {
                MessageBox.Show("请输入工单号码！");
                textBox1.Focus();
                return;
            }

            string datatime;
            datatime = textBox2.Text.Trim();
            if (datatime == "")
            {
                MessageBox.Show("请输入日期！");
                textBox2.Focus();
                return;
            }

            string connectionString = "User Id=用户名; password=密码;Data Source=172.22.10.246:1521/TDBNEW; Pooling=false;";
            OracleConnection con = new OracleConnection();
            con.ConnectionString = connectionString;
            try
            {
                con.Open();
             
                OracleCommand com = con.CreateCommand();

                com.CommandText = "select WORK_ORDER 工单号码,PART_ID 机种,PDLINE_ID 线别,STAGE_ID 区段别,PROCESS_ID 制程别,WORK_DATE 时间,PASS_QTY 良品数,FAIL_QTY 不良数,OUTPUT_QTY 产出数 from G_SN_COUNT where WORK_ORDER = '" + parame1 + "'and WORK_DATE = '" + datatime +"'";
                OracleDataReader odr = com.ExecuteReader();
                OracleDataAdapter oraDA = new OracleDataAdapter(com);
                DataSet ds = new DataSet();
                oraDA.Fill(ds);
                while (odr.Read())
                    {
                    System.Data.DataTable dtbl = ds.Tables[0];
                    this.dataGridView1.DataSource = dtbl;

                   
                }
                    odr.Close();
                
            }
            finally
            {
                con.Close();
            }
        }

        private void ExportExcels(string fileName, DataGridView myDGV)
        {
            string saveFileName = "";
            SaveFileDialog saveDialog = new SaveFileDialog();
            saveDialog.DefaultExt = "xls";
            saveDialog.Filter = "Excel文件|*.xls";
            saveDialog.FileName = fileName;
            saveDialog.ShowDialog();
            saveFileName = saveDialog.FileName;
            if (saveFileName.IndexOf(":") < 0) return; 
            Microsoft.Office.Interop.Excel.Application xlApp = new Microsoft.Office.Interop.Excel.Application();
            if (xlApp == null)
            {
                MessageBox.Show("无法创建Excel对象，可能您的机子未安装Excel");
                return;
            }
            Microsoft.Office.Interop.Excel.Workbooks workbooks = xlApp.Workbooks;
            Microsoft.Office.Interop.Excel.Workbook workbook = workbooks.Add(Microsoft.Office.Interop.Excel.XlWBATemplate.xlWBATWorksheet);
            Microsoft.Office.Interop.Excel.Worksheet worksheet = (Microsoft.Office.Interop.Excel.Worksheet)workbook.Worksheets[1];
                                                                                                                                 
            for (int i = 0; i < myDGV.ColumnCount; i++)
            {
                worksheet.Cells[1, i + 1] = myDGV.Columns[i].HeaderText;
            }
            
            for (int r = 0; r < myDGV.Rows.Count; r++)
            {
                for (int i = 0; i < myDGV.ColumnCount; i++)
                {
                    worksheet.Cells[r + 2, i + 1] = myDGV.Rows[r].Cells[i].Value;
                }
                System.Windows.Forms.Application.DoEvents();
            }
            worksheet.Columns.EntireColumn.AutoFit();
            if (saveFileName != "")
            {
                try
                {
                    workbook.Saved = true;
                    workbook.SaveCopyAs(saveFileName);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("导出文件时出错,文件可能正被打开！\n" + ex.Message);
                }
            }
            xlApp.Quit();
            GC.Collect();
            MessageBox.Show("文件： " + fileName + ".xls 保存成功", "信息提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }




        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
           
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
           
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string a = "F:" + "\\KKHMD.xls";
            ExportExcels(a, dataGridView1);
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }
    }
    }

