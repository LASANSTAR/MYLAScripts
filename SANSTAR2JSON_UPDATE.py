__author__ = 'Administrator'
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

start = time.time()
pyFC = "SO_SC_1"
clauseSBE = "   WHERE Category LIKE '%4%'"
# def printObjects():
#     lResults = []
#     dResult = dict()
#     # Adding additional items  ******************************
#     dResult.setdefault("AddressVerifield", "Y")
#     dResult.setdefault("ReasonCode", "")
#     dResult.setdefault("ResolutionCode", "0")
#     #dResult.setdefault("ListOfLa311ElectronicWaste", dict())
#     l311 = []
#     d = dict()
#     d.setdefault("DriverFirstName", "Geoffrey")
#     d.setdefault("DriverLastName", "West")
#     d.setdefault("ElectronicWasteType", "Cell Phone")
#     d.setdefault("Type", "Electronic Waste")
#     d.setdefault("ItemCount", 2)
#     l311.append(d)
#     d = dict()
#     d.setdefault("DriverFirstName", "Geoffrey")
#     d.setdefault("DriverLastName", "West")
#     d.setdefault("ElectronicWasteType", "Cell Phone")
#     d.setdefault("Type", "Electronic Waste")
#     d.setdefault("ItemCount", 2)
#     l311.append(d)
#     dL311 = dict()
#     dL311.setdefault("La311ElectronicWaste", l311)
#     dResult.setdefault("ListOfLa311ElectronicWaste",dL311)
#     dOthers = dict()
#     #Adding empty dictionaries;
#     dResult.setdefault("ListOfLa311IllegalDumpingPickup", dOthers)
#     dResult.setdefault("ListOfLa311ManualPickup", dOthers)
#     dResult.setdefault("ListOfLa311MetalHouseholdAppliancesPickup", dOthers)
#     dResult.setdefault("ListOfLa311MoveInMoveOut", dOthers)
#     dResult.setdefault("ListOfLa311ServiceNotComplete", dOthers)
#     #Ends of adding additional itmes ****************************************
#     lResults.append({"MetaData": {}, "SRData": dResult})
#
#     sMsg = json.dumps(lResults, sort_keys=True, indent=4)
#     print(sMsg)

if(__name__=='__main__'):
    # sMsg = printObjects()
    # print(sMsg)
    clauseSBE = "WHERE Category LIKE '%4%'"
    connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
    # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
    conn = pyodbc.connect(connstr)
    cursor = conn.cursor()
    FN_SRNumber = "SRNumber"
    lFields = [FN_SRNumber, "RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","last_edited_user"]
    #lFields = ["SRNumber"]
    sFields = ""
    for fld in lFields:
        if(sFields==""):
            sFields = fld
        else:
            sFields = sFields + "," + fld
    #List of the fields you'd like to exclude, like ItemCount for example.
    lFieldsExcluded = ["ITEM_1", "ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1", "RESOLUTION_CODE", "last_edited_user"]

    #sSQL = "SELECT SRNumber FROM {}".format(pyFC)
    sSQL = "SELECT {} FROM {}  {}".format(sFields, pyFC, clauseSBE)
    print sSQL

    cursor.execute(sSQL)
    #columns = [column[0] for column in cursor.description]
    columns = []
    for column in cursor.description:
        if not (column[0] in lFieldsExcluded):
            columns.append(column[0])

