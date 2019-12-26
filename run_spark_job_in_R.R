library(sparklyr)

# Local
#sc <- spark_connect(master = "local")

sc <- spark_connect(master = "spark://192.168.42.72:7077")


library(dplyr)
iris_tbl <- copy_to(sc, iris)
flights_tbl <- copy_to(sc, nycflights13::flights, "flights")
batting_tbl <- copy_to(sc, Lahman::Batting, "batting")
src_tbls(sc)