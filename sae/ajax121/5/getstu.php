﻿<?php
$q=$_GET["q"];
$con = mysql_connect(SAE_MYSQL_HOST_M.':'.SAE_MYSQL_PORT,SAE_MYSQL_USER,SAE_MYSQL_PASS);
if (!$con)
 {
 die('Could not connect: ' . mysql_error());
 }
 
$db_select=mysql_select_db("app_ajax121",$con);

$sql="SELECT * FROM St WHERE sno=".$q;
$sql2="SELECT COUNT(sno) FROM St WHERE sno=".$q;

$result = mysql_query($sql);
$result2= mysql_query($sql2);
$tem=mysql_fetch_array($result2);
$nu=$tem[0];
if(!$result)
{
echo "error";
}else
{
if($nu==0) echo "<p>数据库无此学生信息</p>";
while($row = mysql_fetch_array($result))
 {
 echo "<table border='1'>
 <tr>
 <th>sno</th>
 <th>sname</th>
 <th>sex</th>
 <th>hometown</th>
 <th>tel</th>
 <th>college</th>
 <th>major</th>
 </tr>";
 echo "<tr>";
 echo "<td>" . $row['sno'] . "</td>";
 echo "<td>" . $row['sname'] . "</td>";
 echo "<td>" . $row['sex'] . "</td>";
 echo "<td>" . $row['hometown'] . "</td>";
 echo "<td>" . $row['tel'] . "</td>";
 echo "<td>" . $row['college'] . "</td>";
 echo "<td>" . $row['major'] . "</td>";
 echo "</tr>";
 }
echo "</table>";

mysql_close($con);
}


?>