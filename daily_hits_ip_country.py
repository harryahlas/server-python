# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:26:15 2019

Daily Pull
.
@author: Harry Ahlas
"""

import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import maxminddb

### NEW PIECE FOR NEWER FILES

# Headers for df
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

# Works same as 20190806 file (on 20190807)
df_import = pd.read_csv('logs/access.log.1', header=None, delimiter=r"\s+", quotechar='"', error_bad_lines=False )

# Update column names
df_import.columns = df.columns

# Add timestamp
df_import['TIMESTAMP'] = datetime.now()

# Check
df_import.groupby('CODE3').count().sort_values(['TIMESTAMP'])['TIMESTAMP']

# Add Country - from ip_addresses.py to get countries

# create separate df ips that has unique ip_addresses only. Create blank country column
ips = df_import[['IP']].copy().drop_duplicates()
ips['COUNTRY'] = None
ips = ips.reset_index() # needed because dropped duplicates are not in the index

# Read in country database
reader = maxminddb.open_database('GeoLite2-City_20190730/GeoLite2-City.mmdb')

# Test
#reader.get('162.243.147.46')

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
df_with_countries = pd.merge(df_import, ips, on = 'IP', how = 'left')
del df_with_countries['index'] #Remove index created by join

# View Results
df_with_countries.groupby('COUNTRY').count().sort_values(['TIMESTAMP'])['TIMESTAMP']


# Update MySQL

# Login

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

# Append import to hits_archive
df_with_countries.to_sql(name='hits_archive', con=cnx, if_exists = 'append', index=False)

# Removing piece to update ip_addresses.