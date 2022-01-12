using System;
using System.Data;
using System.Windows.Forms;
using System.Data.OracleClient;
using System.Collections.Generic;

namespace WindowsFormsApp3
{
    public partial class Form1 : Form
    {
       
        public Form1()
        {
            InitializeComponent();

        }





        private void button1_Click(object sender, EventArgs e)
        {

            string datetime1 = dateTimePicker1.Value.ToString("yyyy/MM/dd ");
            string datetime2 = dateTimePicker2.Value.ToString("yyyy/MM/dd ");

            string parame1;
            parame1 = textBox1.Text.Trim();
            if (parame1 == "")
            {
                MessageBox.Show("请输入工单号码！");
                textBox1.Focus();
                return;
            }


            string connString = "User ID=用户名;Password=密码;Data Source=(DESCRIPTION = (ADDRESS_LIST= (ADDRESS = (PROTOCOL = TCP)(HOST = 172.22.10.246)(PORT = 1521))) (CONNECT_DATA = (SERVICE_NAME = TDBNEW)))";

            OracleConnection conn = new OracleConnection(connString);

            conn.Open();


           
            OracleDataAdapter sda = new OracleDataAdapter("select * from G_PACK_BOX WHERE WORK_ORDER = '" + parame1 + "' AND CREATE_TIME between to_date('" + datetime1 + "','yyyy/mm/dd hh24:mi:ss')and to_date('" + datetime2 + "','yyyy/mm/dd hh24:mi:ss') ", conn);
            DataTable dt = new DataTable();

            sda.Fill(dt);


            this.dataGridView1.DataSource = dt;








            dt.Clone();

            conn.Close();

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


        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            
        }

        private void dateTimePicker2_ValueChanged(object sender, EventArgs e)
        {

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            string a = "F:" + "\\DC.xls";
            ExportExcels(a, dataGridView1);
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void chart1_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }
    }
    
}
    

  
    

