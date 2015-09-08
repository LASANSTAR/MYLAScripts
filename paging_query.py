__author__ = 'Administrator'
import json
import jsonpickle
import requests
import time
import datetime


start = time.time()
Start = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
f2 =open('C:\Users\GeoffreyWest\Desktop\Request.json')
data2 = jsonpickle.decode((f2.read()))
Start = datetime.datetime.now()
DD = datetime.timedelta(minutes=5)
earlier = Start - DD
earlier_str = earlier.strftime('X%m/%d/%Y %H:%M:%S').replace('X0','X').replace('X','')
lastpage = 'false'
startrow = 0
newquery = 'new'
pagesize = 100


# for datatime in data2:
   # DataTime = data2["SRData"]['LastUpdatedDate'] = str(earlier_str)

# print data2['QueryRequest']['NewQuery']

data2 = jsonpickle.encode(data2)

url2 = "https://myla311.lacity.org/myla311router/mylasrbe/1/SANQueryPageSR"
headers2 = {'Content-type': 'text/plain', 'Accept': '/'}
# try:
#     r2
# except requests.exceptions.ConnectTimeout as e:
#     print "Too slow Mojo!"
#
# decoded2 = json.loads(r2.text)


while lastpage == 'false':
    r2 = requests.post(url2, data=data2, headers=headers2)
    print r2.text
    decoded2 = json.loads(r2.text)
    f2 =open('C:\Users\GeoffreyWest\Desktop\Request.json')
    data2 = jsonpickle.decode((f2.read()))
    if decoded2['Response']['LastPage'] == 'false':
        data2['QueryRequest']['PageSize'] = pagesize
        startrow = startrow + data2['QueryRequest']['PageSize']
        data2['QueryRequest']['StartRowNum'] = startrow
        data2['QueryRequest']['NewQuery'] = 'false'
        data2 = jsonpickle.encode(data2)
        print startrow
    else:
        lastpage = 'true'





#
# n = 0
# while n < 6:
#     print n
#     n = n+1
# print 'Blastoff!'






# data2 = jsonpickle.decode((f2.read()))
# data2['QueryRequest']['NewQuery'] =='false'
# pagesize = int(data2['QueryRequest']['StartRowNum']) + count
# print pagesize
# data2 = jsonpickle.encode(data2)
# r2



