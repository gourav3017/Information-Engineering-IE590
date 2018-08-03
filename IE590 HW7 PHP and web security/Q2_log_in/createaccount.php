<!DOCTYPE html>
<html>
<body>
<?php

 if(isset($_POST['submit_btn']))
 {
  $username = $_POST['name'];
  $password = $_POST['pwd'];
  if(strlen($username)<7 || !ctype_alnum($username) || !ctype_alpha($username[0]) || strlen($password)<8 || !preg_match('/^[a-zA-Z0-9._]+$/', $password)){
	  echo "Invalid Username or Password";
  }else{
  $text1 = $username.PHP_EOL;
  $text2 = $password.PHP_EOL;
  $fp1 = fopen('accounts.txt', 'a+');
  $fp2 = fopen('passwords.txt', 'a+');

    if(fwrite($fp1, $text1))  {
        echo 'username saved to text file';

    }
    if(fwrite($fp2, $text2))  {
        echo 'password saved to text file';

    }
echo "Your account has been created";
fclose ($fp1);
fclose ($fp2);    
}
}
?>
<h2><a href="Q2login.php">Go back</a></h2>
</body>
</html>