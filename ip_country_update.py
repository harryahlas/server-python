import requests
import re
import pandas as pd

# Initial table creation, maybe move to separate file
# Create ip_country table, columns ip varchar(use my ip and usa for dummy)
ip_country = pd.DataFrame([['70.36.251.205']], columns = ['IP'])

# Import initial_archive_table
from sqlalchemy import create_engine

username = "newuser"
password = "newuser"
engine_text = str('mysql+pymysql://' + username + ':' + password + '@localhost/edemise')
cnx = create_engine(engine_text, echo=False)

df = pd.read_sql_query('SELECT * FROM initial_archive_table', engine_text)

# create separate df ips that has unique ip_addresses only. Create blank country column
ips = df[['IP']].copy().drop_duplicates()
ips['COUNTRY'] = None
ips = ips.reset_index() # needed because dropped duplicates are not in the index

# loop through and run code below for each, storing country



for i in range(len(ips)):
    print(i)
    download_url = 'http://ipinfo.io/' + ips.loc[i,'IP'] 
    page = requests.get(download_url)
    #page.content
    result = re.search('"country": "(.*)",', str(page.content))
    ips.loc[i,'COUNTRY'] = result.group(1)[0:2]
    
    #print df.iloc[i]['c1'], df.iloc[i]['c2']

    
#ip_address = "93.158.161.124";

# left join ip initial_archive_table to ip_countries

# overwrite initial_archive_table in mysql

# Store ip_countries in mysql

# Turn dataframe into SQL table
#cnx = create_engine('mysql+pymysql://newuser:newuser@localhost/EDEMISE', echo=False)
df.to_sql(name='initial_archive_table', con=cnx, if_exists = 'replace', index=False)




ip_address = "93.158.161.124";
download_url = 'http://ipinfo.io/' + ip_address 
page = requests.get(download_url)
#page.content
result = re.search('"country": "(.*)",', str(page.content))
result.group(1)[0:2]
