__author__ = 'GeoffreyWest'
import os
import pyodbc
import json
import collections
import requests
import time
import logging
import httplib
import datetime
import logging
import logging.handlers
import jsonpickle


def GetThisDir():
    import inspect
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def GetDateTimeString(n = None):
        """ format a datetime to string """
        if(n==None):
            s = time.strftime("%Y%m%d%H%M%S", time.localtime())
        else:
            s = time.strftime("%Y%m%d%H%M%S", time.localtime())
            if((isNumeric(n)==True) and ((n>4) and (n<14))):
               s = s[0:n]
            else:
               s = s[0:14]
        return s

def isNumeric(s):
    b = True
    try:
        i = float(s)
    except:    # not numericelse:    # numeric
        b= False
    return b


K_Response = 'Response'
K_ListOfServiceRequest = 'ListOfServiceRequest'
K_ServiceRequest = 'ServiceRequest'
if(__name__=='__main__'):
    lastpage = 'false'
    startrow = 0
    newquery = 'new'
    pagesize = 100

    url2 = "https://myla311.lacity.org/myla311router/mylasrbe/1/SANQueryPageSR"
    #f1 = open('C:\Projects\Trunk\LA2015\data\OrgRequest.json')

    #lReqTypes = ["Bulky Items","Electronic Waste","Metal/Household Appliances","Dead Animal Removal","Manual Pickup","Brush Items Pickup","Move In/Move Out","Illegal Dumping Pickup"]
    #sWhere = 'Select * from MyTBL where ReqType in ("Bulky Items","Electronic Waste","Metal/Household Appliances","Dead Animal Removal","Manual Pickup","Brush Items Pickup","Move In/Move Out","Illegal Dumping Pickup")'
    #sWhere = 'Select * from MyTBL where ReqType in ("Bulky Items")'
    #for ReqType in lReqTypes:
    #    Resp = MyRequest(ReqType)
    #    pJson = Resp.json

    #print (len(lReqTypes))
    pJson = None
    sDir =  GetThisDir()
    sReqFile = os.path.join(sDir, "Request.json")
    f1 = open(sReqFile)           # 'C:\Projects\Trunk\LA2015\data\Request.json')
    data2Json = jsonpickle.decode((f1.read()))
    data2 = jsonpickle.encode(data2Json)
    headers2 = {'Content-type': 'text/plain', 'Accept': '/'}
    sRsltDir = os.path.join(sDir, "Rslt")
    if(os.path.exists(sRsltDir)==False): os.mkdir(sRsltDir)
    sRsltFile = "Resp" + str(GetDateTimeString(12)) + ".log"
    sRsltFile = os.path.join(sRsltDir, sRsltFile)

    with open(sRsltFile,"w") as fout:
        i = 0
        while lastpage == 'false':
            r2 = requests.post(url2, data=data2, headers=headers2)
            decoded2 = r2.json()
            if(pJson==None):
                pJson = r2.json()
            else:
                # Get the list containing the request items[dict()] lRequest=[dict1(), dict2()]
                lServiceRequests = pJson[K_Response][K_ListOfServiceRequest][K_ServiceRequest]
                decoded2 = r2.json()
                lServiceRequetsD = decoded2[K_Response][K_ListOfServiceRequest][K_ServiceRequest]
                for r in lServiceRequetsD:
                    lServiceRequests.append(r)
            lastpage = decoded2['Response']['LastPage']
            i = i + 1
            sMsg = "nRequest={}, len(pJson['Response']['ListOfServiceRequest']['ServiceRequest'])={}".format(i, len(pJson[K_Response][K_ListOfServiceRequest][K_ServiceRequest]))
            print(sMsg)
            pJson['Response']['NumOutputObjects'] = len(pJson[K_Response][K_ListOfServiceRequest][K_ServiceRequest])

            if  lastpage == 'false':
                data2Json['QueryRequest']['PageSize'] = pagesize
                startrow = startrow + data2Json['QueryRequest']['PageSize']
                data2Json['QueryRequest']['StartRowNum'] = startrow
                data2Json['QueryRequest']['NewQuery'] = 'false'
                data2 = jsonpickle.encode(data2Json)
                print startrow

           # open the file as fout
        if(pJson!=None):
            #json.dump(pJson,fout)
            sJson = json.dumps(pJson, sort_keys=True, indent=2)
            fout.write(sJson)
            sMsg = "nRequest={}, TotalServiceRequests={}  ResultsJsonHas {} chars".format(i, len(pJson[K_Response][K_ListOfServiceRequest][K_ServiceRequest]), len(sJson))
            print(sMsg)

    os.popen(sRsltFile)

    #iiException = 0
    #while iiException < 3:
    #    try:
    #        pass
    #        #request.send()
    #    except:
    #        iiException = iiException + 1
    #        pass
    #        #request.send()






