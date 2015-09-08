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
def printObjects():
    lResults = []
    dResult = dict()
    # Adding additional items  ******************************
    dResult.setdefault("AddressVerifield", "Y")
    dResult.setdefault("ReasonCode", "")
    dResult.setdefault("ResolutionCode", "0")
    #dResult.setdefault("ListOfLa311ElectronicWaste", dict())
    l311 = []
    d = dict()
    d.setdefault("DriverFirstName", "Geoffrey")
    d.setdefault("DriverLastName", "West")
    d.setdefault("ElectronicWasteType", "Cell Phone")
    d.setdefault("Type", "Electronic Waste")
    d.setdefault("ItemCount", 2)
    l311.append(d)
    d = dict()
    d.setdefault("DriverFirstName", "Geoffrey")
    d.setdefault("DriverLastName", "West")
    d.setdefault("ElectronicWasteType", "Cell Phone")
    d.setdefault("Type", "Electronic Waste")
    d.setdefault("ItemCount", 2)
    l311.append(d)
    dL311 = dict()
    dL311.setdefault("La311ElectronicWaste", l311)
    dResult.setdefault("ListOfLa311ElectronicWaste",dL311)
    dOthers = dict()
    #Adding empty dictionaries;
    dResult.setdefault("ListOfLa311IllegalDumpingPickup", dOthers)
    dResult.setdefault("ListOfLa311ManualPickup", dOthers)
    dResult.setdefault("ListOfLa311MetalHouseholdAppliancesPickup", dOthers)
    dResult.setdefault("ListOfLa311MoveInMoveOut", dOthers)
    dResult.setdefault("ListOfLa311ServiceNotComplete", dOthers)
    #Ends of adding additional itmes ****************************************
    lResults.append({"MetaData": {}, "SRData": dResult})

    sMsg = json.dumps(lResults, sort_keys=True, indent=4)
    print(sMsg)

if(__name__=='__main__'):
    sMsg = printObjects()
    print(sMsg)

    connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
    # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
    conn = pyodbc.connect(connstr)
    cursor = conn.cursor()
    FN_SRNumber = "SRNumber"
    lFields = [FN_SRNumber, "ItemDesc"]
    #lFields = ["SRNumber"]
    sFields = ""
    for fld in lFields:
        if(sFields==""):
            sFields = fld
        else:
            sFields = sFields + "," + fld
    #List of the fields you'd like to exclude, like ItemCount for example.
    lFieldsExcluded = ["ItemDesc"]


    #sSQL = "SELECT SRNumber FROM {}".format(pyFC)
    sSQL = "SELECT {} FROM {} WHERE {}".format(sFields, pyFC)

    cursor.execute(sSQL)
    #columns = [column[0] for column in cursor.description]
    columns = []
    for column in cursor.description:
        if not (column[0] in lFieldsExcluded):
            columns.append(column[0])


    ii = 0
    sItemDesc = ""
    for row in cursor.fetchall():
        lResults = []    #make sure lResults are initiated here
        lValues = []
        for i in range(len(columns)):
            lValues.append( str(row[i]))
        sItemDesc= (str(row[lFields.index("ItemDesc")]))
        #dResult = dict(zip(columns, row))
        dResult = dict(zip(columns, lValues))

        # Adding additional items  ******************************
        dResult.setdefault("AddressVerifield", "Y")
        dResult.setdefault("ReasonCode", "")
        dResult.setdefault("ResolutionCode", "0")
        #dResult.setdefault("ListOfLa311ElectronicWaste", dict())
        l311 = []
        d = dict()
        d.setdefault("DriverFirstName", "Geoffrey")
        d.setdefault("DriverLastName", "West")
        d.setdefault("ElectronicWasteType", "Cell Phone")
        d.setdefault("Type", "Electronic Waste")
        d.setdefault("ItemCount", sItemDesc)
        l311.append(d)
        #d = dict()
        #d.setdefault("DriverFirstName", "Geoffrey")
        #d.setdefault("DriverLastName", "West")
        #d.setdefault("ElectronicWasteType", "Cell Phone")
        #d.setdefault("Type", "Electronic Waste")
        #d.setdefault("ItemCount", 2)
        #l311.append(d)
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

        ii = ii + 1
        print(json.dumps(lResults, sort_keys=True, indent=4))
    #     for outputs in lResults:
    #         #url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSR"
    #         url = "https://myla311RemoteTest.lacity.org/myla311router/mylasrbe/1/UpsertSANSR"
    #         headers = {'Content-type': 'text/plain', 'Accept': '/'}
    #         r = requests.post(url, data= json.dumps(outputs), headers=headers,  verify=False)
    #         #print 'It took', time.time()-start, 'seconds.'
    #         print r.text
    #         print (str(ii) + ". " + str(len(lResults)), 'It took', time.time()-start, 'seconds.' )
    #
    # print("Finished")

