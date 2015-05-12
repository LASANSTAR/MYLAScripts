__author__ = 'Administrator'
#JSON Web-Service to Enterprise Geodatabase
#By Geoffrey West
#SANSTAR/SOS City of Los Angeles BOS

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
url2 = "https://myla311.lacity.org/myla311router/mylasrbe/1/SANQuerySR"
headers2 = {'Content-type': 'text/plain', 'Accept': '/'}

r2 = requests.post(url2, data=data2, headers=headers2)
decoded2 = json.loads(r2.text)
print json.dumps(decoded2, sort_keys=True, indent=4)

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
    SRAddress = [sr['SRAddress']]
    y = [sr['Latitude']]
    lat = contains '.'
    res = [b for b in y if lat in b]
    print res
    x = [sr['Longitude']]
    ReasonCode = sr['ReasonCode']
    SRNumber = sr['SRNumber']
    FirstName = sr['FirstName']
    LastName = sr['LastName']
    ResolutionCode = sr['ResolutionCode']
    HomePhone = sr['HomePhone']
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



#
#     for sr in ElectronicWaste:
#             for ewastelocation in ElectronicWaste['La311ElectronicWaste']:
#                                     locationewaste =  ewastelocation['CollectionLocation']
#                                     print locationewaste
#     for sr in ElectronicWaste:
#             for ewastetype in ElectronicWaste['La311ElectronicWaste']:
#                                     itemEwaste =  ewastetype['ElectronicWestType']
#     for sr in ElectronicWaste:
#             for ewastecount in ElectronicWaste['La311ElectronicWaste']:
#                                     countEwaste =  ewastecount['ItemCount']
#     for sr in ElectronicWaste:
#             for typeewaste in ElectronicWaste['La311ElectronicWaste']:
#                                     TypeEwaste =  typeewaste['Type']
#     for sr in BulkyItem:
#             for bulkycount in BulkyItem['BulkyItem']:
#                                     countBulky =  bulkycount['BulkyItemCount']
#     for sr in BulkyItem:
#             for bulkyitem in BulkyItem['BulkyItem']:
#                                     itemBulky =  bulkyitem['BulkyItemType']
#     for sr in BulkyItem:
#             for bulkylocation in BulkyItem['BulkyItem']:
#                                     locationbulky =  bulkylocation['CollectionLocation']
#     for sr in BulkyItem:
#             for bulkytype in BulkyItem['BulkyItem']:
#                                     typebulky =  bulkytype['Type']
#     for sr in MHA:
#             for mhalocation in MHA['La311MetalHouseholdAppliancesPickup']:
#                                     locationmha =  mhalocation['CollectionLocation']
#     for sr in MHA:
#             for mhacount in MHA['La311MetalHouseholdAppliancesPickup']:
#                                     countmha =  mhacount['HouseHoldItemCount']
#     for sr in MHA:
#             for mhaitem in MHA['La311MetalHouseholdAppliancesPickup']:
#                                     itemmha =  mhaitem['HouseholdItem']
#     for sr in MHA:
#             for mhatype in MHA['La311MetalHouseholdAppliancesPickup']:
#                                     typemha =  mhatype['Type']
#     for sr in ServiceNotComplete:
#             for missedservice in ServiceNotComplete['La311ServiceNotComplete']:
#                                     servicemissed =  missedservice['MissedCollectionService']
#
#     for sr in DeadAnimalRemoval:
#             for dactype in DeadAnimalRemoval['DeadAnimalRemoval']:
#                                     DARTYPE =  dactype['Type']
#     for sr in DeadAnimalRemoval:
#             for darlocation in DeadAnimalRemoval['DeadAnimalRemoval']:
#                                     locationdar =  darlocation['CollectionLocation']
#     for sr in DeadAnimalRemoval:
#             for darcount in DeadAnimalRemoval['DeadAnimalRemoval']:
#                                     countdar =  darcount['DACItemCount']
#     for sr in DeadAnimalRemoval:
#             for dartype in DeadAnimalRemoval['DeadAnimalRemoval']:
#                                     typedac =  dartype['DACType']
#     for sr in BrushItems:
#             for brlocation in BrushItems['La311BrushItemsPickup']:
#                                     locationbrush =  brlocation['CollectionLocation']
#
#     for sr in BrushItems:
#             for brtype in BrushItems['La311BrushItemsPickup']:
#                                     typebrush =  brtype['BrushType']
#
#             for brcount in BrushItems['La311BrushItemsPickup']:
#                                     countbrush =  brcount['BrushTypeCount']
#
#     for sr in BrushItems:
#             for britem in BrushItems['La311BrushItemsPickup']:
#                                     itembr =  britem['Type']
#
#     for sr in MoveInMoveOut:
#             for movelocation in MoveInMoveOut['La311MoveInMoveOut']:
#                                     locationmove =  movelocation['CollectionLocation']
#
#     for sr in MoveInMoveOut:
#             for movetype in MoveInMoveOut["La311MoveInMoveOut"]:
#                                     typemove =  movetype['MoveType']
#
#     for sr in MoveInMoveOut:
#             for movetype in MoveInMoveOut["La311MoveInMoveOut"]:
#                                     MOVETYPE =  movetype['Type']
#                                     print MOVETYPE
#     for sr in MoveInMoveOut:
#             for moveitemcount in MoveInMoveOut["La311MoveInMoveOut":]:
#                                     coutmove =  moveitemcount['ItemCount']
#                                     print countmove
#     for sr in Manual:
#             for manuallocation in Manual["La311ManualPickup":]:
#                                     locationmanual =  manuallocation['collectionLocation']
#                                     print locationmanual
#     for sr in Manual:
#             for manualpickitem in Manual["La311ManualPickup":]:
#                                     itempickmanual =  manualpickitem['ManualPickupItem']
#                                     print itempickmanual
#     for sr in Manual:
#             for manualcount in Manual["La311ManualPickup"]:
#                                     countmanual =  manualcount['ItemCount']
#                                     print countmanual
#     for sr in Manual:
#             for typemanual in Manual["La311ManualPickup"]:
#                                     MANUALTYPE =  typemanual['Type']
#                                     print MANUALTYPE
#     for sr in IllegalDumping:
#             for illegallocaltion in IllegalDumping["La311IllegalDumpingPickup"]:
#                                     locationillegal =  illegallocaltion['CollectionLocation']
#                                     print locationillegal
#     for sr in IllegalDumping:
#             for illegaltype in IllegalDumping["La311IllegalDumpingPickup"]:
#                                     typeillegal =  illegaltype['Type']
#                                     print typeillegal
#
#
#     outputobjects= int(decoded2['Response']['NumOutputObjects'])
#     print outputobjects
#
#     dt = np.dtype([('Address', 'U40'),
#         ('LatitudeShape', '<f8'),
#         ('LongitudeShape', '<f8'),
#         ('Latitude', '<f8'),
#         ('Longitude', '<f8'),
#         ('ReasonCode','U128'),
#         ('SRNumber', 'U40'),
#         ('FirstName', 'U40'),
#        ('LastName', 'U40'),
#         ('ResolutionCode','U128'),
#        ('HomePhone', 'U40'),
#         ('CreatedDate', 'U128'),
#         ('UpdatedDate', 'U128'),
#
#         ])
#
#
#     items.append((SRAddress,
#                   LatitudeWrite,
#                  LongitudeWrite,
#                   LatitudeWrite,
#                   LongitudeWrite,
#                   ReasonCode,
#                   SRNumber,
#                  FirstName,
#                   LastName,
#                   ResolutionCode,
#                   HomePhone,
#                   CreatedDate,
#                   UpdatedDate,
#
#
#
#     ))
#
#
#
#
#
#     sr = arcpy.SpatialReference(4326)
# arr = np.array(items,dtype=dt)
# NumPyArray = arcpy.da.NumPyArrayToFeatureClass(arr, fc, ['longitudeshape', 'latitudeshape'], sr)
# print "success"
# #
                    # arcpy.AddField_management(fc, "Create_Date", "DATE", '', 255)
                    # arcpy.AddField_management(fc, "Update_Date", "DATE", '', 255)
                    # arcpy.AddField_management(fc, "dateAndTime", "DATE", '', 255)
                    #
                    # CreatedDate = "Create_Date"
                    # UpdatedDate = "Update_Date"
                    # DateAndTime = "dateAndTime"
                    #
                    # cursor = arcpy.UpdateCursor(fc)
                    # for row in cursor:
                    #     row.setValue(CreatedDate, row.getValue("CreatedDate"))
                    # cursor.updateRow(row)
                    #
                    # cursor = arcpy.UpdateCursor(fc)
                    # for row in cursor:
                    #     row.setValue(UpdatedDate, row.getValue("UpdatedDate"))
                    # cursor.updateRow(row)
                    #
                    # cursor = arcpy.UpdateCursor(fc)
                    # for row in cursor:
                    #     row.setValue(DateAndTime, row.getValue("jsonquerydate"))
                    # cursor.updateRow(row)
                    #
                    #
                    # strResult += "3DI to SANSTAR is successful for" + ' ' + str(Start)
                    # success = True or False


                    # rows = arcpy.InsertCursor(aTable)
                    #
                    # for x in xrange(0, outputobjects):
                    #     row = rows.newRow()
                    # row.setValue("Success", 'YES')
                    # row.setValue("Fail", 'NO')
                    # row.setValue("Time", Start)
                    # rows.insertRow(row)
                    #
                    # txtFile = open('C:\logs\sanstar_messages.txt', "a")
                    # txtFile.write("service update is successful.\n" + str(Start))
                    # txtFile.write("\n")
                    # txtFile.write("service update is successful.\n")
                    # txtFile.write("\n")
                    # txtFile.close()

    #             else:
    #                 print "this works"
    #                 print json.dumps(decoded2, sort_keys=True, indent=4)
    #
    #         except:
    #             print "this does not work"
    # except arcpy.ExecuteError:
    #     strResult += arcpy.GetMessages()

        # arcpy.AddMessage(strResult)

# except:
#     rows = arcpy.InsertCursor(aTable)
#     outputobjects= int(decoded2['Response']['NumOutputObjects'])
#     for x in xrange(0, outputobjects):
#         row = rows.newRow()
#     row.setValue("Success", 'NO')
#     row.setValue("Fail", 'YES')
#     row.setValue("Time", Start)
#     rows.insertRow(row)
#     logger.exception("Something has gone wrong!")
#     print "the try has failed!"
#
#     try:
#         print "a"
#
#
#         #RESPONSE FOR 10 minutes




#     except:
#         logger.exception("This works for the nested exception and fail has been logged in History_Table")
#         rows = arcpy.InsertCursor(aTable)
#
#     for x in xrange(0, outputobjects):
#         row = rows.newRow()
#     row.setValue("Success", 'NO')
#     row.setValue("Fail", 'YES')
#     row.setValue("Time", Start)
#     rows.insertRow(row)
#
# sendResultEmail(strResult, success)
# print 'It took', time.time()-start, 'seconds.'


