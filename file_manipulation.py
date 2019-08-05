# from cmd

# Install pip
# wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py --user

# install packages
# ~/.local/bin/pip install pandas --user

import os
import pandas as pd
import gzip #for unzipping gz
import shutil # for file movement

#list functions in module
dir(os)


#get help
help(packagename)

# Get current directory
os.getcwd()


# change directory
os.chdir("C:\Development\\github\\server-python")


#read file
f = open('logs_archive/access20190731.log', "r")
b = f.read()
b

# alternate read
b2 = pd.read_csv("logs_archive/access20190731.log", header=None, delimiter=r"\s+")

# Clean up data

# Retrieve country info
# Translate PHP below to python
# PHP
#https://www.iplocate.io/api/lookup/2620:160:eb08::9

#$ip = $_SERVER['REMOTE_ADDR'];
#$details = json_decode(file_get_contents("http://ipinfo.io/{$ip}"));
#echo $details->country; // -> "




# Get list of files that match pattern .gz
#path = '/usr/share/cups/charmaps'
gz_files = [f for f in os.listdir("logs_archive") if f.endswith('.gz')]
gz_files

# create empty data frame
df = pd.DataFrame(columns=['IP',
                           'NULL1',
                           'NULL2',
                           'DATETIME1',
                           'DATETIME2',
                           'REQUEST',
                           'CODE1',
                           'CODE2',
                           'CODE3',
                           'BROWSERTYPE',
                           'CODE4',
                           'CODE5'])

for i in range(0,len(gz_files)):
    print(i)
 
    # unzip and read in file
    with gzip.open('logs_archive/' + gz_files[i], 'rb') as f_in:
        with open('logs_archive/gz_files' + str(i) + '.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # convert to data frame
    df_temp = pd.read_csv('logs_archive/gz_files' + str(i) + '.txt', header=None,
                          quotechar='"', delimiter=r"\s+",
                          error_bad_lines=False )
    # Rename columns to match main
    df_temp.columns = df.columns
    
    # append to empty data frame
    df = df.append(df_temp)


# get date of file modification date
a = os.path.getmtime("logs_archive/access20190731.log")
b = os.path.getctime("logs_archive/access20190731.log")
c = datetime.fromtimestamp(a)
c.month
c.day
c.year


# Get list of ips from archive
# find country
#create country_ip table

## add yesterday's data
# search for files that have yesterday's modification date
# import data
# add column names
# add timestamp (current time)

# connect to mysql using 2.7

#import mysql.connector    
#cnx = mysql.connector.connect(user='scott', password='tiger',
#                              host='127.0.0.1',
#                              database='employees')
#
#import mysqlclient    
import pymysql
from sqlalchemy import create_engine





# Turn dataframe into SQL table
cnx = create_engine('mysql+pymysql://newuser:newuser@localhost/EDEMISE', echo=False)
df.to_sql(name='sample_table2', con=cnx, if_exists = 'append', index=False)

df2 = df.iloc[0:1,:]
df2.to_sql('EDEMISELOG_TEMP', con)



# Connect to the database
con = pymysql.connect(host='localhost',
                             user='newuser',
                             password='newuser',
                             db='EDEMISE',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



newfile = open("scripts/create_edemiselog.sql", "r")
create_edemiselog_sql = newfile.read()
newfile.close()
create_edemiselog_sql 

# 1 time create log table
with con:

    cur = con.cursor()
    #cur.execute("SELECT * FROM deskhistory")
    cur.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cur.execute("DROP TABLE IF EXISTS EARLYDEMISELOG;")
    cur.execute("SET FOREIGN_KEY_CHECKS = 1;")
    cur.execute("CREATE TABLE EARLYDEMISELOG (IP varchar(20), NULL1 int(1), NULL2 int(1), DATETIME1 varchar(50), DATETIME2 varchar(8), REQUEST TEXT, CODE1 INT(8), CODE2 INT(8), CODE3 INT(8), BROWSERTYPE varchar(255), CODE4 INT(8), CODE5 INT(8));")



# generic
with con:

    cur = con.cursor()
    #cur.execute("SELECT * FROM deskhistory")

    rows = cur.fetchall()

    desc = cur.description

    print("{0:>3} {1:>10}".format(desc[0][0], desc[1][0]))

    for row in rows:    
        print("{0:3} {1:>10}".format(row[0], row[2]))

con.close()



try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()


# append to old file? create new?

# Change column names to match another df
b2.columns = df.columns

# append to empty data frame
df = df.append(b2)




newfile = open("logs_archive/access20190727bob.log", "w")
encoding = 'utf-8'
newfile_encoded =file_content.decode(encoding)
newfile.write(newfile_encoded)
newfile.close()

f.close()
####### Rename old files
# get names of files
# pull number from file names
import re

before_num = "access.log."
after_num = ".gz"

i = 12
days_difference = 10

num_search = re.search('access.log.(.*).gz', gz_files[i])
num_search = num_search.group(1)
num_search = int(num_search)
num_search 

from datetime import datetime
from datetime import date
from datetime import timedelta

StartDate = date(2019, 8, 3)
StartDate  - timedelta(days=(num_search))