try:
    ii = 0
    ewaste_item_1 = ""
    ewaste_item_2 = ""
    ewaste_item_3 = ""
    ewaste_item_4 = ""
    ewaste_item_5 = ""
    ewaste_item_6 = ""
    ewaste_item_7 = ""
    ewaste_item_8 = ""
    ewaste_item_9 = ""
    ewaste_item_10 = ""
    rescode = ""
    reasoncode = ' '
    ewaste_uid = ""
    last_edited_user = " "

    for row in cursor.fetchall():
        lResults = []    #make sure lResults are initiated here
        lValues = []
        for i in range(len(columns)):
            lValues.append( str(row[i]))
        ewaste_item_1 = (str(row[lFields.index("ITEM_1")]))
        ewaste_item_2 = (str(row[lFields.index("ITEM_2")]))
        ewaste_item_3 = (str(row[lFields.index("ITEM_3")]))
        ewaste_item_4 = (str(row[lFields.index("ITEM_4")]))
        ewaste_item_5 = (str(row[lFields.index("ITEM_5")]))
        ewaste_item_5 = (str(row[lFields.index("ITEM_5")]))
        ewaste_item_6 =(str(row[lFields.index("ITEM_6")]))
        ewaste_item_7 = (str(row[lFields.index("ITEM_8")]))
        ewaste_item_8 =(str(row[lFields.index("ITEM_8")]))
        ewaste_item_9 = (str(row[lFields.index("ITEM_9")]))
        ewaste_item_10 = (str(row[lFields.index("ITEM_10")]))
        ewaste_uid = (str(row[lFields.index("UID")]))
        rescode = (str(row[lFields.index("RESOLUTION_CODE")]))
        if rescode == int:
            rescode == reasoncode


        last_edited_user = (str(row[lFields.index("last_edited_user")]))

        #dResult = dict(zip(columns, row))
        dResult = dict(zip(columns, lValues))
        dResult.setdefault("ReasonCode", rescode if rescode.isdigit() else "")
        dResult.setdefault("ResolutionCode",rescode if not rescode.isdigit() else "")

        # Adding additional items  ******************************


        dResult.setdefault("ListOfLa311ElectronicWaste", dict())
        l311 = []
        if  ewaste_item_1  == '7':
            ewaste_item_1 = 'Computers '
        elif  ewaste_item_1 =='1':
             ewaste_item_1 = 'Copiers/Scanners'
        elif  ewaste_item_1 == '2':
             ewaste_item_1 = 'Electronic Equipment'
        elif ewaste_item_1  == "3":
            ewaste_item_1 = 'Laptops/Tablets'
        elif  ewaste_item_1== '4':
             ewaste_item_1  = 'Microwaves'
        elif  ewaste_item_1  == '5':
             ewaste_item_1  = 'Monitors'
        elif  ewaste_item_1  == '6':
            ewaste_item_1  = 'Other Ewaste'
        elif  ewaste_item_1  == '8':
            ewaste_item_1 = 'Printer/Fax Machine'
        elif  ewaste_item_1 == '9':
            ewaste_item_1  = 'Stereo/Radios'
        elif  ewaste_item_1 == '10':
            ewaste_item_1 = 'Stereo/Speakers'
        elif  ewaste_item_1  == '11':
            ewaste_item_1 = 'Telephone'
        elif  ewaste_item_1 == '16':
            ewaste_item_1  = 'Cell Phone'
        elif  ewaste_item_1 == '12':
             ewaste_item_1 = 'TV (Any Size)'
        elif  ewaste_item_1  == '13':
             ewaste_item_1 = 'VCR/DVD Player'
        elif  ewaste_item_1 == '14':
            ewaste_item_1 = 'Video/Film Cameras'
        elif  ewaste_item_1 == '15':
            ewaste_item_1  = 'Video/Games Components'
        elif  ewaste_item_1 == '17':
             ewaste_item_1 = 'Vacuum Cleaner'
        elif ewaste_item_1 ==  None:
            ewaste_item_1 == " "






        d = dict()
        d.setdefault("DriverFirstName",last_edited_user )
        d.setdefault("DriverLastName","Aguilar" )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ElectronicWestType", ewaste_item_1)
        d.setdefault("Type", "Electronic Waste")
        d.setdefault("Name", ewaste_uid )


        l311.append(d)
        # d = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName","Aguilar" )
        # d.setdefault("ElectronicWestType", ewaste_item_2)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName","Aguilar" )
        # d.setdefault("ElectronicWestType", ewaste_item_3)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName",last_edited_user )
        # d.setdefault("DriverLastName","Aguilar" )
        # d.setdefault("ElectronicWestType", ewaste_item_4)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        #
        #
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", ewaste_item_5)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", ewaste_item_6)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", ewaste_item_7)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", ewaste_item_8)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", ewaste_item_9)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        #
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", ewaste_item_10)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        #
        #
        #
        #
        #
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", "Geoffrey")
        # d.setdefault("DriverLastName", "West")
        # d.setdefault("ElectronicWestType", ewaste_item_9)
        # d.setdefault("Type", "Electronic Waste")
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", "Geoffrey")
        # d.setdefault("DriverLastName", "West")
        # d.setdefault("ElectronicWestType", ewaste_item_10)
        # d.setdefault("Type", "Electronic Waste")
        # l311.append(d)
        dL311 = dict()
        dL311.setdefault("La311ElectronicWaste", l311)
        dResult.setdefault("ListOfLa311ElectronicWaste",dL311)
        #dOthers = dict()
        ##Adding empty dictionaries;
        #dResult.setdefault("ListOfLa311IllegalDumpingPickup", dOthers)
        #dResult.setdefault("ListOfLa311ManualPickup", dOthers)
        #dResult.setdefault("ListOfLa311MetalHouseholdAppliancesPickup", dOthers)
        #dResult.setdefault("ListOfLa311MoveInMoveOut", dOthers)
        #dResult.setdefault("ListOfLa311ServiceNotComplete", dOthers)
        #Ends of adding additional itmes ****************************************
        lResults.append({"MetaData": {}, "SRData": dResult})

        # ii = ii + 1
        print(json.dumps(lResults, sort_keys=True, indent=4))
        for outputs in lResults:
            #url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSR"
            url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSRWithCodes"
            headers = {'Content-type': 'text/plain', 'Accept': '/'}
            r = requests.post(url, data= json.dumps(outputs), headers=headers,  verify=False)
            #print 'It took', time.time()-start, 'seconds.'
            print r.text
            print (str(ii) + ". " + str(len(lResults)), 'It took', time.time()-start, 'seconds.' )

    print("Finished")
except:
    print "failed"

