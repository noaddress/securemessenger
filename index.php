<?php
print("user: ".$_GET["user"]);
print("<br>");
print("text: ".$_GET["text"]);
 $file=fopen($_GET["user"].".txt","a") or exit("Unable to write file!");
 fwrite($file,"%26");
 fwrite($file,$_GET["text"]);
 fclose($file);
?>
