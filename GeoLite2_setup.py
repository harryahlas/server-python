# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 23:12:20 2019

How to set up GeoLite2
Download: https://dev.maxmind.com/geoip/geoip2/geolite2/
Reference: https://maxminddb.readthedocs.io/en/latest/

@author: Harry Ahlas
"""

import gzip #for unzipping gz
import shutil # for file movement
#import pandas as pd

with gzip.open('C:\\Users\\Anyone\\Downloads\\GeoLite2-City_20190730.tar.gz', 'rb') as f_in:
        with open('GeoLite2-City_20190730.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
#    # convert to data frame
#    df_temp = pd.read_csv('logs_archive/gz_files' + str(i) + '.txt', header=None, delimiter=r"\s+", quotechar='"', error_bad_lines=False ) 
#    # Rename columns to match main
    
    
import tarfile
#if (fname.endswith("tar.gz")):
    tar = tarfile.open('C:\\Users\\Anyone\\Downloads\\GeoLite2-City_20190730.tar.gz', "r:gz")
    tar.extractall()
    tar.close()