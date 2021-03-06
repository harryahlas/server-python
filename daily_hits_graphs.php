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

/*
$con=mysqli_connect($servername, $username, $password);
// Check connection
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

//$result = mysqli_query($con,"select * from edemise.hits_archive");
/*echo "hello";

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
	
mysqli_close($con);

?>
<a href="sql_images/daily_hits.png">daily_hits.png</a>
</body>
</html>
*/





<?php
$servername = "localhost";
$username = "edemise";
$password = "vo8x8i68vid2";
$dbname = "edemise";
$dataPoints = array();
//Best practice is to create a separate file for handling connection to database
try{
     // Creating a new connection.
    // Replace your-hostname, your-db, your-username, your-password according to your database
    $link = new \PDO(   'mysql:host=$servername;dbname=$dbname;charset=utf8mb4', //'mysql:host=localhost;dbname=canvasjs_db;charset=utf8mb4',
                        $username, //'root',
                        $password, //'',
                        array(
                            \PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                            \PDO::ATTR_PERSISTENT => false
                        )
                    );
	
    $handle = $link->prepare($daily_hits_graphs_sql); 
    $handle->execute(); 
    $result = $handle->fetchAll(\PDO::FETCH_OBJ);
		
    foreach($result as $row){
        array_push($dataPoints, array("x"=> $row->x, "y"=> $row->y));
    }
	$link = null;
}
catch(\PDOException $ex){
    print($ex->getMessage());
}
	
?>
<!DOCTYPE HTML>
<html>
<head>  
<script>
window.onload = function () {
 
var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	exportEnabled: true,
	theme: "light1", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "PHP Column Chart from Database"
	},
	data: [{
		type: "column", //change type to bar, line, area, pie, etc  
		dataPoints: <?php echo json_encode($dataPoints, JSON_NUMERIC_CHECK); ?>
	}]
});
chart.render();
 
}
</script>
</head>
<body>
<div id="chartContainer" style="height: 370px; width: 100%;"></div>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>       
