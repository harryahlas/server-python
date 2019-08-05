import requests
import re

import pandas as pd

ip_address = "93.158.161.124";
download_url = 'http://ipinfo.io/' + ip_address 
page = requests.get(download_url)
page.content

result = re.search('"country": "(.*)",', str(page.content))
result.group(1)[0:2]
