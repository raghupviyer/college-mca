<?php
  print_r($_FILES);
  if(isset($_POST['submitButton'])){
    $name = $_FILES["fileInput"]['name'];
    // $size = $_FILES["fileInput"]['size'];
    $tmpName = $_FILES['fileInput']['tmp_name'];
    $explode = explode('.', $name);
    $ext = strtolower(end($explode));
    // $perm_ext = array('jpeg', 'jpg', 'png', 'gif', 'txt');
    if(is_uploaded_file($tmpName)){
      move_uploaded_file($tmpName, 'img/'.$name);
      echo "$name file uploaded sucessfully";
    }else{
      echo $ext." file cannot be uploaded";
    }
  }
?>