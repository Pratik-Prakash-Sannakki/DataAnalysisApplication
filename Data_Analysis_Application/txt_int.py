import numpy as np
from numpy import unicode
import datetime


# date field conversion function
dateconv = lambda s: datetime.strptime(s, '%Y-%M-%D %H:%M:%S:.%f')

col_names = ["Timestamp", "val1", "val2", "val3", "val4"]
dtypes = ["object", "float", "float", "float", "float"]
col_names1= ["Timestamp", "val1", "val2", "val3"]
dtypes1= ["|S10","|S10","|S10","|S10"]

mydata = np.genfromtxt("workfile.txt",skip_header=4,delimiter='',unpack=None, names=col_names,usecols=(1,2,3,4),dtype=dtypes, converters={"Time": dateconv})
with open("workfile.txt","r",encoding='utf8',errors='ignore') as fp:
    for i, line in enumerate(fp):
        if i == 2:
            myparam=line.strip().split("   ")
            print("$$$$$$$$$$$$$$$$$$$$")
            print(myparam)
            print("$$$$$$$$$$$$$$$$$")
#myparam= np.genfromtxt("workfile.txt",skip_header=2,skip_footer=49,delimiter='', names=col_names1,unpack=None,dtype=dtypes1,usecols=(0,1,2,3,4))
voltage=mydata['val2']
current=mydata['val3']
Temprature=mydata['val4']
print(voltage)
vol=list(voltage)
hello=list(mydata['val1'])
cur=list(current)
temp=list(Temprature)
print(vol)
print(cur)
print(temp)
print(myparam[0])
#param=list(myparam[0])
#print(param)
maxhello=max(hello)
maxvol=max(vol)
maxcur=max(cur)
maxtemp=max(temp)
print(maxhello)
print(maxvol)
print(maxcur)
print(maxtemp)
#print(len(param))
