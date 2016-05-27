from urllib import urlretrieve

url = "ftp://ftp_public:spruce_s1@sprucedata.ornl.gov/DataFiles/EM1_Table1.dat"

import urllib
#link to a url
response=urllib.urlretrieve(url, 'file')


#read from the url
#dat_read=response.read()
#convert the data(which can be of any format) into string
dat_str=str(response)
print dat_str
#breaking the string into different lines
lines=dat_str.split("\\n")
#save the data in a file(locally)
local_file=r'em1_table.dat'
#open the file
fx=open(local_file,"w")
#start writing in the fileusing a loop
for line in lines:
    fx.write(line + "\n")
    fx.close()