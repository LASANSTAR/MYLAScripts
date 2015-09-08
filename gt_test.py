__author__ = 'GeoffreyWest'




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


arcpy.env.workspace = ""



    # class TlsSMTPHandler(logging.handlers.SMTPHandler):
    #     def emit(self, record):
    #         """
    #         Emit a record.
    #
    #         Format the record and send it to the specified addressees.
    #         """
    #         try:
    #             import smtplib
    #             import string # for tls add this line
    #             try:
    #                 from email.utils import formatdate
    #             except ImportError:
    #                 formatdate = self.date_time
    #             port = self.mailport
    #             if not port:
    #                 port = smtplib.SMTP_PORT
    #             smtp = smtplib.SMTP(self.mailhost, port)
    #             msg = self.format(record)
    #             msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
    #                             self.fromaddr,
    #                             string.join(self.toaddrs, ","),
    #                             self.getSubject(record),
    #                             formatdate(), msg)
    #             if self.username:
    #                 smtp.ehlo() # for tls add this line
    #                 smtp.starttls() # for tls add this line
    #                 smtp.ehlo() # for tls add this line
    #                 smtp.login(self.username, self.password)
    #             smtp.sendmail(self.fromaddr, self.toaddrs, msg)
    #             smtp.quit()
    #         except (KeyboardInterrupt, SystemExit):
    #             raise
    #         except:
    #             self.handleError(record)
    #
    # logger = logging.getLogger()
    #
    # gm = TlsSMTPHandler(("smtp.gmail.com", 587), 'geoffreywestgis@gmail.com', ['geoffreywestgis@gmail.com'], 'Error found!', ('geoffreywestgis@gmail.com', 'pythonheat1'))
    # gm.setLevel(logging.ERROR)
    #
    # logger.addHandler(gm)
    #
    # try:
    #     def sendResultEmail(msgContents, success_TF):
    #             '''sendResultEmail(msgContents, success_TF)
    #             This is the module that does the sending - you should only need to edit the top four active lines'''
    #             to = 'geoffreywestgis@gmail.com'
    #             send_username = 'geoffreywestgis@gmail.com'
    #             send_password = 'pythonheat1' # warning - will just be an unencrypted string - so be careful not to leave this file lying around!
    #             smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    #
    #
    #             if success_TF:
    #                 subject = 'Arcpy testing results: script SUCCESS.'
    #             else:
    #                 subject = 'Arcpy testing results: script FAILURE.'
    #
    #             smtpserver.ehlo()
    #             smtpserver.starttls()
    #             smtpserver.ehlo
    #             smtpserver.login(send_username, send_password)
    #
    #             header = 'To:' + to + '\n' + 'From: ' + send_username + '\n' + 'Subject:' + subject + '\n'
    #
    #             msg = header + '\nArcpy results: Listed Below! \n\t' + msgContents + '\n'
    #
    #             smtpserver.sendmail(send_username, to, msg)
    #
    #             arcpy.AddMessage('This is a good thing!!')
    #
    #             smtpserver.close()
    #
    #     success = False
    #     strResult = ''

arcpy.SetLogHistory(True)
start = time.time()
Start = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
msgFolder = "C:/logs/"
sender = "geoffreywestgis@gmail.com"
recipient = "geoffreywestgis@gmail.com"
fc2 = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311"
aContainerFC = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.ContainerFC"
fc = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311AppendFeature"
aTable = "C:\Users\GeoffreyWest\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\ServiceRequest.sde\ServiceRequest.DBO.History_Table_"
connect_timeout = 5
f2 =open('C:\Users\GeoffreyWest\Desktop\Request.json')
data2 = jsonpickle.decode((f2.read()))

# Start = datetime.datetime.now()
# DD = datetime.timedelta(minutes=5)
# earlier = Start - DD
# earlier_str = earlier.strftime('X%m/%d/%Y %H:%M:%S').replace('X0','X').replace('X','')

# for datatime in data2:
#     DataTime = data2["SRData"]['LastUpdatedDate'] = str(earlier_str)
data2 = jsonpickle.encode(data2)



print data2
url2 = "https://myla311.lacity.org/myla311router/mylasrbe/1/SANQueryPageSR"
headers2 = {'Content-type': 'text/plain', 'Accept': '/'}

