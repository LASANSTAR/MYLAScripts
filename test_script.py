__author__ = 'Administrator'

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
import threading
from apscheduler.scheduler import Scheduler
import logging
logging.basicConfig()
import schedule




def lasanbulkyquery():
    start = time.time()
    Start = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    msgFolder = "C:/logs/"
    sender = "geoffreywestgis@gmail.com"
    recipient = "geoffreywestgis@gmail.com"
    fc2 = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311"
    fc = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311Test_bulkyitems"
    fcCopy = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest"
    appendClass = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_SCData_sa.sde\SCData.DBO.SO_SC_1"
    aTable = "C:\Users\GeoffreyWest\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\ServiceRequest.sde\ServiceRequest.DBO.History_Table_"
    aContainerFC = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.aContainerFC21"
    connect_timeout = 5
    gdb = "C:\MYLATesting.gdb"
    f2 =open('C:\Users\GeoffreyWest\Desktop\Requestjson.json')
    history_table = 'C:\MYLATesting.gdb\MYLA311Test_Env'
    # ljson = 'C:\Users\GeoffreyWest\Desktop\json.json'
    k_comment = ' '
    data2 = jsonpickle.decode((f2.read()))
    Start = datetime.datetime.now()
    DD = datetime.timedelta(minutes=300)
    earlier = Start - DD
    earlier_str = earlier.strftime('X%m/%d/%Y %H:%M:%S').replace('X0','X').replace('X','')
    data2["QueryRequest"]['LastUpdatedDate'] = str(earlier_str)
    data2 = jsonpickle.encode(data2)
    BulkyItemInfo = " "
    spatial_ref = arcpy.SpatialReference(4326)
    lastpage = 'false'
    startrow = 0
    newquery = 'new'
    pagesize = 100

    url2 = "https://myla311.lacity.org/myla311router/mylasrbe/1/SANQueryPageSR"


    headers2 = {'Content-type': 'text/plain', 'Accept': '/'}


    if arcpy.Exists(fc):
        arcpy.Delete_management(fc)


    while lastpage == 'false':
        r2 = requests.post(url2, data=data2, headers=headers2)
        # print r2.text
        decoded2 = r2.json()
        f2 =open('C:\Users\GeoffreyWest\Desktop\Requestjson.json')
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

        # print json.dumps(decoded2, sort_keys=True, indent=4)


    try:
        items = []
        for sr in decoded2['Response']['ListOfServiceRequest']['ServiceRequest']:
            Address = sr['SRAddress']
            if sr['Latitude'] != '':
                y = sr['Latitude']
            if sr['Longitude'] != '':
                x = sr['Longitude']
            if sr['Latitude'] == '':
                blanky = sr['Latitude']
            if sr['Longitude'] == '':
                blankx= sr['Longitude']
            ReasonCode = ''
            ResolutionCode = ''
            SRNumber = sr['SRNumber']
            NewContactFirstName = sr['NewContactFirstName']
            NewContactLastName = sr['NewContactLastName']
            Created_FirstName = sr['LA311UpdatedByFirstName']
            Created_LastName = sr ['LA311UpdatedByLastName']
            FirstName = sr['FirstName']
            LastName = sr['LastName']
            if sr['ResolutionCode'] == '':
                ResolutionCode =  sr['ResolutionCode']
            if sr ['ReasonCode'] == '':
                ReasonCode = sr['ReasonCode']
            aReasonCode = sr['ReasonCode']
            HomePhone = sr['HomePhone']
            CreatedDate = sr['CreatedDate']
            UpdatedDate = sr['UpdatedDate']
            BulkyItem = sr['ListOfLa311BulkyItem']
            ElectronicWaste = sr['ListOfLa311ElectronicWaste']
            MoveInMoveOut = sr['ListOfLa311MoveInMoveOut']
            IllegalDumping = sr['ListOfLa311IllegalDumpingPickup']
            BrushItems = sr['ListOfLa311BrushItemsPickup']
            MHA = sr['ListOfLa311MetalHouseholdAppliancesPickup']
            DAR = sr['ListOfLa311DeadAnimalRemoval']
            Manual = sr['ListOfLa311ManualPickup']
            if sr['ServiceDate'] !=  ' ':
                ServiceDate=  sr['ServiceDate']
            try:
                if sr['ListOfLa311GisLayer'] != '{},':
                    GISLayer = sr['ListOfLa311GisLayer']['La311GisLayer'][0]['DistrictName']
            except Exception:
                pass
            NeighborhHoodCouncil = sr['SRNeighborhoodCouncilName']
            ServiceNotes = sr['ListOfLa311ServiceRequestNotes']
            SCCatDesc = ' '
            UpdatedDate = datetime.datetime.strptime(UpdatedDate, "%m/%d/%Y %H:%M:%S")


            if arcpy.Exists(fc):
                    arcpy.Delete_management(fc)

            if 'La311ServiceRequestNotes' in ServiceNotes:
                try:
                    k_comment = ServiceNotes['La311ServiceRequestNotes'][0]['Comment']
                except IndexError:
                    k_comment = ' '
                print k_comment

            if 'BulkyItem' in BulkyItem:
                try:
                    k_bulky_count_1 = BulkyItem['BulkyItem'][0]['BulkyItemCount']
                except IndexError:
                    k_bulky_count_1 = ' '
                print k_bulky_count_1

                try:
                    k_bulky_count_2 = BulkyItem['BulkyItem'][1]['BulkyItemCount']
                except IndexError:
                    k_bulky_count_2 = ' '
                print k_bulky_count_2

                try:
                    k_bulky_count_3 = BulkyItem['BulkyItem'][2]['BulkyItemCount']
                except IndexError:
                    k_bulky_count_3 = ' '
                print k_bulky_count_3

                try:
                    k_bulky_count_4 = BulkyItem['BulkyItem'][3]['BulkyItemCount']
                except IndexError:
                    k_bulky_count_4 = ' '
                print k_bulky_count_4

                try:
                    k_bulky_count_5 = BulkyItem['BulkyItem'][4]['BulkyItemCount']
                except IndexError:
                    k_bulky_count_5 = ' '
                print k_bulky_count_5

                try:
                    k_bulky_count_6 = BulkyItem['BulkyItem'][5]['BulkyItemCount']
                except IndexError:
                    k_bulky_count_6 = ' '
                print k_bulky_count_6

                try:
                    k_bulky_count_7 = BulkyItem['BulkyItem'][6]['BulkyItemCount']
                except IndexError:
                    k_bulky_count_7 = ' '
                print k_bulky_count_7

                try:
                    k_bulky_count_8 = BulkyItem['BulkyItem'][7]['BulkyItemCount']
                except IndexError:
                    k_bulky_count_8 = ' '
                print k_bulky_count_8

                try:
                    k_bulky_count_9 = BulkyItem['BulkyItem'][8]['BulkyItemCount']
                except IndexError:
                    k_bulky_count_9 = ' '
                print k_bulky_count_9

                try:
                    k_bulky_count_10 = BulkyItem['BulkyItem'][9]['BulkyItemCount']
                except IndexError:
                    k_bulky_count_10 = ' '
                print k_bulky_count_10

                try:
                    k_bulky_item_1 = BulkyItem['BulkyItem'][0]['BulkyItemType']
                except IndexError:
                    k_bulky_item_1 = ' '
                print k_bulky_item_1


                try:
                    k_bulky_item_2 = BulkyItem['BulkyItem'][1]['BulkyItemType']
                except IndexError:
                    k_bulky_item_2 = ' '
                print k_bulky_item_2


                try:
                    k_bulky_item_3 = BulkyItem['BulkyItem'][2]['BulkyItemType']
                except IndexError:
                    k_bulky_item_3 = ' '
                print k_bulky_item_3


                try:
                    k_bulky_item_4 = BulkyItem['BulkyItem'][3]['BulkyItemType']
                except IndexError:
                    k_bulky_item_4 = ' '
                print k_bulky_item_4


                try:
                    k_bulky_item_5 = BulkyItem['BulkyItem'][4]['BulkyItemType']
                except IndexError:
                    k_bulky_item_5 = ' '
                print k_bulky_item_5



                try:
                    k_bulky_item_6 = BulkyItem['BulkyItem'][5]['BulkyItemType']
                except IndexError:
                    k_bulky_item_6 = ' '
                print k_bulky_item_6


                try:
                    k_bulky_item_7 = BulkyItem['BulkyItem'][6]['BulkyItemType']
                except IndexError:
                    k_bulky_item_7 = ' '
                print k_bulky_item_7



                try:
                    k_bulky_item_8 = BulkyItem['BulkyItem'][7]['BulkyItemType']
                except IndexError:
                    k_bulky_item_8 = ' '
                print k_bulky_item_8



                try:
                    k_bulky_item_9 = BulkyItem['BulkyItem'][8]['BulkyItemType']
                except IndexError:
                    k_bulky_item_9 = ' '
                print k_bulky_item_9


                try:
                    k_bulky_item_10 = BulkyItem['BulkyItem'][9]['BulkyItemType']
                except IndexError:
                    k_bulky_item_10 = ' '
                print k_bulky_item_10


                try:
                    k_bulky_location_1 = BulkyItem['BulkyItem'][0]['CollectionLocation']
                except IndexError:
                    k_bulky_location_1 = ' '
                print k_bulky_location_1


                try:
                    k_bulky_location_2 = BulkyItem['BulkyItem'][1]['CollectionLocation']
                except IndexError:
                    k_bulky_location_2 = ' '
                print k_bulky_location_2

                try:
                    k_bulky_location_3 = BulkyItem['BulkyItem'][2]['CollectionLocation']
                except IndexError:
                    k_bulky_location_3 = ' '
                print k_bulky_location_3

                try:
                    k_bulky_location_4 = BulkyItem['BulkyItem'][3]['CollectionLocation']
                except IndexError:
                    k_bulky_location_4 = ' '
                print k_bulky_location_4

                try:
                    k_bulky_location_5 = BulkyItem['BulkyItem'][4]['CollectionLocation']
                except IndexError:
                    k_bulky_location_5 = ' '
                print k_bulky_location_5


                try:
                    k_bulky_location_6 = BulkyItem['BulkyItem'][5]['CollectionLocation']
                except IndexError:
                    k_bulky_location_6 = ' '
                print k_bulky_location_6



                try:
                    k_bulky_location_7 = BulkyItem['BulkyItem'][6]['CollectionLocation']
                except IndexError:
                    k_bulky_location_7 = ' '
                print k_bulky_location_7



                try:
                    k_bulky_location_8 = BulkyItem['BulkyItem'][7]['CollectionLocation']
                except IndexError:
                    k_bulky_location_8 = ' '
                print k_bulky_location_8

                try:
                    k_bulky_location_9 = BulkyItem['BulkyItem'][8]['CollectionLocation']
                except IndexError:
                    k_bulky_location_9 = ' '
                print k_bulky_location_9


                try:
                    k_bulky_location_10 = BulkyItem['BulkyItem'][9]['CollectionLocation']
                except IndexError:
                    k_bulky_location_10 = ' '
                print k_bulky_location_10


                try:
                    k_bulky_name_1 = BulkyItem['BulkyItem'][0]['Name']
                except IndexError:
                    k_bulky_name_1 = ' '
                print k_bulky_name_1

                try:
                    k_bulky_name_2 = BulkyItem['BulkyItem'][1]['Name']
                except IndexError:
                    k_bulky_name_2 = ' '
                print k_bulky_name_2



                try:
                    k_bulky_name_3 = BulkyItem['BulkyItem'][2]['Name']
                except IndexError:
                    k_bulky_name_3 = ' '
                print k_bulky_name_3


                try:
                    k_bulky_name_4 = BulkyItem['BulkyItem'][3]['Name']
                except IndexError:
                    k_bulky_name_4 = ' '
                print k_bulky_name_4

                try:
                    k_bulky_name_5 = BulkyItem['BulkyItem'][4]['Name']
                except IndexError:
                    k_bulky_name_5 = ' '
                print k_bulky_name_5

                try:
                    k_bulky_name_6 = BulkyItem['BulkyItem'][5]['Name']
                except IndexError:
                    k_bulky_name_6 = ' '
                print k_bulky_name_6


                try:
                    k_bulky_name_7 = BulkyItem['BulkyItem'][6]['Name']
                except IndexError:
                    k_bulky_name_7 = ' '
                print k_bulky_name_7



                try:
                    k_bulky_name_8 = BulkyItem['BulkyItem'][7]['Name']
                except IndexError:
                    k_bulky_name_8 = ' '
                print k_bulky_name_8



                try:
                    k_bulky_name_9 = BulkyItem['BulkyItem'][8]['Name']
                except IndexError:
                    k_bulky_name_9 = ' '
                print k_bulky_name_9


                try:
                    k_bulky_name_10 = BulkyItem['BulkyItem'][9]['Name']
                except IndexError:
                    k_bulky_name_10 = ' '
                print k_bulky_name_10


                if BulkyItem['BulkyItem'][0]['Type'] == 'Bulky Items':
                    k_bulky_comm_1 = 1


                date_object = ' '
                created_object = ' '

                try:
                    date_object = datetime.datetime.strptime(ServiceDate, "%m/%d/%Y %H:%M:%S")
                    created_object = datetime.datetime.strptime(CreatedDate, "%m/%d/%Y %H:%M:%S")
                except Exception:
                    pass

                    FullName = NewContactFirstName  +  " " + NewContactLastName
                    if FullName  == ' ':
                        FullName = 'Not Specified'

                    if created_object == ' ':
                        created_object = UpdatedDate


                    if date_object == ' ':
                        date_object = '07/01/2015'

                    CreatedBy = Created_FirstName + " " + Created_LastName
                    Prior_Resolution_Code =  ' '

                    dt = np.dtype([('Address', 'U40'),
                        ('Y_CoordShape', '<f8'),
                        ('X_CoordShape', '<f8'),
                        ('Y_COR', '<f8'),
                        ('X_COR', '<f8'),
                        ('ReasonCode','U128'),
                        ('NUMBERCYLA', 'U40'),
                        ('SRNumber', 'U40'),
                        ('Name', 'U40'),
                        ('RESOLUTION_CODE','U128'),
                       ('HOME_PHONE', 'U40'),
                        ('OPEN_TIME', 'U128'),
                        ('OPENED_BY', 'U128'),
                        ('UpdatedDate', 'U128'),
                        ('ItemDesc_1', 'U128'),
                        ('ItemDesc_2', 'U128'),
                        ('ItemDesc_3', 'U128'),
                        ('ItemDesc_4','U128'),
                        ('ItemDesc_5', 'U128'),
                        ('ItemDesc_6', 'U128'),
                        ('ItemDesc_7', 'U128'),
                        ('ItemDesc_8', 'U128'),
                        ('ItemDesc_9', 'U128'),
                        ('ItemDesc_10', 'U128'),
                        ('Category', 'U128'),
                         ('SCHED_DATE', 'U128'),
                        ('CYLA_DISTRICT ', 'U128'),
                    ('BRIEF_DESCRIPTION', 'U128'),
                        ('Comment', 'U128'),
                        ('Prior_RESOLUTION_CODE', 'U128'),
                        ('UID1', 'U128'),
                        ('UID2', 'U128'),
                        ('UID3', 'U128'),
                        ('UID4', 'U128'),
                        ('UID5', 'U128'),
                        ('UID6', 'U128'),
                        ('UID7', 'U128'),
                        ('UID8', 'U128'),
                        ('UID9', 'U128'),
                        ('UID10', 'U128'),
                        ('ItemLoc_1', 'U128'),
                        ('ItemLoc_2', 'U128'),
                        ('ItemLoc_3', 'U128'),
                        ('ItemLoc_4', 'U128'),
                        ('ItemLoc_5', 'U128'),
                        ('ItemLoc_6', 'U128'),
                        ('ItemLoc_7', 'U128'),
                        ('ItemLoc_8', 'U128'),
                        ('ItemLoc_9', 'U128'),
                        ('ItemLoc_10', 'U128'),



                    ])

                    if k_bulky_comm_1 == 1:
                        items.append((Address,
                         x,
                        y,
                          x,
                          y,
                          ReasonCode,
                          SRNumber,
                         SRNumber,
                         FullName,
                          ResolutionCode,
                          HomePhone,
                          created_object,
                         CreatedBy,
                          UpdatedDate,
                         k_bulky_count_1 + ',' + k_bulky_item_1,
                         k_bulky_count_2 + ',' + k_bulky_item_2,
                         k_bulky_count_3 + ',' + k_bulky_item_3,
                         k_bulky_count_4 + ',' + k_bulky_item_4,
                         k_bulky_count_5 + ',' + k_bulky_item_5,
                         k_bulky_count_6 + ',' + k_bulky_item_6,
                         k_bulky_count_7 + ',' + k_bulky_item_7,
                         k_bulky_count_8 + ',' + k_bulky_item_8,
                         k_bulky_count_9 + ',' + k_bulky_item_9,
                         k_bulky_count_10 + ',' + k_bulky_item_10,
                         k_bulky_comm_1,
                          date_object,
                         GISLayer,
                         k_bulky_location_1 +  k_bulky_count_1 + ',' + k_bulky_item_1 + ';' + k_bulky_count_2 + ',' + k_bulky_item_2 + ';' + k_bulky_count_3 + ',' + k_bulky_item_3 + ';' + k_bulky_count_4 + ',' + k_bulky_item_4 + ';' + k_bulky_count_5 + ',' + k_bulky_item_5 + ';' + k_bulky_count_6+ ',' + k_bulky_item_6 + ';' + k_bulky_count_7 + ',' + k_bulky_item_7 + ';' + k_bulky_count_8 + ',' + k_bulky_item_8 + ';' + k_bulky_count_9 + ',' + k_bulky_item_9 + ';' + k_bulky_count_10 + ',' + k_bulky_item_10,
                         k_comment,
                        Prior_Resolution_Code,
                        k_bulky_name_1,
                        k_bulky_name_2,
                        k_bulky_name_3,
                        k_bulky_name_4,
                        k_bulky_name_5,
                        k_bulky_name_6,
                        k_bulky_name_7,
                        k_bulky_name_8,
                        k_bulky_name_9,
                        k_bulky_name_10,
                        k_bulky_location_1,
                        k_bulky_location_2,
                        k_bulky_location_3,
                        k_bulky_location_4,
                        k_bulky_location_5,
                        k_bulky_location_6,
                        k_bulky_location_7,
                        k_bulky_location_8,
                        k_bulky_location_9,
                        k_bulky_location_10,

                        ))


        arr = np.array(items,dtype=dt)

        NumPyArray = arcpy.da.NumPyArrayToFeatureClass(arr, fc, ['Y_CoordShape', 'X_CoordShape'], spatial_ref)

        arcpy.AddField_management(fc, "SCCatDesc", "TEXT")

        codeblock = """def findTwoLetter(Category):
            output = None
            if Category == "1":
                output = "SBI"
            if Category == "13" :
                output = "SMB"
            if Category == "4":
                output = "SBE"
            if  Category =="10":
                output = "ADW"
            if Category == "8":
                output = "DAC"
            if Category == "6":
                output = "SBW"
            if Category == "2":
                output = "SOT"
            return output"""

        ShortCodeExpression = "findTwoLetter(!Category!)"

        arcpy.CalculateField_management(fc, "SCCatDesc", ShortCodeExpression, "PYTHON_9.3", codeblock)


        arcpy.Append_management(fc, appendClass, "NO_TEST")

        print "success is inevitable for bulky items"
    except KeyError, e:
      print "refunction bulky", lasanbulkyquery()
    except IndexError, e:
        print 'I got an IndexError - reason "%s"' % str(e)





