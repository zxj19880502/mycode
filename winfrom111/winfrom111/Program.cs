using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using outlook = Microsoft.Office.Interop.Outlook;

namespace winfrom111
{
    static class Program
    {
        /// <summary>
        /// 应用程序的主入口点。
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }


        public static void send(string textBox4, string textBox5, string textBox7, string richTextBox1)
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


        public static void ExportExcels(string fileName, DataGridView myDGV)
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

        public static class UnZipClass
        {
            /// <summary>
            /// Decompresses the specified data.
            /// </summary>
            /// <param name="data">The data.</param>
            /// <returns></returns>
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