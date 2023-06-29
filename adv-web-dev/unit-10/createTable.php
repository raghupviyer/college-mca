<?php 
  function createRows($data){
    print("
      <table>
      <thead>
        <td>id</td>
        <td>usn</td>
        <td>name</td>
        <td>branch</td>
        <td>age</td>
      </thead>
      <tbody>");
    foreach($data as $row){
      print("<tr>");
      foreach($row as $column){
        print("<td>$column</td>");
      }
      print("</tr>");
    }
    print("</tbody>
    </table>
      ");
  }
?>