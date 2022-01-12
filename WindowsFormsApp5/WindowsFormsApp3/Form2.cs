using System;

using System.Windows.Forms;

using System.Net.Mail;
using System.Net.Mime;
using System.Net;
using System.IO;
using System.Text;
using outlook = Microsoft.Office.Interop.Outlook;

namespace WindowsFormsApp3
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

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }



        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox11_TextChanged(object sender, EventArgs e)
        {

        }





        private void button4_Click(object sender, EventArgs e)
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
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {

            string user1;
            user1 = textBox2.Text.Trim();
            if (user1 == "")
            {
                MessageBox.Show("你的mail邮箱地址");
                textBox2.Focus();
                return;
            }




            string password1;
            password1 = textBox3.Text.Trim();
            if (password1 == "")
            {
                MessageBox.Show("你的mail SMTP授权码");
                textBox3.Focus();
                return;
            }



            string mailAddress1;
            mailAddress1 = textBox5.Text.Trim();
            if (mailAddress1 == "")
            {
                MessageBox.Show("你的mail地址");
                textBox5.Focus();
                return;
            }



            string ToAddress1;
            ToAddress1 = textBox6.Text.Trim();
            if (ToAddress1 == "")
            {
                MessageBox.Show("对方邮箱地址");
                textBox6.Focus();
                return;
            }

            string biaoti1;
            biaoti1 = textBox11.Text.Trim();
            if (biaoti1 == "")
            {
                MessageBox.Show("邮件标题");
                textBox11.Focus();
                return;
            }

            string neirong1;
            neirong1 = richTextBox1.Text;
            if (neirong1 == "")
            {
                MessageBox.Show("邮件内容");
                richTextBox1.Focus();
                return;
            }


            if (user1 == ToAddress1)
            {
                MessageBox.Show("发件邮箱不能是收件邮箱");
                return;
            }

            try
            {

                System.Net.Mail.SmtpClient client = new System.Net.Mail.SmtpClient(textBox1.Text);

                string strFrom = string.Empty;
                if (textBox1.Text.ToString() == "smtp.163.com")

                    strFrom = textBox2.Text;

                else
                    strFrom = textBox2.Text;



                MailAddress from = new MailAddress(strFrom, textBox2.Text, Encoding.UTF8);

                MailAddress to = new MailAddress(textBox6.Text, textBox6.Text, Encoding.UTF8);


                MailMessage message = new MailMessage(from, to);


                foreach (TreeNode treeNode in treeView1.Nodes)
                {

                    string fileName = treeNode.Text;

                    if (File.Exists(fileName))
                    {

                        Attachment attach = new Attachment(fileName);

                        ContentDisposition disposition = attach.ContentDisposition;
                        disposition.CreationDate = System.IO.File.GetCreationTime(fileName);
                        disposition.ModificationDate = System.IO.File.GetLastWriteTime(fileName);
                        disposition.ReadDate = System.IO.File.GetLastAccessTime(fileName);

                        message.Attachments.Add(attach);
                    }
                    else
                    {
                        MessageBox.Show("文件" + fileName + "未找到！");
                    }
                }


                message.Subject = textBox11.Text;
                message.SubjectEncoding = Encoding.UTF8;
                message.Body = richTextBox1.Text;
                message.BodyEncoding = Encoding.UTF8;


                client.DeliveryMethod = SmtpDeliveryMethod.Network;
                message.BodyEncoding = System.Text.Encoding.UTF8;
                message.IsBodyHtml = true;


                if (textBox1.SelectedText == "smpt.163.com")
                    client.EnableSsl = false;
                else
                    client.EnableSsl = true;


                client.UseDefaultCredentials = false;
                string username = textBox2.Text;
                string passwd = textBox3.Text;

                NetworkCredential myCredentials = new NetworkCredential(username, passwd);
                client.Credentials = myCredentials;

                client.Send(message);

                MessageBox.Show("发送成功!");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

       

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            textBox4.Text = treeView1.SelectedNode.Text;
        }

        private void button1_Click(object sender, EventArgs e)
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


        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {


            string fujian;
            fujian = textBox4.Text.Trim();
            if (fujian == "")
            {
                MessageBox.Show("请选择添加附件");
                textBox4.Focus();
                return;
            }

            outlook.Application myapp = new outlook.Application();
            outlook.MAPIFolder myFolder = myapp.GetNamespace("MAPI").GetDefaultFolder(outlook.OlDefaultFolders.olFolderTasks);
            outlook.MailItem myItem = (outlook.MailItem)myFolder.Items.Add(outlook.OlItemType.olMailItem);
            myItem.Attachments.Add(fujian, outlook.OlItemType.olMailItem, 1, "emal");
            myItem.Subject = textBox11.Text;
            myItem.To = textBox6.Text;
            myItem.Body = richTextBox1.Text;
            myItem.Send();
            MessageBox.Show("发送成功");

           
        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {
           
        }
    }
}

