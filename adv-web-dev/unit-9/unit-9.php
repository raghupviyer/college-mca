<?php
  function msg($name, $desg){
    return "Hello $desg $name";
  }

  echo msg("Daniel", "Mr.");

  // call by refrence
  function incr(&$x){
    // so if the value of the argument called by refrence is changed in the function, 
    // it ill reflect every other place that variable is used
    $x++;
    echo "<br/>";
  }

  $arr1 = array("red", "green", "blue");
  echo "<br/>";
  print_r($arr1);
  echo "<br/>";
  print_r(str_replace("green","pink",$arr1, $i));
  echo "<br/> Replacing $i th position";
?>