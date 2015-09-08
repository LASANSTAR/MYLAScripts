Addi__author__ = 'Administrator'

import json
import jsonpickle
import requests
import arcpy
import numpy as np
import datetime
from email.mime.text import MIMEText
import sys
import traceback
import smtplib
from email.MIMEText import MIMEText
import time
import datetime
import logging
import logging.handlers
import io
import os


arcpy.SetLogHistory(True)
start = time.time()
Start = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
msgFolder = "C:/logs/"
sender = "geoffreywestgis@gmail.com"
recipient = "geoffreywestgis@gmail.com"
fc2 = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311"
fc = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311RoutingTest"
appendClass = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_SCData_sa.sde\SCData.DBO.SO_SC_1"
aTable = "C:\Users\GeoffreyWest\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\ServiceRequest.sde\ServiceRequest.DBO.History_Table_"
aContainerFC = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.aContainerFC21"
connect_timeout = 5

# f2 =open('C:\Users\GeoffreyWest\Desktop\ContainerRequest.json')
# data2 = jsonpickle.decode((f2.read()))
# print data2
# Start = datetime.datetime.now()
# # Start = datetime.datetime.strftime(data2['QueryRequest']['LastUpdatedDate'])
# DD = datetime.timedelta(minutes=5)
# earlier = Start - DD
# earlier_str = earlier.strftime('X%m/%d/%Y %H:%M:%S').replace('X0','X').replace('X','')
# # data2["QueryRequest"]['LastUpdatedDate'] = str(earlier_str)
# data2 = jsonpickle.encode(data2)
# BulkyItemInfo = " "
spatial_ref = arcpy.SpatialReference(4326)




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



lastpage = 'false'
startrow = 0
newquery = 'new'
pagesize = 100
K_Response = 'Response'
K_ListOfServiceRequest = 'ListOfServiceRequest'
K_ServiceRequest = 'ServiceRequest'


