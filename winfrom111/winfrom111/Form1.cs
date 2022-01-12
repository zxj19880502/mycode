using System;
using System.Data;
using System.Windows.Forms;
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;
using CompressDataSet;

namespace winfrom111
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }       

        private void button3_Click(object sender, EventArgs e)
        {
            Form2 f = new Form2();

            f.ShowDialog();
        }

        private void button4_Click(object sender, EventArgs e)
        {
           
            w.WebService1 ds = new w.WebService1();
                DateTime dtBegin = DateTime.Now;
            string vCmd = this.richTextBox1.Text;
            byte[] zipBuffer = ds.GetDataSetSurrogateZipBytes(vCmd);
                byte[] buffer = Program.UnZipClass.Decompress(zipBuffer);
                 BinaryFormatter ser = new BinaryFormatter();
                DataSetSurrogate dss = ser.Deserialize(new MemoryStream(buffer)) as DataSetSurrogate;
                 DataSet dataSet = dss.ConvertToDataSet();
                 this.label2.Text = string.Format("耗时：{0}", DateTime.Now - dtBegin) + "  " + zipBuffer.Length;
                 binddata(dataSet);

        }

        private void binddata(DataSet dataSet)

        {

            this.dataGridView1.DataSource = dataSet.Tables[0];

            this.label3.Text = "共计：" + dataSet.Tables[0].Rows.Count + "条记录";

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
        private void button2_Click(object sender, EventArgs e)
        {

            string a = "DC.xls";

           Program. ExportExcels(a, dataGridView1);

        }
        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

     
    }
}
