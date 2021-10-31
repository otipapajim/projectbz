<?php
require 'config.php';

$myemail = mysqli_real_escape_string($conn, $_POST['myemail']);
$mypassword = mysqli_real_escape_string($conn, $_POST['mypassword']);


$sql = "SELECT * FROM users WHERE email = '$myemail' AND pwd = '$mypassword' ";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo json_encode(array('success' => 1));
}
else {
    echo json_encode(array('success' => 0));
}
$conn->close();


?>