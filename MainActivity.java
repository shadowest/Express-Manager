package com.example.kunpeng_weather;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Build;
import android.os.Bundle;
import android.os.StrictMode;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


public class MainActivity extends AppCompatActivity {
    private TextView edittext;
    private TextView tem;
    private TextView tem1;
    private TextView tem2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //定义函数
        edittext = (TextView) findViewById(R.id.editText1);
        Button button = (Button) findViewById(R.id.button1);
        final TextView temp = findViewById(R.id.tem);
        final TextView temp1 = findViewById(R.id.tem1);
        final TextView temp2 = findViewById(R.id.tem2);
        if (android.os.Build.VERSION.SDK_INT > 9) {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }
        //添加点击事件
        button.setOnClickListener(new View.OnClickListener() {
            @RequiresApi(api = Build.VERSION_CODES.KITKAT)
            @SuppressLint("SetTextI18n")
            @Override
            public void onClick(View v) {
                //获取editText控件的数据
                String my_string = edittext.getText().toString();
                //判断有无输入
                if (TextUtils.isEmpty(my_string)) {
                    //在手机上输出
                    //Toast.LENGTH_SHORT:函数功能为显示时间短
                    //Toast.LENGTH_LONG :显示时间长
                    Toast.makeText(MainActivity.this, "没有数据输入", Toast.LENGTH_LONG).show();
                } else {
                    //驱动程序名
                    String driver = "com.mysql.jdbc.Driver";
                    //URL指向要访问的数据库名mydata
                    String url = "jdbc:mysql://116.63.34.228:3306/delivery";
                    //MySQL配置时的用户名
                    String user = "bupt";
                    //MySQL配置时的密码
                    String password = "654321";
                    Connection conn;
                    int flag = -1;
                    Statement stmt;
                    String id;
                    String name = null;
                    String tel = null;
                    String status = null;
                    try{
                        Class.forName(driver);
                        conn = DriverManager.getConnection(url,user,password);
                        stmt = conn.createStatement();
                        String sql;
                        sql = "SELECT ID, NAME, TEL, Status FROM delivery";
                        ResultSet rs = stmt.executeQuery(sql);
                        while(rs.next()){
                            flag = 0;
                            // 通过字段检索
                            id  = rs.getString("ID");
                            name  = rs.getString("NAME");
                            tel = rs.getString("TEL");
                            status = rs.getString("Status");

                            System.out.print("ID: " + id);
                            System.out.print(", 站点名称: " + name);
                            System.out.print(", 站点 URL: " + tel);
                            System.out.print("\n");

                            if(my_string.equals(id)) {
                                flag = 1;
                                break;
                            }
                        }
                        if(flag==1){
                            temp.setText("姓名:" + name);
                            temp1.setText("电话:" + tel.substring(0, 3) + "****" + tel.substring(7, 11));
                            temp2.setText("取件状态:" + status);
                        }else {
                            temp.setText("");
                            temp1.setText("");
                            temp2.setText("");
                            Toast.makeText(MainActivity.this, "快递单号错误", Toast.LENGTH_LONG).show();
                        }

                        rs.close();
                        stmt.close();
                        conn.close();
                    }catch (Exception e) {
                        System.out.println("发送GET请求出现异常！" + e);
                        e.printStackTrace();
                    }
                }
            }
        });

    }

}
