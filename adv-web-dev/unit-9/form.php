<?php 
  echo "hello, Praise The Lord"."<br/>";
  
  date_default_timezone_set('Asia/Kolkata');
  echo date('d-m-Y H:i:s');
  $tz = date_default_timezone_get();
  echo "<br/>";
  echo strcmp($tz, ini_get('date.timezone'));
  echo "<br/>";

  // what the if statements consider true or false
  
  if(0){
    echo "0 is true"; // 0 is not true
  }
  echo "<br/>";
  if(1){
    echo "1 is true";// 1 is true
  }
  echo "<br/>";
  if(-1){
    echo "-1 is true";// -1 is not true
  }
  echo "<br/>";
  // strcmp() returns
  // 0 - if the two strings are equal
  // <0 - if string1 is less than string2
  // >0 - if string1 is greater than string2
  // ini_get() returns the value of the configuration option upon success
  if(strcmp($tz, ini_get('date.timezone'))){
    echo 'Script timezone is different from ini-set timezone';
  }else{
    echo 'Script timezone is same as ini-set timezone';
  }
  echo "<br/>";
  
  print_r($_POST["fname"]);
  echo "<br/>";
  print_r($_POST["lname"]);
  echo "<br/>";
  print_r($_POST["submitButton"]);
  echo "<br/>";
  print_r($_POST["checkLanguage"]);
  echo "<br/>";
  print_r($_POST);
  echo "<br/>";
  
  // isset() returns bool if a variable is set or not
  // if a variable has value, then it is set
  // else it is not set
  if(isset($_POST["submitButton"])){
    $fname = $_POST["fname"];
    $lname = $_POST["lname"];
    $lang = $_POST["checkLanguage"];

    echo "
      <h2>The first name is $fname</h2>
      <h2>The last name is $lname</h2>
      <h4>The intrested languages are:</h4>
      <ul>
    ";

    foreach($lang as $p){
      echo "<li>$p</li>";
    }
    echo "</ul>";
  }else{
    echo "Form data is not submitted successfully";
  }
?>