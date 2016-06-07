
# coding: utf-8

# In[1]:

import pandas as pd
import datetime
#Get from ftp site
from ftplib import FTP
import urllib, shutil
'''
url="ftp://ftp_public:spruce_s1@sprucedata.ornl.gov/DataFiles/EM1_Table1.dat"
ftpfile = urllib.request.urlopen(url)
localfile = open("my.csv", "wb")
shutil.copyfileobj(ftpfile, localfile)
ftp = FTP('sprucedata.ornl.gov') 
ftp.login('ftp_public','spruce_s1')
#load into pandas dataframe
#ftp://sprucedata.ornl.gov/DataFiles/EM1_Table1.dat
'''
#pulling data from the url
url = 'ftp://ftp_public:spruce_s1@sprucedata.ornl.gov/DataFiles/EM1_Table1.dat'
sp_data=pd.read_fwf(url)
#print (sp_data)
columnnames = ["TIMESTAMP","RECORD","Tair","RH","AirTCHumm_Avg","RH_Humm_Avg","VPD","Rain","WS","WindDir_D1_WVT","WindDir_SD1_WVT","WSDiag_Tot","SmplsF_Tot","Axis1Failed_Tot","Axis2Failed_Tot","BothAxisFailed_Tot","NVMerror_Tot","ROMerror_Tot","MaxGain_Tot","NNDF_Tot","HollowSurf_Avg","Hollow5cm_Avg","Tsoil","Hollow40cm_Avg","Hollow80cm_Avg","Hollow160cm_Avg","Hollow200cm_Avg","HummockSurf_Avg","Hummock5cm_Avg","Hummock20cm_Avg","Hummock40cm_Avg","Hummock80cm_Avg","Hummock160cm_Avg","Hummock200cm_Avg","PAR","PAR_NTree1_Avg","PAR_NTree2_Avg","PAR_SouthofHollow1_Avg","PAR_SouthofHollow2_Avg","PAR_NorthofHollow1_Avg","PAR_NorthofHollow2_Avg","PAR_Srub1_Avg","PAR_Srub2_Avg","PAR_Srub3_Avg","PAR_Srub4_Avg","TopofHummock_Avg","MidofHummock_Avg","Surface1_Avg","Surface2_Avg","D1-20cm_Avg","D2-20cm_Avg","TopH_Avg","MidH_Avg","S1_Avg","S2_Avg","Deep-20cm_Avg","short_up_Avg","short_dn_Avg","long_up_Avg","long_dn_Avg","CNR4_Temp_C_Avg","CNR4_Temp_K_Avg","long_up_corr_Avg","long_dn_corr_Avg","Rs_net_Avg","Rl_net_Avg","albedo_Avg","Rn_Avg","SPN1_Total_Avg","SPN1_Diffuse_Avg","Water_Height_Avg","Water_Temp_Avg","Watertable","Dewpoint","Dewpoint_Diff"]
#columnnames = ["TIMESTAMP","RECORD","AirTC_2M_Avg","RH_2M_Avg","AirTCHumm_Avg","RH_Humm_Avg","BP_kPa_Avg","Rain_mm_Tot","WS_ms_S_WVT","WindDir_D1_WVT","WindDir_SD1_WVT","WSDiag_Tot","SmplsF_Tot","Axis1Failed_Tot","Axis2Failed_Tot","BothAxisFailed_Tot","NVMerror_Tot","ROMerror_Tot","MaxGain_Tot","NNDF_Tot","HollowSurf_Avg","Hollow5cm_Avg","Hollow20cm_Avg","Hollow40cm_Avg","Hollow80cm_Avg","Hollow160cm_Avg","Hollow200cm_Avg","HummockSurf_Avg","Hummock5cm_Avg","Hummock20cm_Avg","Hummock40cm_Avg","Hummock80cm_Avg","Hummock160cm_Avg","Hummock200cm_Avg","PAR_2_M_Avg","PAR_NTree1_Avg","PAR_NTree2_Avg","PAR_SouthofHollow1_Avg","PAR_SouthofHollow2_Avg","PAR_NorthofHollow1_Avg","PAR_NorthofHollow2_Avg","PAR_Srub1_Avg","PAR_Srub2_Avg","PAR_Srub3_Avg","PAR_Srub4_Avg","TopofHummock_Avg","MidofHummock_Avg","Surface1_Avg","Surface2_Avg","D1-20cm_Avg","D2-20cm_Avg","TopH_Avg","MidH_Avg","S1_Avg","S2_Avg","Deep-20cm_Avg","short_up_Avg","short_dn_Avg","long_up_Avg","long_dn_Avg","CNR4_Temp_C_Avg","CNR4_Temp_K_Avg","long_up_corr_Avg","long_dn_corr_Avg","Rs_net_Avg","Rl_net_Avg","albedo_Avg","Rn_Avg","SPN1_Total_Avg","SPN1_Diffuse_Avg","Water_Height_Avg","Water_Temp_Avg","Watertable","Dewpoint","Dewpoint_Diff"]
#write to a csv file
sp_data.to_csv('my1.csv',sep=';')
sp_data=pd.read_csv('my1.csv',skiprows=5)
sp_data.to_csv('my1.csv')
sp_data.columns = columnnames