def lasanewastequery():
    start = time.time()
    Start = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    msgFolder = "C:/logs/"
    sender = "geoffreywestgis@gmail.com"
    recipient = "geoffreywestgis@gmail.com"
    fc2 = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311"
    fc = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311Test_ewaste"
    fcCopy = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest"
    appendClass = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_SCData_sa.sde\SCData.DBO.SO_SC_1"
    aTable = "C:\Users\GeoffreyWest\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\ServiceRequest.sde\ServiceRequest.DBO.History_Table_"
    aContainerFC = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.aContainerFC21"
    connect_timeout = 5
    gdb = "C:\MYLATesting.gdb"
    f2 =open('C:\Users\GeoffreyWest\Desktop\jsonewaste.json')
    history_table = 'C:\MYLATesting.gdb\MYLA311Test_Env'
    # ljson = 'C:\Users\GeoffreyWest\Desktop\json.json'
    k_comment = ' '
    data2 = jsonpickle.decode((f2.read()))
    Start = datetime.datetime.now()
    DD = datetime.timedelta(minutes=3)
    earlier = Start - DD
    earlier_str = earlier.strftime('X%m/%d/%Y %H:%M:%S').replace('X0','X').replace('X','')
    data2["QueryRequest"]['LastUpdatedDate'] = str(earlier_str)
    data2 = jsonpickle.encode(data2)
    BulkyItemInfo = " "
    spatial_ref = arcpy.SpatialReference(4326)
    lastpage = 'false'
    startrow = 0
    newquery = 'new'
    pagesize = 100

    url2 = "https://myla311.lacity.org/myla311router/mylasrbe/1/SANQueryPageSR"


    headers2 = {'Content-type': 'text/plain', 'Accept': '/'}


    if arcpy.Exists(fc):
        arcpy.Delete_management(fc)

    while lastpage == 'false':
        r2 = requests.post(url2, data=data2, headers=headers2)
        # print r2.text
        decoded2 = r2.json()
        f2 =open('C:\Users\GeoffreyWest\Desktop\jsonewaste.json')
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

        # print json.dumps(decoded2, sort_keys=True, indent=4)


    try:
        items = []
        for sr in decoded2['Response']['ListOfServiceRequest']['ServiceRequest']:
            Address = sr['SRAddress']
            if sr['Latitude'] != '':
                y = sr['Latitude']
            if sr['Longitude'] != '':
                x = sr['Longitude']
            if sr['Latitude'] == '':
                blanky = sr['Latitude']
            if sr['Longitude'] == '':
                blankx= sr['Longitude']
                print blanky
                print blankx
            ReasonCode = ''
            ResolutionCode = ''
            SRNumber = sr['SRNumber']
            NewContactFirstName = sr['NewContactFirstName']
            NewContactLastName = sr['NewContactLastName']
            Created_FirstName = sr['LA311UpdatedByFirstName']
            Created_LastName = sr ['LA311UpdatedByLastName']
            FirstName = sr['FirstName']
            LastName = sr['LastName']
            if sr['ResolutionCode'] == '':
                ResolutionCode =  sr['ResolutionCode']
            if sr ['ReasonCode'] == '':
                ReasonCode = sr['ReasonCode']
            aReasonCode = sr['ReasonCode']
            HomePhone = sr['HomePhone']
            CreatedDate = sr['CreatedDate']
            UpdatedDate = sr['UpdatedDate']
            BulkyItem = sr['ListOfLa311BulkyItem']
            ElectronicWaste = sr['ListOfLa311ElectronicWaste']
            MoveInMoveOut = sr['ListOfLa311MoveInMoveOut']
            IllegalDumping = sr['ListOfLa311IllegalDumpingPickup']
            BrushItems = sr['ListOfLa311BrushItemsPickup']
            MHA = sr['ListOfLa311MetalHouseholdAppliancesPickup']
            DAR = sr['ListOfLa311DeadAnimalRemoval']
            Manual = sr['ListOfLa311ManualPickup']
            if sr['ServiceDate'] !=  ' ':
                ServiceDate=  sr['ServiceDate']
            try:
                if sr['ListOfLa311GisLayer'] != '{},':
                    GISLayer = sr['ListOfLa311GisLayer']['La311GisLayer'][0]['DistrictName']
            except Exception:
                pass
            NeighborhHoodCouncil = sr['SRNeighborhoodCouncilName']
            ServiceNotes = sr['ListOfLa311ServiceRequestNotes']
            SCCatDesc = ' '
            UpdatedDate = datetime.datetime.strptime(UpdatedDate, "%m/%d/%Y %H:%M:%S")

            if arcpy.Exists(fc):
                    arcpy.Delete_management(fc)

            if 'La311ServiceRequestNotes' in ServiceNotes:
                try:
                    k_comment = ServiceNotes['La311ServiceRequestNotes'][0]['Comment']
                except IndexError:
                    k_comment = ' '
                print k_comment

            if 'La311ElectronicWaste' in ElectronicWaste:
                try:
                    k_ewaste_count_1 = ElectronicWaste['La311ElectronicWaste'][0]['ItemCount']
                except IndexError:
                    k_ewaste_count_1 = ' '
                print k_ewaste_count_1

                try:
                    k_ewaste_count_2 = ElectronicWaste['La311ElectronicWaste'][1]['ItemCount']
                except IndexError:
                    k_ewaste_count_2 = ' '
                print k_ewaste_count_2

                try:
                    k_ewaste_count_3 = ElectronicWaste['La311ElectronicWaste'][2]['ItemCount']
                except IndexError:
                    k_ewaste_count_3 = ' '
                print k_ewaste_count_3

                try:
                    k_ewaste_count_4 = ElectronicWaste['La311ElectronicWaste'][3]['ItemCount']
                except IndexError:
                    k_ewaste_count_4 = ' '
                print k_ewaste_count_4

                try:
                    k_ewaste_count_5 = ElectronicWaste['La311ElectronicWaste'][4]['ItemCount']
                except IndexError:
                    k_ewaste_count_5 = ' '
                print k_ewaste_count_5

                try:
                    k_ewaste_count_6 = ElectronicWaste['La311ElectronicWaste'][5]['ItemCount']
                except IndexError:
                    k_ewaste_count_6 = ' '
                print k_ewaste_count_6

                try:
                    k_ewaste_count_7 = ElectronicWaste['La311ElectronicWaste'][6]['ItemCount']
                except IndexError:
                    k_ewaste_count_7 = ' '
                print k_ewaste_count_7

                try:
                    k_ewaste_count_8 = ElectronicWaste['La311ElectronicWaste'][7]['ItemCount']
                except IndexError:
                    k_ewaste_count_8 = ' '
                print k_ewaste_count_8

                try:
                    k_ewaste_count_9 = ElectronicWaste['La311ElectronicWaste'][8]['ItemCount']
                except IndexError:
                    k_ewaste_count_9 = ' '
                print k_ewaste_count_9

                try:
                    k_ewaste_count_10 = ElectronicWaste['La311ElectronicWaste'][9]['ItemCount']
                except IndexError:
                    k_ewaste_count_10 = ' '
                print k_ewaste_count_10

                try:
                    k_ewaste_item_1 = ElectronicWaste['La311ElectronicWaste'][0]['ElectronicWestType']
                except IndexError:
                    k_ewaste_item_1 = ' '
                print k_ewaste_item_1


                try:
                    k_ewaste_item_2 = ElectronicWaste['La311ElectronicWaste'][1]['ElectronicWestType']
                except IndexError:
                    k_ewaste_item_2 = ' '
                print k_ewaste_item_2


                try:
                    k_ewaste_item_3 = ElectronicWaste['La311ElectronicWaste'][2]['ElectronicWestType']
                except IndexError:
                    k_ewaste_item_3 = ' '
                print k_ewaste_item_3


                try:
                    k_ewaste_item_4 = ElectronicWaste['La311ElectronicWaste'][3]['ElectronicWestType']
                except IndexError:
                    k_ewaste_item_4 = ' '
                print k_ewaste_item_4


                try:
                    k_ewaste_item_5 = ElectronicWaste['La311ElectronicWaste'][4]['ElectronicWestType']
                except IndexError:
                    k_ewaste_item_5 = ' '
                print k_ewaste_item_5

                try:
                    k_ewaste_item_6 = ElectronicWaste['La311ElectronicWaste'][5]['ElectronicWestType']
                except IndexError:
                    k_ewaste_item_6 = ' '
                print k_ewaste_item_6


                try:
                    k_ewaste_item_7 = ElectronicWaste['La311ElectronicWaste'][6]['ElectronicWestType']
                except IndexError:
                    k_ewaste_item_7 = ' '
                print k_ewaste_item_7



                try:
                    k_ewaste_item_8 = ElectronicWaste['La311ElectronicWaste'][7]['ElectronicWestType']
                except IndexError:
                    k_ewaste_item_8 = ' '
                print k_ewaste_item_8



                try:
                    k_ewaste_item_9 = ElectronicWaste['La311ElectronicWaste'][8]['ElectronicWestType']
                except IndexError:
                    k_ewaste_item_9 = ' '
                print k_ewaste_item_9


                try:
                    k_ewaste_item_10 = ElectronicWaste['La311ElectronicWaste'][9]['ElectronicWestType']
                except IndexError:
                    k_ewaste_item_10 = ' '
                print k_ewaste_item_10


                try:
                    k_ewaste_location_1 = ElectronicWaste['La311ElectronicWaste'][0]['CollectionLocation']
                except IndexError:
                    k_ewaste_location_1 = ' '
                print k_ewaste_location_1


                try:
                    k_ewaste_location_2 = ElectronicWaste['La311ElectronicWaste'][1]['CollectionLocation']
                except IndexError:
                    k_ewaste_location_2 = ' '
                print k_ewaste_location_2

                try:
                    k_ewaste_location_3 = ElectronicWaste['La311ElectronicWaste'][2]['CollectionLocation']
                except IndexError:
                    k_ewaste_location_3 = ' '
                print k_ewaste_location_3

                try:
                    k_ewaste_location_4 = ElectronicWaste['La311ElectronicWaste'][3]['CollectionLocation']
                except IndexError:
                    k_ewaste_location_4 = ' '
                print k_ewaste_location_4

                try:
                    k_ewaste_location_5 = ElectronicWaste['La311ElectronicWaste'][4]['CollectionLocation']
                except IndexError:
                    k_ewaste_location_5 = ' '
                print k_ewaste_location_5


                try:
                    k_ewaste_location_6 = ElectronicWaste['La311ElectronicWaste'][5]['CollectionLocation']
                except IndexError:
                    k_ewaste_location_6 = ' '
                print k_ewaste_location_6



                try:
                    k_ewaste_location_7 = ElectronicWaste['La311ElectronicWaste'][6]['CollectionLocation']
                except IndexError:
                    k_ewaste_location_7 = ' '
                print k_ewaste_location_7



                try:
                    k_ewaste_location_8 = ElectronicWaste['La311ElectronicWaste'][7]['CollectionLocation']
                except IndexError:
                    k_ewaste_location_8 = ' '
                print k_ewaste_location_8



                try:
                    k_ewaste_location_9 = ElectronicWaste['La311ElectronicWaste'][8]['CollectionLocation']
                except IndexError:
                    k_ewaste_location_9 = ' '
                print k_ewaste_location_9


                try:
                    k_ewaste_location_10 = ElectronicWaste['La311ElectronicWaste'][9]['CollectionLocation']
                except IndexError:
                    k_ewaste_location_10 = ' '
                print k_ewaste_location_10


                try:
                    k_ewaste_name_1 = ElectronicWaste['La311ElectronicWaste'][0]['Name']
                except IndexError:
                    k_ewaste_name_1 = ' '
                print k_ewaste_name_1



                try:
                    k_ewaste_name_2 = ElectronicWaste['La311ElectronicWaste'][1]['Name']
                except IndexError:
                    k_ewaste_name_2 = ' '
                print k_ewaste_name_2



                try:
                    k_ewaste_name_3 = ElectronicWaste['La311ElectronicWaste'][2]['Name']
                except IndexError:
                    k_ewaste_name_3 = ' '
                print k_ewaste_name_3


                try:
                    k_ewaste_name_4 = ElectronicWaste['La311ElectronicWaste'][3]['Name']
                except IndexError:
                    k_ewaste_name_4 = ' '
                print k_ewaste_name_4

                try:
                    k_ewaste_name_5 = ElectronicWaste['La311ElectronicWaste'][4]['Name']
                except IndexError:
                    k_ewaste_name_5 = ' '
                print k_ewaste_name_5

                try:
                    k_ewaste_name_6 = ElectronicWaste['La311ElectronicWaste'][5]['Name']
                except IndexError:
                    k_ewaste_name_6 = ' '
                print k_ewaste_name_6


                try:
                    k_ewaste_name_7 = ElectronicWaste['La311ElectronicWaste'][6]['Name']
                except IndexError:
                    k_ewaste_name_7 = ' '
                print k_ewaste_name_7



                try:
                    k_ewaste_name_8 = ElectronicWaste['La311ElectronicWaste'][7]['Name']
                except IndexError:
                    k_ewaste_name_8 = ' '
                print k_ewaste_name_8



                try:
                    k_ewaste_name_9 = ElectronicWaste['La311ElectronicWaste'][8]['Name']
                except IndexError:
                    k_ewaste_name_9 = ' '
                print k_ewaste_name_9


                try:
                    k_ewaste_name_10 = ElectronicWaste['La311ElectronicWaste'][9]['Name']
                except IndexError:
                    k_ewaste_name_10 = ' '
                print k_ewaste_name_10

                if ElectronicWaste['La311ElectronicWaste'][0]['Type'] == 'Electronic Waste':
                    k_ewaste_comm_1 = 4

                date_object = ' '
                created_object = ' '

                try:
                    date_object = datetime.datetime.strptime(ServiceDate, "%m/%d/%Y %H:%M:%S")
                    created_object = datetime.datetime.strptime(CreatedDate, "%m/%d/%Y %H:%M:%S")
                except Exception:
                    pass



                FullName = NewContactFirstName  +  " " + NewContactLastName
                if FullName  == ' ':
                    FullName = 'Not Specified'

                if created_object == ' ':
                    created_object = UpdatedDate


                if date_object == ' ':
                    date_object = '07/01/2015'

                CreatedBy = Created_FirstName + " " + Created_LastName
                Prior_Resolution_Code =  ' '

                dt = np.dtype([('Address', 'U40'),
                    ('Y_CoordShape', '<f8'),
                    ('X_CoordShape', '<f8'),
                    ('Y_COR', '<f8'),
                    ('X_COR', '<f8'),
                    ('ReasonCode','U128'),
                    ('NUMBERCYLA', 'U40'),
                    ('SRNumber', 'U40'),
                    ('Name', 'U40'),
                    ('RESOLUTION_CODE','U128'),
                   ('HOME_PHONE', 'U40'),
                    ('OPEN_TIME', 'U128'),
                    ('OPENED_BY', 'U128'),
                    ('UpdatedDate', 'U128'),
                    ('ItemDesc_1', 'U128'),
                    ('ItemDesc_2', 'U128'),
                    ('ItemDesc_3', 'U128'),
                    ('ItemDesc_4','U128'),
                    ('ItemDesc_5', 'U128'),
                    ('ItemDesc_6', 'U128'),
                    ('ItemDesc_7', 'U128'),
                    ('ItemDesc_8', 'U128'),
                    ('ItemDesc_9', 'U128'),
                    ('ItemDesc_10', 'U128'),
                    ('Category', 'U128'),
                     ('SCHED_DATE', 'U128'),
                    ('CYLA_DISTRICT ', 'U128'),
                ('BRIEF_DESCRIPTION', 'U128'),
                    ('Comment', 'U128'),
                    ('Prior_RESOLUTION_CODE', 'U128'),
                    ('UID1', 'U128'),
                    ('UID2', 'U128'),
                    ('UID3', 'U128'),
                    ('UID4', 'U128'),
                    ('UID5', 'U128'),
                    ('UID6', 'U128'),
                    ('UID7', 'U128'),
                    ('UID8', 'U128'),
                    ('UID9', 'U128'),
                    ('UID10', 'U128'),
                    ('ItemLoc_1', 'U128'),
                    ('ItemLoc_2', 'U128'),
                    ('ItemLoc_3', 'U128'),
                    ('ItemLoc_4', 'U128'),
                    ('ItemLoc_5', 'U128'),
                    ('ItemLoc_6', 'U128'),
                    ('ItemLoc_7', 'U128'),
                    ('ItemLoc_8', 'U128'),
                    ('ItemLoc_9', 'U128'),
                    ('ItemLoc_10', 'U128'),



                ])
                elif k_ewaste_comm_1 == 4:
                    items.append((Address,
                             x,
                            y,
                              x,
                              y,
                              ReasonCode,
                              SRNumber,
                             SRNumber,
                             FullName,
                              ResolutionCode,
                              HomePhone,
                              created_object,
                             CreatedBy,
                              UpdatedDate,
                            k_ewaste_count_1 + ',' + k_ewaste_item_1,
                             k_ewaste_count_2 + ',' + k_ewaste_item_2,
                             k_ewaste_count_3 + ',' + k_ewaste_item_3,
                             k_ewaste_count_4 + ',' + k_ewaste_item_4,
                             k_ewaste_count_5 + ',' + k_ewaste_item_5,
                             k_ewaste_count_6 + ',' + k_ewaste_item_6,
                             k_ewaste_count_7 + ',' + k_ewaste_item_7,
                             k_ewaste_count_8 + ',' + k_ewaste_item_8,
                             k_ewaste_count_9 + ',' + k_ewaste_item_9,
                             k_ewaste_count_10 + ',' + k_ewaste_item_10,
                             k_ewaste_comm_1,
                              date_object,
                             GISLayer,
                             k_ewaste_location_1 +  k_ewaste_count_1 + ',' + k_ewaste_item_1 + ';' + k_ewaste_count_2 + ',' + k_ewaste_item_2 + ';' + k_ewaste_count_3 + ',' + k_ewaste_item_3 + ';' + k_ewaste_count_4 + ',' + k_ewaste_item_4 + ';' + k_ewaste_count_5 + ',' + k_ewaste_item_5 + ';' + k_ewaste_count_6+ ',' + k_ewaste_item_6 + ';' + k_ewaste_count_7 + ',' + k_ewaste_item_7 + ';' + k_ewaste_count_8 + ',' + k_ewaste_item_8 + ';' + k_ewaste_count_9 + ',' + k_ewaste_item_9 + ';' + k_ewaste_count_10 + ',' + k_ewaste_item_10,

                            k_comment,
                             Prior_Resolution_Code,
                            k_ewaste_name_1,
                            k_ewaste_name_2,
                            k_ewaste_name_3,
                            k_ewaste_name_4,
                            k_ewaste_name_5,
                            k_ewaste_name_6,
                            k_ewaste_name_7,
                            k_ewaste_name_8,
                            k_ewaste_name_9,
                            k_ewaste_name_10,
                            k_ewaste_location_1,
                            k_ewaste_location_2,
                            k_ewaste_location_3,
                            k_ewaste_location_4,
                            k_ewaste_location_5,
                            k_ewaste_location_6,
                            k_ewaste_location_7,
                            k_ewaste_location_8,
                            k_ewaste_location_9,
                            k_ewaste_location_10,

                            ))

            arr = np.array(items,dtype=dt)

            NumPyArray = arcpy.da.NumPyArrayToFeatureClass(arr, fc, ['Y_CoordShape', 'X_CoordShape'], spatial_ref)

            arcpy.AddField_management(fc, "SCCatDesc", "TEXT")

            codeblock = """def findTwoLetter(Category):
                output = None
                if Category == "1":
                    output = "SBI"
                if Category == "13" :
                    output = "SMB"
                if Category == "4":
                    output = "SBE"
                if  Category =="10":
                    output = "ADW"
                if Category == "8":
                    output = "DAC"
                if Category == "6":
                    output = "SBW"
                if Category == "2":
                    output = "SOT"
                return output"""

            ShortCodeExpression = "findTwoLetter(!Category!)"

            arcpy.CalculateField_management(fc, "SCCatDesc", ShortCodeExpression, "PYTHON_9.3", codeblock)

            arcpy.Append_management(fc, appendClass, "NO_TEST")
            orignal_data = ' '
            print "success is inevitable for ewaste"
    except KeyError, e:
        if KeyError in lasanewastequery():
            lasanewastequery() == orignal_data
    except IndexError, e:
        print 'I got an IndexError - reason "%s"' % str(e)






