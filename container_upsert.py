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



pyFC = "SO_Container_Services_1"
clauseSBE = "WHERE RESOLUTION_CODE <> '0'"
if(__name__=='__main__'):
    # sMsg = printObjects()
    # print(sMsg)

    connstr = 'DRIVER={SQL Server};SERVER=67.203.12.190;DATABASE=ASC0; UID=SA;PWD=p8R151n17A9'
    # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
    conn = pyodbc.connect(connstr)
    cursor = conn.cursor()
    FN_SRNumber = "Numbercyla"
    lFields = [FN_SRNumber, "SO_DIST01", "SO_DIST02", "SO_DIST03", "SO_DIST04", "SO_DIST05", "SO_DIST06",  "last_edited_user","SO_DIST07", "SO_DIST08", "SO_DIST09", "SO_DIST10", "RESOLUTION_CODE", "SO_SN01","SO_SN02", "SO_SN03", "SO_SN04", "SO_SN05", "SO_SN06","SO_SN07","SO_SN08", "SO_SN09", "SO_SN10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","SO_Reas01", "SO_Reas02", "SO_Reas03", "SO_Reas04", "SO_Reas05", "SO_Reas06", "SO_Reas07", "SO_Reas08", "SO_Reas09", "SO_Reas10", "last_edited_date", "SR_Size_1", "SR_Size_2", "SR_Size_3", "SR_Size_4", "SR_Size_5", "SR_Size_6", "SR_Size_7", "SR_Size_8", "SR_Size_9", "SR_Size_10","SR_Color_1", "SR_Color_2", "SR_Color_3", "SR_Color_4", "SR_Color_5", "SR_Color_6", "SR_Color_7", "SR_Color_8", "SR_Color_9", "SR_Color_10" ]
    #lFields = ["SRNumber"]
    sFields = ""
    for fld in lFields:
        if(sFields==""):
            sFields = fld
        else:
            sFields = sFields + "," + fld
    #List of the fields you'd like to exclude, like ItemCount for example.
    lFieldsExcluded = [FN_SRNumber,"SO_DIST01", "SO_DIST02", "SO_DIST03", "SO_DIST04", "SO_DIST05", "SO_DIST06", "SO_DIST07", "SO_DIST08", "SO_DIST09", "SO_DIST10","ContactFirstName", "last_edtited_user", "ContactLastName", "RESOLUTION_CODE", "SO_SN01","SO_SN02", "SO_SN03", "SO_SN04", "SO_SN05", "SO_SN06","SO_SN07","SO_SN08", "SO_SN09", "SO_SN10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","SO_Reas01", "SO_Reas02", "SO_Reas03", "SO_Reas04", "SO_Reas05","SO_Reas06", "SO_Reas07", "SO_Reas08", "SO_Reas09", "SO_Reas10", "last_edited_date", "SR_Color_1", "SR_Color_2", "SR_Color_3", "SR_Color_4", "SR_Color_5", "SR_Color_6", "SR_Color_7", "SR_Color_8", "SR_Color_9", "SR_Color_10","SR_Size_1", "SR_Size_2", "SR_Size_3", "SR_Size_4", "SR_Size_5", "SR_Size_6", "SR_Size_7", "SR_Size_8", "SR_Size_9", "SR_Size_10", "last_edited_user" ]
    #lFields = ["SRNumber"]

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
    container_number_1 = ""
    container_number_2 = ""
    container_number_3 = ""
    container_number_4 = ""
    container_number_5 = ""
    container_number_6 = ""
    container_number_7 = ""
    container_number_8 = ""
    container_number_9 = ""
    container_number_10 = ""
    request_for_1 = " "
    request_for_2 = " "
    request_for_3 = " "
    request_for_4 = " "
    request_for_5 = " "
    request_for_6 = " "
    request_for_7 = " "
    request_for_8 = " "
    request_for_9 = " "
    request_for_10 = " "
    container_uid_1 = ""
    container_uid_2 = " "
    container_uid_3 = ""
    container_uid_4 = ""
    container_uid_5 = ""
    container_uid_6 = ""
    container_uid_7 = ""
    container_uid_8 = ""
    container_uid_9 = ""
    container_uid_10 = ""
    pickup_reason_1 = ""
    pickup_reason_2 = ""
    pickup_reason_3 = ""
    pickup_reason_4 = ""
    pickup_reason_5 = ""
    pickup_reason_6 = ""
    pickup_reason_7 = ""
    pickup_reason_8 = ""
    pickup_reason_9 = ""
    pickup_reason_10 = ""
    delivery_reason_1= ""
    delivery_reason_2 = ""
    delivery_reason_3= ""
    delivery_reason_4= ""
    delivery_reason_5= ""
    delivery_reason_6= ""
    delivery_reason_7= ""
    delivery_reason_8= ""
    delivery_reason_9= ""
    delivery_reason_10= ""
    container_size_1 = ""
    container_size_2 = ""
    container_size_3= ""
    container_size_4= ""
    container_size_5 = ""
    container_size_6=""
    container_size_7= ""
    container_size_8= ""
    container_size_9 = ""
    container_size_10= ""

    container_color_1 = ""
    container_color_2 = ""
    container_color_3 = ""
    container_color_4= ""
    container_color_5=""
    container_color_6=""
    container_color_7=""
    container_color_8= ""
    container_color_9 = ""
    container_color_10= ""
    container_type_1 = ""
    container_type_2 = ""
    container_type_3 = ""
    container_type_4 = ""
    container_type_5 = ""
    container_type_6 = ""
    container_type_7 = ""
    container_type_8 = ""
    container_type_9 = ""
    container_type_10 = ""


    rescode = ""
    reasoncode = " "
    container_uid = ""
    last_edited_user = " "

    for row in cursor.fetchall():
        lResults = []    #make sure lResults are initiated here
        lValues = []
        for i in range(len(columns)):
            lValues.append( str(row[i]))
        container_number_1 = (str(row[lFields.index("SO_SN01")]))
        container_number_2 = (str(row[lFields.index("SO_SN02")]))
        container_number_3 = (str(row[lFields.index("SO_SN03")]))
        container_number_4 = (str(row[lFields.index("SO_SN04")]))
        container_number_5 = (str(row[lFields.index("SO_SN05")]))
        container_number_6= (str(row[lFields.index("SO_SN06")]))
        container_number_7 =(str(row[lFields.index("SO_SN07")]))
        container_number_8 = (str(row[lFields.index("SO_SN08")]))
        container_number_9 =(str(row[lFields.index("SO_SN09")]))
        container_number_10 = (str(row[lFields.index("SO_SN10")]))

        request_for_1 = (str(row[lFields.index("SO_DIST01")]))
        request_for_2 = (str(row[lFields.index("SO_DIST02")]))
        request_for_3 = (str(row[lFields.index("SO_DIST03")]))
        request_for_4 = (str(row[lFields.index("SO_DIST04")]))
        request_for_5 = (str(row[lFields.index("SO_DIST05")]))
        request_for_6 = (str(row[lFields.index("SO_DIST06")]))
        request_for_7 = (str(row[lFields.index("SO_DIST07")]))
        request_for_8 = (str(row[lFields.index("SO_DIST08")]))
        request_for_9 = (str(row[lFields.index("SO_DIST09")]))
        request_for_10 = (str(row[lFields.index("SO_DIST10")]))


        pickup_reason_1 = (str(row[lFields.index("SO_Reas01")]))
        pickup_reason_2 = (str(row[lFields.index("SO_Reas02")]))
        pickup_reason_3 = (str(row[lFields.index("SO_Reas03")]))
        pickup_reason_4 = (str(row[lFields.index("SO_Reas04")]))
        pickup_reason_5 = (str(row[lFields.index("SO_Reas05")]))
        pickup_reason_6 = (str(row[lFields.index("SO_Reas06")]))
        pickup_reason_7 = (str(row[lFields.index("SO_Reas07")]))
        pickup_reason_8 = (str(row[lFields.index("SO_Reas08")]))
        pickup_reason_9 = (str(row[lFields.index("SO_Reas09")]))
        pickup_reason_10 = (str(row[lFields.index("SO_Reas10")]))



        delivery_reason_1 = (str(row[lFields.index("SO_Reas01")]))
        delivery_reason_2 = (str(row[lFields.index("SO_Reas02")]))
        delivery_reason_3 = (str(row[lFields.index("SO_Reas03")]))
        delivery_reason_4 = (str(row[lFields.index("SO_Reas04")]))
        delivery_reason_5 = (str(row[lFields.index("SO_Reas05")]))
        delivery_reason_6 = (str(row[lFields.index("SO_Reas06")]))
        delivery_reason_7 = (str(row[lFields.index("SO_Reas07")]))
        delivery_reason_8 = (str(row[lFields.index("SO_Reas08")]))
        delivery_reason_9 = (str(row[lFields.index("SO_Reas09")]))
        delivery_reason_10 = (str(row[lFields.index("SO_Reas10")]))


        container_size_1 = (str(row[lFields.index("SR_Size_1")]))
        container_size_2 = (str(row[lFields.index("SR_Size_2")]))
        container_size_3 = (str(row[lFields.index("SR_Size_3")]))
        container_size_4 = (str(row[lFields.index("SR_Size_4")]))
        container_size_5 = (str(row[lFields.index("SR_Size_5")]))
        container_size_6 = (str(row[lFields.index("SR_Size_6")]))
        container_size_7 = (str(row[lFields.index("SR_Size_7")]))
        container_size_8 = (str(row[lFields.index("SR_Size_8")]))
        container_size_9 = (str(row[lFields.index("SR_Size_9")]))
        container_size_10 = (str(row[lFields.index("SR_Size_10")]))


        container_color_1 = (str(row[lFields.index("SR_Color_1")]))
        container_color_2 = (str(row[lFields.index("SR_Color_2")]))
        container_color_3 = (str(row[lFields.index("SR_Color_3")]))
        container_color_4 = (str(row[lFields.index("SR_Color_4")]))
        container_color_5 = (str(row[lFields.index("SR_Color_5")]))
        container_color_6 = (str(row[lFields.index("SR_Color_6")]))
        container_color_7 = (str(row[lFields.index("SR_Color_7")]))
        container_color_8 = (str(row[lFields.index("SR_Color_8")]))
        container_color_9 = (str(row[lFields.index("SR_Color_9")]))
        container_color_10 = (str(row[lFields.index("SR_Color_10")]))




        container_uid_1 = (str(row[lFields.index("UID1")]))
        container_uid_2 = (str(row[lFields.index("UID2")]))
        container_uid_3 = (str(row[lFields.index("UID3")]))
        container_uid_4 = (str(row[lFields.index("UID4")]))
        container_uid_5 = (str(row[lFields.index("UID5")]))
        container_uid_6 = (str(row[lFields.index("UID6")]))
        container_uid_7 = (str(row[lFields.index("UID7")]))
        container_uid_8 = (str(row[lFields.index("UID8")]))
        container_uid_9 = (str(row[lFields.index("UID9")]))
        container_uid_10 = (str(row[lFields.index("UID10")]))

        rescode = (str(row[lFields.index("RESOLUTION_CODE")]))
        SRNumber = (str(row[lFields.index("Numbercyla")]))


        last_edited_user = (str(row[lFields.index("last_edited_user")]))

        print container_size_1
        print container_color_1

        #dResult = dict(zip(columns, row))
        dResult = dict(zip(columns, lValues))

        # Adding additional items  ******************************
        dResult.setdefault("ReasonCode", rescode if rescode.isdigit() else "")
        dResult.setdefault("UpdatedByUserLogin", "SANSTAR1")
        dResult.setdefault("SRNumber", SRNumber)
        dResult.setdefault("ResolutionCode",rescode if not rescode.isdigit() else "")

        if delivery_reason_1  == 'DAM':
            request_for_1 = 'Pickup'
        elif  delivery_reason_1 =='NCS':
             delivery_reason_1 = 'New Construction'
        elif  delivery_reason_1 =='ECP':
             delivery_reason_1 = 'Extra Capacity'
        elif  delivery_reason_1 == 'PCS':
             delivery_reason_1 = 'Private to City Service'
        elif delivery_reason_1  == "NVR":
         delivery_reason_1 == 'Never Received'
        elif delivery_reason_1  == "MIS":
            delivery_reason_1 = 'Missing'

        if delivery_reason_1  == 'DAM':
            delivery_reason_1 = ""
        if pickup_reason_1  == 'DAM':
            pickup_reason_1 = ""


        if  pickup_reason_1  == 'DAM':
            request_for_1 = 'Pickup'
        elif  pickup_reason_1 =='EXC':
             pickup_reason_1 = 'Exchange2'
        elif  pickup_reason_1 =='ECP':
             pickup_reason_1 = 'Extra Capacity (Billed)'
        elif pickup_reason_1  == "ABD":
         pickup_reason_1 = 'Abandoned'
        elif pickup_reason_1  == "PCS":
            pickup_reason_1 ='City to Private Service'
        elif pickup_reason_1  == "MIS":
            pickup_reason_1 = 'Missing'




        if  delivery_reason_2  == 'DAM':
            request_for_2 = 'Pickup'
        elif  delivery_reason_2 =='NCS':
             delivery_reason_2 = 'New Construction'
        elif  delivery_reason_2 =='ECP':
             delivery_reason_2 = 'Extra Capacity'
        elif  delivery_reason_2 == 'PCS':
             delivery_reason_2 = 'Private to City Service'
        elif delivery_reason_2  == "NVR":
         delivery_reason_2 == 'Never Received'
        elif delivery_reason_2  == "MIS":
            delivery_reason_2 == 'Missing'



        if  pickup_reason_2  == 'DAM':
            request_for_2 = 'Pickup'
        elif  pickup_reason_2 =='EXC':
             pickup_reason_2 = 'Exchange2'
        elif  pickup_reason_2 =='ECP':
             pickup_reason_2 = 'Extra Capacity (Billed)'
        elif pickup_reason_2  == "ABD":
         pickup_reason_2 == 'Abandoned'
        elif pickup_reason_2  == "CPS":
            pickup_reason_2 == 'City to Private Service'










        if  delivery_reason_3  == 'DAM':
            request_for_3 = 'Damage'
        elif  delivery_reason_3 =='NCS':
             delivery_reason_3 = 'New Construction'
        elif  delivery_reason_3 =='ECP':
             delivery_reason_3 = 'Extra Capacity'
        elif  delivery_reason_3 == 'PCS':
             delivery_reason_3 = 'Private to City Service'
        elif delivery_reason_3  == "NVR":
         delivery_reason_3 == 'Never Received'
        elif delivery_reason_3  == "MIS":
            delivery_reason_3 == 'Missing'



        if  pickup_reason_3  == 'DAM':
            request_for_3 = 'Damage'
        elif  pickup_reason_3 =='EXC':
             pickup_reason_3 = 'Exchange2'
        elif  pickup_reason_3 =='ECP':
             pickup_reason_3 = 'Extra Capacity (Billed)'
        elif pickup_reason_3  == "ABD":
         pickup_reason_3 == 'Abandoned'
        elif pickup_reason_3  == "CPS":
            pickup_reason_3 == 'City to Private Service'





        if  delivery_reason_4  == 'DAM':
            request_for_4 = 'Damage'
        elif  delivery_reason_4 =='NCS':
             delivery_reason_4 = 'New Construction'
        elif  delivery_reason_4 =='ECP':
             delivery_reason_4 = 'Extra Capacity'
        elif  delivery_reason_4 == 'PCS':
             delivery_reason_4 = 'Private to City Service'
        elif delivery_reason_4  == "NVR":
         delivery_reason_4 == 'Never Received'
        elif delivery_reason_4  == "MIS":
            delivery_reason_4 == 'Missing'



        if  pickup_reason_4  == 'DAM':
            request_for_4 = 'Damage'
        elif  pickup_reason_4 =='EXC':
             pickup_reason_4 = 'Exchange2'
        elif  pickup_reason_4 =='ECP':
             pickup_reason_4 = 'Extra Capacity (Billed)'
        elif pickup_reason_4  == "ABD":
         pickup_reason_4 == 'Abandoned'
        elif pickup_reason_4  == "CPS":
            pickup_reason_4 == 'City to Private Service'






        if  delivery_reason_5  == 'DAM':
            request_for_5 = 'Damage'
        elif  delivery_reason_5 =='NCS':
             delivery_reason_5 = 'New Construction'
        elif  delivery_reason_5 =='ECP':
             delivery_reason_5 = 'Extra Capacity'
        elif  delivery_reason_5 == 'PCS':
             delivery_reason_5 = 'Private to City Service'
        elif delivery_reason_5  == "NVR":
         delivery_reason_5 == 'Never Received'
        elif delivery_reason_5  == "MIS":
            delivery_reason_5 == 'Missing'



        if  pickup_reason_5  == 'DAM':
            request_for_5 = 'Damage'
        elif  pickup_reason_5 =='EXC':
             pickup_reason_5 = 'Exchange2'
        elif  pickup_reason_5 =='ECP':
             pickup_reason_5 = 'Extra Capacity (Billed)'
        elif pickup_reason_5  == "ABD":
         pickup_reason_5 == 'Abandoned'
        elif pickup_reason_5  == "CPS":
            pickup_reason_5 == 'City to Private Service'






        if  delivery_reason_6  == 'DAM':
            request_for_6 = 'Damage'
        elif  delivery_reason_6 =='NCS':
             delivery_reason_6 = 'New Construction'
        elif  delivery_reason_6 =='ECP':
             delivery_reason_6 = 'Extra Capacity'
        elif  delivery_reason_6 == 'PCS':
             delivery_reason_6 = 'Private to City Service'
        elif delivery_reason_6  == "NVR":
         delivery_reason_6 == 'Never Received'
        elif delivery_reason_6  == "MIS":
            delivery_reason_6 == 'Missing'



        if  pickup_reason_6  == 'DAM':
            request_for_6 = 'Damage'
        elif  pickup_reason_6 =='EXC':
             pickup_reason_6 = 'Exchange2'
        elif  pickup_reason_6 =='ECP':
             pickup_reason_6 = 'Extra Capacity (Billed)'
        elif pickup_reason_6  == "ABD":
         pickup_reason_6 == 'Abandoned'
        elif pickup_reason_6  == "CPS":
            pickup_reason_6 == 'City to Private Service'






        if  delivery_reason_7  == 'DAM':
            request_for_7 = 'Damage'
        elif  delivery_reason_7 =='NCS':
             delivery_reason_7 = 'New Construction'
        elif  delivery_reason_7 =='ECP':
             delivery_reason_7 = 'Extra Capacity'
        elif  delivery_reason_7 == 'PCS':
             delivery_reason_7 = 'Private to City Service'
        elif delivery_reason_7  == "NVR":
         delivery_reason_7 == 'Never Received'
        elif delivery_reason_7  == "MIS":
            delivery_reason_7 == 'Missing'



        if  pickup_reason_7  == 'DAM':
            request_for_7 = 'Damage'
        elif  pickup_reason_7 =='EXC':
             pickup_reason_7 = 'Exchange2'
        elif  pickup_reason_7 =='ECP':
             pickup_reason_7 = 'Extra Capacity (Billed)'
        elif pickup_reason_7  == "ABD":
         pickup_reason_7 == 'Abandoned'
        elif pickup_reason_7  == "CPS":
            pickup_reason_7 == 'City to Private Service'






        if  delivery_reason_8  == 'DAM':
            request_for_8 = 'Damage'
        elif  delivery_reason_8 =='NCS':
             delivery_reason_8 = 'New Construction'
        elif  delivery_reason_8 =='ECP':
             delivery_reason_8 = 'Extra Capacity'
        elif  delivery_reason_8 == 'PCS':
             delivery_reason_8 = 'Private to City Service'
        elif delivery_reason_8  == "NVR":
         delivery_reason_8 == 'Never Received'
        elif delivery_reason_8  == "MIS":
            delivery_reason_8 == 'Missing'



        if  pickup_reason_8  == 'DAM':
            request_for_8 = 'Damage'
        elif  pickup_reason_8 =='EXC':
             pickup_reason_8 = 'Exchange8'
        elif  pickup_reason_8 =='ECP':
             pickup_reason_8 = 'Extra Capacity (Billed)'
        elif pickup_reason_8  == "ABD":
         pickup_reason_8 == 'Abandoned'
        elif pickup_reason_8  == "CPS":
            pickup_reason_8 == 'City to Private Service'


        if  delivery_reason_9  == 'DAM':
            request_for_9 = 'Damage'
        elif  delivery_reason_9 =='NCS':
             delivery_reason_9 = 'New Construction'
        elif  delivery_reason_9 =='ECP':
             delivery_reason_9 = 'Extra Capacity'
        elif  delivery_reason_9 == 'PCS':
             delivery_reason_9 = 'Private to City Service'
        elif delivery_reason_9  == "NVR":
         delivery_reason_9 == 'Never Received'
        elif delivery_reason_9  == "MIS":
            delivery_reason_9 == 'Missing'



        if  pickup_reason_9  == 'DAM':
            request_for_9 = 'Damage'
        elif  pickup_reason_9 =='EXC':
             pickup_reason_9 = 'Exchange2'
        elif  pickup_reason_9 =='ECP':
             pickup_reason_9 = 'Extra Capacity (Billed)'
        elif pickup_reason_9  == "ABD":
         pickup_reason_9 == 'Abandoned'
        elif pickup_reason_9  == "CPS":
            pickup_reason_9 == 'City to Private Service'




        if  delivery_reason_10  == 'DAM':
            request_for_10 = 'Damage'
        elif  delivery_reason_10 =='NCS':
             delivery_reason_10 = 'New Construction'
        elif  delivery_reason_10 =='ECP':
             delivery_reason_10 = 'Extra Capacity'
        elif  delivery_reason_10 == 'PCS':
             delivery_reason_10 = 'Private to City Service'
        elif delivery_reason_10  == "NVR":
         delivery_reason_10 == 'Never Received'
        elif delivery_reason_10  == "MIS":
            delivery_reason_10 == 'Missing'



        if  pickup_reason_10  == 'DAM':
            request_for_10 = 'Damage'
        elif  pickup_reason_10 =='EXC':
             pickup_reason_10 = 'Exchange10'
        elif  pickup_reason_10 =='ECP':
             pickup_reason_10 = 'Extra Capacity (Billed)'
        elif pickup_reason_10  == "ABD":
         pickup_reason_10 == 'Abandoned'
        elif pickup_reason_10  == "CPS":
            pickup_reason_10 == 'City to Private Service'





        if request_for_1 == 'Pickup':
            delivery_reason_1 = ""
            
        

        if request_for_1 == 'Pickup':
            pickup_reason_ = ""










        if request_for_1 == 'P':
            request_for_1 = "Pickup"


        if request_for_1 == 'I':
            request_for_1 = "Delivery"



        if request_for_1 == 'DAMAGE':
            request_for_1 = "Pickup"



        if request_for_2 == 'P':
            request_for_2 = "Pickup"


        if request_for_2 == 'I':
            request_for_2 = "Delivery"



        if request_for_2 == 'DAMAGE':
            request_for_2 = "Pickup"

        if request_for_3 == 'P':
            request_for_3 = "Pickup"


        if request_for_3 == 'I':
            request_for_3 = "Delivery"



        if request_for_3 == 'DAMAGE':
            request_for_3 = "Pickup"




        if request_for_4 == 'P':
            request_for_4 = "Pickup"


        if request_for_4 == 'I':
            request_for_4 = "Delivery"



        if request_for_4 == 'DAMAGE':
            request_for_4 = "Pickup"


        if request_for_5 == 'P':
            request_for_5 = "Pickup"


        if request_for_5 == 'I':
            request_for_5 = "Delivery"



        if request_for_5 == 'DAMAGE':
            request_for_5 = "Pickup"





        if request_for_6 == 'P':
            request_for_6 = "Pickup"


        if request_for_6 == 'I':
            request_for_6 = "Delivery"



        if request_for_6 == 'DAMAGE':
            request_for_6 = "Pickup"




        if request_for_7 == 'P':
            request_for_7 = "Pickup"


        if request_for_7 == 'I':
            request_for_7 = "Delivery"



        if request_for_7 == 'DAMAGE':
            request_for_7 = "Pickup"



        if request_for_8 == 'P':
            request_for_8 = "Pickup"


        if request_for_8 == 'I':
            request_for_8 = "Delivery"



        if request_for_8 == 'DAMAGE':
            request_for_8 = "Pickup"




        if request_for_9 == 'P':
            request_for_9 = "Pickup"


        if request_for_9 == 'I':
            request_for_9 = "Delivery"



        if request_for_9 == 'DAMAGE':
            request_for_9 = "Pickup"


        if request_for_10 == 'P':
            request_for_10 = "Pickup"


        if request_for_10 == 'I':
            request_for_10 = "Delivery"



        if request_for_10 == 'DAMAGE':
            request_for_10 = "Pickup"












        container_type_1 = ""
        container_type_2 = ""
        container_type_3 = ""
        container_type_4 = ""
        container_type_5 = ""
        container_type_6 = ""
        container_type_7 = ""
        container_type_8 = ""
        container_type_9 = ""
        container_type_10 = ""



        if "90" in container_size_1 and "BLU" in container_color_1:
            container_type_1 = "90 Gallon (Large) Blue"

        elif "90" in container_size_1 and "BLK" in container_color_1:
            container_type_1 = "90 Gallon (Large) Black"

        elif "60" in container_size_1 and "BLU" in container_color_1:
            container_type_1 = "60 Gallon (Regular) Blue"

        elif "30" in container_size_1 and "BLU" in container_color_1:
            container_type_1 = "30 Gallon (Small) Blue"

        elif "30" in container_size_1 and "GRN" in container_color_1:
            container_type_1 = "30 Gallon (Small) Green"

        elif "60" in container_size_1 and "BRN" in container_color_1:
            container_type_1 = "60 Gallon (Regular) Brown"


        elif "60" in container_size_1 and "BLK" in container_color_1:
            container_type_1 = "60 Gallon (Regular) Black"


        elif "60" in container_size_1 and "GRN" in container_color_1:
            container_type_1 = "60 Gallon (Regular) Green"


        if  '30' in container_size_1 and 'BLK' in container_color_1:
            container_type_1 = "30 Gallon (Small) Black"


        if "90" in container_size_2 and "BLU" in container_color_2:
            container_type_2 = "90 Gallon (Large) Blue"

        elif "90" in container_size_2 and "BLK" in container_color_2:
            container_type_2 = "90 Gallon (Large) Black"

        elif "60" in container_size_2 and "BLU" in container_color_2:
            container_type_2 = "60 Gallon (Regular) Blue"

        elif "30" in container_size_2 and "BLU" in container_color_2:
            container_type_2 = "30 Gallon (Small) Blue"


        elif "30" in container_size_2 and "GRN" in container_color_2:
            container_type_2 = "30 Gallon (Small) Green"

        elif "60" in container_size_2 and "BRN" in container_color_2:
            container_type_2 = "60 Gallon (Regular) Brown"


        elif "60" in container_size_2 and "BLK" in container_color_2:
            container_type_2 = "60 Gallon (Regular) Black"


        elif "60" in container_size_2 and "GRN" in container_color_2:
            container_type_2 = "60 Gallon (Regular) Green"


        elif  '30' in container_size_2 and "BLK" in container_color_2:
            ContainerSize2 = "30 Gallon (Small) Black"



        if "90" in container_size_3 and "BLU" in container_color_3:
            container_type_3 = "90 Gallon (Large) Blue"

        elif "90" in container_size_3 and "BLK" in container_color_3:
            container_type_3 = "90 Gallon (Large) Black"

        elif "60" in container_size_3 and "BLU" in container_color_3:
            container_type_3 = "60 Gallon (Regular) Blue"

        elif "30" in container_size_3 and "BLU" in container_color_3:
            container_type_3 = "30 Gallon (Small) Blue"


        elif "30" in container_size_3 and "GRN" in container_color_3:
            container_type_3 = "30 Gallon (Small) Green"

        elif "60" in container_size_3 and "BRN" in container_color_3:
            container_type_3 = "60 Gallon (Regular) Brown"


        elif "60" in container_size_3 and "BLK" in container_color_3:
            container_type_3 = "60 Gallon (Regular) Black"


        elif "60" in container_size_3 and "GRN" in container_color_3:
            container_type_3 = "60 Gallon (Regular) Green"


        elif  "30" in container_size_3 and "BLK" in container_color_3:
            container_type_4 = "30 Gallon (Small) Black"


        if "90" in container_size_4 and "BLU" in container_color_4:
            container_type_4 = "90 Gallon (Large) Blue"

        elif "90" in container_size_4 and "BLK" in container_color_4:
            container_type_4 = "90 Gallon (Large) Black"

        elif "60" in container_size_4 and "BLU" in container_color_4:
            container_type_4 = "60 Gallon (Regular) Blue"

        elif "30" in container_size_4 and "BLU" in container_color_4:
            container_type_4 = "30 Gallon (Small) Blue"


        elif "30" in container_size_4 and "GRN" in container_color_4:
            container_type_4 = "30 Gallon (Small) Green"

        elif "60" in container_size_4 and "BRN" in container_color_4:
            container_type_4 = "60 Gallon (Regular) Brown"


        elif "60" in container_size_4 and "BLK" in container_color_4:
            container_type_4 = "60 Gallon (Regular) Black"


        elif "60" in container_size_4 and "GRN" in container_color_4:
            container_type_4 = "60 Gallon (Regular) Green"


        elif  "30" in container_size_4 and "BLK" in container_color_4:
            container_type_4 = "30 Gallon (Small) Black"


        if "90" in container_size_5 and "BLU" in container_color_5:
            container_type_5 = "90 Gallon (Large) Blue"

        elif "90" in container_size_5 and "BLK" in container_color_5:
            container_type_5 = "90 Gallon (Large) Black"

        elif "60" in container_size_5 and "BLU" in container_color_5:
            container_type_5 = "60 Gallon (Regular) Blue"

        elif "30" in container_size_5 and "BLU" in container_color_5:
            container_type_5 = "30 Gallon (Small) Blue"


        elif "30" in container_size_5 and "GRN" in container_color_5:
            container_type_5 = "30 Gallon (Small) Green"

        elif "60" in container_size_5 and "Brown" in container_color_5:
            container_type_5 = "60 Gallon (Regular) Brown"


        elif "60" in container_size_5 and "BLK" in container_color_5:
            container_type_5 = "60 Gallon (Regular) Black"


        elif "60" in container_size_5 and "GRN" in container_color_5:
            container_type_5 = "60 Gallon (Regular) Green"


        elif  "30" in container_size_5 and "BLK" in container_color_5:
            container_type_5 = "30 Gallon (Small) Black"


        if "90" in container_size_6 and "BLU" in container_color_6:
            container_type_6 = "90 Gallon (Large) Blue"

        elif "90" in container_size_6 and "BLK" in container_color_6:
            container_type_6 = "90 Gallon (Large) Black"

        elif "60" in container_size_6 and "BLU" in container_color_6:
            container_type_6 = "60 Gallon (Regular) Blue"

        elif "30" in container_size_6 and "BLU" in container_color_6:
            container_type_6 = "30 Gallon (Small) Blue"


        elif "30" in container_size_6 and "GRN" in container_color_6:
            container_type_6 = "30 Gallon (Small) Green"

        elif "60" in container_size_6 and "Brown" in container_color_6:
            container_type_6 = "60 Gallon (Regular) Brown"


        elif "60" in container_size_6 and "BLK" in container_color_6:
            container_type_6 = "60 Gallon (Regular) Black"


        elif "60" in container_size_6 and "GRN" in container_color_6:
            container_type_6 = "60 Gallon (Regular) Green"


        elif  "30" in container_size_6 and "BLK" in container_color_6:
            container_type_6 = "30 Gallon (Small) Black"



        if "90" in container_size_7 and "BLU" in container_color_7:
            container_type_7 = "90 Gallon (Large) Blue"

        elif "90" in container_size_7 and "BLK" in container_color_7:
            container_type_7 = "90 Gallon (Large) Black"

        elif "60" in container_size_7 and "BLU" in container_color_7:
            container_type_7 = "60 Gallon (Regular) Blue"

        elif "30" in container_size_7 and "BLU" in container_color_7:
            container_type_7 = "30 Gallon (Small) Blue"


        elif "30" in container_size_7 and "GRN" in container_color_7:
            container_type_7 = "30 Gallon (Small) Green"

        elif "60" in container_size_7 and "Brown" in container_color_7:
            container_type_7 = "60 Gallon (Regular) Brown"


        elif "60" in container_size_7 and "BLK" in container_color_7:
            container_type_7 = "60 Gallon (Regular) Black"


        elif "60" in container_size_7 and "GRN" in container_color_7:
            container_type_7 = "60 Gallon (Regular) Green"


        elif  "30" in container_size_7 and "BLK" in container_color_7:
            container_type_7 = "30 Gallon (Small) Black"

        if "90" in container_size_8 and "BLU" in container_color_8:
            container_type_8 = "90 Gallon (Large) Blue"

        elif "90" in container_size_8 and "BLK" in container_color_8:
            container_type_8 = "90 Gallon (Large) Black"

        elif "60" in container_size_8 and "BLU" in container_color_8:
            container_type_8 = "60 Gallon (Regular) Blue"

        elif "30" in container_size_8 and "BLU" in container_color_8:
            container_type_8 = "30 Gallon (Small) Blue"


        elif "30" in container_size_8 and "GRN" in container_color_8:
            container_type_8 = "30 Gallon (Small) Green"

        elif "60" in container_size_8 and "Brown" in container_color_8:
            container_type_8 = "60 Gallon (Regular) Brown"


        elif "60" in container_size_8 and "BLK" in container_color_8:
            container_type_8 = "60 Gallon (Regular) Black"


        elif "60" in container_size_8 and "GRN" in container_color_8:
            container_type_8 = "60 Gallon (Regular) Green"


        elif  "30" in container_size_8 and "BLK" in container_color_8:
            container_type_8 = "30 Gallon (Small) Black"



        if "90" in container_size_9 and "BLU" in container_color_9:
            container_type_9 = "90 Gallon (Large) Blue"

        elif "90" in container_size_9 and "BLK" in container_color_9:
            container_type_9 = "90 Gallon (Large) Black"

        elif "60" in container_size_9 and "BLU" in container_color_9:
            container_type_9 = "60 Gallon (Regular) Blue"

        elif "30" in container_size_9 and "BLU" in container_color_9:
            container_type_9 = "30 Gallon (Small) Blue"


        elif "30" in container_size_9 and "GRN" in container_color_9:
            container_type_9 = "30 Gallon (Small) Green"

        elif "60" in container_size_9 and "Brown" in container_color_9:
            container_type_9 = "60 Gallon (Regular) Brown"


        elif "60" in container_size_9 and "BLK" in container_color_9:
            container_type_9 = "60 Gallon (Regular) Black"


        elif "60" in container_size_9 and "GRN" in container_color_9:
            container_type_9 = "60 Gallon (Regular) Green"


        elif  "30" in container_size_9 and "BLK" in container_color_9:
            container_type_9 = "30 Gallon (Small) Black"


        if "90" in container_size_10 and "BLU" in container_color_10:
            container_type_10 = "90 Gallon (Large) Blue"

        elif "90" in container_size_10 and "BLK" in container_color_10:
            container_type_10 = "90 Gallon (Large) Black"

        elif "60" in container_size_10 and "BLU" in container_color_10:
            container_type_10 = "60 Gallon (Regular) Blue"

        elif "30" in container_size_10 and "BLU" in container_color_10:
            container_type_10 = "30 Gallon (Small) Blue"


        elif "30" in container_size_10 and "GRN" in container_color_10:
            container_type_10 = "30 Gallon (Small) Green"

        elif "60" in container_size_10 and "Brown" in container_color_10:
            container_type_10 = "60 Gallon (Regular) Brown"


        elif "60" in container_size_10 and "BLK" in container_color_10:
            container_type_10 = "60 Gallon (Regular) Black"


        elif "60" in container_size_10 and "GRN" in container_color_10:
            container_type_10 = "60 Gallon (Regular) Green"


        elif  "30" in container_size_10 and "BLK" in container_color_10:
            container_type_10 = "30 Gallon (Small) Black"


        # dResult.setdefault("ListOfLa311DeadAnimalRemoval", dict())
        l311 = []

        if last_edited_user == "SA":
            last_edited_user = "SANSTAR PROXY"

        firstName, lastName = last_edited_user.split()

        print firstName
        print lastName
        print container_type_1


        dL311 = dict()
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName)
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ContainerNumber", container_number_1)
        d.setdefault("Type", "Containers")
        d.setdefault("Name", container_uid_1 )
        d.setdefault("RequestFor", request_for_1)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("DeliveryReason", delivery_reason_1)
        d.setdefault("PickupReason", pickup_reason_1)
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        d.setdefault("ContainerSize", container_type_1)
        l311.append(d)
        dL311 = dict()
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverFirstName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ContainerNumber", container_number_2)
        d.setdefault("Type", "Containers")
        d.setdefault("Name", container_uid_2)
        d.setdefault("RequestFor", request_for_2)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        d.setdefault("ContainerSize", container_type_2)
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverFirstName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ContainerNumber", container_number_3)
        d.setdefault("Type", "Containers")
        d.setdefault("Name", container_uid_3)
        d.setdefault("RequestFor", request_for_3)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        d.setdefault("ContainerSize", container_type_3)
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverFirstName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ContainerNumber", container_number_4)
        d.setdefault("Type", "Containers")
        d.setdefault("Name", container_uid_4)
        d.setdefault("RequestFor", request_for_4)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        d.setdefault("ContainerSize", container_type_4)
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverFirstName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ContainerNumber", container_number_5)
        d.setdefault("Type", "Containers")
        d.setdefault("Name", container_uid_5)
        d.setdefault("RequestFor", request_for_5)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        d.setdefault("ContainerSize", container_type_5)
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverFirstName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ContainerNumber", container_number_6)
        d.setdefault("Type", "Containers")
        d.setdefault("Name", container_uid_6)
        d.setdefault("RequestFor", request_for_6)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        d.setdefault("ContainerSize", container_type_6)




        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverFirstName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ContainerNumber", container_number_7)
        d.setdefault("Type", "Containers")
        d.setdefault("Name", container_uid_7)
        d.setdefault("RequestFor", request_for_7)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        d.setdefault("ContainerSize", container_type_7)

        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverFirstName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ContainerNumber", container_number_8)
        d.setdefault("Type", "Containers")
        d.setdefault("Name", container_uid_8)
        d.setdefault("RequestFor", request_for_8)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        d.setdefault("ContainerSize", container_type_8)
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",last_edited_user)
        d.setdefault("DriverFirstName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ContainerNumber", container_number_9)
        d.setdefault("Type", "Containers")
        d.setdefault("Name", container_uid_9)
        d.setdefault("RequestFor", request_for_9)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        d.setdefault("ContainerSize", container_type_9)
        l311.append(d)
        d = dict()
        d.setdefault("DriverFirstName",last_edited_user)
        d.setdefault("DriverFirstName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ContainerNumber", container_number_10)
        d.setdefault("Type", "Containers")
        d.setdefault("Name", container_uid_10)
        d.setdefault("RequestFor", request_for_10)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        d.setdefault("ContainerSize", container_type_10)
        l311.append(d)
        #
        lIndexes = []
        nCnt = len(l311)
        for i in range(nCnt):
            d = l311[i]
            if(d['Name'].strip() == '') or (d['Name'].strip() == "None"):
                del d['Name']

            if(d['ContainerNumber'] == "None"):
                lIndexes.append(i)

        if(len(lIndexes)>0):
            for i in reversed(lIndexes):
                del l311[i]

        if(len(l311)>0):
                dL311.setdefault("La311Containers", l311)
                dResult.setdefault("ListOfLa311Containers",dL311)
                lResults.append({"MetaData": {}, "SRData": dResult})
                sReq = json.dumps(dResult,sort_keys=True, indent=2)
                results = {"MetaData": {}, "SRData": dResult}
                sReqj = json.dumps(results,sort_keys=True, indent=2)
                print sReqj
                url = "https://myla311Test.lacity.org/myla311router/mylasrbe/1/UpsertSANSRWithCodes"
                headers = {'Content-type': 'text/plain', 'Accept': '/'}
                r = requests.post(url, data= json.dumps(results), headers=headers,  verify=False)
                # print results
                print r.text
                # print 'It took', time.time()-start, 'seconds.'


                # ii = ii + 1
                # print (str(ii) + " recs sent to server.",  'It took', time.time()-start, 'seconds.')

    print("Finished")
except Exception,e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
