# from cmd

# Install pip
# wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py --user

# install packages
# ~/.local/bin/pip install pandas --user


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


#crontab 
crontab -e
cp filename newfilenameandlocation


# PHP
https://www.iplocate.io/api/lookup/2620:160:eb08::9

$ip = $_SERVER['REMOTE_ADDR'];
$details = json_decode(file_get_contents("http://ipinfo.io/{$ip}"));
echo $details->country; // -> "