<!DOCTYPE html>
<html>
<head>
<style>
body {
  margin: 0;
  min-width: 250px;
  background-color: #FFD700;
}
input[type=text]{
  border: none;
  padding: 10px;
  font-size: 16px;
}
input[type=password]{
  border: none;
  padding: 10px;
  font-size: 16px;
}
.submit_btn{
  padding: 10px;
  width: 20%;
  background: #ff8c00;
  color: #555;
  float: left;
  text-align: center;
  font-size: 16px;
  cursor: pointer;
  transition: 0.3s;
}
.submit_btn:hover {
  background-color: #bbb;
}
.reset_btn{
  padding: 10px;
  width: 20%;
  background: #ff8c00;
  color: #555;
  float: left;
  text-align: center;
  font-size: 16px;
  cursor: pointer;
  transition: 0.3s;
}
.reset_btn:hover {
  background-color: #bbb;
}
</style>
</head>
<body>
 <form action = "process_password.php" method="POST">
      <h1> Please enter your information to login to account</h1>
        <p>  
          <label><h3>Username: </label><input type = "text"  name = "name" /></h3>
          <label><h3>Password: </label><input type = "password" name = "pwd" /></h3>
          <br/>
          <br/>
        </p>
      <input type = "submit" name="submit_btn" class="submit_btn" id = "submit" value = "Login"/>
      <input type = "reset"  name="reset_btn" class="reset_btn" id = "reset" value = "reset"/>
	  
    </form>
</body>
</html>