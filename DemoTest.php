<?php

$user = 'root';
$password = 'root';
$db = 'DBTest';
$host = 'localhost';
$port = 8889;

$link = mysqli_init();
$success = mysqli_real_connect($link, $host, $user, $password, $db, $port);

$id = $_POST['id'];
$name = $_POST['name'];
$city = $_POST['city'];
$zipCode = $_POST['zip_code'];

$querySent = "insert into customer(customer_id, customer_name, customer_city, customer_zipcode)
values(".$id.", '" .$name. "', '" .$city. "', ".$zipCode.");";

echo "<h1> $querySent </h1>";

$test = $link->query($querySent);
var_dump($test);

$ans = $link->query("select * from customer");

$strAns = $ans->fetch_all();

foreach ($strAns as $item)
{
    echo "$item[1] $item[2] </br>";
}
$link->close();

// another comment to test