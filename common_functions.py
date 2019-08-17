# from cmd

# Install pip
# wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py --user

# install packages
# ~/.local/bin/pip install pandas --user

## Virtual env install: 
[https://realpython.com/effective-python-environment/#virtual-environments](https://realpython.com/effective-python-environment/#virtual-environments)
# from powershell
# python -m venv ~/.virtualenvs/my-env
# source ~/.virtualenvs/my-env/bin/activate #may be in Scripts folder
# deactivate
## From cmd
# C:\Development\Python\virtual_environments\testenv\Scripts\activate.bat
## From conda
# conda create --name condaenv ## can add this argument as well: python=3.7.3
# To activate this environment, use:
# > activate condaenv
# To deactivate this environment, use:
# > deactivate condaenv
# install packages (in conda), create requirements.txt with package name and optional version, eg scipy==1.3.0 
 
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