url2 = "https://myla311RemoteTest.lacity.org/myla311router/mylasrbe/1/SANQueryPageSR"

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

        if  lastpage == 'false':
            data2Json['QueryRequest']['PageSize'] = pagesize
            startrow = startrow + data2Json['QueryRequest']['PageSize']
            data2Json['QueryRequest']['StartRowNum'] = startrow
            data2Json['QueryRequest']['NewQuery'] = 'false'
            data2 = jsonpickle.encode(data2Json)
            print startrow


    if(pJson!=None):
            #json.dump(pJson,fout)
            sJson = json.dumps(pJson, sort_keys=True, indent=2)
            fout.write(sJson)
            sMsg = "nRequest={}, TotalServiceRequests={}  ResultsJsonHas {} chars".format(i, len(pJson[K_Response][K_ListOfServiceRequest][K_ServiceRequest]), len(sJson))
            print(sMsg)


    k_illegal_comm = ' '
    BulkyItemInfo = " "
    EwasteItemInfo = " "
    MHAItemInfo = " "
    DACItemInfo = " "
    ServiceNotCompleteInfo = " "
    ManualPickUpInfo= " "
    BrushItemInfo = " "
    MoveInMoveOutInfo  =  " "
    ContainersInfo =  " "
    IllegalDumpingInfo = " "
    k_bulky_count =  " "
    k_bulky_item = ' '
    BulkyItemInfo = " "
    itemDesc = " "
    iteminfoewaste = ' '
    k_ewaste_comm = ' '
    k_bulky_comm = ' '
    itemDesc = ' '
    eItemInfo = " "
    dar_comm  = ' '
    k_dar_comm = ' '
    MHAItemInfo = ' '
    k_brush_comm = ' '
    k_man_comm = ' '
    k_container_type = ' '
    k_container_request_for = ' '
    k_damage_on_wheels = ' '
    k_damage_axle = ' '
    k_damage_lid =  ' '
    k_damage_on_handle = ' '
    k_container_number = ' '
    k_container_reason = ' '

    #
    # if 'La311ServiceRequestNotes' in ServiceNotes:
    #                 try:
    #                     k_comment = ServiceNotes['La311ServiceRequestNotes'][0]['Comment']
    #                 except IndexError:
    #                     k_comment = ' '
    #                 print k_comment


    containerItems = []
    for sr in pJson['Response']['ListOfServiceRequest']['ServiceRequest']:
        ContainerAddress = sr['SRAddress']
        if sr['Latitude'] != '':
            container_y = sr['Latitude']
        if sr['Longitude'] != '':
            container_x = sr['Longitude']
        if sr['Latitude'] == '':
            container_blanky = sr['Latitude']
        if sr['Longitude'] == '':
            container_blankx= sr['Longitude']
        Containers = sr['ListOfLa311Containers']
        Container_ReasonCode = sr['ReasonCode']
        Container_SRNumber = sr['SRNumber']
        Container_FirstName = sr['FirstName']
        Container_LastName = sr['LastName']
        Container_ResolutionCode = sr['ResolutionCode']
        Container_HomePhone = sr['HomePhone']
        Container_CreatedDate = sr['CreatedDate']
        Container_UpdatedDate = sr['UpdatedDate']

        if sr['ServiceDate'] !=  '':
            ServiceDate=  sr['ServiceDate']


    try:
        if sr['ListOfLa311GisLayer'] != '{},':
            Container_GISLayer = sr['ListOfLa311GisLayer']['La311GisLayer'][0]['DistrictName']
        print GISLayer
    except Exception:
        pass

    Container_CreatedDate = datetime.datetime.strptime(Container_CreatedDate, "%m/%d/%Y %H:%M:%S")
    Container_UpdatedDate = datetime.datetime.strptime(Container_UpdatedDate, "%m/%d/%Y %H:%M:%S")

    k_illegal_comm = ' '
    BulkyItemInfo = " "
    EwasteItemInfo = " "
    MHAItemInfo = " "
    DACItemInfo = " "
    ServiceNotCompleteInfo = " "
    ManualPickUpInfo= " "
    BrushItemInfo = " "
    MoveInMoveOutInfo  =  " "
    ContainersInfo =  " "
    IllegalDumpingInfo = " "
    k_bulky_count =  " "
    k_bulky_item = ' '
    BulkyItemInfo = " "
    itemDesc = " "
    iteminfoewaste = ' '
    k_ewaste_comm = ' '
    k_bulky_comm = ' '
    itemDesc = ' '
    eItemInfo = " "
    dar_comm  = ' '
    k_dar_comm = ' '
    MHAItemInfo = ' '
    k_brush_comm = ' '
    k_man_comm = ' '
    k_container_type = ' '
    k_container_request_for = ' '
    k_damage_on_wheels = ' '
    k_damage_axle = ' '
    k_damage_lid =  ' '
    k_damage_on_handle = ' '
    k_container_number = ' '
    k_container_reason = ' '
    SCCatDesc = ' '





    k_bulky_comm = ' '
    itemDesc = ' '

    try:

        k_container = ' '
        k_container_size_1 = ' '
        container_info = " "
        for sr in Containers:
          if("La311Containers" in Containers):
            lcontainers311 = Containers ["La311Containers"]
            for Containers in lcontainers311:
                k_container_size_1= Containers['ContainerSize']
                k_container_type_1 = Containers['ContainerType']
                k_damage_lid_1 = Containers['DamageonLid']
                k_damage_axle_1 = Containers['DamageonAxle']
                k_damage_on_body_1 = Containers['DamageonBody']
                k_damage_on_handle_1 = Containers['DamageonHandleEndcap']
                k_damage_on_wheels_1 = Containers ['DamageonWheels']
                k_container_number_1= Containers['ContainerNumber']
                k_container_name_1= Containers['Name']
                # print k_container_number_1
                if Containers==lcontainers311[0]:
                    k_container_number_1 = k_container_number_1
                    k_damage_on_wheels_1 = k_damage_on_wheels_1
                    k_damage_on_handle_1 = k_damage_on_handle_1
                    k_damage_on_body_1 = k_damage_on_body_1
                    k_damage_axle_1 = k_damage_axle_1
                    k_damage_lid_1 = k_damage_lid_1
                    k_container_type_1 =k_container_type_1
                    k_container_size_1 = k_container_size_1
                    k_container_name_1=k_container_name_1

    except:
        print "No Container Information"






    try:
        k_container_size_2= ' '
        k_container_number_2 = ' '
        k_damage_on_wheels_2 = ' '
        k_container_type_2 = ' '
        k_damage_on_handle_2 = ' '
        k_damage_axle_2 = ' '
        k_damage_on_body_2 = ' '
        k_damage_lid_2 = ' '

        k_container = ' '
        k_container_size = ' '
        container_info = " "
        for sr in Containers:
          if("La311Containers" in Containers):
            lcontainers311 = Containers ["La311Containers"]
            for Containers in lcontainers311:
                k_container_size_2= Containers['ContainerSize']
                k_container_type_2 = Containers['ContainerType']
                k_damage_lid_2 = Containers['DamageonLid']
                k_damage_axle_2 = Containers['DamageonAxle']
                k_damage_on_body_2 = Containers['DamageonBody']
                k_damage_on_handle_2 = Containers['DamageonHandleEndcap']
                k_damage_on_wheels_2 = Containers ['DamageonWheels']
                k_container_number_2= Containers['ContainerNumber']
                k_container_name_2= Containers['Name']
                # print k_container_number_1
                if Containers==lcontainers311[1]:
                    k_container_number_2 = k_container_number_2
                    k_damage_on_wheels_2 = k_damage_on_wheels_2
                    k_damage_on_handle_2 = k_damage_on_handle_2
                    k_damage_on_body_2 = k_damage_on_body_2
                    k_damage_axle_2 = k_damage_axle_2
                    k_damage_lid_2 = k_damage_lid_2
                    k_container_type_2 =k_container_type_2
                    k_container_size_2 = k_container_size_2
                    k_container_name_2=k_container_name_2

    except:
        print "No Container Information"






    try:
        k_container_size_3= ' '
        k_container_number_3 = ' '
        k_damage_on_wheels_3 = ' '
        k_container_type_3 = ' '
        k_damage_on_handle_3 = ' '
        k_damage_axle_3 = ' '
        k_damage_on_body_3 = ' '
        k_damage_lid_3 = ' '






        k_container = ' '
        k_container_size = ' '
        container_info = " "
        for sr in Containers:
          if("La311Containers" in Containers):
            lcontainers311 = Containers ["La311Containers"]
            for Containers in lcontainers311:
                k_container_size_3= Containers['ContainerSize']
                k_container_type_3 = Containers['ContainerType']
                k_damage_lid_3 = Containers['DamageonLid']
                k_damage_axle_3= Containers['DamageonAxle']
                k_damage_on_body_3 = Containers['DamageonBody']
                k_damage_on_handle_3 = Containers['DamageonHandleEndcap']
                k_damage_on_wheels_3 = Containers ['DamageonWheels']
                k_container_number_3= Containers['ContainerNumber']
                k_container_name_3= Containers['Name']
                # print k_container_number_1
                if Containers==lcontainers311[2]:
                    k_container_number_3 = k_container_number_3
                    k_damage_on_wheels_3 = k_damage_on_wheels_3
                    k_damage_on_handle_3 = k_damage_on_handle_3
                    k_damage_on_body_3 = k_damage_on_body_3
                    k_damage_axle_3 = k_damage_axle_3
                    k_damage_lid_3 = k_damage_lid_3
                    k_container_type_3 =k_container_type_3
                    k_container_size_3 = k_container_size_3
                    k_container_name_3=k_container_name_3


    except:
        print "No Container Information"





    try:

        k_container_size_4= ' '
        k_container_number_4 = ' '
        k_damage_on_wheels_4 = ' '
        k_container_type_4 = ' '
        k_damage_on_handle_4 = ' '
        k_damage_axle_4 = ' '
        k_damage_on_body_4 = ' '
        k_damage_lid_4 = ' '
        k_container = ' '
        k_container_size = ' '
        container_info = " "
        for sr in Containers:
          if("La311Containers" in Containers):
            lcontainers311 = Containers ["La311Containers"]
            for Containers in lcontainers311:
                k_container_size_4= Containers['ContainerSize']
                k_container_type_4 = Containers['ContainerType']
                k_damage_lid_4 = Containers['DamageonLid']
                k_damage_axle_4 = Containers['DamageonAxle']
                k_damage_on_body_4 = Containers['DamageonBody']
                k_damage_on_handle_4 = Containers['DamageonHandleEndcap']
                k_damage_on_wheels_4 = Containers ['DamageonWheels']
                k_container_number_4= Containers['ContainerNumber']
                k_container_name_4= Containers['Name']
                # print k_container_number_1
                if Containers==lcontainers311[3]:
                    k_container_number_4 = k_container_number_4
                    k_damage_on_wheels_4 = k_damage_on_wheels_4
                    k_damage_on_handle_4 = k_damage_on_handle_4
                    k_damage_on_body_4 = k_damage_on_body_4
                    k_damage_axle_4 = k_damage_axle_4
                    k_damage_lid_4 = k_damage_lid_4
                    k_container_type_4 =k_container_type_4
                    k_container_size_4 = k_container_size_4
                    k_container_name_4=k_container_name_4
    except:
        print "No Container Information"





    try:

        k_container = ' '
        k_container_size = ' '
        container_info = " "
        k_container_size_5= ' '
        k_container_number_5 = ' '
        k_damage_on_wheels_5 = ' '
        k_container_type_5 = ' '
        k_damage_on_handle_5 = ' '
        k_damage_axle_5 = ' '
        k_damage_on_body_5 = ' '
        k_damage_lid_5 = ' '
        for sr in Containers:
          if("La311Containers" in Containers):
            lcontainers311 = Containers ["La311Containers"]
            for Containers in lcontainers311:
                k_container_size_5= Containers['ContainerSize']
                k_container_type_5 = Containers['ContainerType']
                k_damage_lid_5 = Containers['DamageonLid']
                k_damage_axle_5 = Containers['DamageonAxle']
                k_damage_on_body_5 = Containers['DamageonBody']
                k_damage_on_handle_5 = Containers['DamageonHandleEndcap']
                k_damage_on_wheels_5 = Containers ['DamageonWheels']
                k_container_number_5= Containers['ContainerNumber']
                k_container_name_5= Containers['Name']
                # print k_container_number_1
                if Containers==lcontainers311[4]:
                    k_container_number_5 = k_container_number_5
                    k_damage_on_wheels_5 = k_damage_on_wheels_5
                    k_damage_on_handle_5 = k_damage_on_handle_5
                    k_damage_on_body_5 = k_damage_on_body_5
                    k_damage_axle_5 = k_damage_axle_5
                    k_damage_lid_5 = k_damage_lid_5
                    k_container_type_5 =k_container_type_5
                    k_container_size_5 = k_container_size_5
                    k_container_name_5=k_container_name_5
    except:
        print "No Container Information"


    try:
        k_container_size_6= ' '
        k_container_number_6 = ' '
        k_damage_on_wheels_6 = ' '
        k_container_type_6 = ' '
        k_damage_on_handle_6 = ' '
        k_damage_axle_6 = ' '
        k_damage_on_body_6 = ' '
        k_damage_lid_6 = ' '
        k_container = ' '
        k_container_size = ' '
        container_info = " "
        for sr in Containers:
          if("La311Containers" in Containers):
            lcontainers311 = Containers ["La311Containers"]
            for Containers in lcontainers311:
                k_container_size_6= Containers['ContainerSize']
                k_container_type_6 = Containers['ContainerType']
                k_damage_lid_6 = Containers['DamageonLid']
                k_damage_axle_6 = Containers['DamageonAxle']
                k_damage_on_body_6 = Containers['DamageonBody']
                k_damage_on_handle_6 = Containers['DamageonHandleEndcap']
                k_damage_on_wheels_6 = Containers ['DamageonWheels']
                k_container_number_6= Containers['ContainerNumber']
                k_container_name_6= Containers['Name']
                # print k_container_number_1
                if Containers==lcontainers311[5]:
                    k_container_number_6 = k_container_number_6
                    k_damage_on_wheels_6 = k_damage_on_wheels_6
                    k_damage_on_handle_6 = k_damage_on_handle_6
                    k_damage_on_body_6 = k_damage_on_body_6
                    k_damage_axle_6 = k_damage_axle_6
                    k_damage_lid_6 = k_damage_lid_6
                    k_container_type_6 =k_container_type_6
                    k_container_size_6 = k_container_size_6
                    k_container_name_6=k_container_name_6
    except:
        print "No Container Information"



    try:
        k_container_size_7= ' '
        k_container_number_7 = ' '
        k_damage_on_wheels_7 = ' '
        k_container_type_7 = ' '
        k_damage_on_handle_7 = ' '
        k_damage_axle_7 = ' '
        k_damage_on_body_7 = ' '
        k_damage_lid_7 = ' '
        k_container = ' '
        k_container_size = ' '
        container_info = " "
        for sr in Containers:
          if("La311Containers" in Containers):
            lcontainers311 = Containers ["La311Containers"]
            for Containers in lcontainers311:
                k_container_size_7= Containers['ContainerSize']
                k_container_type_7 = Containers['ContainerType']
                k_damage_lid_7 = Containers['DamageonLid']
                k_damage_axle_7 = Containers['DamageonAxle']
                k_damage_on_body_7 = Containers['DamageonBody']
                k_damage_on_handle_7 = Containers['DamageonHandleEndcap']
                k_damage_on_wheels_7 = Containers ['DamageonWheels']
                k_container_number_7= Containers['ContainerNumber']
                k_container_name_7= Containers['Name']
                # print k_container_number_1
                if Containers==lcontainers311[6]:
                    k_container_number_7 = k_container_number_7
                    k_damage_on_wheels_7 = k_damage_on_wheels_7
                    k_damage_on_handle_7 = k_damage_on_handle_7
                    k_damage_on_body_7 = k_damage_on_body_7
                    k_damage_axle_7 = k_damage_axle_7
                    k_damage_lid_7 = k_damage_lid_7
                    k_container_type_7 =k_container_type_7
                    k_container_size_7 = k_container_size_7
                    k_container_name_7=k_container_name_7
    except:
        print "No Container Information"





    try:
        k_container_size_8= ' '
        k_container_number_8 = ' '
        k_damage_on_wheels_8 = ' '
        k_container_type_8 = ' '
        k_damage_on_handle_8 = ' '
        k_damage_axle_8 = ' '
        k_damage_on_body_8 = ' '
        k_damage_lid_8 = ' '
        k_container = ' '
        k_container_size = ' '
        container_info = " "
        for sr in Containers:
          if("La311Containers" in Containers):
            lcontainers311 = Containers ["La311Containers"]
            for Containers in lcontainers311:
                k_container_size_8= Containers['ContainerSize']
                k_container_type_8 = Containers['ContainerType']
                k_damage_lid_8 = Containers['DamageonLid']
                k_damage_axle_8 = Containers['DamageonAxle']
                k_damage_on_body_8 = Containers['DamageonBody']
                k_damage_on_handle_8 = Containers['DamageonHandleEndcap']
                k_damage_on_wheels_8 = Containers ['DamageonWheels']
                k_container_number_8= Containers['ContainerNumber']
                k_container_name_8= Containers['Name']
                # print k_container_number_1
                if Containers==lcontainers311[7]:
                    k_container_number_8 = k_container_number_8
                    k_damage_on_wheels_8 = k_damage_on_wheels_8
                    k_damage_on_handle_8 = k_damage_on_handle_8
                    k_damage_on_body_8 = k_damage_on_body_8
                    k_damage_axle_8 = k_damage_axle_8
                    k_damage_lid_8 = k_damage_lid_8
                    k_container_type_8 =k_container_type_8
                    k_container_size_8 = k_container_size_8
                    k_container_name_8=k_container_name_8
    except:
        print "No Container Information"




    try:
        k_container_size_9= ' '
        k_container_number_9 = ' '
        k_damage_on_wheels_9 = ' '
        k_container_type_9 = ' '
        k_damage_on_handle_9 = ' '
        k_damage_axle_9 = ' '
        k_damage_on_body_9 = ' '
        k_damage_lid_9 = ' '
        k_container = ' '
        k_container_size = ' '
        container_info = " "
        for sr in Containers:
          if("La311Containers" in Containers):
            lcontainers311 = Containers ["La311Containers"]
            for Containers in lcontainers311:
                k_container_size_9= Containers['ContainerSize']
                k_container_type_9 = Containers['ContainerType']
                k_damage_lid_9 = Containers['DamageonLid']
                k_damage_axle_9 = Containers['DamageonAxle']
                k_damage_on_body_9 = Containers['DamageonBody']
                k_damage_on_handle_9 = Containers['DamageonHandleEndcap']
                k_damage_on_wheels_9 = Containers ['DamageonWheels']
                k_container_number_9= Containers['ContainerNumber']
                k_container_name_9= Containers['Name']
                # print k_container_number_1
                if Containers==lcontainers311[8]:
                    k_container_number_9 = k_container_number_9
                    k_damage_on_wheels_9 = k_damage_on_wheels_9
                    k_damage_on_handle_9 = k_damage_on_handle_9
                    k_damage_on_body_9 = k_damage_on_body_9
                    k_damage_axle_9 = k_damage_axle_9
                    k_damage_lid_9 = k_damage_lid_9
                    k_container_type_9 =k_container_type_9
                    k_container_size_9 = k_container_size_9
                    k_container_name_9=k_container_name_9
    except:
        print "No Container Information"


    try:


        k_container_size_10= ' '
        k_container_number_10 = ' '
        k_damage_on_wheels_10 = ' '
        k_container_type_10 = ' '
        k_damage_on_handle_10 = ' '
        k_damage_axle_10 = ' '
        k_damage_on_body_10 = ' '
        k_damage_lid_10 = ' '
        k_container = ' '
        k_container_size = ' '
        container_info = " "
        for sr in Containers:
          if("La311Containers" in Containers):
            lcontainers311 = Containers ["La311Containers"]
            for Containers in lcontainers311:
                k_container_size_10= Containers['ContainerSize']
                k_container_type_10= Containers['ContainerType']
                k_damage_lid_10 = Containers['DamageonLid']
                k_damage_axle_10 = Containers['DamageonAxle']
                k_damage_on_body_10 = Containers['DamageonBody']
                k_damage_on_handle_10 = Containers['DamageonHandleEndcap']
                k_damage_on_wheels_10 = Containers ['DamageonWheels']
                k_container_number_10= Containers['ContainerNumber']
                k_container_name_10 = Containers['Name']
                # print k_container_number_1
                if Containers==lcontainers311[9]:
                    k_container_number_10 = k_container_number_10
                    k_damage_on_wheels_10 = k_damage_on_wheels_10
                    k_damage_on_handle_10 = k_damage_on_handle_10
                    k_damage_on_body_10 = k_damage_on_body_10
                    k_damage_axle_10 = k_damage_axle_10
                    k_damage_lid_10 = k_damage_lid_10
                    k_container_type_10 =k_container_type_10
                    k_container_size_10 = k_container_size_10
                    k_container_name_10=k_container_name_10
    except:
        print "No Container Information"


    if("La311Containers" in Containers):
            lcontainers311
    if  '90' in  k_container_size_1:
            k_container_size_1='90'
    elif '60' in k_container_size_1:
            k_container_size_1 = '60'
    elif '30' in k_container_size_1:
            k_container_size_1 = '30'

    if("La311Containers" in Containers):
            lcontainers311
    if  '90' in  k_container_size_2:
            k_container_size_2='90'
    elif '60' in k_container_size_2:
            k_container_size_2 = '60'
    elif '30' in k_container_size_2:
            k_container_size_2 = '30'

    if("La311Containers" in Containers):
            lcontainers311
    if  '90' in  k_container_size_3:
            k_container_size_3='90'
    elif '60' in k_container_size_3:
            k_container_size_3 = '60'
    elif '30' in k_container_size_3:
            k_container_size_3 = '30'

    if("La311Containers" in Containers):
            lcontainers311
    if  '90' in  k_container_size_4:
            k_container_size_4='90'
    elif '60' in k_container_size_4:
            k_container_size_4 = '60'
    elif '30' in k_container_size_4:
            k_container_size_4 = '30'

    if("La311Containers" in Containers):
            lcontainers311
    if  '90' in  k_container_size_5:
            k_container_size_5='90'
    elif '60' in k_container_size_5:
            k_container_size_5 = '60'
    elif '30' in k_container_size_5:
            k_container_size_5 = '30'

    if("La311Containers" in Containers):
            lcontainers311
    if  '90' in  k_container_size_5:
            k_container_size_6='90'
    elif '60' in k_container_size_5:
            k_container_size_6 = '60'
    elif '30' in k_container_size_5:
            k_container_size_6 = '30'

    if("La311Containers" in Containers):
            lcontainers311
    if  '90' in  k_container_size_5:
            k_container_size_7='90'
    elif '60' in k_container_size_5:
            k_container_size_7= '60'
    elif '30' in k_container_size_5:
            k_container_size_7= '30'

    if("La311Containers" in Containers):
            lcontainers311
    if  '90' in  k_container_size_5:
            k_container_size_8='90'
    elif '60' in k_container_size_5:
            k_container_size_8= '60'
    elif '30' in k_container_size_5:
            k_container_size_8= '30'

    if("La311Containers" in Containers):
            lcontainers311
    if  '90' in  k_container_size_5:
            k_container_size_9='90'
    elif '60' in k_container_size_5:
            k_container_size_9= '60'
    elif '30' in k_container_size_5:
            k_container_size_9= '30'

    if("La311Containers" in Containers):
            lcontainers311
    if  '90' in  k_container_size_5:
            k_container_size_10='90'
    elif '60' in k_container_size_5:
            k_container_size_10= '60'
    elif '30' in k_container_size_5:
            k_container_size_10= '30'

    if 'Blue Recycling' in k_container_type_1:
        k_container_type_1 = 'BLU'
    elif 'Black Refuse' in k_container_type_1:
        k_container_type_1 = 'BLK'
    elif 'Green Yard Trimmings' in k_container_type_1:
        k_container_type_1 = 'GRN'
    elif 'Brown Horse Manure' in k_container_type_1:
        k_container_type_1 = 'HMU'

    if 'Blue Recycling' in k_container_type_2:
        k_container_type_2 = 'BLU'
    elif 'Black Refuse' in k_container_type_2:
        k_container_type_2 = 'BLK'
    elif 'Green Yard Trimmings' in k_container_type_2:
        k_container_type_2 = 'GRN'
    elif 'Brown Horse Manure' in k_container_type_2:
        k_container_type_2 = 'HMU'

    if 'Blue Recycling' in k_container_type_3:
        k_container_type_3 = 'BLU'
    elif 'Black Refuse' in k_container_type_3:
        k_container_type_3 = 'BLK'
    elif 'Green Yard Trimmings' in k_container_type_3:
        k_container_type_3 = 'GRN'
    elif 'Brown Horse Manure' in k_container_type_3:
        k_container_type_3 = 'HMU'

    if 'Blue Recycling' in k_container_type_4:
        k_container_type_4 = 'BLU'
    elif 'Black Refuse' in k_container_type_4:
        k_container_type_4 = 'BLK'
    elif 'Green Yard Trimmings' in k_container_type_4:
        k_container_type_4 = 'GRN'
    elif 'Brown Horse Manure' in k_container_type_4:
        k_container_type_4 = 'HMU'

    if 'Blue Recycling' in k_container_type_5:
        k_container_type_5 = 'BLU'
    elif 'Black Refuse' in k_container_type_5:
        k_container_type_5 = 'BLK'
    elif 'Green Yard Trimmings' in k_container_type_5:
        k_container_type_5 = 'GRN'
    elif 'Brown Horse Manure' in k_container_type_5:
        k_container_type_5 = 'HMU'

    if 'Blue Recycling' in k_container_type_6:
        k_container_type_6 = 'BLU'
    elif 'Black Refuse' in k_container_type_6:
        k_container_type_6 = 'BLK'
    elif 'Green Yard Trimmings' in k_container_type_6:
        k_container_type_6 = 'GRN'
    elif 'Brown Horse Manure' in k_container_type_6:
        k_container_type_6 = 'HMU'

    if 'Blue Recycling' in k_container_type_7:
        k_container_type_7 = 'BLU'
    elif 'Black Refuse' in k_container_type_7:
        k_container_type_7 = 'BLK'
    elif 'Green Yard Trimmings' in k_container_type_7:
        k_container_type_7 = 'GRN'
    elif 'Brown Horse Manure' in k_container_type_7:
        k_container_type_7 = 'HMU'

    if 'Blue Recycling' in k_container_type_8:
        k_container_type_8 = 'BLU'
    elif 'Black Refuse' in k_container_type_8:
        k_container_type_8 = 'BLK'
    elif 'Green Yard Trimmings' in k_container_type_8:
        k_container_type_8 = 'GRN'
    elif 'Brown Horse Manure' in k_container_type_8:
        k_container_type_8 = 'HMU'

    if 'Blue Recycling' in k_container_type_9:
        k_container_type_9 = 'BLU'
    elif 'Black Refuse' in k_container_type_9:
        k_container_type_9 = 'BLK'
    elif 'Green Yard Trimmings' in k_container_type_9:
        k_container_type_9 = 'GRN'
    elif 'Brown Horse Manure' in k_container_type_9:
        k_container_type_9 = 'HMU'

    if 'Blue Recycling' in k_container_type_10:
        k_container_type_10 = 'BLU'
    elif 'Black Refuse' in k_container_type_10:
        k_container_type_10 = 'BLK'
    elif 'Green Yard Trimmings' in k_container_type_10:
        k_container_type_10 = 'GRN'
    elif 'Brown Horse Manure' in k_container_type_10:
        k_container_type_10 = 'HMU'

    if k_damage_lid_1 == 'Y' and k_container_type_1 == 'BLU':
        k_damage_lid_1 = 'LDR'
    elif k_damage_lid_1 == 'Y' and k_container_type_1 == 'BLK':
        k_damage_lid_1 = 'LDB'
    elif k_damage_lid_1 == 'Y' and k_container_type_1 == 'GRN':
        k_damage_lid_1 = 'LDG'

    if k_damage_lid_2 == 'Y' and k_container_type_2 == 'BLU':
        k_damage_lid_2 = 'LDR'
    elif k_damage_lid_2 == 'Y' and k_container_type_2 == 'BLK':
        k_damage_lid_2 = 'LDB'
    elif k_damage_lid_2 == 'Y' and k_container_type_2 == 'GRN':
        k_damage_lid_2 = 'LDG'

    if k_damage_lid_3 == 'Y' and k_container_type_3 == 'BLU':
        k_damage_lid_3 = 'LDR'
    elif k_damage_lid_3 == 'Y' and k_container_type_3 == 'BLK':
        k_damage_lid_3 = 'LDB'
    elif k_damage_lid_3 == 'Y' and k_container_type_3 == 'GRN':
        k_damage_lid_3 = 'LDG'

    if k_damage_lid_4 == 'Y' and k_container_type_4 == 'BLU':
        k_damage_lid_4 = 'LDR'
    elif k_damage_lid_4 == 'Y' and k_container_type_4 == 'BLK':
        k_damage_lid_4 = 'LDB'
    elif k_damage_lid_4 == 'Y' and k_container_type_4 == 'GRN':
        k_damage_lid_4 = 'LDG'

    if k_damage_lid_5 == 'Y' and k_container_type_5 == 'BLU':
        k_damage_lid_5 = 'LDR'
    elif k_damage_lid_5 == 'Y' and k_container_type_5 == 'BLK':
        k_damage_lid_5 = 'LDB'
    elif k_damage_lid_5 == 'Y' and k_container_type_5 == 'GRN':
        k_damage_lid_5 = 'LDG'


    if k_damage_lid_6 == 'Y' and k_container_type_6 == 'BLU':
        k_damage_lid_6 = 'LDR'
    elif k_damage_lid_6 == 'Y' and k_container_type_6 == 'BLK':
        k_damage_lid_6 = 'LDB'
    elif k_damage_lid_6 == 'Y' and k_container_type_6 == 'GRN':
        k_damage_lid_6 = 'LDG'

    if k_damage_lid_7 == 'Y' and k_container_type_7 == 'BLU':
        k_damage_lid_7 = 'LDR'
    elif k_damage_lid_7 == 'Y' and k_container_type_7 == 'BLK':
        k_damage_lid_7 = 'LDB'
    elif k_damage_lid_7 == 'Y' and k_container_type_7 == 'GRN':
        k_damage_lid_7 = 'LDG'

    if k_damage_lid_8 == 'Y' and k_container_type_8 == 'BLU':
        k_damage_lid_8 = 'LDR'
    elif k_damage_lid_8 == 'Y' and k_container_type_8 == 'BLK':
        k_damage_lid_8 = 'LDB'
    elif k_damage_lid_8 == 'Y' and k_container_type_8 == 'GRN':
        k_damage_lid_8 = 'LDG'

    if k_damage_lid_9 == 'Y' and k_container_type_9 == 'BLU':
        k_damage_lid_9 = 'LDR'
    elif k_damage_lid_9 == 'Y' and k_container_type_9 == 'BLK':
        k_damage_lid_9 = 'LDB'
    elif k_damage_lid_9 == 'Y' and k_container_type_9 == 'GRN':
        k_damage_lid_9 = 'LDG'

    if k_damage_lid_10 == 'Y' and k_container_type_10 == 'BLU':
        k_damage_lid_10 = 'LDR'
    elif k_damage_lid_10 == 'Y' and k_container_type_10 == 'BLK':
        k_damage_lid_10 = 'LDB'
    elif k_damage_lid_10 == 'Y' and k_container_type_10 == 'GRN':
        k_damage_lid_10 = 'LDG'


    if k_damage_on_body_1 == 'Y':
        k_damage_on_body_1 = 'BFT'

    if k_damage_on_body_2 == 'Y':
        k_damage_on_body_2 = 'BFT'


    if k_damage_on_body_3 == 'Y':
        k_damage_on_body_3 = 'BFT'


    if k_damage_on_body_4 == 'Y':
        k_damage_on_body_4 = 'BFT'


    if k_damage_on_body_5 == 'Y':
        k_damage_on_body_5 = 'BFT'


    if k_damage_on_body_6 == 'Y':
        k_damage_on_body_6 = 'BFT'


    if k_damage_on_body_7 == 'Y':
        k_damage_on_body_7 = 'BFT'


    if k_damage_on_body_8 == 'Y':
        k_damage_on_body_8 = 'BFT'


    if k_damage_on_body_9 == 'Y':
        k_damage_on_body_9 = 'BFT'


    if k_damage_on_body_10 == 'Y':
        k_damage_on_body_10 = 'BFT'



    if k_damage_on_handle_1 == 'Y':
        k_damage_on_handle_1   = 'HAN'


    if k_damage_on_handle_2 == 'Y':
            k_damage_on_handle_2   = 'HAN'



    if k_damage_on_handle_3 == 'Y':
            k_damage_on_handle_3   = 'HAN'


    if k_damage_on_handle_4 == 'Y':
            k_damage_on_handle_4   = 'HAN'


    if k_damage_on_handle_5 == 'Y':
                k_damage_on_handle_5   = 'HAN'


    if k_damage_on_handle_6 == 'Y':
                     k_damage_on_handle_6   = 'HAN'


    if k_damage_on_handle_7 == 'Y':
                k_damage_on_handle_7   = 'HAN'


    if k_damage_on_handle_8 == 'Y':
                k_damage_on_handle_8   = 'HAN'


    if k_damage_on_handle_9 == 'Y':
            k_damage_on_handle_9   = 'HAN'


    if k_damage_on_handle_10 == 'Y':
        k_damage_on_handle_10   = 'HAN'

    if k_damage_on_wheels_1 == 'Y':
            k_damage_on_wheels_1 = 'WHL'

    if k_damage_on_wheels_2 == 'Y':
            k_damage_on_wheels_2 = 'WHL'


    if k_damage_on_wheels_3 == 'Y':
            k_damage_on_wheels_3 = 'WHL'


    if k_damage_on_wheels_4 == 'Y':
            k_damage_on_wheels_4 = 'WHL'


    if k_damage_on_wheels_5 == 'Y':
            k_damage_on_wheels_5 = 'WHL'


    if k_damage_on_wheels_6 == 'Y':
            k_damage_on_wheels_6 = 'WHL'


    if k_damage_on_wheels_7 == 'Y':
            k_damage_on_wheels_7 = 'WHL'


    if k_damage_on_wheels_8 == 'Y':
            k_damage_on_wheels_8 = 'WHL'

    if k_damage_on_wheels_9 == 'Y':
            k_damage_on_wheels_9 = 'WHL'


    if k_damage_on_wheels_10 == 'Y':
            k_damage_on_wheels_10 = 'WHL'









