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



/*
//chart
//initialize the array to store the processed data
    $jsonArray = array();
    //check if there is any data returned by the SQL Query
    if ($result->num_rows > 0) {
      //Converting the results into an associative array
      while($row = $result->fetch_assoc()) {
        $jsonArrayItem = array();
        $jsonArrayItem['hitdate'] = $row[0];
        $jsonArrayItem['count'] = $row[1];
        //append the above created object into the main array.
        array_push($jsonArray, $jsonArrayItem);
      }
    }

	
	

	
//set the response content type as JSON
    header('Content-type: application/json');
    //output the return value of json encode using the echo function.
    echo json_encode($jsonArray);
*/	
mysqli_close($con);

?>
<a href="sql_images/daily_hits.png">daily_hits.png</a>
</body>
</html>
