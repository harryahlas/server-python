#devtools::install_github("rstudio/sparklyr")
library(sparklyr)

# Local
#sc <- spark_connect(master = "local")

Sys.setenv("SPARK_HOME" = "C:\\Users\\Spark") #try without, error added ';'
sc <- spark_connect(master = "local", app_name = "Harry")

# 
# sc <- spark_connect(master = "spark://127.0.0.1:7077", app_name = "Harry", spark_home = "C:/Users/Spark")
# sc <- spark_connect(master = "spark://192.168.42.72:7077", app_name = "Harry2")
# sc <- spark_connect(master = "spark://192.168.42.80:7077", app_name = "Harry", version = "2.4.4")
connection_is_open(sc)
library(dplyr)
cars <- copy_to(sc, mtcars[1:3])
spark_mtcars <- sdf_copy_to(sc, mtcars, "my_mtcars")
iris_tbl <- copy_to(sc, iris, overwrite = T)
flights_tbl <- copy_to(sc, nycflights13::flights, "flights")
batting_tbl <- copy_to(sc, Lahman::Batting, "batting")
src_tbls(sc)

spark_disconnect(sc)


library(SparkR, lib.loc = "C:\\Users\\Spark\\R\\lib")
sc <- sparkR.session(master = "spark://121.0.0.1:7077")
