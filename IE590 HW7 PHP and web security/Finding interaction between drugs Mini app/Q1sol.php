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
.submit_btn{
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
.submit_btn:hover {
  background-color: #bbb;
}
</style>
</head>
<body >
<form method="get" action="Q1.php">
<h2>Enter Drug 1: <input type="text" name="drugone"></h2>
<h2>Enter Drug 2: <input type="text" name="drugtwo"></h2>
  <input type="submit" class="submit_btn">
</form>
</body>
</html>