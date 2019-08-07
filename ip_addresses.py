

import maxminddb

reader = maxminddb.open_database('GeoLite2-City_20190730/GeoLite2-City.mmdb')
reader.get('162.243.147.46')
{'country': ... }

reader.close()

# Find country in dictionary. if no Country then pick first name that comes up.
for i in range(0,1782):#len(ips)):
    print(i)
    url_country = reader.get(ips.loc[i,'IP'])
    j = 0  
    for x in url_country:
        if x == "country":          
          ips.loc[i,'COUNTRY'] = url_country[list(url_country)[j]]['names']['en']
        j = j + 1

ips.groupby('COUNTRY').count().sort_values(['IP'])
         
## OR ####

#for i in range(0,1782):#len(ips)):
#    print(i)
#    url_country = reader.get(ips.loc[i,'IP'])
#    ips.loc[i,'COUNTRY'] = url_country['country']['names']['en']
#
#    url_country = reader.get(ips.loc[336,'IP'])
#    ips.loc[336,'COUNTRY'] = url_country['country']['names']['en']




url_country[list(url_country)[0]]['names']['en']

for x in url_country[list(url_country)[0]]:
  print(x)

print(url_country['country']['names']['en'])
  
for x in url_country[list(url_country)]:
  print(x)

namelist = list()
for x in url_country[list(url_country)[0]]:
  list.append((x))
  
pd.DataFrame.from_dict(url_country).iloc(0,0)

for x in url_country:
  list.append((x))
  print(x)
url_country[0][0][0]

url_country[[0]]

if (y == "u"): 
    print(y)