r2 = requests.post(url2, data=data2, headers=headers2)
decoded2 = json.loads(r2.text)
    # print json.dumps(decoded2, sort_keys=True, indent=4)


        # Start = datetime.datetime.now()
        # i = 5
        # i2= 10
        # now_minus_5 = Start - datetime.timedelta(minutes =i)
        # now_minus_10 = Start - datetime.timedelta(minutes =i2)


        #begnining of arcpy-email try block
        # try:
if arcpy.Exists(fc):
    arcpy.Delete_management(fc)
try:
    r2
except requests.exceptions.ConnectTimeout as e:
    print "Too slow Mojo!"



    # order_fld =  "Time"
    # return_flds = ["Time", "SUCCESS"]
    # where_str = """Time != DATEADD(minute, -10,  GETDATE()) AND SUCCESS = 'NO'"""
    # sql_clause = (None,'ORDER BY {} DESC'.format(order_fld))
    # last_row = ''
    # with arcpy.da.SearchCursor(aTable, return_flds, where_clause=where_str, sql_clause=sql_clause) as cursor:
    #     last_row = cursor.next()
    #     last_time = last_row[0]
    #     last_success = last_row[1]
    #     last_run = datetime.datetime.strptime(last_time,"%m/%d/%Y %H:%M")
        # print last_row
        # print last_run
        # print last_success
        #
        # print now_minus_5
     # try:
     #    if last_run != now_minus_5:
     #        print "this block is activated"