sp_data.to_csv('my1.csv')

df=pd.read_csv('my1.csv')
#trying to bring the timestamp into a format
data=df['TIMESTAMP']
data=data.str.lstrip('0123456789')
data=data.str.strip(';"')
#adding it to the existing data frame
df['Date_Time']=data

#Trim columns
teco_spruce =df[['Date_Time','Tair','Tsoil','RH','VPD','Rain','WS','PAR']]
#dividing Date_Time to year,day and hour
time=teco_spruce['Date_Time']
#getting the year
year=time.str.split('-').str.get(0)
#gettting the month
#month=time.str.split('-').str.get(1)
#getting the Day and hour
day_hour=time.str.split('-').str.get(2)
#day_hour
day=day_hour.str.split(' ').str.get(0)
hour=day_hour.str.split(' ').str.get(1)
#extracting only the hour from a given time
hour=hour.str.rstrip('0')
hour=hour.str.rstrip(':')
hour=hour.str.rstrip('1234567890')
hour=hour.str.rstrip(':')
#adding it to the existing data frame
df['year']=year
df['day']=day
df['hour']=hour
teco_spruce=df[['year','day','hour','Tair','Tsoil','RH','VPD','Rain','WS','PAR']]
#Write to tab delimited file
teco_spruce.to_csv('teco_spruce.txt','\t')


# In[2]:

df


# In[81]:

time=teco_spruce['Date_Time']
year=time.str.split('-').str.get(0)
day_hour=time.str.split('-').str.get(2)
#day_hour
day=day_hour.str.split(' ').str.get(0)
hour=day_hour.str.split(' ').str.get(1)


# In[4]:

import pandas as pd
import datetime
#Get from ftp site
from ftplib import FTP
import urllib, shutil
def cal_day_num(year,mon,day):
    if((year%4)==0):
        month=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        month=[31,28,31,30,31,30,31,31,30,31,30,31]
    i=0
    day_number=0
    for i in range(mon-1):
        day_number=day_number+month[i]
          #print(day_number)
    day_number=day_number+day    
    return day_number   
'''
url="ftp://ftp_public:spruce_s1@sprucedata.ornl.gov/DataFiles/EM1_Table1.dat"
ftpfile = urllib.request.urlopen(url)
localfile = open("my.csv", "wb")
shutil.copyfileobj(ftpfile, localfile)
ftp = FTP('sprucedata.ornl.gov') 
ftp.login('ftp_public','spruce_s1')
#load into pandas dataframe
#ftp://sprucedata.ornl.gov/DataFiles/EM1_Table1.dat
'''
#pulling data from the url
url = 'ftp://ftp_public:spruce_s1@sprucedata.ornl.gov/DataFiles/EM1_Table1.dat'
sp_data=pd.read_fwf(url)
#print (sp_data)
columnnames = ["TIMESTAMP","RECORD","Tair","RH","AirTCHumm_Avg","RH_Humm_Avg","VPD","Rain","WS","WindDir_D1_WVT","WindDir_SD1_WVT","WSDiag_Tot","SmplsF_Tot","Axis1Failed_Tot","Axis2Failed_Tot","BothAxisFailed_Tot","NVMerror_Tot","ROMerror_Tot","MaxGain_Tot","NNDF_Tot","HollowSurf_Avg","Hollow5cm_Avg","Tsoil","Hollow40cm_Avg","Hollow80cm_Avg","Hollow160cm_Avg","Hollow200cm_Avg","HummockSurf_Avg","Hummock5cm_Avg","Hummock20cm_Avg","Hummock40cm_Avg","Hummock80cm_Avg","Hummock160cm_Avg","Hummock200cm_Avg","PAR","PAR_NTree1_Avg","PAR_NTree2_Avg","PAR_SouthofHollow1_Avg","PAR_SouthofHollow2_Avg","PAR_NorthofHollow1_Avg","PAR_NorthofHollow2_Avg","PAR_Srub1_Avg","PAR_Srub2_Avg","PAR_Srub3_Avg","PAR_Srub4_Avg","TopofHummock_Avg","MidofHummock_Avg","Surface1_Avg","Surface2_Avg","D1-20cm_Avg","D2-20cm_Avg","TopH_Avg","MidH_Avg","S1_Avg","S2_Avg","Deep-20cm_Avg","short_up_Avg","short_dn_Avg","long_up_Avg","long_dn_Avg","CNR4_Temp_C_Avg","CNR4_Temp_K_Avg","long_up_corr_Avg","long_dn_corr_Avg","Rs_net_Avg","Rl_net_Avg","albedo_Avg","Rn_Avg","SPN1_Total_Avg","SPN1_Diffuse_Avg","Water_Height_Avg","Water_Temp_Avg","Watertable","Dewpoint","Dewpoint_Diff"]
#columnnames = ["TIMESTAMP","RECORD","AirTC_2M_Avg","RH_2M_Avg","AirTCHumm_Avg","RH_Humm_Avg","BP_kPa_Avg","Rain_mm_Tot","WS_ms_S_WVT","WindDir_D1_WVT","WindDir_SD1_WVT","WSDiag_Tot","SmplsF_Tot","Axis1Failed_Tot","Axis2Failed_Tot","BothAxisFailed_Tot","NVMerror_Tot","ROMerror_Tot","MaxGain_Tot","NNDF_Tot","HollowSurf_Avg","Hollow5cm_Avg","Hollow20cm_Avg","Hollow40cm_Avg","Hollow80cm_Avg","Hollow160cm_Avg","Hollow200cm_Avg","HummockSurf_Avg","Hummock5cm_Avg","Hummock20cm_Avg","Hummock40cm_Avg","Hummock80cm_Avg","Hummock160cm_Avg","Hummock200cm_Avg","PAR_2_M_Avg","PAR_NTree1_Avg","PAR_NTree2_Avg","PAR_SouthofHollow1_Avg","PAR_SouthofHollow2_Avg","PAR_NorthofHollow1_Avg","PAR_NorthofHollow2_Avg","PAR_Srub1_Avg","PAR_Srub2_Avg","PAR_Srub3_Avg","PAR_Srub4_Avg","TopofHummock_Avg","MidofHummock_Avg","Surface1_Avg","Surface2_Avg","D1-20cm_Avg","D2-20cm_Avg","TopH_Avg","MidH_Avg","S1_Avg","S2_Avg","Deep-20cm_Avg","short_up_Avg","short_dn_Avg","long_up_Avg","long_dn_Avg","CNR4_Temp_C_Avg","CNR4_Temp_K_Avg","long_up_corr_Avg","long_dn_corr_Avg","Rs_net_Avg","Rl_net_Avg","albedo_Avg","Rn_Avg","SPN1_Total_Avg","SPN1_Diffuse_Avg","Water_Height_Avg","Water_Temp_Avg","Watertable","Dewpoint","Dewpoint_Diff"]
#write to a csv file
sp_data.to_csv('my1.csv',sep=';')
sp_data=pd.read_csv('my1.csv',skiprows=5)
sp_data.to_csv('my1.csv')
sp_data.columns = columnnames

