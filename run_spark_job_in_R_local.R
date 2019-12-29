#devtools::install_github("rstudio/sparklyr")
library(sparklyr)
library(dplyr)

# Local
#sc <- spark_connect(master = "local")

Sys.setenv("SPARK_HOME" = "C:\\Users\\Spark") #try without, error added ';'
sc <- spark_connect(master = "local", app_name = "Harry")

# 
# sc <- spark_connect(master = "spark://127.0.0.1:7077", app_name = "Harry", spark_home = "C:/Users/Spark")
# sc <- spark_connect(master = "spark://192.168.42.72:7077", app_name = "Harry2")
# sc <- spark_connect(master = "spark://192.168.42.80:7077", app_name = "Harry", version = "2.4.4")
connection_is_open(sc)

starttime <- Sys.time()
sdf_len(sc, 5, repartition = 1) %>%
  spark_apply(function(e) I(e))
Sys.time()-starttime


starttime <- Sys.time()
sdf_len(sc, 200, repartition = 1) %>%
  spark_apply(function(e) I(e))
Sys.time()-starttime


cars <- copy_to(sc, mtcars)
summarize_all(cars, mean) 
summarize_all(cars, mean) %>%
  show_query()

# from https://therinspark.com/analysis.html
cars %>% 
  group_by(am) %>% 
  summarize_all(mean) %>% 
  show_query()

#explode list
cars %>% 
  summarize(mpg_percentile = percentile(mpg, array(.25, .5,.75))) %>% 
  mutate(mpg_percentile = explode(mpg_percentile))

#In the background, the correlate() function runs sparklyr::ml_corr()
library(corrr)
correlate(cars, use = "pairwise.complete.obs", method = "pearson") 

correlate(cars, use = "pairwise.complete.obs", method = "pearson") %>%
  shave() %>%
  rplot()


library(ggplot2)
# not run on spark
ggplot(aes(as.factor(cyl), mpg), data = mtcars) + geom_col()

# does run on spark
cars %>%
  group_by(cyl) %>%
  summarise(mpg = sum(mpg, na.rm = TRUE)) %>%
  collect() %>%
  ggplot(aes(as.factor(cyl), mpg)) + 
  geom_col(fill = "#999999") + coord_flip()


spark_mtcars <- sdf_copy_to(sc, mtcars, "my_mtcars")
iris_tbl <- copy_to(sc, iris, overwrite = T)
flights_tbl <- copy_to(sc, nycflights13::flights, "flights")
batting_tbl <- copy_to(sc, Lahman::Batting, "batting")
src_tbls(sc)

spark_disconnect(sc)


library(SparkR, lib.loc = "C:\\Users\\Spark\\R\\lib")
sc <- sparkR.session(master = "spark://121.0.0.1:7077")