#
#     pyFC = "SO_SC_1"
#     clauseSBE = "WHERE Category LIKE '%6%' AND ITEM_1 IS NOT NULL"
#     connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
#     # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
#     conn = pyodbc.connect(connstr)
#     cursor = conn.cursor()
#     FN_SRNumber = "SRNumber"
#     lFields = [FN_SRNumber, "RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "QYT_1", "UID","last_edited_user"]
#     #lFields = ["SRNumber"]
#     sFields = ""
#     for fld in lFields:
#         if(sFields==""):
#             sFields = fld
#         else:
#             sFields = sFields + "," + fld
#     #List of the fields you'd like to exclude, like ItemCount for example.
#     lFieldsExcluded = ["ITEM_1", "ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID", "RESOLUTION_CODE", "QYT_1", "last_edited_user"]
#
#     #sSQL = "SELECT SRNumber FROM {}".format(pyFC)
#     sSQL = "SELECT {} FROM {}  {}".format(sFields, pyFC, clauseSBE)
#     print sSQL
#
#     cursor.execute(sSQL)
#     #columns = [column[0] for column in cursor.description]
#     columns = []
#     for column in cursor.description:
#         if not (column[0] in lFieldsExcluded):
#             columns.append(column[0])
#
# try:
#     ii = 0
#     ewaste_item_1 = ""
#     ewaste_item_2 = ""
#     ewaste_item_3 = ""
#     ewaste_item_4 = ""
#     ewaste_item_5 = ""
#     ewaste_item_6 = ""
#     ewaste_item_7 = ""
#     ewaste_item_8 = ""
#     ewaste_item_9 = ""
#     ewaste_item_10 = ""
#     rescode = ""
#     reasoncode = " "
#     ewaste_uid = ""
#     last_edited_user = " "
#
#     for row in cursor.fetchall():
#         lResults = []    #make sure lResults are initiated here
#         lValues = []
#         for i in range(len(columns)):
#             lValues.append( str(row[i]))
#         white_item_1 = (str(row[lFields.index("ITEM_1")]))
#         white_item_2 = (str(row[lFields.index("ITEM_2")]))
#         white_item_3 = (str(row[lFields.index("ITEM_3")]))
#         white_item_4 = (str(row[lFields.index("ITEM_4")]))
#         white_item_5 = (str(row[lFields.index("ITEM_5")]))
#         white_item_6= (str(row[lFields.index("ITEM_6")]))
#         white_item_7 =(str(row[lFields.index("ITEM_7")]))
#         white_item_8 = (str(row[lFields.index("ITEM_8")]))
#         white_item_9 =(str(row[lFields.index("ITEM_9")]))
#         white_item_10 = (str(row[lFields.index("ITEM_10")]))
#         MHA_QYT_1 =   (str(row[lFields.index("QYT_1")]))
#
#         white_uid = (str(row[lFields.index("UID")]))
#         rescode = (str(row[lFields.index("RESOLUTION_CODE")]))
#
#         last_edited_user = (str(row[lFields.index("last_edited_user")]))
#
#         #dResult = dict(zip(columns, row))
#         dResult = dict(zip(columns, lValues))
#
#         # Adding additional items  ******************************
#         dResult.setdefault("ReasonCode", rescode if rescode.isdigit() else "")
#         dResult.setdefault("ResolutionCode",rescode if not rescode.isdigit() else "")
#         #dResult.setdefault("ListOfLa311ElectronicWaste", dict())
#         l311 = []
#         if  white_item_1  == '7':
#             white_item_1 = 'Dishwasher '
#         elif  white_item_1 =='1':
#              white_item_1 = 'AC'
#         elif  white_item_1 == '2':
#              white_item_1 = 'BBQ'
#         elif white_item_1  == "3":
#             white_item_1 = 'Bed Frame Metal'
#         elif  white_item_1== '4':
#              white_item_1  = 'Bike Parts'
#         elif  white_item_1  == '5':
#              white_item_1  = 'Bird Cage Metal'
#         elif  white_item_1  == '6':
#             white_item_1  = 'Cooler'
#         elif  white_item_1  == '8':
#             white_item_1 = 'Dryer'
#         elif  white_item_1 == '9':
#             white_item_1  = 'Fence Metal'
#         elif  white_item_1 == '10':
#             white_item_1 = 'File Cabinet Metal'
#         elif  white_item_1  == '11':
#             white_item_1 = 'Freezer'
#         elif  white_item_1 == '16':
#             white_item_1  = 'Ovens'
#         elif  white_item_1 == '12':
#              white_item_1 = 'Heater'
#         elif  white_item_1  == '13':
#              white_item_1 = 'Iron Tub'
#         elif  white_item_1 == '14':
#             white_item_1 = 'Metal Cabinet'
#         elif  white_item_1 == '15':
#             white_item_1  = 'Other WG'
#         elif  white_item_1 == '17':
#              white_item_1 = 'Pipes (Metal)'
#         elif white_item_1 ==  '18':
#             white_item_1 = 'Pool Heater'
#         elif white_item_1 ==  '25':
#             white_item_1 = 'Refrigerator'
#         elif white_item_1 ==  '19':
#             white_item_1 = 'Scrap Metal'
#         elif white_item_1 ==  '20':
#             white_item_1 = 'Stove'
#         elif white_item_1 ==  '19':
#             white_item_1 =  'Swamp Cooler'
#         elif white_item_1 ==  '20':
#             white_item_1 = 'Stove'
#         elif white_item_1 ==  '21':
#             white_item_1 ='Swamp Cooler'
#         elif white_item_1 ==  '22':
#             white_item_1 = 'Trash Compactor'
#         elif white_item_1 ==  '23':
#             white_item_1 = 'Washing Machine'
#
#
#         print white_item_1
#
#         d = dict()
#         d.setdefault("DriverFirstName",last_edited_user )
#         d.setdefault("DriverLastName","Aguilar" )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("HouseholdItem", white_item_1)
#         d.setdefault("Type", "Metal/Household Appliances")
#         d.setdefault("HouseHoldItemCount", MHA_QYT_1 )
#
#
#         l311.append(d)
#         # d = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName","Aguilar" )
#         # d.setdefault("ElectronicWestType", ewaste_item_2)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName","Aguilar" )
#         # d.setdefault("ElectronicWestType", ewaste_item_3)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName",last_edited_user )
#         # d.setdefault("DriverLastName","Aguilar" )
#         # d.setdefault("ElectronicWestType", ewaste_item_4)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         #
#         #
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_5)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_6)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_7)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_8)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_9)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         #
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_10)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         #
#         #
#         #
#         #
#         #
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", "Geoffrey")
#         # d.setdefault("DriverLastName", "West")
#         # d.setdefault("ElectronicWestType", ewaste_item_9)
#         # d.setdefault("Type", "Electronic Waste")
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", "Geoffrey")
#         # d.setdefault("DriverLastName", "West")
#         # d.setdefault("ElectronicWestType", ewaste_item_10)
#         # d.setdefault("Type", "Electronic Waste")
#         # l311.append(d)
#         dL311 = dict()
#         dL311.setdefault("La311MetalHouseholdAppliancesPickup", l311)
#         dResult.setdefault("ListOfLa311MetalHouseholdAppliancesPickup",dL311)
#         #dOthers = dict()
#         ##Adding empty dictionaries;
#         #dResult.setdefault("ListOfLa311IllegalDumpingPickup", dOthers)
#         #dResult.setdefault("ListOfLa311ManualPickup", dOthers)
#         #dResult.setdefault("ListOfLa311MetalHouseholdAppliancesPickup", dOthers)
#         #dResult.setdefault("ListOfLa311MoveInMoveOut", dOthers)
#         #dResult.setdefault("ListOfLa311ServiceNotComplete", dOthers)
#         #Ends of adding additional itmes ****************************************
#         lResults.append({"MetaData": {}, "SRData": dResult})
#
#
#         ii = ii + 1
#         print(json.dumps(lResults, sort_keys=True, indent=4))
#         for outputs in lResults:
#             #url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSR"
#             url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSRWithCodes"
#             headers = {'Content-type': 'text/plain', 'Accept': '/'}
#             r = requests.post(url, data= json.dumps(outputs), headers=headers,  verify=False)
#             #print 'It took', time.time()-start, 'seconds.'
#             print r.text
#             print (str(ii) + ". " + str(len(lResults)), 'It took', time.time()-start, 'seconds.' )
#
#     print("Finished")
# except:
#     print "failed for white goods"
#
#
# start = time.time()
# pyFC = "SO_SC_1"
# clauseSBE = "WHERE Category LIKE '%8%'"
#
# if(__name__=='__main__'):
#     # sMsg = printObjects()
#     # print(sMsg)
#
#     start = time.time()
#     pyFC = "SO_SC_1"
#     clauseSBE = "WHERE Category LIKE '%8%' AND ITEM_1 IS NOT NULL"
#
#
#
#     connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
#     # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
#     conn = pyodbc.connect(connstr)
#     cursor = conn.cursor()
#     FN_SRNumber = "SRNumber"
#     lFields = [FN_SRNumber, "RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "QYT_1" "UID","last_edited_user"]
#     #lFields = ["SRNumber"]
#     sFields = ""
#     for fld in lFields:
#         if(sFields==""):
#             sFields = fld
#         else:
#             sFields = sFields + "," + fld
#     #List of the fields you'd like to exclude, like ItemCount for example.
#     lFieldsExcluded = ["ITEM_1", "ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID", "RESOLUTION_CODE", "last_edited_user", "QYT_1"]
#
#     #sSQL = "SELECT SRNumber FROM {}".format(pyFC)
#     sSQL = "SELECT {} FROM {}  {}".format(sFields, pyFC, clauseSBE)
#     print sSQL
#
#     cursor.execute(sSQL)
#     #columns = [column[0] for column in cursor.description]
#     columns = []
#     for column in cursor.description:
#         if not (column[0] in lFieldsExcluded):
#             columns.append(column[0])
#
# try:
#     ii = 0
#     dar_item_1 = ""
#     dar_item_2 = ""
#     dar_item_3 = ""
#     dar_item_4 = ""
#     dar_item_5 = ""
#     dar_item_6 = ""
#     dar_item_7 = ""
#     dar_item_8 = ""
#     dar_item_9 = ""
#     dar_item_10 = ""
#     rescode = ""
#     reasoncode = " "
#     ewaste_uid = ""
#     last_edited_user = " "
#
#     for row in cursor.fetchall():
#         lResults = []    #make sure lResults are initiated here
#         lValues = []
#         for i in range(len(columns)):
#             lValues.append( str(row[i]))
#         dar_item_1 = (str(row[lFields.index("ITEM_1")]))
#         dar_item_2 = (str(row[lFields.index("ITEM_2")]))
#         dar_item_3 = (str(row[lFields.index("ITEM_3")]))
#         dar_item_4 = (str(row[lFields.index("ITEM_4")]))
#         dar_item_5 = (str(row[lFields.index("ITEM_5")]))
#         dar_item_6= (str(row[lFields.index("ITEM_6")]))
#         dar_item_7 =(str(row[lFields.index("ITEM_7")]))
#         dar_item_8 = (str(row[lFields.index("ITEM_8")]))
#         dar_item_9 =(str(row[lFields.index("ITEM_9")]))
#         dar_item_10 = (str(row[lFields.index("ITEM_10")]))
#         dar_qyt_1 = (str(row[lFields.index("QYT_1")]))
#         white_uid = (str(row[lFields.index("UID")]))
#         rescode = (str(row[lFields.index("RESOLUTION_CODE")]))
#
#         last_edited_user = (str(row[lFields.index("last_edited_user")]))
#
#         #dResult = dict(zip(columns, row))
#         dResult = dict(zip(columns, lValues))
#
#         # Adding additional items  ******************************
#         dResult.setdefault("ReasonCode", rescode if rescode.isdigit() else "")
#         dResult.setdefault("ResolutionCode",rescode if not rescode.isdigit() else "")
#         #dResult.setdefault("ListOfLa311ElectronicWaste", dict())
#         l311 = []
#         if  dar_item_1  == '7':
#             dar_item_1 = 'Coyote '
#         elif  dar_item_1 =='1':
#              dar_item_1 = 'Alligator'
#         elif  dar_item_1 == '2':
#              dar_item_1 = 'Bat'
#         elif dar_item_1  == "3":
#             dar_item_1 = 'Bird'
#         elif  dar_item_1== '4':
#              dar_item_1  = 'Cat'
#         elif  dar_item_1  == '5':
#              dar_item_1  = 'Chicken'
#         elif  dar_item_1  == '6':
#             dar_item_1  = 'Cow'
#         elif  dar_item_1  == '8':
#             dar_item_1 = 'Crow (Pigeon Size)'
#         elif  dar_item_1 == '9':
#             dar_item_1  = 'Deer'
#         elif  dar_item_1 == '10':
#             dar_item_1 = 'Dog'
#         elif  dar_item_1  == '11':
#             dar_item_1 = 'Duck'
#         elif  dar_item_1 == '16':
#             dar_item_1  = 'Llama'
#         elif  dar_item_1 == '12':
#              dar_item_1 = 'Heater'
#         elif  dar_item_1  == '13':
#              dar_item_1 = 'Fox'
#         elif  dar_item_1 == '14':
#             dar_item_1 = 'Geese'
#         elif  dar_item_1 == '15':
#             dar_item_1  = 'Guts'
#         elif  dar_item_1 == '17':
#              dar_item_1 = 'Monkey'
#         elif dar_item_1 ==  '18':
#             dar_item_1 = 'Opposum'
#         elif dar_item_1 ==  '25':
#             dar_item_1 = 'Seal'
#         elif dar_item_1 ==  '19':
#             dar_item_1 = 'Owl'
#         elif dar_item_1 ==  '20':
#             dar_item_1 = 'Peacock'
#         elif dar_item_1 ==  '19':
#             dar_item_1 =  'Swamp Cooler'
#         elif dar_item_1 ==  '20':
#             dar_item_1 = 'Stove'
#         elif dar_item_1 ==  '21':
#             dar_item_1 ='Pig'
#         elif dar_item_1 ==  '22':
#             dar_item_1 = 'Rabbit'
#         elif dar_item_1 ==  '23':
#             dar_item_1 = 'Racoon'
#         elif dar_item_1 ==  '24':
#             dar_item_1 = 'Rats'
#         elif dar_item_1 ==  '26':
#             dar_item_1 = 'Sheep'
#         elif dar_item_1 ==  '27':
#             dar_item_1 = 'Snake'
#         elif dar_item_1 ==  '28':
#             dar_item_1 = 'Spoiled Meat'
#         elif dar_item_1 ==  '29':
#             dar_item_1 = 'Squirrel'
#         elif dar_item_1 ==  '30':
#             dar_item_1 = 'Turkey'
#         elif dar_item_1 ==  '31':
#             dar_item_1 = 'Turtle'
#         elif dar_item_1 ==  '32':
#             dar_item_1 = 'Unknown'
#         elif dar_item_1 ==  '33':
#             dar_item_1 = 'Skunk'
#         elif dar_item_1 ==  '34':
#             dar_item_1 = 'Raven (Chicken Size)'
#         elif dar_item_1 ==  '35':
#             dar_item_1 = 'Raven (Unknown Size)'
#         elif dar_item_1 ==  '36':
#             dar_item_1 = 'Other'
#
#         d = dict()
#         d.setdefault("DriverFirstName",last_edited_user )
#         d.setdefault("DriverLastName","Aguilar" )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("DACType", dar_item_1)
#         d.setdefault("Type", "Dead Animal Removal")
#         d.setdefault("DACItemCount", dar_qyt_1)
#         # d.setdefault("Name", dar_item_1 )
#
#         l311.append(d)
#         # d = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName","Aguilar" )
#         # d.setdefault("ElectronicWestType", ewaste_item_2)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName","Aguilar" )
#         # d.setdefault("ElectronicWestType", ewaste_item_3)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName",last_edited_user )
#         # d.setdefault("DriverLastName","Aguilar" )
#         # d.setdefault("ElectronicWestType", ewaste_item_4)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         #
#         #
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_5)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_6)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_7)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_8)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_9)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         # l311.append(d)
#         # dL311 = dict()
#         #
#         # d.setdefault("DriverFirstName", last_edited_user)
#         # d.setdefault("DriverLastName", "Aguilar")
#         # d.setdefault("ElectronicWestType", ewaste_item_10)
#         # d.setdefault("Type", "Electronic Waste")
#         # d.setdefault("Name", ewaste_uid )
#         #
#         #
#         #
#         #
#         #
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", "Geoffrey")
#         # d.setdefault("DriverLastName", "West")
#         # d.setdefault("ElectronicWestType", ewaste_item_9)
#         # d.setdefault("Type", "Electronic Waste")
#         # l311.append(d)
#         # dL311 = dict()
#         # d.setdefault("DriverFirstName", "Geoffrey")
#         # d.setdefault("DriverLastName", "West")
#         # d.setdefault("ElectronicWestType", ewaste_item_10)
#         # d.setdefault("Type", "Electronic Waste")
#         # l311.append(d)
#         dL311 = dict()
#         dL311.setdefault("DeadAnimalRemoval", l311)
#         dResult.setdefault("ListOfLa311DeadAnimalRemoval",dL311)
#         #dOthers = dict()
#         ##Adding empty dictionaries;
#         #dResult.setdefault("ListOfLa311IllegalDumpingPickup", dOthers)
#         #dResult.setdefault("ListOfLa311ManualPickup", dOthers)
#         #dResult.setdefault("ListOfLa311MetalHouseholdAppliancesPickup", dOthers)
#         #dResult.setdefault("ListOfLa311MoveInMoveOut", dOthers)
#         #dResult.setdefault("ListOfLa311ServiceNotComplete", dOthers)
#         #Ends of adding additional itmes ****************************************
#         lResults.append({"MetaData": {}, "SRData": dResult})
#
#
#         ii = ii + 1
#         print(json.dumps(lResults, sort_keys=True, indent=4))
#         for outputs in lResults:
#             #url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSR"
#             url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSRWithCodes"
#             headers = {'Content-type': 'text/plain', 'Accept': '/'}
#             r = requests.post(url, data= json.dumps(outputs), headers=headers,  verify=False)
#             #print 'It took', time.time()-start, 'seconds.'
#             print r.text
#             print (str(ii) + ". " + str(len(lResults)), 'It took', time.time()-start, 'seconds.' )
#
#     print("Finished")
# except:
#     print "dar failed"
#


