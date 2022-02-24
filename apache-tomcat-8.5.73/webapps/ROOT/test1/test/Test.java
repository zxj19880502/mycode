package test;

public class Test {

    String user = "sajet";
    String password = "tech";
    String url ="jdbc:oracle:thin:@172.22.24.221:1521:ledmes1";//orcl表示你的SID
//        String url="jdbc:oracle:thin:@localhost:1521:orcl";
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;
    public Dbconn(){
        try {
            //注册驱动程序
            DriverManager.registerDriver(new oracle.jdbc.driver.OracleDriver());
            //获得数据库连接
            conn = DriverManager.getConnection(url,user,password);
            //设置为自动提交
            conn.setAutoCommit(true);
//            建立Statement对象
            stmt =conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,ResultSet.CONCUR_READ_ONLY);
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
//        System.out.println("hello");
    }
    //查询语句方法
    public ResultSet executeQuery(String sql){
        try {
            rs = stmt.executeQuery(sql);
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        return rs;
    }
    //下面测试
    public static void main(String[] args){
        String sql = "select * from sajet.g_sn_count";
        
        ResultSet rs = new Dbconn().executeQuery(sql);
        try {
            while(rs.next()){
                System.out.println(rs.getString(1)+"  "+rs.getString(2)+"  "+rs.getString(3)+"  "+rs.getString(4));
                
            }
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        System.out.println("henolks");
    }
    
    }