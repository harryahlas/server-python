# Spark Cluster Setup

## Master
* Ubuntu
	* Open Ubuntu as administrator
	* (if needed) chmod 755 -R /mnt/c/Users/Spark/logs
	* cd /mnt/c/Users/Spark/sbin
	* ./start-master.sh
	* if it fails, run ./stop-master.sh then go back to above step
* Browser
	* visit http://127.0.0.1:8080/

## Slave
* cmd: spark-class org.apache.spark.deploy.worker.Worker spark://192.168.42.72:7077
* R: 

## Master
* Ubuntu
	* ./stop-master.sh

