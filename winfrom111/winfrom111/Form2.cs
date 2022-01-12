
using System;
using System.Net.Mail;
using System.Windows.Forms;
using outlook = Microsoft.Office.Interop.Outlook;

namespace winfrom111
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }
     
        private void textBox4_TextChanged_1(object sender, EventArgs e)
        {

        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }

        private void richTextBox1_TextChanged_1(object sender, EventArgs e)
        {

        }

        private void treeView1_AfterSelect_1(object sender, TreeViewEventArgs e)
        {
            
        }


        private void textBox7_TextChanged(object sender, EventArgs e)
        {
          //  textBox7.Text = treeView1.SelectedNode.Text;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFile = new OpenFileDialog();
            openFile.InitialDirectory = Application.StartupPath;
            openFile.FileName = "";
            openFile.RestoreDirectory = true;
            openFile.Multiselect = false;


            if (openFile.ShowDialog() == DialogResult.OK)
            {

                string fileName = openFile.FileName;

                treeView1.Nodes.Add(fileName);
                textBox7.AppendText(fileName);
            }
        }

        private void button4_Click_1(object sender, EventArgs e)
        {
            if (treeView1.SelectedNode != null)
            {

                TreeNode tempNode = treeView1.SelectedNode;

                treeView1.Nodes.Remove(tempNode);
            }
            else
            {
                MessageBox.Show("请选择要删除的附件。");
            }
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
           
            string a = richTextBox1.Text;
            string b = textBox4.Text;
            string c = textBox5.Text;
            string d = textBox7.Text;
            Program.send(b,c,d,a);

        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {

        }
    }
}

