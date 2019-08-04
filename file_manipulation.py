# from cmd

# Install pip
# wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py --user

# install packages
# ~/.local/bin/pip install pandas --user

import os
import pandas as pd
import gzip #for unzipping gz
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

#not used
file_list = list()
file_list[[1]] = b2

f = gzip.open('logs_archive/access.log.7.gz', 'rb')


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
                           'NULL',
                           'BROWSERTYPE',
                           'CODE2',
                           'CODE3'])

i = 1
# for each item in gz_files
# import data
# Unzip
f = gzip.open('logs_archive/' + gz_files[i], 'rb')


#
#
#
#  START BELOW
#


import shutil
with gzip.open('logs_archive/' + gz_files[i], 'rb') as f_in:
    with open('logs_archive/gz_files' + str(i) + '.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

df_temp2 = pd.read_csv('logs_archive/' + gz_files[i],
                       compression='gzip', 
                       header=None, 
                       delimiter=r"\s+")

# read in file
file_content = f.read()

# convert to data frame
df_temp = pd.read_csv('logs_archive/gz_files' + str(i) + '.txt', header=None,
                      quotechar='"', delimiter=r"\s+",
                      error_bad_lines=False )

# append to empty data frame
df = df.append(df_temp)




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
