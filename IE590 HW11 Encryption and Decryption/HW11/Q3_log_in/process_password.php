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
<script>
function encode_encrypt(){
    var str=document.getElementById("pwd");
    var values = [];
    for (i=0; i < str.value.length; i++){
    values.push(str.value.charCodeAt(i));
    }
    
    var pr = 0;
    var tmp = 0;
    for (i=0; i < values.length; i++){
        tmp = parseInt(values[i]);
        pr = pr + tmp;
    }
    
			
    function gcd_two_numbers(x, y) {
    if ((typeof x !== 'number') || (typeof y !== 'number')) 
    return false;
    x = Math.abs(x);
    y = Math.abs(y);
    while(y) {
    var t = y;
    y = x % y;
    x = t;
    }
    return x;
    }

	//
    var z = Math.pow(pr, 7);
    //alert(pr);
	//n is a large prime no. 
	var n = 68921165197333432780723328886913639248410009106281096788582947499706088155929;
	
	//transfer this value to our message = m 
	var m = pr ;

	
	//now we check if the message m is relatively prime to n 
	i = 0 
	while(i<100000){
		if(gcd_two_numbers(m,n)==1){
			break;
	}else{
		m = m + 1;
		i = i + 1 
	}
    }
	
    //now have to send this value of m to the server but must encrypt it before 	
	var c = z % n;
    alert(c);
	
	//we send the value of c from the client to the server to client (this is encrypted) 
	$.ajax({
	type: 'POST',
	url: 'process_password.php',
	data: {'enmessage': c},
});
}

</script>
</body>
</html>

