# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:26:15 2019

Run after gz_data_load.py

@author: Harry Ahlas
"""

import requests
import re
import pandas as pd

# Initial table creation, maybe move to separate file
# Create ip_country table, columns ip varchar(use my ip and usa for dummy)

#Add back?
#ip_country = pd.DataFrame([['70.36.251.205']], columns = ['IP'])

# Import initial_archive_table
from sqlalchemy import create_engine

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

df = pd.read_sql_query('SELECT * FROM initial_archive_table', engine_text)

# create separate df ips that has unique ip_addresses only. Create blank country column
ips = df[['IP']].copy().drop_duplicates()
ips['COUNTRY'] = None
ips = ips.reset_index() # needed because dropped duplicates are not in the index



# Next run ip_addresses.py to get countries

df_with_countries = df.set_index('IP').join(ips.set_index('IP'))

# View Results
df_with_countries.groupby('COUNTRY').count().sort_values(['index'])[['index']]


# Save initial_archive_table
df_with_countries.to_sql(name='initial_archive_table', con=cnx, if_exists = 'replace', index=False)
