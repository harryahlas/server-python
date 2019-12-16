jupyter# server-python
Scratch code for use with server

## Spark on windows

[https://www.knowledgehut.com/blog/big-data/how-to-install-apache-spark-on-windows](https://www.knowledgehut.com/blog/big-data/how-to-install-apache-spark-on-windows)
spark-shell

cmd: jupyter notebook
run in IE
copy url

This works:
start with: jupyter notebook C:\Development\github\server-python
**pyspark+mysql+connection+attempt.ipynb**

Note: to restart mysql:
* Open Run Window by Winkey + R
* Type services.msc
* Search MySQL service based on version installed.
* Click stop, start or restart the service option.

## Old
<code>import findspark.init()

import pyspark

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.sql("select 'spark' as hello ")

df.show()

from pyspark.sql import SQLContext

from pyspark import SparkContext

sc = SparkContext.getOrCreate();

sqlContext = pyspark.SQLContext(sc)

#error
source_df = sqlContext.read.format('jdbc').options(
          url='jdbc:mysql://localhost/hrsample',
          driver='com.mysql.jdbc.Driver',
          dbtable='employeeinfo',
          user='newuser',
          password='newuser').load()
</code>

* next: multiple nodes: (https://www.davidadrian.cc/posts/2017/08/how-to-spark-cluster/)[https://www.davidadrian.cc/posts/2017/08/how-to-spark-cluster/]