__author__ = 'GeoffreyWest'


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
import sys, os




pyFC = "SO_SC"
clauseSBE = "WHERE RESOLUTION_CODE <> '' AND  Category LIKE '%1%' OR Category LIKE '%2%' OR Category LIKE '%18%' "
if(__name__=='__main__'):
    # sMsg = printObjects()
    # print(sMsg)

    connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
    # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
    conn = pyodbc.connect(connstr)
    cursor = conn.cursor()
    FN_SRNumber = "NumberCYLA"
    lFields = ["NumberCYLA","RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user"]
    #lFields = ["SRNumber"]
    sFields = ""
    for fld in lFields:
        if(sFields==""):
            sFields = fld
        else:
            sFields = sFields + "," + fld
    #List of the fields you'd like to exclude, like ItemCount for example.
    lFieldsExcluded = ["NumberCYLA","RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user"]

    #sSQL = "SELECT SRNumber FROM {}".format(pyFC)
    sSQL = "SELECT {} FROM {}  {}".format(sFields, pyFC, clauseSBE)


    cursor.execute(sSQL)
    #columns = [column[0] for column in cursor.description]
    columns = []
    for column in cursor.description:
        if not (column[0] in lFieldsExcluded):
            columns.append(column[0])




try:
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
    bulky_qyt_1 = " "
    bulky_qyt_2 = " "
    bulky_qyt_3 = " "
    bulky_qyt_4 = " "
    bulky_qyt_5 = " "
    bulky_qyt_6 = " "
    bulky_qyt_7 = " "
    bulky_qyt_8 = " "
    bulky_qyt_9 = " "
    bulky_qyt_10 = " "
    bulky_uid_1 = ""
    bulky_uid_2 = " "
    bulky_uid_3 = ""
    bulky_uid_4 = ""
    bulky_uid_5 = ""
    bulky_uid_6 = ""
    bulky_uid_7 = ""
    bulky_uid_8 = ""
    bulky_uid_9 = ""
    bulky_uid_10 = ""
    rescode = ""
    reasoncode = " "
    ewaste_uid = ""
    last_edited_user = " "
    SRNumber = ''


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
        bulky_item_6= (str(row[lFields.index("ITEM_6")]))
        bulky_item_7 =(str(row[lFields.index("ITEM_7")]))
        bulky_item_8 = (str(row[lFields.index("ITEM_8")]))
        bulky_item_9 =(str(row[lFields.index("ITEM_9")]))
        bulky_item_10 = (str(row[lFields.index("ITEM_10")]))

        bulky_qyt_1 = (str(row[lFields.index("QYT_1")]))
        bulky_qyt_2 = (str(row[lFields.index("QYT_2")]))
        bulky_qyt_3 = (str(row[lFields.index("QYT_3")]))
        bulky_qyt_4 = (str(row[lFields.index("QYT_4")]))
        bulky_qyt_5 = (str(row[lFields.index("QYT_5")]))
        bulky_qyt_6 = (str(row[lFields.index("QTY_6")]))
        bulky_qyt_7 = (str(row[lFields.index("QTY_7")]))
        bulky_qyt_8 = (str(row[lFields.index("QTY_8")]))
        bulky_qyt_9 = (str(row[lFields.index("QTY_9")]))
        bulky_qyt_10 = (str(row[lFields.index("QTY_10")]))

        bulky_uid_1 = (str(row[lFields.index("UID1")]))
        bulky_uid_2 = (str(row[lFields.index("UID2")]))
        bulky_uid_3 = (str(row[lFields.index("UID3")]))
        bulky_uid_4 = (str(row[lFields.index("UID4")]))
        bulky_uid_5 = (str(row[lFields.index("UID5")]))
        bulky_uid_6 = (str(row[lFields.index("UID6")]))
        bulky_uid_7 = (str(row[lFields.index("UID7")]))
        bulky_uid_8 = (str(row[lFields.index("UID8")]))
        bulky_uid_9 = (str(row[lFields.index("UID9")]))
        bulky_uid_10 = (str(row[lFields.index("UID10")]))


        rescode = (str(row[lFields.index("RESOLUTION_CODE")]))
        SRNumber = (str(row[lFields.index("NumberCYLA")]))


        last_edited_user = (str(row[lFields.index("last_edited_user")]))

        #dResult = dict(zip(columns, row))
        dResult = dict(zip(columns, lValues))

        # Adding additional items  ******************************
        dResult.setdefault("ReasonCode", rescode if rescode.isdigit() else "")
        dResult.setdefault("UpdatedByUserLogin", "SANSTAR1")
        dResult.setdefault("SRNumber", SRNumber)
        dResult.setdefault("ResolutionCode",rescode if not rescode.isdigit() else "")
        # dResult.setdefault("ListOfLa311DeadAnimalRemoval", dict())
        dItemKeyValueList = dict()
        dItemKeyValueList.setdefault('None','None')
        dItemKeyValueList.setdefault('1','Other')
        dItemKeyValueList.setdefault('2','Basketball Set')
        dItemKeyValueList.setdefault('3','Bed Frame')
        dItemKeyValueList.setdefault('4','Bicycle Parts')
        dItemKeyValueList.setdefault('5','Bird Cage (Plastic)')
        dItemKeyValueList.setdefault('6','Blinds')
        dItemKeyValueList.setdefault('7','Bookcase')
        dItemKeyValueList.setdefault('8','Box Any Size')
        dItemKeyValueList.setdefault('9','Box  Spring')
        dItemKeyValueList.setdefault('10','Cabinet')
        dItemKeyValueList.setdefault('11','Car Parts')
        dItemKeyValueList.setdefault('12','Carpet')
        dItemKeyValueList.setdefault('79','Child Day Bed')
        dItemKeyValueList.setdefault('14','Crib')
        dItemKeyValueList.setdefault('15','Curtain Rod')
        dItemKeyValueList.setdefault('16','Cushions')
        dItemKeyValueList.setdefault('17','Pipes (Metal)')
        dItemKeyValueList.setdefault('18','pool heater')
        dItemKeyValueList.setdefault('19','Scrap Metal')
        dItemKeyValueList.setdefault('20','Stove')
        dItemKeyValueList.setdefault('21','Dresser')
        dItemKeyValueList.setdefault('22','Entertainment Center')
        dItemKeyValueList.setdefault('23','Fan (Any Size)')
        dItemKeyValueList.setdefault('24','Fence (Wood)')
        dItemKeyValueList.setdefault('25','File Cabinet (Wood')
        dItemKeyValueList.setdefault('26','Garage Door')
        dItemKeyValueList.setdefault('80','Gate (Wood)')
        dItemKeyValueList.setdefault('29','Glass Window in Frame')
        dItemKeyValueList.setdefault('30','Headboard (Wood)')
        dItemKeyValueList.setdefault('31','Ladders (Wood')
        dItemKeyValueList.setdefault('32','Lamp')
        dItemKeyValueList.setdefault('33','Light Fixture)')
        dItemKeyValueList.setdefault('34','Loose Debris)')
        dItemKeyValueList.setdefault('35','Mattress)')
        dItemKeyValueList.setdefault('36','Mirror')
        dItemKeyValueList.setdefault('37','Other')
        dItemKeyValueList.setdefault('38','Pallet')
        dItemKeyValueList.setdefault('39','Patio Umbrella')
        dItemKeyValueList.setdefault('40','Patio Furniture')
        dItemKeyValueList.setdefault('41','Piano')
        dItemKeyValueList.setdefault('42','Planter Pot')
        dItemKeyValueList.setdefault('43','Playpen')
        dItemKeyValueList.setdefault('44','Pool Cover')
        dItemKeyValueList.setdefault('45','Rain Gutter')
        dItemKeyValueList.setdefault('46','Recliner')
        dItemKeyValueList.setdefault('47','Rug)')
        dItemKeyValueList.setdefault('48','Shelf')
        dItemKeyValueList.setdefault('49','Shopping Cart')
        dItemKeyValueList.setdefault('50','Shower Door')
        dItemKeyValueList.setdefault('51','Shutter')
        dItemKeyValueList.setdefault('52','Sink')
        dItemKeyValueList.setdefault('53','Sliding Door')
        dItemKeyValueList.setdefault('54','Sofa')
        dItemKeyValueList.setdefault('55','Sofa Bed')
        dItemKeyValueList.setdefault('56','Spa Cover')
        dItemKeyValueList.setdefault('57','Spa/Jacuzzi')
        dItemKeyValueList.setdefault('58','Stroller')
        dItemKeyValueList.setdefault('59','Suitcase')
        dItemKeyValueList.setdefault('60','Table')
        dItemKeyValueList.setdefault('61','Tank Any Size)')
        dItemKeyValueList.setdefault('62','Tire Less Than 5')
        dItemKeyValueList.setdefault('63','Toilet')
        dItemKeyValueList.setdefault('64','Toys (Large Ones)')
        dItemKeyValueList.setdefault('65','Trash Cans')
        dItemKeyValueList.setdefault('66','Trunk')
        dItemKeyValueList.setdefault('67','Tub (Non Metal)')
        dItemKeyValueList.setdefault('68','Vaccum')
        dItemKeyValueList.setdefault('69','Vehicle Tire')
        dItemKeyValueList.setdefault('70','Walker')
        dItemKeyValueList.setdefault('71','Window (Glass in Frame)')
        dItemKeyValueList.setdefault('72','Window Frame')
        dItemKeyValueList.setdefault('73','Windows')
        dItemKeyValueList.setdefault('74','Wood Boards')
        dItemKeyValueList.setdefault('75','Wood Bundles')
        dItemKeyValueList.setdefault('76','Wood Cabinets')
        dItemKeyValueList.setdefault('77','Artificial Christmas tree')




        if(bulky_item_1 in dItemKeyValueList): bulky_item_1 = dItemKeyValueList[bulky_item_1]
        bulky_item_2 = dItemKeyValueList[bulky_item_2]
        bulky_item_3 = dItemKeyValueList[bulky_item_3]
        bulky_item_4 = dItemKeyValueList[bulky_item_4]
        bulky_item_5 = dItemKeyValueList[bulky_item_5]
        bulky_item_6 = dItemKeyValueList[bulky_item_6]
        bulky_item_7 = dItemKeyValueList[bulky_item_7]
        bulky_item_8 = dItemKeyValueList[bulky_item_8]
        bulky_item_9 = dItemKeyValueList[bulky_item_9]
        bulky_item_10 = dItemKeyValueList[bulky_item_10]

        if last_edited_user == "SA":
            last_edited_user = "Sanstar Proxy"

        if last_edited_user == "Manuel P Rodriguez":
            last_edited_user = "Manuel Rodriguez"


        if last_edited_user == "Herbert Gomez":
            last_edited_user = "Herbert Gomez"

        if last_edited_user == "Esri_Anonymous":
            last_edited_user = "Esri Anonymous"


        # print last_edited_user



        firstName, lastName = last_edited_user.split()


        dL311 = dict()
        l311 = []
        d = dict()
        d.setdefault("DriverFirstName",firstName)
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("BulkyItemType", bulky_item_1)
        d.setdefault("Type", "Bulky Items")
        d.setdefault("Name", bulky_uid_1 )
        d.setdefault("BulkyItemCount", bulky_qyt_1)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)
        dL311 = dict()
        d = dict()
        d.setdefault("DriverFirstName",firstName)
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("BulkyItemType", bulky_item_2)
        d.setdefault("Type", "Bulky Items")
        d.setdefault("Name", bulky_uid_2)
        d.setdefault("BulkyItemCount", bulky_qyt_2)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")

        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName)
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("BulkyItemType", bulky_item_3)
        d.setdefault("Type", "Bulky Items")
        d.setdefault("Name", bulky_uid_3)
        d.setdefault("BulkyItemCount", bulky_qyt_3)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")

        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("BulkyItemType", bulky_item_4)
        d.setdefault("Type", "Bulky Items")
        d.setdefault("Name", bulky_uid_4)
        d.setdefault("BulkyItemCount", bulky_qyt_4)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("BulkyItemType", bulky_item_5)
        d.setdefault("Type", "Bulky Items")
        d.setdefault("Name", bulky_uid_5)
        d.setdefault("BulkyItemCount", bulky_qyt_5)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName)
        d.setdefault("DriverLastName", lastName)
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("BulkyItemType", bulky_item_6)
        d.setdefault("Type", "Bulky Items")
        d.setdefault("Name", bulky_uid_6)
        d.setdefault("BulkyItemCount", bulky_qyt_6)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("BulkyItemType", bulky_item_7)
        d.setdefault("Type", "Bulky Items")
        d.setdefault("Name", bulky_uid_7)
        d.setdefault("BulkyItemCount", bulky_qyt_7)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName", lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("BulkyItemType", bulky_item_8)
        d.setdefault("Type", "Bulky Items")
        d.setdefault("Name", bulky_uid_8)
        d.setdefault("BulkyItemCount", bulky_qyt_8)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName)
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("BulkyItemType", bulky_item_9)
        d.setdefault("Type", "Bulky Items")
        d.setdefault("Name", bulky_uid_9)
        d.setdefault("BulkyItemCount", bulky_qyt_9)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName)
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("BulkyItemType", bulky_item_10)
        d.setdefault("Type", "Bulky Items")
        d.setdefault("Name", bulky_uid_10)
        d.setdefault("BulkyItemCount", bulky_qyt_10)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)
        test = "a"
        print test

        lIndexes = []
        nCnt = len(l311)
        for i in range(nCnt):
            d = l311[i]
            if(d['Name'].strip() == ''):
                del d['Name']

            if(d['BulkyItemCount'] == "None") or (d['BulkyItemType'] == "None")  :
                lIndexes.append(i)
        if(len(lIndexes)>0):
            for i in reversed(lIndexes):
                del l311[i]

        if(len(l311)>0):
            dL311.setdefault("BulkyItem", l311)
            dResult.setdefault("ListOfLa311BulkyItem",dL311)
            sReq = json.dumps(dResult,sort_keys=True, indent=2)
            results = {"MetaData": {}, "SRData": dResult}
            sReqj = json.dumps(results,sort_keys=True, indent=2)
            print sReqj
            # start = time.time()

            #
            # start = time.time()
            # url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSRWithCodes"
            # headers = {'Content-type': 'text/plain', 'Accept': '/'}
            # r = requests.post(url, data= json.dumps(results), headers=headers,  verify=False)
            # print r.text

            # with open('C:\Users\GeoffreyWest\Desktop\'rlsts.txt', 'a') as f:
            #     for row in r.text
            #      print row
            #     f.write("%s\n" % str(row))


            # print 'It took', time.time()-start, 'seconds.'

            ii = ii + 1
            # print (str(ii) + " recs sent to server.",  'It took', time.time()-start, 'seconds.')





    print("Finished")
except Exception,e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)



