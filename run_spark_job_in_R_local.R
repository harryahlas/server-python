#devtools::install_github("rstudio/sparklyr")
library(sparklyr)
library(dplyr)

# Local
#sc <- spark_connect(master = "local")

#Sys.setenv("SPARK_HOME" = "C:\\Users\\Spark") #try without, error added ';'
sc <- spark_connect(master = "local", app_name = "Harry")

# 
# sc <- spark_connect(master = "spark://127.0.0.1:7077", app_name = "Harry", spark_home = "C:/Users/Spark")
# sc <- spark_connect(master = "spark://192.168.42.72:7077", app_name = "Harry2")
# sc <- spark_connect(master = "spark://192.168.42.80:7077", app_name = "Harry", version = "2.4.4")
spark_web(sc)
connection_is_open(sc)

starttime <- Sys.time()
sdf_len(sc, 5, repartition = 1) %>%
  spark_apply(function(e) I(e))
Sys.time()-starttime


starttime <- Sys.time()
sdf_len(sc, 200, repartition = 1) %>%
  spark_apply(function(e) I(e))
Sys.time()-starttime

summarize_all(spark_mtcars, mean) 

carsx <- copy_to(sc, mtcars)
summarize_all(carsx, mean) 
summarize_all(cars, mean) %>%
  show_query()

testdf <- copy_to(sc, tibble(x=1,y=2))
summarize_all(testdf, mean) 

testdf2 <- copy_to(sc, tibble(x=1,y=2))




# from https://therinspark.com/analysis.html
carsx %>% 
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



# Retrieve the Spark installation directory
spark_home <- spark_home_dir()

# Build paths and classes
spark_path <- "C:\\Users\\Spark\\bin\\spark-class"#file.path(spark_home, "bin", "spark-class")

# Start cluster manager master node
system2(spark_path, "org.apache.spark.deploy.master.Master", wait = FALSE)

# Start worker node, find master URL at http://localhost:8080/
system2(spark_path, c("org.apache.spark.deploy.worker.Worker",
                      #"spark://192.168.99.1:7077"), wait = FALSE)
                      "spark://121.0.0.1:7077"), wait = FALSE)


# From https://therinspark.com/modeling.html#exploratory-data-analysis
download.file(
  "https://github.com/r-spark/okcupid/raw/master/profiles.csv.zip",
  "okcupid.zip")
unzip("okcupid.zip", exdir = "data")
unlink("okcupid.zip")
profiles <- read.csv("data/profiles.csv")
write.csv(dplyr::sample_n(profiles, 10^3),
          "data/profiles.csv", row.names = FALSE)
okc <- spark_read_csv(
  sc, 
  "data/profiles.csv", 
  escape = "\"", 
  memory = FALSE,
  options = list(multiline = TRUE)
) %>%
  mutate(
    height = as.numeric(height),
    income = ifelse(income == "-1", NA, as.numeric(income))
  ) %>%
  mutate(sex = ifelse(is.na(sex), "missing", sex)) %>%
  mutate(drinks = ifelse(is.na(drinks), "missing", drinks)) %>%
  mutate(drugs = ifelse(is.na(drugs), "missing", drugs)) %>%
  mutate(job = ifelse(is.na(job), "missing", job))

okc <- okc %>%
  mutate(
    not_working = ifelse(job %in% c("student", "unemployed", "retired"), 1 , 0)
  )

okc %>% 
  group_by(not_working) %>% 
  tally()

data_splits <- okc %>% 
  sdf_random_split(train = .8, test = .2, seed = 42)
okc_train <- data_splits$train
okc_test <- data_splits$test

sdf_describe(okc_train, cols = c("age", "income"))

library(ggplot2)
library(dbplot)

dbplot_histogram(okc_train, age)

prop_data <- okc_train %>%
  mutate(religion = regexp_extract(religion, "^\\\\w+", 0)) %>% 
  group_by(religion, not_working) %>%
  tally() %>%
  group_by(religion) %>%
  summarize(
    count = sum(n),
    prop = sum(not_working * n) / sum(n)
  ) %>%
  mutate(se = sqrt(prop * (1 - prop) / count)) %>%
  collect()

prop_data

prop_data %>%
  ggplot(aes(x = religion, y = prop)) + geom_point(size = 2) +
  geom_errorbar(aes(ymin = prop - 1.96 * se, ymax = prop + 1.96 * se),
                width = .1) +
  geom_hline(yintercept = sum(prop_data$prop * prop_data$count) /
               sum(prop_data$count))

contingency_tbl <- okc_train %>% 
  sdf_crosstab("drinks", "drugs") %>%
  collect()

contingency_tbl

library(ggmosaic)
library(forcats)
library(tidyr)

contingency_tbl %>%
  rename(drinks = drinks_drugs) %>%
  gather("drugs", "count", missing:sometimes) %>%
  mutate(
    drinks = as_factor(drinks) %>% 
      fct_relevel("missing", "not at all", "rarely", "socially", 
                  "very often", "desperately"),
    drugs = as_factor(drugs) %>%
      fct_relevel("missing", "never", "sometimes", "often")
  ) %>%
  ggplot() +
  geom_mosaic(aes(x = product(drinks, drugs), fill = drinks, 
                  weight = count))

library(FactoMineR)
dd_obj <- contingency_tbl %>% 
  tibble::column_to_rownames(var = "drinks_drugs") %>%
  FactoMineR::CA(graph = FALSE)

dd_drugs <-
  dd_obj$row$coord %>%
  as.data.frame() %>%
  mutate(
    label = gsub("_", " ", rownames(dd_obj$row$coord)),
    Variable = "Drugs"
  )

dd_drinks <-
  dd_obj$col$coord %>%
  as.data.frame() %>%
  mutate(
    label = gsub("_", " ", rownames(dd_obj$col$coord)),
    Variable = "Alcohol"
  )

ca_coord <- rbind(dd_drugs, dd_drinks)

ggplot(ca_coord, aes(x = `Dim 1`, y = `Dim 2`, 
                     col = Variable)) +
  geom_vline(xintercept = 0) +
  geom_hline(yintercept = 0) +
  geom_text(aes(label = label)) +
  coord_equal()

scale_values <- okc_train %>%
  summarize(
    mean_age = mean(age),
    sd_age = sd(age)
  ) %>%
  collect()

scale_values

okc_train <- okc_train %>%
  mutate(scaled_age = (age - !!scale_values$mean_age) /
           !!scale_values$sd_age)

dbplot_histogram(okc_train, scaled_age)

okc_train %>%
  group_by(ethnicity) %>%
  tally()
