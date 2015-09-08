__author__ = 'GeoffreyWest'
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
clauseSBE = "WHERE Category LIKE '%6%'"
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

    connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
    # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
    conn = pyodbc.connect(connstr)
    cursor = conn.cursor()
    FN_SRNumber = "SRNumber"
    lFields = [FN_SRNumber, "RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "QYT_1", "ITEM_10", "UID","last_edited_user"]
    #lFields = ["SRNumber"]
    sFields = ""
    for fld in lFields:
        if(sFields==""):
            sFields = fld
        else:
            sFields = sFields + "," + fld
    #List of the fields you'd like to exclude, like ItemCount for example.
    lFieldsExcluded = ["ITEM_1", "ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID", "QYT_1", "RESOLUTION_CODE", "last_edited_user"]

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
    reasoncode = " "
    ewaste_uid = ""
    last_edited_user = " "

    for row in cursor.fetchall():
        lResults = []    #make sure lResults are initiated here
        lValues = []
        for i in range(len(columns)):
            lValues.append( str(row[i]))
        white_item_1 = (str(row[lFields.index("ITEM_1")]))
        white_item_2 = (str(row[lFields.index("ITEM_2")]))
        white_item_3 = (str(row[lFields.index("ITEM_3")]))
        white_item_4 = (str(row[lFields.index("ITEM_4")]))
        white_item_5 = (str(row[lFields.index("ITEM_5")]))
        white_item_6= (str(row[lFields.index("ITEM_6")]))
        white_item_7 =(str(row[lFields.index("ITEM_7")]))
        white_item_8 = (str(row[lFields.index("ITEM_8")]))
        white_item_9 =(str(row[lFields.index("ITEM_9")]))
        white_item_10 = (str(row[lFields.index("ITEM_10")]))
        white_qyt_1 = (str(row[lFields.index("QYT_1")]))

        white_uid = (str(row[lFields.index("UID")]))
        rescode = (str(row[lFields.index("RESOLUTION_CODE")]))

        last_edited_user = (str(row[lFields.index("last_edited_user")]))

        #dResult = dict(zip(columns, row))
        dResult = dict(zip(columns, lValues))

        # Adding additional items  ******************************
        dResult.setdefault("ReasonCode", rescode if rescode.isdigit() else "")
        dResult.setdefault("ResolutionCode",rescode if not rescode.isdigit() else "")
        dResult.setdefault("ListOfLa311ElectronicWaste", dict())
        l311 = []
        if  white_item_1  == '7':
            white_item_1 = 'Dishwasher '
        elif  white_item_1 =='1':
             white_item_1 = 'AC'
        elif  white_item_1 == '2':
             white_item_1 = 'BBQ'
        elif white_item_1  == "3":
            white_item_1 = 'Bed Frame Metal'
        elif  white_item_1== '4':
             white_item_1  = 'Bike Parts'
        elif  white_item_1  == '5':
             white_item_1  = 'Bird Cage Metal'
        elif  white_item_1  == '6':
            white_item_1  = 'Cooler'
        elif  white_item_1  == '8':
            white_item_1 = 'Dryer'
        elif  white_item_1 == '9':
            white_item_1  = 'Fence Metal'
        elif  white_item_1 == '10':
            white_item_1 = 'File Cabinet Metal'
        elif  white_item_1  == '11':
            white_item_1 = 'Freezer'
        elif  white_item_1 == '16':
            white_item_1  = 'Ovens'
        elif  white_item_1 == '12':
             white_item_1 = 'Heater'
        elif  white_item_1  == '13':
             white_item_1 = 'Iron Tub'
        elif  white_item_1 == '14':
            white_item_1 = 'Metal Cabinet'
        elif  white_item_1 == '15':
            white_item_1  = 'Other WG'
        elif  white_item_1 == '17':
             white_item_1 = 'Pipes (Metal)'
        elif white_item_1 ==  '18':
            white_item_1 = 'Pool Heater'
        elif white_item_1 ==  '25':
            white_item_1 = 'Refrigerator'
        elif white_item_1 ==  '19':
            white_item_1 = 'Scrap Metal'
        elif white_item_1 ==  '20':
            white_item_1 = 'Stove'
        elif white_item_1 ==  '19':
            white_item_1 =  'Swamp Cooler'
        elif white_item_1 ==  '20':
            white_item_1 = 'Stove'
        elif white_item_1 ==  '21':
            white_item_1 ='Swamp Cooler'
        elif white_item_1 ==  '22':
            white_item_1 = 'Trash Compactor'
        elif white_item_1 ==  '23':
            white_item_1 = 'Washing Machine'


        # d = dict()
        # d.setdefault("DriverFirstName",last_edited_user )
        # d.setdefault("DriverLastName","Aguilar" )
        # d.setdefault("LastUpdatedBy", "SANSTAR1")
        # d.setdefault("HouseholdItem", white_item_1)
        # d.setdefault("Type", "Metal/Household Appliances")
        # d.setdefault("HouseHoldItemCount", white_qyt_1 )
        #
        #
        # l311.append(d)
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
        # dL311 = dict()
        # dL311.setdefault("La311MetalHouseholdAppliancesPickup", l311)
        # dResult.setdefault("ListOfLa311MetalHouseholdAppliancesPickup",dL311)
        #dOthers = dict()
        ##Adding empty dictionaries;
        #dResult.setdefault("ListOfLa311IllegalDumpingPickup", dOthers)
        #dResult.setdefault("ListOfLa311ManualPickup", dOthers)
        #dResult.setdefault("ListOfLa311MetalHouseholdAppliancesPickup", dOthers)
        #dResult.setdefault("ListOfLa311MoveInMoveOut", dOthers)
        #dResult.setdefault("ListOfLa311ServiceNotComplete", dOthers)
        #Ends of adding additional itmes ****************************************
        lResults.append({"MetaData": {}, "SRData": dResult})


        ii = ii + 1
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





