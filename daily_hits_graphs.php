<html>
<body>
<?php 

$command = escapeshellcmd('/usr/custom/test.py');
$output = shell_exec($command);
echo $output;

?>
<a href="sql_images/daily_hits.png">daily_hits.png</a>
</body>
</html>