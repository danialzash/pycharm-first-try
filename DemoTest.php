<?php

$user = 'root';
$password = 'root';
$db = 'DBTest';
$host = 'localhost';
$port = 8889;

$link = mysqli_init();
$success = mysqli_real_connect($link, $host, $user, $password, $db, $port);

$ans = $link->query("select * from customer");

$strAns = $ans->fetch_all();

foreach ($strAns as $item)
{
    echo "$item[1] $item[2] </br>";
}
$link->close();

echo "<h1>" . $_POST['name']."</h1>";
echo $_POST['lname'];