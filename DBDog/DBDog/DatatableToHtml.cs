using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Data;


namespace DBDog
{
    class DatatableToHtml
    {
        public static string GetHtmlString(DataTable tbl)
        {
            StringBuilder sb = new StringBuilder();

            sb.Append("<table cellSpacing='0' cellPadding='0' width ='100%' border='1'>"); 
            sb.Append("<tr valign='middle'>");
            foreach (DataColumn column in tbl.Columns)
            {
                sb.Append("<td><b><span>" + column.ColumnName + "</span></b></td>");
            }
            sb.Append("</tr>");
            int iColsCount = tbl.Columns.Count;
            int rowsCount = tbl.Rows.Count - 1;
            for (int j = 0; j <= rowsCount; j++)
            {
                sb.Append("<tr>");
            //    sb.Append("<td>" + ((int)(j + 1)).ToString() + "</td>");
                for (int k = 0; k <= iColsCount - 1; k++)
                {
                    sb.Append("<td");
                    sb.Append(">");
                    object obj = tbl.Rows[j][k];
                    if (obj == DBNull.Value)
                    {
                        // 如果是NULL则在HTML里面使用一个空格替换之
                        obj = "&nbsp;";
                    }
                    if (obj.ToString() == "")
                    {
                        obj = "&nbsp;";
                    }
                    string strCellContent = obj.ToString().Trim();
                    sb.Append("<span>" + strCellContent + "</span>");
                    sb.Append("</td>");
                }
                sb.Append("</tr>");
            }
            sb.Append("</TABLE>");
            return sb.ToString();
        }
    }
}
