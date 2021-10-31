<?php
error_reporting(0);
$servername="localhost";
$username="root";
$pwd="r6eAbana@wasak1";
$dbname="sas";

$conn = new mysqli($servername, $username, $pwd, $dbname);

if ($conn->connect_error) {
die("<h2>Database Connection Failure : " . $conn->connect_error . "</h2><hr>");
}
?>