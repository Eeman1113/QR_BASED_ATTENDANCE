import pandas as pd
import requests
import pyqrcode
import png
from pyqrcode import QRCode
import random

def qr_gen(s):
    url = pyqrcode.create(s)
    url.svg("/Users/eemanmajumder/code_shit/QR_BASED_ATTENDANCE/QR/{}.svg".format(s), scale = 8)
    url.png('/Users/eemanmajumder/code_shit/QR_BASED_ATTENDANCE/QR/{}.png'.format(s), scale = 6)
a=input('enter event name')
if a=='TAB':
    df=pd.read_csv('/Users/eemanmajumder/code_shit/QR_BASED_ATTENDANCE/Database/TAB.csv','w')
    df=df.dropna()
    #add a coloumn to the csv file with random string
    
    df['Unique_ID']=df['Name'].apply(lambda x: ''.join(random.choice('0123456789ABCDEF') for i in range(16)))
    for i in df['Unique_ID']:
        qr_gen(i)
elif a=='AB':
    
    df=pd.read_csv('/Users/eemanmajumder/code_shit/QR_BASED_ATTENDANCE/Database/AB.csv','w',error_bad_lines=False)
    df=df.dropna()
    #add a coloumn to the csv file with random string
    df['Unique_ID']=df['Name'].apply(lambda x: ''.join(random.choice('0123456789ABCDEF') for i in range(16)))
    for i in df['Unique_ID']:
        qr_gen(i)
elif a=="C":
    df=pd.read_csv('/Users/eemanmajumder/code_shit/QR_BASED_ATTENDANCE/Database/C.csv','w')
    df=df.dropna()
    #add a coloumn to the csv file with random string
    df['Unique_ID']=df['Name'].apply(lambda x: ''.join(random.choice('0123456789ABCDEF') for i in range(16)))
    for i in df['Unique_ID']:
        qr_gen(i)

else:
    print('wrong event name')

# s = "congratulations! sakshiiiii"
# url = pyqrcode.create(s)
# url.svg("/Users/eemanmajumder/code_shit/QR_BASED_ATTENDANCE/QR/myqr.svg", scale = 8)
# url.png('/Users/eemanmajumder/code_shit/QR_BASED_ATTENDANCE/QR/myqr.png', scale = 6)