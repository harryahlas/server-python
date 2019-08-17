# from cmd

# Install pip
# wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py --user

# install packages
# ~/.local/bin/pip install pandas --user

# Virtual env
# python -m venv ~/.virtualenvs/my-env

#list functions in module
dir(os)


#get help
help(packagename)

# Get current directory
os.getcwd()


# change directory
 os.chdir()
os.chdir("..")


#read file
f = open('directory/filename', "r")
b = f.read()
b


# Change column names to match another pandas df
b2.columns = df.columns

# text replace
import re
s = 'asdf=5;iwantthis123jasd'
result = re.search('asdf=5;(.*)123jasd', s)
print(result.group(1))

# Get list of files that match pattern .gz
#path = '/usr/share/cups/charmaps'
import gzip
gz_files = [f for f in os.listdir("logs_archive") if f.endswith('.gz')]
gz_files
f = gzip.open('logs_archive/access.log.7.gz', 'rb')



#crontab 
crontab -e
cp filename newfilenameandlocation


# PHP
https://www.iplocate.io/api/lookup/2620:160:eb08::9

$ip = $_SERVER['REMOTE_ADDR'];
$details = json_decode(file_get_contents("http://ipinfo.io/{$ip}"));
echo $details->country; // -> "
