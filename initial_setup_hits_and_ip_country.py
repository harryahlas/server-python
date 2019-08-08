# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:26:15 2019

Pulls
.
@author: Harry Ahlas
"""

#import requests
#import re
import pandas as pd
import gzip #for unzipping gz
import shutil # for file movement
import os
from sqlalchemy import create_engine
from datetime import datetime
import maxminddb

### NEW PIECE FOR NEWER FILES

# Import logs_archive/accessYYYYMMDD.log files starting on July 29
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

file_list = list(['access20190729',
                  'access20190730',
                  'access20190731',
                  'access20190801',
                  'access20190802',
                  'access20190803',
                  'access20190804',
                  'access20190805'])

for file in file_list:
    print(file)
    df_log_temp = pd.read_csv(str('logs_archive/' + file + '.log'), header=None, delimiter=r"\s+", quotechar='"', error_bad_lines=False ) 
    df_log_temp.columns = df.columns
    df = df.append(df_log_temp)


### END NEW PIECE FOR NEWER FILES


### start NEW PIECE FOR archive FILES
# update archived gz files

directory_to_search = "logs_archive"

# Get list of files that match pattern .gz
#path = '/usr/share/cups/charmaps'
gz_files = [f for f in os.listdir(directory_to_search) if f.endswith('.gz')]
gz_files


# import data and save to a single dataframe
for i in range(0,len(gz_files)):
    print(i)
# unzip and read in file
    with gzip.open('logs_archive/' + gz_files[i], 'rb') as f_in:
        with open('logs_archive/gz_files' + str(i) + '.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    # convert to data frame
    df_gz_temp = pd.read_csv('logs_archive/gz_files' + str(i) + '.txt', header=None, delimiter=r"\s+", quotechar='"', error_bad_lines=False ) 
    # Rename columns to match main
    df_gz_temp.columns = df.columns
    # append to empty data frame
    df = df.append(df_gz_temp)


# Add timestamp
df['TIMESTAMP'] = datetime.now()

# Check
df.groupby('CODE3').count().sort_values(['TIMESTAMP'])['TIMESTAMP']

### END NEW PIECE FOR archiveFILES



#### Add countries


# create separate df ips that has unique ip_addresses only. Create blank country column
ips = df[['IP']].copy().drop_duplicates()
ips['COUNTRY'] = None
ips = ips.reset_index() # needed because dropped duplicates are not in the index







# Next run ip_addresses.py to get countries






# Read in country database
reader = maxminddb.open_database('GeoLite2-City_20190730/GeoLite2-City.mmdb')

# Test
reader.get('162.243.147.46')


# Find country in dictionary. if no Country then pick first name that comes up.
for i in range(0, len(ips)):
    print(i)
    url_country = reader.get(ips.loc[i,'IP'])
    j = 0  
    for x in url_country:
        if x == "country":          
          ips.loc[i,'COUNTRY'] = url_country[list(url_country)[j]]['names']['en']
        j = j + 1

reader.close()

# View results - Should have countries listed
ips.groupby('COUNTRY').count().sort_values(['IP'])
         


# Join data together and remove index
df_with_countries = pd.merge(df, ips, on = 'IP', how = 'left')
del df_with_countries['index'] #Remove index created by join

# View Results
df_with_countries.groupby('COUNTRY').count().sort_values(['TIMESTAMP'])['TIMESTAMP']





#### Upload archive tables

# Initial table creation, maybe move to separate file
# Create ip_country table, columns ip varchar(use my ip and usa for dummy)

# Import initial_archive_table


# Manual Credentials
username = "newuser"
password = "newuser"

# Auto Credentials
f = open("cred.txt")
cred = pd.read_csv(f)
f.close()
username = cred['username'][0]
password = cred['password'][0]


engine_text = str('mysql+pymysql://' + username + ':' + password + '@localhost/edemise')
cnx = create_engine(engine_text, echo=False)

# Save hits_archive
df_with_countries.to_sql(name='hits_archive', con=cnx, if_exists = 'replace', index=False)

# Save ip_country
ips.to_sql(name='ip_country', con=cnx, if_exists = 'replace', index=False)


