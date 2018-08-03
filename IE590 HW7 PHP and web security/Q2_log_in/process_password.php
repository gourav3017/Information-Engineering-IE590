<html>
<body>
<?php


function test_input($data){
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
if($_SERVER["REQUEST_METHOD"] == "POST"){
    $username = test_input($_POST["name"]);
    $password = test_input($_POST["pwd"]);
}

$userListFile = "accounts.txt";
$passListFile = "passwords.txt";
$usernameList = file($userListFile,FILE_IGNORE_NEW_LINES);
$passwordList = file($passListFile,FILE_IGNORE_NEW_LINES);

$i = 0 ;
foreach($usernameList as $user){
    if($user == $username && $passwordList[$i]==$password){
        include "todo.html";
		echo '<h2><a href="Q2login.php">Sign out</a></h2>';
            exit;
    }
    $i = $i + 1;
}
echo "Invalid username or password. Please check the entries ";

?>

</body>
</html>

