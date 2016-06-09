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
doy=day_hour.str.split(' ').str.get(0)
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
df['doy']=doy
df['hour']=hour
df['month']=month
i=0
length=len(df.index)
for i in range(length):
    doy=df.iloc[i]['doy']
    #print('hello')
    #print('day->'+str(day))
    #print('hi')
    doy=int(doy)
    month=df.iloc[i]['month']
    
    month=int(month)
    #print('month->'+str(month))
    year=df.iloc[i]['year']
    year=int(year)
    #print('year->'+str(year))
    doy_cal=cal_day_num(year,month,doy)
    #print('day_cal->'+str(day_cal))
    #setting each day to day of year
    df.loc[i,('doy')]=doy_cal
    #df.set_value('day',i,day_cal)
    i=i+1
    #print('i->'+str(i))
    #df.iloc[i]['day']=day_cal 
teco_spruce=df[['year','doy','hour','Tair','Tsoil','RH','VPD','Rain','WS','PAR']]
#teco_spruce=pd.DataFrame(teco_spruce)
#getting the mean of 'Tair','Tsoil','RH','VPD','WS','PAR' n sum of ,'Rain' by combining half n full hour(e.i.12 & 12:30)
group_treat=teco_spruce.groupby(['year','doy','hour'])
tair=group_treat['Tair'].mean()
tsoil=group_treat['Tsoil'].mean()
rh=group_treat['RH'].mean()
vpd=group_treat['VPD'].mean()
rain=group_treat['Rain'].sum()
ws=group_treat['WS'].mean()
par=group_treat['PAR'].mean()
#Taking only the even coulums(as half hourly details not required) i.e. 12:30 not required only 12 required 
#teco_spruce1=teco_spruce.iloc[::2]
teco_spruce1=teco_spruce.iloc[::2]
#need to reset the index number[from 0 2 4 8] [to 0 1 2 3]
teco_spruce1=teco_spruce1.reset_index(drop=True)
i=0
length1=len(teco_spruce1.index)
#setting the mean of 'Tair','Tsoil','RH','VPD','WS','PAR' n sum of ,'Rain' to this new dataframe teco_spruce1

for i in range(length1):
    teco_spruce1.loc[i,('Tair')]=tair.iloc[i]
    teco_spruce1.loc[i,('Tsoil')]=tsoil.iloc[i]
    teco_spruce1.loc[i,('RH')]=rh.iloc[i]
    teco_spruce1.loc[i,('VPD')]=vpd.iloc[i]
    teco_spruce1.loc[i,('Rain')]=rain.iloc[i]
    teco_spruce1.loc[i,('WS')]=ws.iloc[i]
    teco_spruce1.loc[i,('PAR')]=par.iloc[i]
   

#Write to tab delimited file
teco_spruce1.to_csv('teco_spruce.txt','\t',index=False)
# joining the new file with the earlier file

#file which contain earlier data(2011-2015)
j1=pd.read_csv('join_try.txt','\t')

#file which contain the new data
j2=pd.read_csv('teco_spruce.txt','\t')

#joining both the files together and removing the duplicate rows
j3=pd.concat([j1,j2]).drop_duplicates().reset_index(drop=True)

#writing it to a file
j3.to_csv('final.txt','\t',index=False)