#
#                 if k_container_reason == 'Abandoned':
#                     k_container_reason = 'DAM'
#                 #
#                 # elif k_container_reason == 'Abandoned':
#                 #     k_container_reason = 'ABD'
#                 if k_container_request_for  == ' Damage':
#                     k_container_request_for = 'DAM'
#
#                 #request for = service type
#
#                 print k_container_type
#                 print k_container_size
#                 print k_damage_on_handle
#                 print k_damage_on_body
#
#     except:
#         print "No Container Info"
#
#

    Container_FullName = Container_FirstName + " " + Container_LastName +  "Placeholder String"


    date_object = ' '
    created_object = ' '
    try:
        date_object = datetime.datetime.strptime(ServiceDate, "%m/%d/%Y %H:%M:%S")
        created_object = datetime.datetime.strptime(Container_CreatedDate, "%m/%d/%Y %H:%M:%S")

    except Exception:
        pass


    Containerdt = np.dtype([('Address', 'U128'),
                                ('Y_CoordShape', '<f8'),
                                ('X_CoordShape', '<f8'),
                                ('Y_COR', '<f8'),
                                ('X_COR', '<f8'),
                                ('ReasonCode','U128'),
                                ('NUMBERCYLA', 'U128'),
                                ('SRNumber', 'U128'),
                                ('Name', 'U128'),
                                ('RESOLUTION_CODE','U128'),
                               ('HOME_PHONE', 'U40'),
                                ('CreatedDate', 'U128'),
                                ('UpdatedDate', 'U128'),
                                ('ItemDesc', 'U128'),
                                ('SCHED_DATE', 'U128'),
                                ('CYLA_DISTRICT ', 'U128'),
		                                ('SR_Cont_Color01','U128'),
		                                ('SR_Cont_Color02','U128'),
		                                ('SR_Cont_Color03','U128'),
		                                ('SR_Cont_Color04','U128'),
		                                ('SR_Cont_Color05','U128'),
		                                ('SR_Cont_Color06','U128'),
		                                ('SR_Cont_Color07','U128'),
		                                ('SR_Cont_Color08','U128'),
		                                ('SR_Cont_Color09','U128'),
		                                ('SR_Cont_Color10','U128'),
		                                ('SR_Cont_Size01','U128'),
		                                ('SO_Cont_Size02','U128'),
		                                ('SO_Cont_Size03','U128'),
		                                ('SO_Cont_Size04','U128'),
		                                ('SO_Cont_Size05','U128'),
		                                ('SO_Cont_Size06','U128'),
		                                ('SO_Cont_Size07','U128'),
		                                ('SO_Cont_Size08','U128'),
		                                ('SO_Cont_Size09','U128'),
		                                ('SO_Cont_Size10','U128'),
		                                ('Dist01','U128'),
		                                ('Dist02','U128'),
		                                ('Dist03','U128'),
		                                ('Dist04','U128'),
		                                ('Dist05','U128'),
		                                ('Dist06','U128'),
		                                ('Dist07','U128'),
		                                ('Dist08','U128'),
		                                ('Dist09','U128'),
		                                ('Dist10','U128'),
		                                ('Dam01','U128'),
		                                ('Dam02','U128'),
		                                ('Dam03','U128'),
		                                ('Dam04','U128'),
		                                ('Dam05','U128'),
		                                ('Dam06','U128'),
		                                ('Dam07','U128'),
		                                ('Dam08','U128'),
		                                ('Dam09','U128'),
		                                ('Dam10','U128'),
		                                ('SN01','U128'),
		                                ('SN02','U128'),
		                                ('SN03','U128'),
		                                ('SN04','U128'),
		                                ('SN05','U128'),
		                                ('SN06','U128'),
		                                ('SN07','U128'),
		                                ('SN08','U128'),
		                                ('SN09','U128'),
		                                ('SN10','U128'),
		                                ('Reas01','U128'),
		                                ('Reas02','U128'),
		                                ('Reas03','U128'),
		                                ('Reas04','U128'),
		                                ('Reas05','U128'),
		                                ('Reas06','U128'),
		                                ('Reas07','U128'),
		                                ('Reas08','U128'),
		                                ('Reas09','U128'),
		                                ('Reas10','U128'),
		                                ('SCCatDesc', 'U128'),


                                ])

    if k_container_type_1 == 'GRN':
           containerItems.append((ContainerAddress,
                 container_x,
                 container_y,
                  container_x,
                  container_y,
                  Container_ReasonCode,
                  Container_SRNumber,
                  Container_SRNumber,
                 Container_FullName,
                  Container_ResolutionCode,
                  Container_HomePhone,
                  Container_CreatedDate,
                  Container_UpdatedDate,
                "ItemDesc",
                date_object,
                "CS",
                k_container_type_1,
                k_container_type_2,
                k_container_type_1,
                k_container_type_1,
                k_container_type_1,
                k_container_type_1,
                k_container_type_1,
                k_container_type_1,
                k_container_type_1,
                k_container_type_1,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                k_damage_on_wheels,
                k_damage_on_wheels,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                Container_GISLayer,





        ))



    elif k_container_type_2 == 'GRN':
           containerItems.append((ContainerAddress,
                 container_x,
                 container_y,
                  container_x,
                  container_y,
                  Container_ReasonCode,
                  Container_SRNumber,
                  Container_SRNumber,
                 Container_FullName,
                  Container_ResolutionCode,
                  Container_HomePhone,
                  Container_CreatedDate,
                  Container_UpdatedDate,
                # "ItemDesc",
                date_object,
                "CS",
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                k_damage_on_wheels,
                k_damage_on_wheels,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                Container_GISLayer,

        ))




    elif k_container_type == 'BLU':
           containerItems.append((ContainerAddress,
                 container_x,
                 container_y,
                  container_x,
                  container_y,
                  Container_ReasonCode,
                  Container_SRNumber,
                  Container_SRNumber,
                 Container_FullName,
                  Container_ResolutionCode,
                  Container_HomePhone,
                  Container_CreatedDate,
                  Container_UpdatedDate,
                # "ItemDesc",
                date_object,
                "CS",
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_type,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                k_container_size,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_container_request_for,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                    k_damage_on_wheels,
                k_damage_on_wheels,
                k_damage_on_wheels,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_number,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                k_container_reason,
                Container_GISLayer,

        ))

arr = np.array(containerItems ,dtype=Containerdt)


NumPyArray = arcpy.da.NumPyArrayToFeatureClass(arr, aContainerFC, ['Y_CoordShape', 'X_CoordShape'], spatial_ref)


