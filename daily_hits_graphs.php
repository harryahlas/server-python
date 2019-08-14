<html>
<body>
<?php 

$daily_hits_graphs_sql = "SELECT STR_TO_DATE(CONCAT(A.YEAR, A.MONTH, A.DAY), '%Y%b%d') AS HIT_DATE, 
COUNT(*) AS HIT_COUNT
FROM 
(select  
DATETIME1, 
	SUBSTRING(DATETIME1, 2, 2) AS DAY, 
    SUBSTRING(DATETIME1, 5, 3) AS MONTH, 
    SUBSTRING(DATETIME1, 9, 4) AS YEAR 
    from edemise.hits_archive where COUNTRY = 'United States') A 
GROUP BY STR_TO_DATE(CONCAT(A.YEAR, A.MONTH, A.DAY), '%Y%b%d');";


$servername = "localhost";
$username = "edemise";
$password = "vo8x8i68vid2";

$con=mysqli_connect($servername, $username, $password);
// Check connection
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

//$result = mysqli_query($con,"select * from edemise.hits_archive");
/*echo "hello";
*/
echo "hellook";
$result = mysqli_query($con, $daily_hits_graphs_sql);



echo "<table border='1'>
<tr>
<th>DATE</th>
<th>HITCOUNT</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row[0] . ".</td>";
echo "<td>" . $row[1] . ".</td>";
echo "</tr>";
}
echo "</table>";

#echo $result;

//$command = escapeshellcmd('/home/edemise/daily_hits_graphs.py');
//$output = shell_exec($command);
//echo $output;

mysqli_close($con);


?>
<a href="sql_images/daily_hits.png">daily_hits.png</a>
</body>
</html>
