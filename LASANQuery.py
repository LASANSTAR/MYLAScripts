__author__ = 'Administrator'
#JSON Web-Service to Enterprise Geodatabase
#By Geoffrey West
#SANSTAR/SOS City of Los Angeles BOS

import json
import jsonpickle
import pyodbc 
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


# FN_JsonFile = r'C:\Projects\Trunk\LA2015\data\Query_Request.json'
K_SRAddress='SRAddress'
K_SRNumber = 'SRNumber'
K_ListOfServiceRequest='ListOfServiceRequest'
K_Latitude = 'Latitude'
K_Longitude = 'Longitude'
K_ResolutionCode = 'ResolutionCode'
K_HomePhone = 'HomePhone'
K_FirstName = 'FirstName'
K_LastName = 'LastName'
K_CreatedDate = 'CreatedDate'
K_UpdatedDate = 'UpdatedDate'
K_BulkyItem = 'ListOfLa311BulkyItem'
K_EWasteItem = 'ListOfLa311ElectronicWaste'
K_MoveInMoveOut = 'ListOfLa311MoveInMoveOut'
K_IllegalDumping = 'ListOfLa311IllegalDumpingPickup'
K_ServiceNotComplete = 'ServiceNotComplete'
K_BrushItems = 'ListOfLa311BrushItemsPickup'
K_Containers = 'ListOfLa311Containers'
K_MHA = 'ListOfLa311MetalHouseholdAppliancesPickup'
K_DAR = 'ListOfLa311DeadAnimalRemoval'
K_MANUAL = 'ListOfLa311ManualPickup'
K_ReasonCode = 'K_ReasonCode'





def trace():
    import traceback, inspect
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    # script name + line number
    line = tbinfo.split(", ")[1]
    filename = inspect.getfile(inspect.currentframe())
    # Get Python syntax error
    synerror = traceback.format_exc().splitlines()[-1]
    return line, filename, synerror


def GetThisDir():
    import inspect 
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))     

class TlsSMTPHandler(logging.handlers.SMTPHandler):
    def emit(self, record):
        """
        Emit a record.

        Format the record and send it to the specified addressees.
        """
        try:
            import smtplib
            import string # for tls add this line
            try:
                from email.utils import formatdate
            except ImportError:
                formatdate = self.date_time
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port)
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
                            self.fromaddr,
                            string.join(self.toaddrs, ","),
                            self.getSubject(record),
                            formatdate(), msg)
            if self.username:
                smtp.ehlo() # for tls add this line
                smtp.starttls() # for tls add this line
                smtp.ehlo() # for tls add this line
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


def sendResultEmail(msgContents, success_TF):
    '''sendResultEmail(msgContents, success_TF)
    This is the module that does the sending - you should only need to edit the top four active lines'''
    to = 'geoffreywestgis@gmail.com'
    send_username = 'geoffreywestgis@gmail.com'
    send_password = 'pythonheat1' # warning - will just be an unencrypted string - so be careful not to leave this file lying around!
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)


    if success_TF:
        subject = 'Arcpy testing results: script SUCCESS.'
    else:
        subject = 'Arcpy testing results: script FAILURE.'

    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(send_username, send_password)

    header = 'To:' + to + '\n' + 'From: ' + send_username + '\n' + 'Subject:' + subject + '\n'

    msg = header + '\nArcpy results: Listed Below! \n\t' + msgContents + '\n'

    smtpserver.sendmail(send_username, to, msg)

    arcpy.AddMessage('This is a good thing!!')

    smtpserver.close()
    success = True or False


