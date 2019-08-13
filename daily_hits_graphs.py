# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:43:16 2019

Create graphics for web hits

@author: Harry Ahlas
"""

import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
#import mysql.connector as sql
import gzip #for unzipping gz
import shutil # for file movement
import os
import re
# Retrieve daily counts --------------
# Connect 
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

# Import SQL and replace %
f = open('scripts/hitcount_by_country_day.sql', "r")
sql_hitcount_by_country_day = f.read()
sql_hitcount_by_country_day = re.sub('%', '%%', sql_hitcount_by_country_day)
f.close()

# Retrieve data
data = pd.read_sql(sql_hitcount_by_country_day, cnx)

#Plot data --------------

# Export image ----------






import numpy as np
import matplotlib.pyplot as plt
import datetime

x = [datetime.datetime(2010, 12, 1, 10, 0),
    datetime.datetime(2011, 1, 4, 9, 0),
    datetime.datetime(2011, 5, 5, 9, 0)]
y = [4, 9, 2]

ax = plt.subplot(111)
ax.bar(x, y, width=10)
ax.xaxis_date()

plt.show()