start = time.time()


if(__name__=='__main__'):
    pyFC = "SO_SC_1"
    clauseSBE = "WHERE Category LIKE '%1%'"
    connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
    # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
    conn = pyodbc.connect(connstr)
    cursor = conn.cursor()
    FN_SRNumber = "SRNumber"
    lFields = [FN_SRNumber, "RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","last_edited_user", 'QYT_1']
    #lFields = ["SRNumber"]
    sFields = ""
    for fld in lFields:
        if(sFields==""):
            sFields = fld
        else:
            sFields = sFields + "," + fld
    #List of the fields you'd like to exclude, like ItemCount for example.
    lFieldsExcluded = ["ITEM_1", "ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1", "RESOLUTION_CODE", "last_edited_user", 'QYT_1']

    #sSQL = "SELECT SRNumber FROM {}".format(pyFC)
    sSQL = "SELECT {} FROM {}  {}".format(sFields, pyFC, clauseSBE)
    print sSQL

    cursor.execute(sSQL)
    #columns = [column[0] for column in cursor.description]
    columns = []
    for column in cursor.description:
        if not (column[0] in lFieldsExcluded):
            columns.append(column[0])



    ii = 0
    bulky_item_1 = ""
    bulky_item_2 = ""
    bulky_item_3 = ""
    bulky_item_4 = ""
    bulky_item_5 = ""
    bulky_item_6 = ""
    bulky_item_7 = ""
    bulky_item_8 = ""
    bulky_item_9 = ""
    bulky_item_10 = ""
    bulky_item_11 = ""
    bulky_item_12 = ""
    bulky_item_13 = ""
    bulky_item_14 = ""
    bulky_item_15 = ""
    bulky_item_16 = ""
    bulky_item_17 = ""
    bulky_item_18 = ""
    bulky_item_19 = ""
    bulky_item_20 = ""
    bulky_item_21 = ""
    bulky_item_22 = ""
    bulky_item_23 = ""
    bulky_item_24 = ""
    bulky_item_25 = ""
    bulky_item_26= ""
    bulky_item_27 = ""
    bulky_item_28 = ""
    bulky_item_29 = ""
    bulky_item_30 = ""
    bulky_item_31 = ""
    bulky_item_32 = ""
    bulky_item_33 = ""
    bulky_item_34 = ""
    bulky_item_35= ""
    bulky_item_36 = ""
    bulky_item_37 = ""
    bulky_item_38 = ""
    bulky_item_39 = ""
    bulky_item_40 = ""


    rescode = ""
    bulky_uid = ""
    last_edited_user = " "

    for row in cursor.fetchall():
        lResults = []    #make sure lResults are initiated here
        lValues = []
        for i in range(len(columns)):
            lValues.append( str(row[i]))
        bulky_item_1 = (str(row[lFields.index("ITEM_1")]))
        bulky_item_2 = (str(row[lFields.index("ITEM_2")]))
        bulky_item_3 = (str(row[lFields.index("ITEM_3")]))
        bulky_item_4 = (str(row[lFields.index("ITEM_4")]))
        bulky_item_5 = (str(row[lFields.index("ITEM_5")]))
        bulky_item_5 = (str(row[lFields.index("ITEM_5")]))
        bulky_item_6 =(str(row[lFields.index("ITEM_6")]))
        bulky_item_7 = (str(row[lFields.index("ITEM_8")]))
        bulky_item_8 =(str(row[lFields.index("ITEM_8")]))
        bulky_item_9 = (str(row[lFields.index("ITEM_9")]))
        bulky_item_10 = (str(row[lFields.index("ITEM_10")]))
        ewaste_uid = (str(row[lFields.index("UID1")]))
        QYT_1 = ewaste_uid = (str(row[lFields.index("QYT_1")]))
        rescode = (str(row[lFields.index("RESOLUTION_CODE")]))
        last_edited_user = (str(row[lFields.index("last_edited_user")]))

        print bulky_item_1
        #dResult = dict(zip(columns, row))
        dResult = dict(zip(columns, lValues))
        # Adding additional items  ******************************
        dResult.setdefault("ReasonCode", rescode if rescode.isdigit() else "")
        dResult.setdefault("ResolutionCode",rescode if not rescode.isdigit() else "")
        #dResult.setdefault("ListOfLa311ElectronicWaste", dict())
        l311 = []
        if  bulky_item_1  == '1':
            bulky_item_1 = 'Bags Any Size '
        elif  bulky_item_1 =='3':
             bulky_item_1 = 'Bed Frame (wood)'
        elif  bulky_item_1 == '2':
             bulky_item_1 = 'Bed Set'
        elif bulky_item_1  == "78":
            bulky_item_1 = 'Bicycle'
        elif  bulky_item_1== '5':
             bulky_item_1  = 'Bird Cage Plastic'
        elif  bulky_item_1  == '6':
             bulky_item_1  = 'Blinds'
        elif  bulky_item_1  == '7':
            bulky_item_1  = 'Bookcase'
        elif  bulky_item_1  == '8':
            bulky_item_1 = 'Box Any Size'
        elif  bulky_item_1 == '9':
            bulky_item_1  = 'Box Spring'
        elif  bulky_item_1 == '10':
            bulky_item_1 = 'Cabinets'
        elif  bulky_item_1  == '11':
            bulky_item_1 = 'Car Parts'
        elif  bulky_item_1 == '12':
            bulky_item_1  = 'Carpet'
        elif  bulky_item_1 == '13':
             bulky_item_1 = 'Chair'
        elif  bulky_item_1  == '79':
             bulky_item_1 = 'Child Day Bed'
        elif  bulky_item_1 == '14':
            bulky_item_1 = 'Crib'
        elif  bulky_item_1 == '15':
            bulky_item_1  = 'Curtain Rod'
        elif  bulky_item_1 == '16':
             bulky_item_1 = 'Cushions'
        elif bulky_item_1 ==  '18':
            bulky_item_1 = "Decorating Item "
        if  bulky_item_1  == '19':
            bulky_item_1 = 'Desk'
        elif  bulky_item_1 =='20':
             bulky_item_1 = 'Door'
        elif  bulky_item_1 == '21':
             bulky_item_1 = 'Dresser'
        elif bulky_item_1  == "22":
            bulky_item_1 = 'Entertainment Center'
        elif  bulky_item_1== '23':
             bulky_item_1  = 'Fan (Any Size)'
        elif  bulky_item_1  == '24':
             bulky_item_1  = 'Fence (Wood)'
        elif  bulky_item_1  == '25':
            bulky_item_1  = 'File Cabinet (Wood)'
        elif  bulky_item_1  == '26':
            bulky_item_1 = 'Garage Door'
        elif  bulky_item_1 == '27':
            bulky_item_1  = 'Garage Door Opener'
        elif  bulky_item_1 == '80':
            bulky_item_1 = 'Gate (Wood)'
        elif  bulky_item_1  == '28':
            bulky_item_1 = 'Glass'
        elif  bulky_item_1 == '29':
            bulky_item_1  = 'Glass Window in Frame'
        elif  bulky_item_1 == '30':
             bulky_item_1 = 'Headboard'
        elif  bulky_item_1  == '31':
             bulky_item_1 = 'Ladders (Wood & Metal)'
        elif  bulky_item_1 == '14':
            bulky_item_1 = 'Video/Film Cameras'
        elif  bulky_item_1 == '32':
            bulky_item_1  = 'Lamp'
        elif  bulky_item_1 == '33':
             bulky_item_1 = 'Light Fixture'
        elif  bulky_item_1 == '34':
             bulky_item_1 = 'Loose Debris'
        elif  bulky_item_1 == '35':
            bulky_item_1 = 'Mattress'
        elif  bulky_item_1 == '36':
            bulky_item_1 = 'Mirror'
        elif  bulky_item_1 == '37':
            bulky_item_1 = 'Other BI'
        elif  bulky_item_1 == '38':
            bulky_item_1 = 'Pallet'
        elif  bulky_item_1 == '39':
            bulky_item_1 = 'Patio Cover'
        elif  bulky_item_1 == '40':
            bulky_item_1 = 'Patio Furniture'
        elif  bulky_item_1 == '41':
            bulky_item_1 = 'Piano'
        elif  bulky_item_1 == '42':
            bulky_item_1 = 'Planter Pot'
        elif  bulky_item_1 == '43':
            bulky_item_1 = 'Playpen'
        elif  bulky_item_1 == '44':
            bulky_item_1 = 'Pool Cover'
        elif  bulky_item_1 == '45':
            bulky_item_1 = 'Rain Gutter'
        elif  bulky_item_1 == '46':
            bulky_item_1 = 'Recliner'
        elif  bulky_item_1 == '47':
            bulky_item_1 = 'Rug'
        elif  bulky_item_1 == '48':
            bulky_item_1 = 'Shelf'
        elif  bulky_item_1 == '49':
            bulky_item_1 = 'Shopping Cart'
        elif  bulky_item_1 == '50':
            bulky_item_1 = 'Shower Door'
        elif  bulky_item_1 == '51':
            bulky_item_1 = 'Shutter'
        elif  bulky_item_1 == '52':
            bulky_item_1 = 'Sink'
        elif  bulky_item_1 == '53':
            bulky_item_1 = 'Sliding Door'
        elif  bulky_item_1 == '54':
            bulky_item_1 = 'Sofa'
        elif  bulky_item_1 == '55':
            bulky_item_1 = 'Sofa bed'
        elif  bulky_item_1 == '56':
            bulky_item_1 = 'Spa Cover'
        elif  bulky_item_1 == '57':
            bulky_item_1 = 'Spa/Jacuzzi'
        elif  bulky_item_1 == '58':
            bulky_item_1 = 'Stroller'
        elif  bulky_item_1 == '59':
            bulky_item_1 = 'Suitcase'
        elif  bulky_item_1 == '60':
            bulky_item_1 = 'Table'
        elif  bulky_item_1 == '61':
            bulky_item_1 = 'Tank Any Size'
        elif  bulky_item_1 == '62':
                 bulky_item_1 = 'Tire Less Than 5'
        elif  bulky_item_1 == '63':
            bulky_item_1 = 'Toilet'
        elif  bulky_item_1 == '64':
            bulky_item_1 = 'Toys (Large Ones)'
        elif  bulky_item_1 == '65':
            bulky_item_1 = 'Trash Cans'
        elif  bulky_item_1 == '66':
             bulky_item_1 = 'Trunk'
        elif  bulky_item_1 == '67':
            bulky_item_1 = 'Tub (Non Metal)'
        elif  bulky_item_1 == '68':
            bulky_item_1 = ' Vacuum Cleaner'
        elif  bulky_item_1 == '69':
            bulky_item_1 = 'Vehicle Tire'
        elif  bulky_item_1 == '70':
            bulky_item_1 = 'Walker'
        elif  bulky_item_1 == '71':
                bulky_item_1 = 'Window Blinds'
        elif  bulky_item_1 == '72':
                bulky_item_1 = 'Window Frame'
        elif  bulky_item_1 == '73':
            bulky_item_1 = 'Windows'
        elif  bulky_item_1 == '74':
                bulky_item_1 = 'Wood Boards'
        elif  bulky_item_1 == '75':
            bulky_item_1 = 'Wood Bundled'
        elif  bulky_item_1 == '76':
            bulky_item_1 = 'Wood Cabinets'
        elif  bulky_item_1 == '77':
            bulky_item_1 = 'XMAS TREE'
        elif  bulky_item_1 == '2':
            bulky_item_1 = 'Basketball Set'

        # d = dict()
        # d.setdefault("DriverFirstName",last_edited_user )
        # d.setdefault("DriverLastName","Aguilar" )
        # d.setdefault("BulkyItemType",bulky_item_1)
        # d.setdefault("Type", "Bulky Items")
        # d.setdefault("BulkyItemCount", QYT_1 )
        # # d.setdefault("Name", bulky_uid)
        # l311.append(d)
        # d = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName","Aguilar" )
        # d.setdefault("ElectronicWestType", bulky_item_2)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName","Aguilar" )
        # d.setdefault("ElectronicWestType", bulky_item_3)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName",last_edited_user )
        # d.setdefault("DriverLastName","Aguilar" )
        # d.setdefault("ElectronicWestType", bulky_item_4)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        #
        #
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", bulky_item_5)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", bulky_item_6)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", bulky_item_7)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", bulky_item_8)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", bulky_item_9)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        # l311.append(d)
        # dL311 = dict()
        #
        # d.setdefault("DriverFirstName", last_edited_user)
        # d.setdefault("DriverLastName", "Aguilar")
        # d.setdefault("ElectronicWestType", bulky_item_10)
        # d.setdefault("Type", "Electronic Waste")
        # d.setdefault("Name", ewaste_uid )
        #
        #
        #
        #
        #
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", "Geoffrey")
        # d.setdefault("DriverLastName", "West")
        # d.setdefault("ElectronicWestType", bulky_item_9)
        # d.setdefault("Type", "Electronic Waste")
        # l311.append(d)
        # dL311 = dict()
        # d.setdefault("DriverFirstName", "Geoffrey")
        # d.setdefault("DriverLastName", "West")
        # d.setdefault("ElectronicWestType", bulky_item_10)
        # d.setdefault("Type", "Electronic Waste")
        # l311.append(d)
        # dL311 = dict()
        # dL311.setdefault("BulkyItem", l311)
        # dResult.setdefault("ListOfLa311BulkyItem",dL311)
        #dOthers = dict()
        ##Adding empty dictionaries;
        #dResult.setdefault("ListOfLa311IllegalDumpingPickup", dOthers)
        #dResult.setdefault("ListOfLa311ManualPickup", dOthers)
        #dResult.setdefault("ListOfLa311MetalHouseholdAppliancesPickup", dOthers)
        #dResult.setdefault("ListOfLa311MoveInMoveOut", dOthers)
        #dResult.setdefault("ListOfLa311ServiceNotComplete", dOthers)
        #Ends of adding additional itmes ****************************************
        lResults.append({"MetaData": {}, "SRData": dResult})

        # ii = ii + 1
        print(json.dumps(lResults, sort_keys=True, indent=4))
        # for outputs in lResults:
        #     #url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSR"
        #     url = "https://myla311RemoteTest.lacity.org/myla311router/mylasrbe/1/UpsertSANSR"
        #     headers = {'Content-type': 'text/plain', 'Accept': '/'}
        #     r = requests.post(url, data= json.dumps(outputs), headers=headers,  verify=False)
        #     #print 'It took', time.time()-start, 'seconds.'
        #     print r.text
        #     print (str(ii) + ". " + str(len(lResults)), 'It took', time.time()-start, 'seconds.' )

    print("Finished")




