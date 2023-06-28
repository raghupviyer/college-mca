package com.example;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/MyServlet")
public class MyServlet extends HttpServlet{
  public MyServlet(){
    super();
  }
  public void service(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException{
    String username = req.getParameter("pname");
    PrintWriter result = res.getWriter();
    result.print(username);
  }
  @Override
  protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException{
    PrintWriter out = res.getWriter();
    out.println(getServletInfo());
    out.print("<html>");
    out.print("<head>");
    out.print("<title>Servlet Page</title>");
    out.print("</head>");
    out.print("<body>");
    out.print("<h1>Jesus Saves</h1>");
    out.print("</body>");
    out.print("</html>");
  }
}