def lasandarquery():
    start = time.time()
    print "done"
schedule.every(0-20).minutes.do(lasandarquery)
schedule.every(0-20).minutes.do(lasanbulkyquery)
schedule.every(0-20).minutes.do(lasanewastequery)
while True:
    schedule.run_pending()
    time.sleep(1)
#     Start = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
#     msgFolder = "C:/logs/"
#     sender = "geoffreywestgis@gmail.com"
#     recipient = "geoffreywestgis@gmail.com"
#     fc2 = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311"
#     fc = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311Test_Env_2_ewaste"
#     fcCopy = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest"
#     appendClass = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_SCData_sa.sde\SCData.DBO.SO_SC_1"
#     aTable = "C:\Users\GeoffreyWest\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\ServiceRequest.sde\ServiceRequest.DBO.History_Table_"
#     aContainerFC = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.aContainerFC21"
#     connect_timeout = 5
#     gdb = "C:\MYLATesting.gdb"
#     f2 =open('C:\Users\GeoffreyWest\Desktop\jsonewaste.json')
#     history_table = 'C:\MYLATesting.gdb\MYLA311Test_Env'
#     # ljson = 'C:\Users\GeoffreyWest\Desktop\json.json'
#     k_comment = ' '
#     data2 = jsonpickle.decode((f2.read()))
#     Start = datetime.datetime.now()
#     DD = datetime.timedelta(minutes=300)
#     earlier = Start - DD
#     earlier_str = earlier.strftime('X%m/%d/%Y %H:%M:%S').replace('X0','X').replace('X','')
#     data2["QueryRequest"]['LastUpdatedDate'] = str(earlier_str)
#     data2 = jsonpickle.encode(data2)
#     BulkyItemInfo = " "
#     spatial_ref = arcpy.SpatialReference(4326)
#     lastpage = 'false'
#     startrow = 0
#     newquery = 'new'
#     pagesize = 100
#
#     url2 = "https://myla311.lacity.org/myla311router/mylasrbe/1/SANQueryPageSR"
#
#
#     headers2 = {'Content-type': 'text/plain', 'Accept': '/'}
#
#
#     if arcpy.Exists(fc):
#         arcpy.Delete_management(fc)
#
#     while lastpage == 'false':
#         r2 = requests.post(url2, data=data2, headers=headers2)
#         # print r2.text
#         decoded2 = r2.json()
#         f2 =open('C:\Users\GeoffreyWest\Desktop\jsondar.json')
#         data2 = jsonpickle.decode((f2.read()))
#         if decoded2['Response']['LastPage'] == 'false':
#             data2['QueryRequest']['PageSize'] = pagesize
#             startrow = startrow + data2['QueryRequest']['PageSize']
#             data2['QueryRequest']['StartRowNum'] = startrow
#             data2['QueryRequest']['NewQuery'] = 'false'
#             data2 = jsonpickle.encode(data2)
#             print startrow
#         else:
#             lastpage = 'true'
#
#         # print json.dumps(decoded2, sort_keys=True, indent=4)
#
#
#     try:
#         items = []
#         for sr in decoded2['Response']['ListOfServiceRequest']['ServiceRequest']:
#             Address = sr['SRAddress']
#             if sr['Latitude'] != '':
#                 y = sr['Latitude']
#             if sr['Longitude'] != '':
#                 x = sr['Longitude']
#             if sr['Latitude'] == '':
#                 blanky = sr['Latitude']
#             if sr['Longitude'] == '':
#                 blankx= sr['Longitude']
#                 print blanky
#                 print blankx
#             ReasonCode = ''
#             ResolutionCode = ''
#             SRNumber = sr['SRNumber']
#             NewContactFirstName = sr['NewContactFirstName']
#             NewContactLastName = sr['NewContactLastName']
#             Created_FirstName = sr['LA311UpdatedByFirstName']
#             Created_LastName = sr ['LA311UpdatedByLastName']
#             FirstName = sr['FirstName']
#             LastName = sr['LastName']
#             if sr['ResolutionCode'] == '':
#                 ResolutionCode =  sr['ResolutionCode']
#             if sr ['ReasonCode'] == '':
#                 ReasonCode = sr['ReasonCode']
#             aReasonCode = sr['ReasonCode']
#             HomePhone = sr['HomePhone']
#             CreatedDate = sr['CreatedDate']
#             UpdatedDate = sr['UpdatedDate']
#             BulkyItem = sr['ListOfLa311BulkyItem']
#             ElectronicWaste = sr['ListOfLa311ElectronicWaste']
#             MoveInMoveOut = sr['ListOfLa311MoveInMoveOut']
#             IllegalDumping = sr['ListOfLa311IllegalDumpingPickup']
#             BrushItems = sr['ListOfLa311BrushItemsPickup']
#             MHA = sr['ListOfLa311MetalHouseholdAppliancesPickup']
#             DAR = sr['ListOfLa311DeadAnimalRemoval']
#             Manual = sr['ListOfLa311ManualPickup']
#             if sr['ServiceDate'] !=  ' ':
#                 ServiceDate=  sr['ServiceDate']
#             try:
#                 if sr['ListOfLa311GisLayer'] != '{},':
#                     GISLayer = sr['ListOfLa311GisLayer']['La311GisLayer'][0]['DistrictName']
#             except Exception:
#                 pass
#             NeighborhHoodCouncil = sr['SRNeighborhoodCouncilName']
#             ServiceNotes = sr['ListOfLa311ServiceRequestNotes']
#             SCCatDesc = ' '
#             UpdatedDate = datetime.datetime.strptime(UpdatedDate, "%m/%d/%Y %H:%M:%S")
#
#             if arcpy.Exists(fc):
#                     arcpy.Delete_management(fc)
#
#             if 'La311ServiceRequestNotes' in ServiceNotes:
#                 try:
#                     k_comment = ServiceNotes['La311ServiceRequestNotes'][0]['Comment']
#                 except IndexError:
#                     k_comment = ' '
#                 print k_comment
#
#             if 'DeadAnimalRemoval' in DAR:
#                 try:
#                     k_dar_count_1 = DAR['DeadAnimalRemoval'][0]['DACItemCount']
#                 except IndexError:
#                     k_dar_count_1 = ' '
#                 print k_dar_count_1
#
#                 try:
#                      k_dar_count_2 = DAR['DeadAnimalRemoval'][1]['DACItemCount']
#                 except IndexError:
#                      k_dar_count_2 = ' '
#                 print  k_dar_count_2
#
#                 try:
#                     k_dar_count_3 = DAR['DeadAnimalRemoval'][2]['DACItemCount']
#                 except IndexError:
#                     k_dar_count_3 = ' '
#                 print k_dar_count_3
#
#                 try:
#                     k_dar_count_4 = DAR['DeadAnimalRemoval'][3]['DACItemCount']
#                 except IndexError:
#                     k_dar_count_4 = ' '
#                 print k_dar_count_4
#
#                 try:
#                      k_dar_count_5 = DAR['DeadAnimalRemoval'][4]['DACItemCount']
#                 except IndexError:
#                      k_dar_count_5 = ' '
#                 print  k_dar_count_5
#
#                 try:
#                     k_dar_count_6 = DAR['DeadAnimalRemoval'][5]['DACItemCount']
#                 except IndexError:
#                     k_dar_count_6 = ' '
#                 print k_dar_count_6
#
#                 try:
#                     k_dar_count_7 = DAR['DeadAnimalRemoval'][6]['DACItemCount']
#                 except IndexError:
#                     k_dar_count_7 = ' '
#                 print k_dar_count_7
#
#                 try:
#                    k_dar_count_8 = DAR['DeadAnimalRemoval'][7]['DACItemCount']
#                 except IndexError:
#                     k_dar_count_8 = ' '
#                 print k_dar_count_8
#
#                 try:
#                     k_dar_count_9 = DAR['DeadAnimalRemoval'][8]['DACItemCount']
#                 except IndexError:
#                     k_dar_count_9 = ' '
#                 print k_dar_count_9
#
#                 try:
#                     k_dar_count_10 = DAR['DeadAnimalRemoval'][9]['DACItemCount']
#                 except IndexError:
#                     k_dar_count_10 = ' '
#                 print k_dar_count_10
#
#                 try:
#                     k_dar_item_1 = DAR['DeadAnimalRemoval'][0]['DACType']
#                 except IndexError:
#                     k_dar_item_1 = ' '
#                 print k_dar_item_1
#
#
#                 try:
#                     k_dar_item_2 = DAR['DeadAnimalRemoval'][1]['DACType']
#                 except IndexError:
#                     k_dar_item_2 = ' '
#                 print k_dar_item_2
#
#
#                 try:
#                    k_dar_item_3 = DAR['DeadAnimalRemoval'][2]['DACType']
#                 except IndexError:
#                     k_dar_item_3 = ' '
#                 print k_dar_item_3
#
#
#                 try:
#                     k_dar_item_4 = DAR['DeadAnimalRemoval'][3]['DACType']
#                 except IndexError:
#                     k_dar_item_4 = ' '
#                 print k_dar_item_4
#
#
#                 try:
#                     k_dar_item_5 = DAR['DeadAnimalRemoval'][4]['DACType']
#                 except IndexError:
#                     k_dar_item_5 = ' '
#                 print k_dar_item_5
#
#                 try:
#                     k_dar_item_6 = DAR['DeadAnimalRemoval'][5]['DACType']
#                 except IndexError:
#                     k_dar_item_6 = ' '
#                 print k_dar_item_6
#
#
#                 try:
#                     k_dar_item_7 = DAR['DeadAnimalRemoval'][6]['DACType']
#                 except IndexError:
#                     k_dar_item_7 = ' '
#                 print k_dar_item_7
#
#
#
#                 try:
#                     k_dar_item_8 = DAR['DeadAnimalRemoval'][7]['DACType']
#                 except IndexError:
#                     k_dar_item_8 = ' '
#                 print k_dar_item_8
#
#
#
#                 try:
#                     k_dar_item_9 = DAR['DeadAnimalRemoval'][8]['DACType']
#                 except IndexError:
#                     k_dar_item_9 = ' '
#                 print k_dar_item_9
#
#
#                 try:
#                     k_dar_item_10 = DAR['DeadAnimalRemoval'][9]['DACType']
#                 except IndexError:
#                     k_dar_item_10 = ' '
#                 print k_dar_item_10
#
#
#                 try:
#                     k_dar_location_1 = DAR['DeadAnimalRemoval'][0]['CollectionLocation']
#                 except IndexError:
#                     k_dar_location_1 = ' '
#                 print k_dar_location_1
#
#
#                 try:
#                     k_dar_location_2 = DAR['DeadAnimalRemoval'][1]['CollectionLocation']
#                 except IndexError:
#                     k_dar_location_2 = ' '
#                 print k_dar_location_2
#
#                 try:
#                     k_dar_location_3 = DAR['DeadAnimalRemoval'][2]['CollectionLocation']
#                 except IndexError:
#                     k_dar_location_3 = ' '
#                 print k_dar_location_3
#
#                 try:
#                     k_dar_location_4 = DAR['DeadAnimalRemoval'][3]['CollectionLocation']
#                 except IndexError:
#                     k_dar_location_4 = ' '
#                 print k_dar_location_4
#
#                 try:
#                     k_dar_location_5 = DAR['DeadAnimalRemoval'][4]['CollectionLocation']
#                 except IndexError:
#                     k_dar_location_5 = ' '
#                 print k_dar_location_5
#
#
#                 try:
#                     k_dar_location_6 = DAR['DeadAnimalRemoval'][5]['CollectionLocation']
#                 except IndexError:
#                     k_dar_location_6 = ' '
#                 print k_dar_location_6
#
#
#
#                 try:
#                     k_dar_location_7 = DAR['DeadAnimalRemoval'][6]['CollectionLocation']
#                 except IndexError:
#                     k_dar_location_7 = ' '
#                 print k_dar_location_7
#
#
#
#                 try:
#                     k_dar_location_8 = DAR['DeadAnimalRemoval'][7]['CollectionLocation']
#                 except IndexError:
#                     k_dar_location_8 = ' '
#                 print k_dar_location_8
#
#
#
#                 try:
#                     k_dar_location_9 = DAR['DeadAnimalRemoval'][8]['CollectionLocation']
#                 except IndexError:
#                     k_dar_location_9 = ' '
#                 print k_dar_location_9
#
#
#                 try:
#                     k_dar_location_10 = DAR['DeadAnimalRemoval'][9]['CollectionLocation']
#                 except IndexError:
#                     k_dar_location_10 = ' '
#                 print k_dar_location_10
#
#
#                 try:
#                     k_dar_name_1 = DAR['DeadAnimalRemoval'][0]['Name']
#                 except IndexError:
#                     k_dar_name_1 = ' '
#                 print k_dar_name_1
#
#
#
#                 try:
#                     k_dar_name_2 = DAR['DeadAnimalRemoval'][1]['Name']
#                 except IndexError:
#                     k_dar_name_2 = ' '
#                 print k_dar_name_2
#
#
#
#                 try:
#                     k_dar_name_3 = DAR['DeadAnimalRemoval'][2]['Name']
#                 except IndexError:
#                     k_dar_name_3 = ' '
#                 print k_dar_name_3
#
#
#                 try:
#                     k_dar_name_4 = DAR['DeadAnimalRemoval'][3]['Name']
#                 except IndexError:
#                     k_dar_name_4 = ' '
#                 print k_dar_name_4
#
#                 try:
#                     k_dar_name_5 = DAR['DeadAnimalRemoval'][4]['Name']
#                 except IndexError:
#                     k_dar_name_5 = ' '
#                 print k_dar_name_5
#
#                 try:
#                     k_dar_name_6 = DAR['DeadAnimalRemoval'][5]['Name']
#                 except IndexError:
#                     k_dar_name_6 = ' '
#                 print k_dar_name_6
#
#
#                 try:
#                     k_dar_name_7 = DAR['DeadAnimalRemoval'][6]['Name']
#                 except IndexError:
#                     k_dar_name_7 = ' '
#                 print k_dar_name_7
#
#
#
#                 try:
#                     k_dar_name_8 = DAR['DeadAnimalRemoval'][7]['Name']
#                 except IndexError:
#                     k_dar_name_8 = ' '
#                 print k_dar_name_8
#
#
#
#                 try:
#                     k_dar_name_9 = DAR['DeadAnimalRemoval'][8]['Name']
#                 except IndexError:
#                     k_dar_name_9 = ' '
#                 print k_dar_name_9
#
#
#                 try:
#                     k_dar_name_10 = DAR['DeadAnimalRemoval'][9]['Name']
#                 except IndexError:
#                     k_dar_name_10 = ' '
#                 print k_dar_name_10
#
#                 if DAR['DeadAnimalRemoval'][0]['Type'] == 'Dead Animal Removal':
#                     k_dar_comm_1 = 8
#
#                 date_object = ' '
#                 created_object = ' '
#
#                 try:
#                     date_object = datetime.datetime.strptime(ServiceDate, "%m/%d/%Y %H:%M:%S")
#                     created_object = datetime.datetime.strptime(CreatedDate, "%m/%d/%Y %H:%M:%S")
#                 except Exception:
#                     pass
#
#
#
#                 FullName = NewContactFirstName  +  " " + NewContactLastName
#                 if FullName  == ' ':
#                     FullName = 'Not Specified'
#
#                 if created_object == ' ':
#                     created_object = UpdatedDate
#
#
#                 if date_object == ' ':
#                     date_object = '07/01/2015'
#
#                 CreatedBy = Created_FirstName + " " + Created_LastName
#                 Prior_Resolution_Code =  ' '
#
#                 dt = np.dtype([('Address', 'U40'),
#                     ('Y_CoordShape', '<f8'),
#                     ('X_CoordShape', '<f8'),
#                     ('Y_COR', '<f8'),
#                     ('X_COR', '<f8'),
#                     ('ReasonCode','U128'),
#                     ('NUMBERCYLA', 'U40'),
#                     ('SRNumber', 'U40'),
#                     ('Name', 'U40'),
#                     ('RESOLUTION_CODE','U128'),
#                    ('HOME_PHONE', 'U40'),
#                     ('OPEN_TIME', 'U128'),
#                     ('OPENED_BY', 'U128'),
#                     ('UpdatedDate', 'U128'),
#                     ('ItemDesc_1', 'U128'),
#                     ('ItemDesc_2', 'U128'),
#                     ('ItemDesc_3', 'U128'),
#                     ('ItemDesc_4','U128'),
#                     ('ItemDesc_5', 'U128'),
#                     ('ItemDesc_6', 'U128'),
#                     ('ItemDesc_7', 'U128'),
#                     ('ItemDesc_8', 'U128'),
#                     ('ItemDesc_9', 'U128'),
#                     ('ItemDesc_10', 'U128'),
#                     ('Category', 'U128'),
#                      ('SCHED_DATE', 'U128'),
#                     ('CYLA_DISTRICT ', 'U128'),
#                 ('BRIEF_DESCRIPTION', 'U128'),
#                     ('Comment', 'U128'),
#                     ('Prior_RESOLUTION_CODE', 'U128'),
#                     ('UID1', 'U128'),
#                     ('UID2', 'U128'),
#                     ('UID3', 'U128'),
#                     ('UID4', 'U128'),
#                     ('UID5', 'U128'),
#                     ('UID6', 'U128'),
#                     ('UID7', 'U128'),
#                     ('UID8', 'U128'),
#                     ('UID9', 'U128'),
#                     ('UID10', 'U128'),
#                     ('ItemLoc_1', 'U128'),
#                     ('ItemLoc_2', 'U128'),
#                     ('ItemLoc_3', 'U128'),
#                     ('ItemLoc_4', 'U128'),
#                     ('ItemLoc_5', 'U128'),
#                     ('ItemLoc_6', 'U128'),
#                     ('ItemLoc_7', 'U128'),
#                     ('ItemLoc_8', 'U128'),
#                     ('ItemLoc_9', 'U128'),
#                     ('ItemLoc_10', 'U128'),
#
#
#
#                 ])
#                 if k_dar_comm_1 == 8:
#                     items.append((Address,
#                              x,
#                             y,
#                               x,
#                               y,
#                               ReasonCode,
#                               SRNumber,
#                              SRNumber,
#                              FullName,
#                               ResolutionCode,
#                               HomePhone,
#                               created_object,
#                              CreatedBy,
#                               UpdatedDate,
#                            k_dar_name_1,
#                             k_dar_name_2,
#                             k_dar_name_3,
#                             k_dar_name_4,
#                             k_dar_name_5,
#                             k_dar_name_6,
#                             k_dar_name_7,
#                             k_dar_name_8,
#                             k_dar_name_9,
#                             k_dar_name_10,
#                             k_dar_location_1,
#                             k_dar_location_2,
#                             k_dar_location_3,
#                             k_dar_location_4,
#                             k_dar_location_5,
#                             k_dar_location_6,
#                             k_dar_location_7,
#                             k_dar_location_8,
#                             k_dar_location_9,
#                             k_dar_location_10,
#                               date_object,
#                              GISLayer,
#                              k_dar_location_1 +  k_dar_count_1 + ',' + k_dar_item_1 + ';' + k_dar_count_2 + ',' + k_dar_item_2 + ';' + k_dar_count_3 + ',' + k_dar_item_3 + ';' + k_dar_count_4 + ',' + k_dar_item_4 + ';' + k_dar_count_5 + ',' + k_dar_item_5 + ';' + k_dar_count_6+ ',' + k_dar_item_6 + ';' + k_dar_count_7 + ',' + k_dar_item_7 + ';' + k_dar_count_8 + ',' + k_dar_item_8 + ';' + k_dar_count_9 + ',' + k_dar_item_9 + ';' + k_dar_count_10 + ',' + k_dar_item_10,
#                             k_comment,
#                              Prior_Resolution_Code,
#                             k_dar_name_1,
#                             k_dar_name_2,
#                             k_dar_name_3,
#                             k_dar_name_4,
#                             k_dar_name_5,
#                             k_dar_name_6,
#                             k_dar_name_7,
#                             k_dar_name_8,
#                             k_dar_name_9,
#                             k_dar_name_10,
#                             k_dar_location_1,
#                             k_dar_location_2,
#                             k_dar_location_3,
#                             k_dar_location_4,
#                             k_dar_location_5,
#                             k_dar_location_6,
#                             k_dar_location_7,
#                             k_dar_location_8,
#                             k_dar_location_9,
#                             k_dar_location_10,
#
#                             ))
#
#             arr = np.array(items,dtype=dt)
#
#             NumPyArray = arcpy.da.NumPyArrayToFeatureClass(arr, fc, ['Y_CoordShape', 'X_CoordShape'], spatial_ref)
#
#             arcpy.AddField_management(fc, "SCCatDesc", "TEXT")
#
#             codeblock = """def findTwoLetter(Category):
#                 output = None
#                 if Category == "1":
#                     output = "SBI"
#                 if Category == "13" :
#                     output = "SMB"
#                 if Category == "4":
#                     output = "SBE"
#                 if  Category =="10":
#                     output = "ADW"
#                 if Category == "8":
#                     output = "DAC"
#                 if Category == "6":
#                     output = "SBW"
#                 if Category == "2":
#                     output = "SOT"
#                 return output"""
#
#             ShortCodeExpression = "findTwoLetter(!Category!)"
#
#             arcpy.CalculateField_management(fc, "SCCatDesc", ShortCodeExpression, "PYTHON_9.3", codeblock)
#
#
#             arcpy.Append_management(fc, appendClass, "NO_TEST")
#
#             print "success is inevitable for dar"
#     except KeyError, e:
#         print "refunction dar", lasandarquery()
#     except IndexError, e:
#         print 'I got an IndexError - reason "%s"' % str(e)
#
#
#
#
#
#
# def lasanmhaquery():
#     start = time.time()
#     Start = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
#     msgFolder = "C:/logs/"
#     sender = "geoffreywestgis@gmail.com"
#     recipient = "geoffreywestgis@gmail.com"
#     fc2 = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311"
#     fc = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311Test_Env_2_ewaste"
#     fcCopy = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest"
#     appendClass = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_SCData_sa.sde\SCData.DBO.SO_SC_1"
#     aTable = "C:\Users\GeoffreyWest\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\ServiceRequest.sde\ServiceRequest.DBO.History_Table_"
#     aContainerFC = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.aContainerFC21"
#     connect_timeout = 5
#     gdb = "C:\MYLATesting.gdb"
#     f2 =open('C:\Users\GeoffreyWest\Desktop\jsonewaste.json')
#     history_table = 'C:\MYLATesting.gdb\MYLA311Test_Env'
#     # ljson = 'C:\Users\GeoffreyWest\Desktop\json.json'
#     k_comment = ' '
#     data2 = jsonpickle.decode((f2.read()))
#     Start = datetime.datetime.now()
#     DD = datetime.timedelta(minutes=300)
#     earlier = Start - DD
#     earlier_str = earlier.strftime('X%m/%d/%Y %H:%M:%S').replace('X0','X').replace('X','')
#     data2["QueryRequest"]['LastUpdatedDate'] = str(earlier_str)
#     data2 = jsonpickle.encode(data2)
#     BulkyItemInfo = " "
#     spatial_ref = arcpy.SpatialReference(4326)
#     lastpage = 'false'
#     startrow = 0
#     newquery = 'new'
#     pagesize = 100
#
#     url2 = "https://myla311.lacity.org/myla311router/mylasrbe/1/SANQueryPageSR"
#
#
#     headers2 = {'Content-type': 'text/plain', 'Accept': '/'}
#
#
#     if arcpy.Exists(fc):
#         arcpy.Delete_management(fc)
#
#     while lastpage == 'false':
#         r2 = requests.post(url2, data=data2, headers=headers2)
#         # print r2.text
#         decoded2 = r2.json()
#         f2 =open('C:\Users\GeoffreyWest\Desktop\jsondar.json')
#         data2 = jsonpickle.decode((f2.read()))
#         if decoded2['Response']['LastPage'] == 'false':
#             data2['QueryRequest']['PageSize'] = pagesize
#             startrow = startrow + data2['QueryRequest']['PageSize']
#             data2['QueryRequest']['StartRowNum'] = startrow
#             data2['QueryRequest']['NewQuery'] = 'false'
#             data2 = jsonpickle.encode(data2)
#             print startrow
#         else:
#             lastpage = 'true'
#
#         # print json.dumps(decoded2, sort_keys=True, indent=4)
#
#
#     try:
#         items = []
#         for sr in decoded2['Response']['ListOfServiceRequest']['ServiceRequest']:
#             Address = sr['SRAddress']
#             if sr['Latitude'] != '':
#                 y = sr['Latitude']
#             if sr['Longitude'] != '':
#                 x = sr['Longitude']
#             if sr['Latitude'] == '':
#                 blanky = sr['Latitude']
#             if sr['Longitude'] == '':
#                 blankx= sr['Longitude']
#                 print blanky
#                 print blankx
#             ReasonCode = ''
#             ResolutionCode = ''
#             SRNumber = sr['SRNumber']
#             NewContactFirstName = sr['NewContactFirstName']
#             NewContactLastName = sr['NewContactLastName']
#             Created_FirstName = sr['LA311UpdatedByFirstName']
#             Created_LastName = sr ['LA311UpdatedByLastName']
#             FirstName = sr['FirstName']
#             LastName = sr['LastName']
#             if sr['ResolutionCode'] == '':
#                 ResolutionCode =  sr['ResolutionCode']
#             if sr ['ReasonCode'] == '':
#                 ReasonCode = sr['ReasonCode']
#             aReasonCode = sr['ReasonCode']
#             HomePhone = sr['HomePhone']
#             CreatedDate = sr['CreatedDate']
#             UpdatedDate = sr['UpdatedDate']
#             BulkyItem = sr['ListOfLa311BulkyItem']
#             ElectronicWaste = sr['ListOfLa311ElectronicWaste']
#             MoveInMoveOut = sr['ListOfLa311MoveInMoveOut']
#             IllegalDumping = sr['ListOfLa311IllegalDumpingPickup']
#             BrushItems = sr['ListOfLa311BrushItemsPickup']
#             MHA = sr['ListOfLa311MetalHouseholdAppliancesPickup']
#             DAR = sr['ListOfLa311DeadAnimalRemoval']
#             Manual = sr['ListOfLa311ManualPickup']
#             if sr['ServiceDate'] !=  ' ':
#                 ServiceDate=  sr['ServiceDate']
#             try:
#                 if sr['ListOfLa311GisLayer'] != '{},':
#                     GISLayer = sr['ListOfLa311GisLayer']['La311GisLayer'][0]['DistrictName']
#             except Exception:
#                 pass
#             NeighborhHoodCouncil = sr['SRNeighborhoodCouncilName']
#             ServiceNotes = sr['ListOfLa311ServiceRequestNotes']
#             SCCatDesc = ' '
#             UpdatedDate = datetime.datetime.strptime(UpdatedDate, "%m/%d/%Y %H:%M:%S")
#
#             if arcpy.Exists(fc):
#                     arcpy.Delete_management(fc)
#
#             if 'La311ServiceRequestNotes' in ServiceNotes:
#                 try:
#                     k_comment = ServiceNotes['La311ServiceRequestNotes'][0]['Comment']
#                 except IndexError:
#                     k_comment = ' '
#                 print k_comment
#
            if 'La311MetalHouseholdAppliancesPickup' in MHA:
                try:
                    k_mha_count_1 = MHA['La311MetalHouseholdAppliancesPickup'][0]['HouseHoldItemCount']
                except IndexError:
                    k_mha_count_1 = ' '
                print k_mha_count_1

                try:
                     k_mha_count_2 = MHA['La311MetalHouseholdAppliancesPickup'][1]['HouseHoldItemCount']
                except IndexError:
                     k_mha_count_2 = ' '
                print  k_mha_count_2

                try:
                    k_mha_count_3 = MHA['La311MetalHouseholdAppliancesPickup'][2]['HouseHoldItemCount']
                except IndexError:
                    k_mha_count_3 = ' '
                print k_mha_count_3

                try:
                    k_mha_count_4 = MHA['La311MetalHouseholdAppliancesPickup'][3]['HouseHoldItemCount']
                except IndexError:
                    k_mha_count_4 = ' '
                print k_mha_count_4

                try:
                     k_mha_count_5 = MHA['La311MetalHouseholdAppliancesPickup'][4]['HouseHoldItemCount']
                except IndexError:
                     k_mha_count_5 = ' '
                print  k_mha_count_5

                try:
                    k_dar_count_6 = MHA['La311MetalHouseholdAppliancesPickup'][5]['HouseHoldItemCount']
                except IndexError:
                    k_dar_count_6 = ' '
                print k_dar_count_6

                try:
                    k_mha_count_7 = MHA['La311MetalHouseholdAppliancesPickup'][6]['HouseHoldItemCount']
                except IndexError:
                    k_mha_count_7 = ' '
                print k_mha_count_7

                try:
                   k_mha_count_8 = MHA['La311MetalHouseholdAppliancesPickup'][7]['DACItemCount']
                except IndexError:
                    k_mha_count_8 = ' '
                print k_mha_count_8

                try:
                    k_mha_count_9 = MHA['La311MetalHouseholdAppliancesPickup'][8]['DACItemCount']
                except IndexError:
                    k_mha_count_9 = ' '
                print k_mha_count_9

                try:
                    k_mha_count_10 = MHA['La311MetalHouseholdAppliancesPickup'][9]['DACItemCount']
                except IndexError:
                    k_mha_count_10 = ' '
                print k_mha_count_10

                try:
                    k_mha_item_1 = MHA['La311MetalHouseholdAppliancesPickup'][0]['HouseholdItem']
                except IndexError:
                    k_mha_item_1 = ' '
                print k_mha_item_1


                try:
                    k_mha_item_2 = MHA['La311MetalHouseholdAppliancesPickup'][1]['HouseholdItem']
                except IndexError:
                    k_mha_item_2 = ' '
                print k_mha_item_2


                try:
                   k_mha_item_3 = MHA['La311MetalHouseholdAppliancesPickup'][2]['HouseholdItem']
                except IndexError:
                    k_mha_item_3 = ' '
                print k_mha_item_3


                try:
                    k_mha_item_4 = MHA['La311MetalHouseholdAppliancesPickup'][3]['HouseholdItem']
                except IndexError:
                    k_mha_item_4 = ' '
                print k_mha_item_4


                try:
                    k_mha_item_5 = MHA['La311MetalHouseholdAppliancesPickup'][4]['HouseholdItem']
                except IndexError:
                    k_mha_item_5 = ' '
                print k_mha_item_5

                try:
                    k_mha_item_6 = MHA['La311MetalHouseholdAppliancesPickup'][5]['HouseholdItem']
                except IndexError:
                    k_mha_item_6 = ' '
                print k_mha_item_6


                try:
                    k_mha_item_7 = MHA['La311MetalHouseholdAppliancesPickup'][6]['HouseholdItem']
                except IndexError:
                    k_mha_item_7 = ' '
                print k_mha_item_7



                try:
                    k_mha_item_8 = MHA['La311MetalHouseholdAppliancesPickup'][7]['HouseholdItem']
                except IndexError:
                    k_mha_item_8 = ' '
                print k_mha_item_8



                try:
                    k_mha_item_9 = MHA['La311MetalHouseholdAppliancesPickup'][8]['HouseholdItem']
                except IndexError:
                    k_mha_item_9 = ' '
                print k_mha_item_9


                try:
                    k_mha_item_10 = MHA['La311MetalHouseholdAppliancesPickup'][9]['HouseholdItem']
                except IndexError:
                    k_mha_item_10 = ' '
                print k_mha_item_10


                try:
                    k_mha_location_1 = MHA['La311MetalHouseholdAppliancesPickup'][0]['CollectionLocation']
                except IndexError:
                    k_mha_location_1 = ' '
                print k_mha_location_1


                try:
                    k_mha_location_2 = MHA['La311MetalHouseholdAppliancesPickup'][1]['CollectionLocation']
                except IndexError:
                    k_mha_location_2 = ' '
                print k_mha_location_2

                try:
                    k_mha_location_3 = MHA['La311MetalHouseholdAppliancesPickup'][2]['CollectionLocation']
                except IndexError:
                    k_mha_location_3 = ' '
                print k_mha_location_3

                try:
                    k_mha_location_4 = MHA['La311MetalHouseholdAppliancesPickup'][3]['CollectionLocation']
                except IndexError:
                    k_mha_location_4 = ' '
                print k_mha_location_4

                try:
                    k_mha_location_5 = MHA['La311MetalHouseholdAppliancesPickup'][4]['CollectionLocation']
                except IndexError:
                    k_mha_location_5 = ' '
                print k_mha_location_5


                try:
                    k_mha_location_6 = MHA['La311MetalHouseholdAppliancesPickup'][5]['CollectionLocation']
                except IndexError:
                    k_mha_location_6 = ' '
                print k_mha_location_6



                try:
                    k_mha_location_7 = MHA['La311MetalHouseholdAppliancesPickup'][6]['CollectionLocation']
                except IndexError:
                    k_mha_location_7 = ' '
                print k_mha_location_7



                try:
                    k_mha_location_8 = MHA['La311MetalHouseholdAppliancesPickup'][7]['CollectionLocation']
                except IndexError:
                    k_mha_location_8 = ' '
                print k_mha_location_8



                try:
                    k_mha_location_9 = MHA['La311MetalHouseholdAppliancesPickup'][8]['CollectionLocation']
                except IndexError:
                    k_mha_location_9 = ' '
                print k_mha_location_9


                try:
                    k_mha_location_10 = MHA['La311MetalHouseholdAppliancesPickup'][9]['CollectionLocation']
                except IndexError:
                    k_mha_location_10 = ' '
                print k_mha_location_10


                try:
                    k_mha_name_1 = MHA['La311MetalHouseholdAppliancesPickup'][0]['Name']
                except IndexError:
                    k_dar_name_1 = ' '
                print k_dar_name_1



                try:
                    k_mha_name_2 = MHA['La311MetalHouseholdAppliancesPickup'][1]['Name']
                except IndexError:
                    k_mha_name_2 = ' '
                print k_mha_name_2



                try:
                    k_mha_name_3 = MHA['La311MetalHouseholdAppliancesPickup'][2]['Name']
                except IndexError:
                    k_mha_name_3 = ' '
                print k_mha_name_3


                try:
                    k_mha_name_4 = MHA['La311MetalHouseholdAppliancesPickup'][3]['Name']
                except IndexError:
                    k_mha_name_4 = ' '
                print k_mha_name_4

                try:
                    k_mha_name_5 = MHA['La311MetalHouseholdAppliancesPickup'][4]['Name']
                except IndexError:
                    k_mha_name_5 = ' '
                print k_mha_name_5

                try:
                    k_mha_name_6 = MHA['La311MetalHouseholdAppliancesPickup'][5]['Name']
                except IndexError:
                    k_mha_name_6 = ' '
                print k_mha_name_6


                try:
                    k_mha_name_7 = MHA['La311MetalHouseholdAppliancesPickup'][6]['Name']
                except IndexError:
                    k_mha_name_7 = ' '
                print k_mha_name_7



                try:
                    k_mha_name_8 = MHA['La311MetalHouseholdAppliancesPickup'][7]['Name']
                except IndexError:
                    k_mha_name_8 = ' '
                print k_mha_name_8


                try:
                    k_mha_name_9 = MHA['La311MetalHouseholdAppliancesPickup'][8]['Name']
                except IndexError:
                    k_mha_name_9 = ' '
                print k_mha_name_9



                try:
                    k_mha_name_10 = MHA['La311MetalHouseholdAppliancesPickup'][9]['Name']
                except IndexError:
                    k_mha_name_10 = ' '
                print k_mha_name_10



                if MHA['La311MetalHouseholdAppliancesPickup'][0]['Type'] == 'Metal/Household Appliances':
                    k_mha_comm_1 = 6
