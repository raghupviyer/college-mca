package com.example;

import java.sql.Statement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Savepoint;

public class jdbc {
  public static void main(String[] args) throws Exception{
    Savepoint savepoint = null;
    Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3006/ebookshop", "root", "password");
    try{
      Statement statement = connection.createStatement();
      connection.setAutoCommit(false);
      savepoint = connection.setSavepoint("savepoint 1");
      String sql = "INSERT into books (id, title, author) values (3001, \"The Earth\", \"John\")";
      statement.executeUpdate(sql);
      savepoint = connection.setSavepoint("savepoint 2");
      sql = "INSERT into books (id, title, author) values (3001, \"The Earth\", \"John\")";
      statement.executeUpdate(sql);
      connection.commit(); 
    }catch(SQLException e){
      e.printStackTrace(); 
    }
  }
}
