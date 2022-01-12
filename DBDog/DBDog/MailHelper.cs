using System.Net;
using System.Net.Mail;
using System.Linq;

namespace DBDog
{
    class MailHelper
    {
        string SMTPSvr;
        string FromName;
        string From;

        public MailHelper(string argSMTPSvr = "172.22.8.5", string argFromName = "WRS邮件系统", string argFrom = "WRS@sz.chiconypower.com.cn")
        {
            SMTPSvr = argSMTPSvr;
            FromName = argFromName;
            From = argFrom;
        }
        public string SendMailWithIPAddr(string To, string EmailTitle, string EmailHtmlBody)
        {
            string IPAddr=GetIPAddr();
            return SendMail(To,EmailTitle,EmailHtmlBody+"<br/>"+IPAddr);
        }
        private string SendMail(string To, string EmailTitle, string EmailHtmlBody)
        {
            //string To1 = "Jack_Wei@sz.chiconypower.com.cn,13913700503@139.com,szmis-staff@sz.chiconypower.com.cn,Hope_Tang@sz.chiconypower.com.cn,Yy_Jia@sz.chiconypower.com.cn,Wendy_Wen@sz.chiconypower.com.cn";
            //if (To1 != To)
            //    To = To1;
            //else
            //    To = To1;

            System.Net.Mail.MailMessage msg = new System.Net.Mail.MailMessage();
            To = To.Replace(';', ',').Trim();
            msg.To.Add(To);
            //msg.To.Add("b@b.com");//可以发送给多人 
            //msg.CC.Add("c@c.com");可以抄送给多人 

            msg.From = new MailAddress(From, FromName, System.Text.Encoding.UTF8);
            /* 上面3个参数分别是发件人地址（可以随便写），发件人姓名，编码*/
            msg.Subject = EmailTitle;//邮件标题 
            msg.SubjectEncoding = System.Text.Encoding.UTF8;//邮件标题编码 
            msg.Body = EmailHtmlBody;//邮件内容 
            msg.BodyEncoding = System.Text.Encoding.UTF8;//邮件内容编码 
            msg.IsBodyHtml = true;//是否是HTML邮件 
            msg.Priority = MailPriority.Normal;//邮件优先级 

            SmtpClient client = new SmtpClient();
            client.Host = this.SMTPSvr;
            //smtp server
            //object userState = msg;
            try
            {
                //client.SendAsync(msg, userState);
                //简单一点儿可以client.Send(msg);
                 client.Send(msg);
                return "OK";

            }
            catch (System.Net.Mail.SmtpException ex)
            {
                return "Send Fail!: " + ex.ToString();
            }
        }
        private string  GetIPAddr()
        {
            IPAddress[] ipList = Dns.GetHostAddresses(Dns.GetHostName());
            var list = ipList.ToList<IPAddress>();
            var ipV4Addr = from i in list
                           where i.AddressFamily == System.Net.Sockets.AddressFamily.InterNetwork
                           select i.ToString();
            string rst = string.Join(";", ipV4Addr.ToArray());
            return rst;
        }
    }
}
