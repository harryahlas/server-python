# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:50:22 2019

This script unzips web logs and saves them to a mysql database

@author: Harry Ahlas
"""

import os
import pandas as pd
import gzip #for unzipping gz
import shutil # for file movement
import pymysql
from datetime import datetime
from sqlalchemy import create_engine

# Credentials
f = open("cred.txt")
cred = pd.read_csv(f)
f.close()
username = cred['username'][0]
password = cred['password'][0]
# change directory
#os.chdir("C:\Development\\github\\server-python")

directory_to_search = "logs_archive"

# Get list of files that match pattern .gz
#path = '/usr/share/cups/charmaps'
gz_files = [f for f in os.listdir(directory_to_search) if f.endswith('.gz')]
gz_files

# create empty dataframe
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

# import data and save to a single dataframe
for i in range(0,len(gz_files)):
    print(i)
# unzip and read in file
    with gzip.open('logs_archive/' + gz_files[i], 'rb') as f_in:
        with open('logs_archive/gz_files' + str(i) + '.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    # convert to data frame
    df_temp = pd.read_csv('logs_archive/gz_files' + str(i) + '.txt', header=None, delimiter=r"\s+", quotechar='"', error_bad_lines=False ) 
    # Rename columns to match main
    df_temp.columns = df.columns
    # append to empty data frame
    df = df.append(df_temp)

# Add timestamp
df['TIMESTAMP'] = datetime.now()

engine_text = str('mysql+pymysql://' + username + ':' + password + '@localhost/edemise')

# Turn dataframe into SQL table
cnx = create_engine(engine_text, echo=False)
#cnx = create_engine('mysql+pymysql://newuser:newuser@localhost/EDEMISE', echo=False)
df.to_sql(name='initial_archive_table', con=cnx, if_exists = 'replace', index=False)



