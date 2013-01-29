<?php
if ($_GET['address'])
{
       $ret = "";
       $out = `./connect.py audiophile`;
       $list = explode("\n", $out);
       #echo $_GET['address'];
       #echo $ret; 
       #$ret = shell_exec("python /var/www/daap/connect.py '" + $_GET['address'] + "'");
       foreach($list as $playlist){
           $ret .= "<h1>$playlist</h1>";
       }
       echo $ret;
}

 ?>

