<?php
  $number = 33;
  $message = "Welcome";
  if( isset( $_POST ["submit"] )){
    $guessedNo = (int) $_POST ["guessedNo"];
    $nOfTries = (int) $_POST ["nOfTries"];
    if($guessedNo !== $number){
      $message = "Incorrect";
    }else{
      $message = "Correct";
    }
    $nOfTries++;
  }
?>
<!DOCTYPE html>
<head>
  <title>Guess the number game</title>
</head>
<body>
  <?php print $message?>
  <form action="<?php print $_SERVER ['PHP_SELF'] ?>" method="post">
    No of Tries: <?php isset($nOfTries) && print $nOfTries ?><br/>
    <input type="hidden" name="nOfTries" value="<?php isset($nOfTries) && print $nOfTries ?>">
    Enter your guess here:
    <input type="number" name="guessedNo" value="<?php isset($guessedNo) & print $guessedNo ?>">
    <input type="submit" name="submit" value="Submit">
  </form>
</body>
</html>