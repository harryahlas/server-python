# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 23:12:20 2019

@author: Anyone
"""

import gzip #for unzipping gz
import shutil # for file movement

with gzip.open('C:\\Users\\Anyone\\Downloads\\GeoLite2-City_20190730.tar.gz', 'rb') as f_in:
        with open('GeoLite2-City_20190730.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    # convert to data frame
    df_temp = pd.read_csv('logs_archive/gz_files' + str(i) + '.txt', header=None, delimiter=r"\s+", quotechar='"', error_bad_lines=False ) 
    # Rename columns to match main
    
    
import tarfile
#if (fname.endswith("tar.gz")):
    tar = tarfile.open('C:\\Users\\Anyone\\Downloads\\GeoLite2-City_20190730.tar.gz', "r:gz")
    tar.extractall()
    tar.close()

import maxminddb

reader = maxminddb.open_database('GeoLite2-City_20190730/GeoLite2-City.mmdb')
reader.get('162.243.147.46')
{'country': ... }

reader.close()

#### Need to try for country and then if not get continent, if not then skip
i = 1343
for i in range(1400,1700):#len(ips)):
    print(i)
    url_country = reader.get(ips.loc[i,'IP'])
    ips.loc[i,'COUNTRY'] = url_country[list(url_country)[0]]['names']['en']
