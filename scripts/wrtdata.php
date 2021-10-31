<?php
$currsku = fopen("currdata.txt", "w");
$txt = $_POST['sku'];
fwrite($currsku, $txt);
fclose($currsku);
?>