<!DOCTYPE html>
<html>
<head>
<style>
body {
  margin: 0;
  min-width: 250px;
  background-color: #f9f9f9;
}
input[type=text]{
  border: none;
  width: 75%;
  padding: 10px;
  float: left;
  font-size: 16px;
}
.submit{
  padding: 10px;
  width: 25%;
  background: #ff8c00;
  color: #555;
  float: left;
  text-align: center;
  font-size: 16px;
  cursor: pointer;
  transition: 0.3s;
}
.submit:hover {
  background-color: #bbb;
}
</style>
<body>
<form action = "createaccount.php" method="post">
    <h1> Please enter your information to create a new login account</h1>
    <p>  
        <label>Login Name:</label><input type = "text"  name = "name" />
        <label>Password:</label><input type = "password" name = "pwd" />
        <br/><br/>
    </p>
    <input type = "submit"  id = "submit" value = "submit"/>
    <input type = "reset"  id = "reset" value = "reset"/>
</form>
</body>
</html>