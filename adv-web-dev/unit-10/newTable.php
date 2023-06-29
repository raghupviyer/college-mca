<?php 
  include 'DBConnect.php';
  include 'createTable.php';
  $connection = OpenConnection();
  
  $createTable = "
    create table student(
      id int not null auto_increment,
      usn varchar(100) not null,
      name varchar(100) not null,
      branch varchar(100) not null,
      age int(3),
      primary key (id)
    );    
  ";
  // if($connection -> query($createTable)){
  //   printf("student table was created succesfully");
  //   CloseConnection($connection);
  // } else {
  //   printf("could not create student table: %s <br/>", $connection->error);
  // }
  $insertData = "
    insert into student (usn, name, branch, age) values
    ('BTH1', 'Daniel', 'FULL BIBLE', 23),
    ('BTH2', 'Christ', 'FULL BIBLE', 33)
  ";

  $getData = "select * from student";
  
  $updateData = "
  update student
  set age = 24
  where usn = 'BTH1'
  ";
  
  $deleteData = "delete from student where usn = 'BTH1'";

  try {
    // $connection -> query($createTable);
    // printf("student table was created succesfully <br/>");
    // $connection -> query($deleteData);
    // printf("values were added succesfully <br/>");
    $queryResult = $connection -> query($getData);
    if(mysqli_num_rows($queryResult) > 0){
      $rows = mysqli_fetch_all($queryResult);
      createRows($rows);
    }else{
      echo "No Records";
    }
    mysqli_free_result($queryResult);
    CloseConnection($connection);
  } catch (\Throwable $e) {
    printf("could not create student table: %s <br/>", $connection -> error);
    CloseConnection($connection);
  }
?>