
# coding: utf-8

# In[38]:

import pandas as pd
import datetime
#Get from ftp site
from ftplib import FTP
import urllib, shutil
'''
url="ftp://ftp_public:spruce_s1@sprucedata.ornl.gov/DataFiles_2014/EM1_Table1.dat"
ftpfile = urllib.request.urlopen(url)
localfile = open("my.csv", "wb")
shutil.copyfileobj(ftpfile, localfile)
ftp = FTP('sprucedata.ornl.gov') 
ftp.login('ftp_public','spruce_s1')
#load into pandas dataframe
'''
url = 'ftp://ftp_public:spruce_s1@sprucedata.ornl.gov/DataFiles_2014/EM1_Table1.dat'
sp_data=pd.read_fwf(url)
#print (sp_data)
columnnames = ["TIMESTAMP","RECORD","AirTC_2M_Avg","RH_2M_Avg","AirTCHumm_Avg","RH_Humm_Avg","BP_kPa_Avg","Rain_mm_Tot","WS_ms_S_WVT","WindDir_D1_WVT","WindDir_SD1_WVT","WSDiag_Tot","SmplsF_Tot","Axis1Failed_Tot","Axis2Failed_Tot","BothAxisFailed_Tot","NVMerror_Tot","ROMerror_Tot","MaxGain_Tot","NNDF_Tot","HollowSurf_Avg","Hollow5cm_Avg","Hollow20cm_Avg","Hollow40cm_Avg","Hollow80cm_Avg","Hollow160cm_Avg","Hollow200cm_Avg","HummockSurf_Avg","Hummock5cm_Avg","Hummock20cm_Avg","Hummock40cm_Avg","Hummock80cm_Avg","Hummock160cm_Avg","Hummock200cm_Avg","PAR_2_M_Avg","PAR_NTree1_Avg","PAR_NTree2_Avg","PAR_SouthofHollow1_Avg","PAR_SouthofHollow2_Avg","PAR_NorthofHollow1_Avg","PAR_NorthofHollow2_Avg","PAR_Srub1_Avg","PAR_Srub2_Avg","PAR_Srub3_Avg","PAR_Srub4_Avg","TopofHummock_Avg","MidofHummock_Avg","Surface1_Avg","Surface2_Avg","D1-20cm_Avg","D2-20cm_Avg","TopH_Avg","MidH_Avg","S1_Avg","S2_Avg","Deep-20cm_Avg","short_up_Avg","short_dn_Avg","long_up_Avg","long_dn_Avg","CNR4_Temp_C_Avg","CNR4_Temp_K_Avg","long_up_corr_Avg","long_dn_corr_Avg","Rs_net_Avg","Rl_net_Avg","albedo_Avg","Rn_Avg","SPN1_Total_Avg","SPN1_Diffuse_Avg","Water_Height_Avg","Water_Temp_Avg","Watertable","Dewpoint","Dewpoint_Diff"]
#write to a csv file
sp_data.to_csv('my1.csv')
sp_data=pd.read_csv('my.csv',skiprows=4)
sp_data.to_csv('my1.csv')
sp_data.columns = columnnames
sp_data.to_csv('my1.csv')
df=pd.read_csv('my1.csv')
#Trim columns
teco_spruce =df[['AirTC_2M_Avg','RH_2M_Avg','Rain_mm_Tot','WS_ms_S_WVT','Hollow20cm_Avg','PAR_2_M_Avg']]

#Write to tab delimited file
teco_spruce.to_csv('teco_spruce.txt','\t')

