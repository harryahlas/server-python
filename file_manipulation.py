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

# Get list of files that match pattern .gz
#path = '/usr/share/cups/charmaps'
gz_files = [f for f in os.listdir("logs_archive") if f.endswith('.gz')]
gz_files

# Unzip old file and write to new file
f = gzip.open('logs_archive/access.log.7.gz', 'rb')
file_content = f.read()
b2 = pd.read_csv(file_content, header=None, delimiter=r"\s+")

newfile = open("logs_archive/access20190727bob.log", "w")
encoding = 'utf-8'
newfile_encoded =file_content.decode(encoding)
newfile.write(newfile_encoded)
newfile.close()

f.close()
####### Rename old files
