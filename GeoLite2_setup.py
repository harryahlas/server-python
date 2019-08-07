# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 23:12:20 2019

How to set up GeoLite2
Download: https://dev.maxmind.com/geoip/geoip2/geolite2/
Reference: https://maxminddb.readthedocs.io/en/latest/

@author: Harry Ahlas
"""

import tarfile
#if (fname.endswith("tar.gz")):
tar = tarfile.open('C:\\Users\\Anyone\\Downloads\\GeoLite2-City_20190730.tar.gz', "r:gz")
tar.extractall() #extract to current folder
tar.close()