items = []
for sr in decoded2['Response']['ListOfServiceRequest']['ServiceRequest']:
    SRAddress = sr['SRAddress']
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
    ReasonCode = sr['ReasonCode']
    SRNumber = sr['SRNumber']
    FirstName = sr['FirstName']
    HomePhone = sr['HomePhone']
    LastName = sr['LastName']
    ResolutionCode = sr['ResolutionCode']
    # SRType = sr['SRType']
    # HomePhone = sr['HomePhone']
    CreatedDate = sr['CreatedDate']
    UpdatedDate = sr['UpdatedDate']
    BulkyItem = sr['ListOfLa311BulkyItem']
    ElectronicWaste = sr['ListOfLa311ElectronicWaste']
    MoveInMoveOut = sr['ListOfLa311MoveInMoveOut']
    IllegalDumping = sr['ListOfLa311IllegalDumpingPickup']
    ServiceNotComplete = sr['ListOfLa311ServiceNotComplete']
    BrushItems = sr['ListOfLa311BrushItemsPickup']
    Containers = sr['ListOfLa311Containers']
    MHA = sr['ListOfLa311MetalHouseholdAppliancesPickup']
    DeadAnimalRemoval = sr['ListOfLa311DeadAnimalRemoval']
    Manual = sr['ListOfLa311ManualPickup']
    CreatedDate = datetime.datetime.strptime(CreatedDate, "%m/%d/%Y %H:%M:%S")
    UpdatedDate = datetime.datetime.strptime(UpdatedDate, "%m/%d/%Y %H:%M:%S")
    # print SRType






    ItemDesc =  " "
    BulkyItemInfo = " "
    EwasteItemInfo = " "
    MHAItemInfo = ""
    DACItemInfo = " "
    ServiceInfo = " "

    try:
        locationEwastePrevious = ''
        for sr in ElectronicWaste:
                for ewastelocation in ElectronicWaste['La311ElectronicWaste']:
                                    locationewaste = ewastelocation['CollectionLocation']
                                    if locationEwastePrevious != locationewaste:
                                        locationEwastePrevious = locationewaste


    except:
        print "No Electronic Waste Types"

    try:
        itemEwastePrevious = ''
        for sr in ElectronicWaste:
                for ewastetype in ElectronicWaste['La311ElectronicWaste']:
                                itemEwaste =  ewastetype['ElectronicWestType']
                                if itemEwastePrevious != itemEwaste:
                                    itemEwastePrevious = itemEwaste

                                    iteminfoewasteprevious = ''
                                    countEwastePrevious = ''
                                    for sr in ElectronicWaste:
                                            for ewastecount in ElectronicWaste['La311ElectronicWaste']:
                                                            countEwaste = ewastecount['ItemCount']
                                                            if countEwastePrevious != countEwaste:
                                                                countEwastePrevious = countEwaste
                                                                EwasteItemInfo = '{0},  {1}, '.format(itemEwastePrevious, countEwastePrevious)
                                                                if iteminfoewasteprevious != EwasteItemInfo:
                                                                    iteminfoewasteprevious = EwasteItemInfo
                                                                print EwasteItemInfo


        # previousbulkyitem = ''
        # for sr in BulkyItem:
        #         for bulkyitem in BulkyItem['BulkyItem']:
        #                                 itemBulky =  bulkyitem['BulkyItemType']
        #                                 if previousbulkyitem != itemBulky:
        #                                     previousbulkyitem = itemBulky
        #                                     listofdata = ''.join(previousbulkycount + ',' + previousbulkyitem)
        #                                     BulkyItemInfo += '{0}, {1} '.format (previousbulkyitem, previousbulkycount)
        #                                     print BulkyItemInfo
    except:
        print "No Bulky Items"

    try:
        previousbulkylocation = ''
        for sr in BulkyItem:
            for bulkylocation in BulkyItem['BulkyItem']:
                                    locationbulky =  bulkylocation['CollectionLocation']
                                    if previousbulkyitem != locationbulky:
                                        previousbulkylocation = locationbulky
    except:
        print "No Bulky Location"




    try:

            locationmhaprevious = ''
            for sr in MHA:
                    for mhalocation in MHA['La311MetalHouseholdAppliancesPickup']:
                                            locationmha =  mhalocation['CollectionLocation']
                                            if locationmhaprevious != locationmha:
                                                locationmhaprevious = locationmha
    except:
            print "No Metal Household Appliance Location"


    try:
            countmhaprevious = ''
            for sr in MHA:
                    for mhacount in MHA['La311MetalHouseholdAppliancesPickup']:
                                            countmha =  mhacount['HouseHoldItemCount']
                                            if countmhaprevious != countmha:
                                                countmhaprevious = countmha
                                                MHAItemInfo += '{0}, {1} '.format (previousbulkycount, previousbulkyitem)
    except:
            print"No Household Item Count"

    try:

            itemmhaprevious = ''
            for sr in MHA:
                    for mhaitem in MHA['La311MetalHouseholdAppliancesPickup']:
                                            itemmha =  mhaitem['HouseholdItem']
                                            if itemmhaprevious != itemmha:
                                                itemmhaprevious = itemmha
    except:
            print"No Household Item"


    try:

            previousservicenotcomplete = ''
            for sr in ServiceNotComplete:
                    for missedservice in ServiceNotComplete['La311ServiceNotComplete']:
                                            servicemissed =  missedservice['MissedCollectionService']
                                            if previousservicenotcomplete != servicemissed:
                                                previousservicenotcomplete = servicemissed
                                                ServiceInfo += '{0} '.format (previousservicenotcomplete)
    except:
            print "MissedCollection not Availalble"

    try:
            previousdarlocation = ''
            for sr in DeadAnimalRemoval:
                    for darlocation in DeadAnimalRemoval['DeadAnimalRemoval']:
                                            locationdar =  darlocation['CollectionLocation']
                                            if previousdarlocation != locationdar:
                                                previousdarlocation = locationdar
    except:
            print "DarLocation Not Avaialble"

    try:
            countdacprevious = ''
            for sr in DeadAnimalRemoval:
                    for darcount in DeadAnimalRemoval['DeadAnimalRemoval']:
                                            countdar =  darcount['DACItemCount']
                                            if countdacprevious != countdar:
                                                countdacprevious = countdar
    except:
            print "DacItemCount Not Found"

    try:
            typedacprevious = ''
            for sr in DeadAnimalRemoval:
                    for dartype in DeadAnimalRemoval['DeadAnimalRemoval']:
                                        typedac =  dartype['DACType']
                                        if typedacprevious != typedac:
                                            typedacprevious = typedac
                                            DACItemInfo += '{0}, {1} '.format (typedacprevious, countdacprevious)
                                            print typedacprevious, countdacprevious
    except:
        print "DacType Not Found"

    try:
            previouslocationBrush = ''
            for sr in BrushItems:
                    for brlocation in BrushItems['La311BrushItemsPickup']:
                                            locationbrush =  brlocation['CollectionLocation']
                                            if previouslocationBrush != locationbrush:
                                                previouslocationBrush = locationbrush
    except:
        print "CollectionLocation Brush Items Not Found"

    try:
            previousbrushitem = ''
            for sr in BrushItems:
                for brtype in BrushItems['La311BrushItemsPickup']:
                                        typebrush =  brtype['BrushType']
                                        if previousbrushitem != typebrush:
                                                previousbrushitem = typebrush
    except:
        print ""

    try:
                previousbrushcount = ''
                for brcount in BrushItems['La311BrushItemsPickup']:
                                        countbrush =  brcount['BrushTypeCount']
                                        if previousbrushcount != countbrush:
                                            previousbrushcount = countbrush
    except:
        print " "


    try:
        previousMoveInMoveOutLocation = ''
        for sr in MoveInMoveOut:
                for movelocation in MoveInMoveOut['La311MoveInMoveOut']:
                                        locationmove =  movelocation['CollectionLocation']
                                        if previousMoveInMoveOutLocation != locationmove:
                                            previousMoveInMoveOutLocation = locationmove

    except:
        print " No Collection for move in move out"

    try:
        previousMovetype = ''
        for sr in MoveInMoveOut:
                for movetype in MoveInMoveOut["La311MoveInMoveOut"]:
                                        typemove =  movetype['MoveType']
                                        if previousMovetype != typemove:
                                            previousMovetype = typemove

    except:
        print "Move Type Move in Move Out Not Found"


    try:
        previousmovecount = ''
        for sr in MoveInMoveOut:
                for moveitemcount in MoveInMoveOut["La311MoveInMoveOut":]:
                                        coutmove =  moveitemcount['ItemCount']
                                        if previousmovecount != coutmove:
                                            previousmovecount = coutmove

    except:
        print "No Item Count for Move in Move Out Found"

    try:
        previousmanualLocation = ''
        for sr in Manual:
                for manuallocation in Manual["La311ManualPickup":]:
                                        locationmanual =  manuallocation['collectionLocation']
                                        if previousmanualcount != locationmanual:
                                            previousmanualcount = locationmanual

    except:
        print "ManualLocation not found "
    try:
        previousmanualitem = ' '
        for sr in Manual:
                for manualpickitem in Manual["La311ManualPickup":]:
                                        itempickmanual =  manualpickitem['ManualPickupItem']
                                        if previousmanualitem != itempickmanual:
                                            previousmanualitem = itempickmanual


    except:
        print "There is no manual item pickup"

    try:
        previousmanualiemcount = ''
        for sr in Manual:
                for manualcount in Manual["La311ManualPickup"]:
                                        countmanual =  manualcount['ItemCount']
                                        if previousmanualiemcount != countmanual:
                                            previousmanualiemcount = countmanual
    except:
        print "No Count for manual items"

    try:
        previousillegallocation = ''
        for sr in IllegalDumping:
                for illegallocaltion in IllegalDumping["La311IllegalDumpingPickup"]:
                                        locationillegal =  illegallocaltion['CollectionLocation']
                                        if previousillegallocation != locationillegal:
                                            previousillegallocation = locationillegal
    except:
       print "CollectionLocation for Illegal dumping not available"

    print DACItemInfo
    ItemDesc = BulkyItemInfo + DACItemInfo + MHAItemInfo + EwasteItemInfo + ServiceInfo
    dt = np.dtype([('Address', 'U40'),
        ('LatitudeShape', '<f8'),
        ('LongitudeShape', '<f8'),
        ('Latitude', '<f8'),
        ('Longitude', '<f8'),
        ('ReasonCode','U128'),
        ('SRNumber', 'U40'),
        ('FirstName', 'U40'),
       ('LastName', 'U40'),
        ('ResolutionCode','U128'),
       ('HomePhone', 'U40'),
        ('CreatedDate', 'U128'),
        ('UpdatedDate', 'U128'),
        ('ItemDesc', 'U256',),

        ])


    items.append((SRAddress,
             x,

            y,
              x,
              y,
              ReasonCode,
              SRNumber,
             FirstName,
              LastName,
              ResolutionCode,
              HomePhone,
              CreatedDate,
              UpdatedDate,
              ItemDesc,
            ))

#     sr = arcpy.SpatialReference(4326)
# arr = np.array(items,dtype=dt)
# NumPyArray = arcpy.da.NumPyArrayToFeatureClass(arr, fc, ['longitudeshape', 'latitudeshape'], sr)
#
