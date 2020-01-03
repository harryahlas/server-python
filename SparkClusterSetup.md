# Spark Cluster Setup
Refer to README.md for details

## Master
* Ubuntu
	* Open Ubuntu as administrator
	* (if needed) chmod 755 -R /mnt/c/Users/Spark/logs
	* <code>cd /mnt/c/Users/Spark/sbin</code>
	* <code>./start-master.sh</code>
	* if it fails, run ./stop-master.sh then go back to above step
* Browser
	* visit http://127.0.0.1:8080/

## Slave
* cmd: spark-class org.apache.spark.deploy.worker.Worker spark://192.168.42.72:7077
* R: 

## Master
* Ubuntu
	* <code>./stop-master.sh</code>

