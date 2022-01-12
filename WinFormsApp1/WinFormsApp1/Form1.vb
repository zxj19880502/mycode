
Imports System.Data.OracleClient

Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub DataGridView1_CellContentClick(sender As Object, e As DataGridViewCellEventArgs) Handles DataGridView1.CellContentClick

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click

        Dim conn As New OracleConnection
        Dim ServerIP As String = "10.0.10.17:1521/MESDB"
        conn.ConnectionString = "Data Source=" + ServerIP + ";User ID=sajet;Password=tech"


        ' Dim ConnectionString = "Password=tech;User ID=sajet;Data Source=""(DESCRIPTION =(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=10.0.10.17)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=mesdb)))"";Persist Security Info=True"

        ' Dim conn As OracleConnection = New OracleConnection(ConnectionString)

        '  Dim conn As OracleConnection = New OracleConnection()
        '  conn.ConnectionString = ConnectionString



        conn.Open()
        Dim strOraRS = "select * from G_SN_COUNT WHERE WORK_ORDER = 'M2017K08' AND CREATE_TIME between to_date('2020.04.01','yyyy/mm/dd hh24:mi:ss')and to_date('2020.04.30','yyyy/mm/dd hh24:mi:ss')"



        Dim gjqyDataSet As New DataSet
        Dim dt As New DataTable
        Dim gjqyCommand1 As OracleDataAdapter = New OracleDataAdapter(strOraRS, conn)
        ' gjqyCommand1.Fill(gjqyDataSet)
        ' dt = gjqyDataSet.Tables(0)
        'DataGridView1.DataSource = dt


        Dim MyTable As New DataTable()
        gjqyCommand1.Fill(MyTable)
        DataGridView1.DataSource = MyTable
        conn.Close()
        'MsgBox("查询成功")




        conn.Close()

    End Sub

    Dim OraDB As ADODB.Connection
    Public Sub OpenOraDB()
        On Error GoTo ToExit
        Dim OraDB_Open = False
        OraDB = New ADODB.Connection
        Dim ConnectionString = "Provider=OraOLEDB.Oracle;Password=tech;User ID=sajet;Data Source=""(DESCRIPTION =(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=10.0.10.17)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=mesdb)))"";Persist Security Info=True"

        Dim adUseServer = OraDB.CursorLocation

        OraDB.Open(ConnectionString)
        OraDB_Open = True

        Exit Sub
ToExit:
        MsgBox("连接数据库服务器错误，您可以在网络正常后继续使用。", vbInformation, "错误信息")
        OraDB_Open = False
    End Sub

    '关闭数据库
    Public Sub CloseOraDB()
        Dim OraDB_Open
        Dim adStateOpen
        If OraDB_Open = True Then
            If OraDB.State = adStateOpen Then
                OraDB.Close()
                OraDB = Nothing
                OraDB_Open = False
            End If
        End If
    End Sub




End Class
