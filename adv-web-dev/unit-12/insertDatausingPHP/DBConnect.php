<?php 
  function OpenConnection()
  {
    $host = "localhost";
    $user = "root";
    $pass = "";
    $name = "test";
    // $connection = new mysqli($host, $user, $pass, $name) or die("connection failed". mysqli_connect_error());
    // or
    $connection = new mysqli($host, $user, $pass, $name);
    if($connection -> connect_errno){
      printf("Connection Failed%s<br/>", $connection->connect_error);
      exit();
    }
    printf("Db Connection Successful <br/>");
    return $connection;
  }

  // print_r(OpenConnection());

  function CloseConnection($connection)
  {
    $connection -> close();
  }
?>