def doWork(fc, aTable):
    logger = logging.getLogger()
    gm = TlsSMTPHandler(("smtp.gmail.com", 587), 'geoffreywestgis@gmail.com', ['geoffreywestgis@gmail.com'], 'Error found!', ('geoffreywestgis@gmail.com', 'pythonheat1'))
    gm.setLevel(logging.ERROR)
    logger.addHandler(gm)
    try:
        strResult = ''
        arcpy.SetLogHistory(True)
        start = time.time()
        Start = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        msgFolder = "C:/logs/"
        sender = "geoffreywestgis@gmail.com"
        recipient = "geoffreywestgis@gmail.com"
        #fc2 = "C:\Projects\Trunk\LA2015\data\ConnectionToLA2015Atzye8.sde\LA2015.SDE.Py_fc"
        #fc2 = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311"
        fc = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to localhost_ServiceRequest.sde\ServiceRequest.DBO.MYLA311AppendFeature"
        aTable = "C:\Users\GeoffreyWest\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\ServiceRequest.sde\ServiceRequest.DBO.History_Table_"
        connect_timeout = 5
        f2 =open('C:\Users\GeoffreyWest\Desktop\Request.json')
        f2 =open(FN_JsonFile)
        data2 = jsonpickle.decode((f2.read()))

        Start = datetime.datetime.now()
        DD = datetime.timedelta(minutes=5)
        earlier = Start - DD
        earlier_str = earlier.strftime('X%m/%d/%Y %H:%M:%S').replace('X0','X').replace('X','')
        #
        # for datatime in data2:
        #     DataTime = data2["SRData"]['LastUpdatedDate'] = str(earlier_str)
        data2 = jsonpickle.encode(data2)
        #print data2
        url2 = "https://myla311.lacity.org/myla311router/mylasrbe/1/SANQuerySR"
        headers2 = {'Content-type': 'text/plain', 'Accept': '/'}
        r2 = requests.post(url2, data=data2, headers=headers2)
        decoded2 = json.loads(r2.text)
        print json.dumps(decoded2, sort_keys=True, indent=4)

             
        Start = datetime.datetime.now()
        i = 5
        i2= 10
        now_minus_5 = Start - datetime.timedelta(minutes =i)
        now_minus_10 = Start - datetime.timedelta(minutes =i2)
        try:
            #if arcpy.Exists(fc):
            #    arcpy.Delete_management(fc)
            try:
               r2
            except requests.exceptions.ConnectTimeout as e:
               print "Too slow Mojo!"


            order_fld =  "Time"
            return_flds = ["Time", "SUCCESS"]
            where_str = """Time != DATEADD(minute, -10,  GETDATE()) AND SUCCESS = 'NO'"""
            sql_clause = (None,'ORDER BY {} DESC'.format(order_fld))


            with arcpy.da.SearchCursor(aTable, return_flds, where_clause=where_str, sql_clause=sql_clause) as cursor:
                last_row = cursor.next()
                last_time = last_row[0]
                last_success = last_row[1]
                last_run = datetime.datetime.strptime(last_time,"%m/%d/%Y %H:%M")

                try:
                    if last_run != now_minus_5:
                        print "this block is activated"

                    items = []
                    for sr in decoded2['Response'][K_ListOfServiceRequest]['ServiceRequest']:
                        SRAddress = sr[K_SRAddress]
                        # SRType = sr['SRType']
                        if sr[K_Latitude] != '':
                            y = sr[K_Latitude]
                        if sr[K_Longitude] != '':
                            x = sr[K_Longitude]
                        if sr[K_Latitude] == '':
                            blanky = sr[K_Latitude]
                        if sr[K_Longitude] == '':
                            blankx= sr[K_Longitude]
                            print blanky
                            print blankx
                        ReasonCode = sr[K_ReasonCode]
                        SRNumber = sr[K_SRNumber]
                        FirstName = sr[K_FirstName]
                        LastName = sr[K_LastName]
                        ResolutionCode = sr[K_ResolutionCode]
                        HomePhone = sr[K_HomePhone]
                        CreatedDate = sr[K_CreatedDate]
                        UpdatedDate = sr[K_UpdatedDate]
                        BulkyItem = sr[K_BulkyItem]
                        ElectronicWaste = sr[K_EWasteItem]
                        MoveInMoveOut = sr[K_MoveInMoveOut]
                        IllegalDumping = sr[K_IllegalDumping]
                        ServiceNotComplete = sr[K_ServiceNotComplete]
                        BrushItems = sr[K_BrushItems]
                        Containers = sr[K_Containers]
                        MHA = sr[K_MHA]
                        DeadAnimalRemoval = sr[K_DAR]
                        Manual = sr[K_MANUAL]

                        lServiceRequests = decoded2['Response'][K_ListOfServiceRequest]['ServiceRequest']
                        print lServiceRequests


                        CreatedDate = datetime.datetime.strptime(CreatedDate, "%m/%d/%Y %H:%M:%S")
                        UpdatedDate = datetime.datetime.strptime(UpdatedDate, "%m/%d/%Y %H:%M:%S")

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
                        except:
                            print("No Ewaste items")
                        try:
                            iteminfoewasteprevious = ''
                            countEwastePrevious = ''
                            for sr in ElectronicWaste:
                                for ewastecount in ElectronicWaste['La311ElectronicWaste']:
                                    countEwaste = ewastecount['ItemCount']
                                    if countEwastePrevious != countEwaste:
                                        countEwastePrevious = countEwaste
                                        iteminfoewaste = '{0},  {1}, '.format(countEwastePrevious, itemEwastePrevious)
                                        if iteminfoewasteprevious != iteminfoewaste:
                                            iteminfoewasteprevious = iteminfoewaste

                        except:
                            print "No E-Waste Item Count"

                        try:
                            previousbulkycount = ' '
                            for sr in BulkyItem:
                                for bulkycount in BulkyItem['BulkyItem']:
                                    countBulky =  bulkycount['BulkyItemCount']
                                    if previousbulkycount != countBulky:
                                        previousbulkycount =  countBulky
                        except:
                            print "No bulky counts"

                        try:
                            previousbulkyitem = ''
                            for sr in BulkyItem:
                                for bulkyitem in BulkyItem['BulkyItem']:
                                    itemBulky =  bulkyitem['BulkyItemType']
                                    if previousbulkyitem != itemBulky:
                                        previousbulkyitem = itemBulky
                                        listofdata = ''.join(previousbulkycount + ',' + previousbulkyitem)
                                        BulkyItemInfo += '{0}, {1} '.format (previousbulkycount, previousbulkyitem)
                        except:
                            print "No Bulky Items"

                        try:
                            previousbulkylocation = ''
                            for sr in BulkyItem:
                                for bulkylocation in BulkyItem['BulkyItem']:
                                                        locationbulky =  bulkylocation['CollectionLocation']
                                                        if previousbulkyitem != locationbulky:
                                                            previousbulkylocation = itemBulky
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


                        ItemDesc = BulkyItemInfo + DACItemInfo
                        outputobjects= int(decoded2['Response']['NumOutputObjects'])

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
                                    ('ItemDesc','U128' ),

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


                            sr = arcpy.SpatialReference(4326)
                        arr = np.array(items,dtype=dt)
                        NumPyArray = arcpy.da.NumPyArrayToFeatureClass(arr, fc, ['longitudeshape', 'latitudeshape'], sr)

                        CreatedDate = "Create_Date"
                        UpdatedDate = "Update_Date"
                        DateAndTime = "dateAndTime"

                        arcpy.AddField_management(fc, CreatedDate, "DATE", '', 255)
                        arcpy.AddField_management(fc, UpdatedDate, "DATE", '', 255)
                        arcpy.AddField_management(fc, DateAndTime, "DATE", '', 255)

                        CreatedDate = "Create_Date"
                        UpdatedDate = "Update_Date"
                        DateAndTime = "dateAndTime"

                        cursor =  arcpy.da.UpdateCursor(fc)
                        for row in cursor:
                            row.setValue(CreatedDate, row.getValue("CreatedDate"))
                        cursor.updateRow(row)

                        cursor = arcpy.da.UpdateCursor(fc)
                        for row in cursor:
                            row.setValue(UpdatedDate, row.getValue("UpdatedDate"))
                        cursor.updateRow(row)

                        cursor = arcpy.da.UpdateCursor(fc)
                        for row in cursor:
                            row.setValue(DateAndTime, row.getValue("jsonquerydate"))
                        cursor.updateRow(row)

                        strResult += "3DI to SANSTAR is successful for" + ' ' + str(Start)
                        success = True or False

                        rows = arcpy.da.InsertCursor(aTable)

                        for x in xrange(0, outputobjects):
                            row = rows.newRow()
                        row.setValue("Success", 'YES')
                        row.setValue("Fail", 'NO')
                        row.setValue("Time", Start)
                        rows.insertRow(row)

                        txtFile = open('C:\logs\sanstar_messages.txt', "a")
                        txtFile.write("service update is successful.\n" + str(Start))
                        txtFile.write("\n")
                        txtFile.write("service update is successful.\n")
                        txtFile.write("\n")
                        txtFile.close()

                    else:
                            print "this works"
                            print json.dumps(decoded2, sort_keys=True, indent=4)

                except:
                    print "this does not work"
        except arcpy.ExecuteError:
                strResult += arcpy.GetMessages()
                arcpy.AddMessage(strResult)

    except:
        rows = arcpy.da.InsertCursor(aTable)
        outputobjects= int(decoded2['Response']['NumOutputObjects'])
        for x in xrange(0, outputobjects):
            row = rows.newRow()
        row.setValue("Success", 'NO')
        row.setValue("Fail", 'YES')
        row.setValue("Time", Start)
        rows.insertRow(row)
        logger.exception("Something has gone wrong!")
        print "the try has failed!"

        try:
            print ("a")


        except:
            logger.exception("This works for the nested exception and fail has been logged in History_Table")
            rows = arcpy.InsertCursor(aTable)

        for x in xrange(0, outputobjects):
            row = rows.newRow()
        row.setValue("Success", 'NO')
        row.setValue("Fail", 'YES')
        row.setValue("Time", Start)
        rows.insertRow(row)
    doWork(fc, aTable)
    sendResultEmail(strResult, success)
    print 'It took', time.time()-start, 'seconds.'

