# Spark Cluster Setup
Refer to README.md for details

## Master
* Ubuntu
	* Open Ubuntu as administrator
	* if needed, <code>chmod 755 -R /mnt/c/Users/Spark/logs</code>
	* <code>/mnt/c/Users/Spark/sbin/start-master.sh</code>
	* if it fails, run <code>/mnt/c/Users/Spark/sbin/stop-master.sh</code> then go back to above step
* Browser
	* visit http://127.0.0.1:8080/

## Slave
* cmd: <code>spark-class org.apache.spark.deploy.worker.Worker spark://192.168.42.72:7077</code>
* R: run run_spark_job_in_R.R
	* use ip that is on top left of browser on master
* Can check jobs using something like: <code>http://192.168.42.86:4040/storage/</code>

## Master
* Ubuntu
	* <code>/mnt/c/Users/Spark/sbin/stop-master.sh</code>