sp_data.to_csv('my1.csv')

df=pd.read_csv('my1.csv')
#trying to bring the timestamp into a format
data=df['TIMESTAMP']
data=data.str.lstrip('0123456789')
data=data.str.strip(';"')
#adding it to the existing data frame
df['Date_Time']=data

#Trim columns
teco_spruce =df[['Date_Time','Tair','Tsoil','RH','VPD','Rain','WS','PAR']]
#dividing Date_Time to year,day and hour
time=teco_spruce['Date_Time']
#getting the year
year=time.str.split('-').str.get(0)
#gettting the month
month=time.str.split('-').str.get(1)
#getting the Day and hour
day_hour=time.str.split('-').str.get(2)
#day_hour
day=day_hour.str.split(' ').str.get(0)
hour=day_hour.str.split(' ').str.get(1)
#getting the day number from the year,month and day
#day=cal_day_num(year,month,day)
#extracting only the hour from a given time
hour=hour.str.rstrip('0')
hour=hour.str.rstrip(':')
hour=hour.str.rstrip('1234567890')
hour=hour.str.rstrip(':')
#adding it to the existing data frame
df['year']=year
df['day']=day
df['hour']=hour
df['month']=month
i=0

for i in range(6337):
    day=df.iloc[i]['day']
    #print('hello')
    #print('day->'+str(day))
    #print('hi')
    day=int(day)
    month=df.iloc[i]['month']
    
    month=int(month)
    #print('month->'+str(month))
    year=df.iloc[i]['year']
    year=int(year)
    #print('year->'+str(year))
    day_cal=cal_day_num(year,month,day)
    print('day_cal->'+str(day_cal))
    #setting each day to day of year
    df.loc[i,('day')]=day_cal
    #df.set_value('day',i,day_cal)
    i=i+1
    #print('i->'+str(i))
    #df.iloc[i]['day']=day_cal 
teco_spruce=df[['year','month','day','hour','Tair','Tsoil','RH','VPD','Rain','WS','PAR']]
#teco_spruce=pd.DataFrame(teco_spruce)
#getting the day number from the year,month and day
#Write to tab delimited file
teco_spruce.to_csv('teco_spruce.txt','\t')



# In[36]:

day_cal=cal_day_num(2016,1,26)
print('helo')
print(day_cal)


# In[33]:

print('helo')


# In[47]:

day=df.iloc[0]['day']
day=int(day)
month=teco_spruce.iloc[0]['month']
month=int(month)
year=teco_spruce.iloc[0]['year']
year=int(year)
day_cal=cal_day_num(year,month,day)
day_cal=55
df.iloc[0]['day1']=day_cal