#
#                 date_object = ' '
#                 created_object = ' '
#
#                 try:
#                     date_object = datetime.datetime.strptime(ServiceDate, "%m/%d/%Y %H:%M:%S")
#                     created_object = datetime.datetime.strptime(CreatedDate, "%m/%d/%Y %H:%M:%S")
#                 except Exception:
#                     pass
#
#
#
#                 FullName = NewContactFirstName  +  " " + NewContactLastName
#                 if FullName  == ' ':
#                     FullName = 'Not Specified'
#
#                 if created_object == ' ':
#                     created_object = UpdatedDate
#
#
#                 if date_object == ' ':
#                     date_object = '07/01/2015'
#
#                 CreatedBy = Created_FirstName + " " + Created_LastName
#                 Prior_Resolution_Code =  ' '
#
#                 dt = np.dtype([('Address', 'U40'),
#                     ('Y_CoordShape', '<f8'),
#                     ('X_CoordShape', '<f8'),
#                     ('Y_COR', '<f8'),
#                     ('X_COR', '<f8'),
#                     ('ReasonCode','U128'),
#                     ('NUMBERCYLA', 'U40'),
#                     ('SRNumber', 'U40'),
#                     ('Name', 'U40'),
#                     ('RESOLUTION_CODE','U128'),
#                    ('HOME_PHONE', 'U40'),
#                     ('OPEN_TIME', 'U128'),
#                     ('OPENED_BY', 'U128'),
#                     ('UpdatedDate', 'U128'),
#                     ('ItemDesc_1', 'U128'),
#                     ('ItemDesc_2', 'U128'),
#                     ('ItemDesc_3', 'U128'),
#                     ('ItemDesc_4','U128'),
#                     ('ItemDesc_5', 'U128'),
#                     ('ItemDesc_6', 'U128'),
#                     ('ItemDesc_7', 'U128'),
#                     ('ItemDesc_8', 'U128'),
#                     ('ItemDesc_9', 'U128'),
#                     ('ItemDesc_10', 'U128'),
#                     ('Category', 'U128'),
#                      ('SCHED_DATE', 'U128'),
#                     ('CYLA_DISTRICT ', 'U128'),
#                 ('BRIEF_DESCRIPTION', 'U128'),
#                     ('Comment', 'U128'),
#                     ('Prior_RESOLUTION_CODE', 'U128'),
#                     ('UID1', 'U128'),
#                     ('UID2', 'U128'),
#                     ('UID3', 'U128'),
#                     ('UID4', 'U128'),
#                     ('UID5', 'U128'),
#                     ('UID6', 'U128'),
#                     ('UID7', 'U128'),
#                     ('UID8', 'U128'),
#                     ('UID9', 'U128'),
#                     ('UID10', 'U128'),
#                     ('ItemLoc_1', 'U128'),
#                     ('ItemLoc_2', 'U128'),
#                     ('ItemLoc_3', 'U128'),
#                     ('ItemLoc_4', 'U128'),
#                     ('ItemLoc_5', 'U128'),
#                     ('ItemLoc_6', 'U128'),
#                     ('ItemLoc_7', 'U128'),
#                     ('ItemLoc_8', 'U128'),
#                     ('ItemLoc_9', 'U128'),
#                     ('ItemLoc_10', 'U128'),
#
#
#
#                 ])
#                 if k_dar_comm_1 == 6:
#                     items.append((Address,
#                              x,
#                             y,
#                               x,
#                               y,
#                               ReasonCode,
#                               SRNumber,
#                              SRNumber,
#                              FullName,
#                               ResolutionCode,
#                               HomePhone,
#                               created_object,
#                              CreatedBy,
#                               UpdatedDate,
#                            k_mha_name_1,
#                             k_mha_name_2,
#                             k_mha_name_3,
#                             k_mha_name_4,
#                             k_mha_name_5,
#                             k_mha_name_6,
#                             k_mha_name_7,
#                             k_mha_name_8,
#                             k_mha_name_9,
#                             k_mha_name_10,
#                             k_mha_location_1,
#                             k_mha_location_2,
#                             k_mha_location_3,
#                             k_mha_location_4,
#                             k_mha_location_5,
#                             k_mha_location_6,
#                             k_mha_location_7,
#                             k_mha_location_8,
#                             k_mha_location_9,
#                             k_mha_location_10,
#                               date_object,
#                              GISLayer,
#                              k_mha_location_1 +  k_mha_count_1 + ',' + k_mha_item_1 + ';' + k_mha_count_2 + ',' + k_mha_item_2 + ';' + k_mha_count_3 + ',' + k_mha_item_3 + ';' + k_mha_count_4 + ',' + k_mha_item_4 + ';' + k_mha_count_5 + ',' + k_mha_item_5 + ';' + k_mha_count_6+ ',' + k_mha_item_6 + ';' + k_mha_count_7 + ',' + k_mha_item_7 + ';' + k_mha_count_8 + ',' + k_mha_item_8 + ';' + k_mha_count_9 + ',' + k_mha_item_9 + ';' + k_mha_count_10 + ',' + k_mha_item_10,
#                             k_comment,
#                              Prior_Resolution_Code,
#                             k_mha_name_1,
#                             k_mha_name_2,
#                             k_mha_name_3,
#                             k_mha_name_4,
#                             k_mha_name_5,
#                             k_mha_name_6,
#                             k_mha_name_7,
#                             k_mha_name_8,
#                             k_mha_name_9,
#                             k_mha_name_10,
#                             k_mha_location_1,
#                             k_mha_location_2,
#                             k_mha_location_3,
#                             k_mha_location_4,
#                             k_mha_location_5,
#                             k_mha_location_6,
#                             k_mha_location_7,
#                             k_mha_location_8,
#                             k_mha_location_9,
#                             k_mha_location_10,
#
#
#                             ))
#
#             arr = np.array(items,dtype=dt)
#
#             NumPyArray = arcpy.da.NumPyArrayToFeatureClass(arr, fc, ['Y_CoordShape', 'X_CoordShape'], spatial_ref)
#
#             arcpy.AddField_management(fc, "SCCatDesc", "TEXT")
#
#             codeblock = """def findTwoLetter(Category):
#                 output = None
#                 if Category == "1":
#                     output = "SBI"
#                 if Category == "13" :
#                     output = "SMB"
#                 if Category == "4":
#                     output = "SBE"
#                 if  Category =="10":
#                     output = "ADW"
#                 if Category == "8":
#                     output = "DAC"
#                 if Category == "6":
#                     output = "SBW"
#                 if Category == "2":
#                     output = "SOT"
#                 return output"""
#
#             ShortCodeExpression = "findTwoLetter(!Category!)"
#
#             arcpy.CalculateField_management(fc, "SCCatDesc", ShortCodeExpression, "PYTHON_9.3", codeblock)
#
#
#             arcpy.Append_management(fc, appendClass, "NO_TEST")
#
#             print "success is inevitable for dar"
#     except KeyError, e:
#         print "refunction dar", lasandarquery()
#     except IndexError, e:
#         print 'I got an IndexError - reason "%s"' % str(e)
# schedule.every(2).minutes.do(lasanbulkyquery)
# schedule.every(2).minutes.do(lasanewastequery)
# schedule.every(2).minutes.do(lasandarquery)
# schedule.every(2).minutes.do(lasanmhaquery)
while True:
    schedule.run_pending()
    time.sleep(1)

##############Start METAL HOUSEHOLD APPLIANCES################






































































































































































































































        # selection = 'OPEN_TIME >= DATEADD(minute, -10,  GETDATE())'
        #
        # if arcpy.Exists(history_table):
        #     arcpy.Delete_management(history_table)

        # copyFC = arcpy.FeatureClassToFeatureClass_conversion(fc, gdb, 'MYLA311Test_Env', selection)











