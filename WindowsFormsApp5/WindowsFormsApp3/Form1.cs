using System;
using System.Data;
using System.Windows.Forms;
using System.Data.OracleClient;


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

            

            string parame1;
            parame1 = textBox1.Text.Trim();
            if (parame1 == "")
            {
                MessageBox.Show("请输入查询语句");
                textBox1.Focus();
                return;
            }


            string host1;
            host1 = textBox7.Text.Trim();
            if (host1 == "")
            {
                MessageBox.Show("请输入数据库 IP");
                textBox7.Focus();
                return;
            }


            string User1;
            User1 = textBox8.Text.Trim();
            if (User1 == "")
            {
                MessageBox.Show("请输入数据库用户名");
                textBox8.Focus();
                return;
            }


            string Password1;
            Password1 = textBox9.Text.Trim();
            if (Password1 == "")
            {
                MessageBox.Show("请输入数据库密码");
                textBox9.Focus();
                return;
            }

            string service1;
            service1 = textBox10.Text.Trim();
            if (service1 == "")
            {
                MessageBox.Show("请输入数据库名");
                textBox10.Focus();
                return;
            }



            string connString = "User ID=" + User1 + ";Password= " + Password1 + ";Data Source=(DESCRIPTION = (ADDRESS_LIST= (ADDRESS = (PROTOCOL = TCP)(HOST = " + host1 + ")(PORT = 1521))) (CONNECT_DATA = (SERVICE_NAME = " + service1 + ")))";

            OracleConnection conn = new OracleConnection(connString);

            conn.Open();


           
            OracleDataAdapter sda = new OracleDataAdapter("" + parame1 + "", conn);
           
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



        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            string a = "DC.xls";
            ExportExcels(a, dataGridView1);
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

       

        private void textBox7_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox8_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox9_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox10_TextChanged(object sender, EventArgs e)
        {

        }     

        private void button5_Click(object sender, EventArgs e)
        {
            Form2 f = new Form2();

            f.ShowDialog();
        }

      
    }
    
}
    

  
    

