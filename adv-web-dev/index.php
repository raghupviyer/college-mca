<?php
  echo  "Jesus loves you"
?>

<?php echo 'if you want to serve PHP code in XHTML or XML documents,
                use these tags'; ?>

<? echo 'this code is within short tags, but will only work '.
'if short_open_tag is enabled'; ?>

<?php echo "Some text"; ?>
No newline

<?= "But newline now" ?>

<?php

$a_bool = true;
$a_str = "hello";
$a_str2 = 'string 2';
$an_int = 33;

echo get_debug_type($a_bool);

if(is_int($an_int)){
  $an_int += 4;
}

// var_dump($an_int); 

if(is_string($a_str)){
  // var_dump($a_str);
}

$string = "5";
// var_dump((int)$string); 

$array = ["one", "two", "three"];

// var_dump($array);

$array = [
  "foo" => "fooo",
  "bar" => "baarr",
];

var_dump($array);

$array = array(1, 2, 3, 4, 5);
print_r($array);

// Now delete every item, but leave the array itself intact:
foreach ($array as $i => $value) {
    unset($array[$i]);
}
print_r($array);

// Append an item (note that the new key is 5, instead of 0).
$array[] = 6;
print_r($array);

// Re-index:
$array = array_values($array);
$array[] = 7;
print_r($array);
?>
<div>
  <?php
    echo "hello";
  ?>
</div>
<div>
  <?php
    print "Jesus loves you";
  ?>
</div>

<?php
class Vehicle{
  function model(){
    $model_name = "BMW";
    echo "Vehicle Model: ".$model_name;
  }
}
$obj = new Vehicle();
$obj -> model();
?>
hi
<?php
  function myFunction()
  {
    $x = 6;
    echo "Result1: $x , ";
  }
  myFunction();
  echo "Result2: $x";

  $name = "name";
  echo ("Hello $name <br/>");

  var_dump (print "welcome");

  echo strpos("Hello, Includehelp!", "Includehelp!");

  $x = -23.45;
echo var_dump(is_int($x));

  // $SMTP = smtp.secureserver.net;
  mail('raghupviyer@gmail.com', 'none', 'hi how are you');
?>