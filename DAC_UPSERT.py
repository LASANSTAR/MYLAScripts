__author__ = 'Administrator'
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
import sys, os
#
#
# start = time.time()
# pyFC = "import_311"
# clauseSBE = "WHERE CATEGORY = 4 OR CATEGORY =  19 AND RESOLUTION_CODE <> ''  AND RESOLUTION_CODE <> '0'"
# if(__name__=='__main__'):
#     # sMsg = printObjects()
#     # print(sMsg)
#
#     connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
#     # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
#     conn = pyodbc.connect(connstr)
#     cursor = conn.cursor()
#     FN_SRNumber = "NumberCYLA"
#     lFields = [FN_SRNumber, "RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user", "last_edited_date"]
#     #lFields = ["SRNumber"]
#     sFields = ""
#     for fld in lFields:
#         if(sFields==""):
#             sFields = fld
#         else:
#             sFields = sFields + "," + fld
#     #List of the fields you'd like to exclude, like ItemCount for example.
#     lFieldsExcluded = ["RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user", "last_edited_date"]
#
#     #sSQL = "SELECT SRNumber FROM {}".format(pyFC)
#     sSQL = "SELECT {} FROM {}  {}".format(sFields, pyFC, clauseSBE)
#
#     cursor.execute(sSQL)
#     #columns = [column[0] for column in cursor.description]
#     columns = []
#     for column in cursor.description:
#         if not (column[0] in lFieldsExcluded):
#             columns.append(column[0])
#
# #
# #
# #
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
#     dar_qyt_1 = " "
#     dar_qyt_2 = " "
#     dar_qyt_3 = " "
#     dar_qyt_4 = " "
#     dar_qyt_5 = " "
#     dar_qyt_6 = " "
#     dar_qyt_7 = " "
#     dar_qyt_8 = " "
#     dar_qyt_9 = " "
#     dar_qyt_10 = " "
#     dar_uid_1 = ""
#     dar_uid_2 = " "
#     dar_uid_3 = ""
#     dar_uid_4 = ""
#     dar_uid_5 = ""
#     dar_uid_6 = ""
#     dar_uid_7 = ""
#     dar_uid_8 = ""
#     dar_uid_9 = ""
#     dar_uid_10 = ""
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
#         dar_qyt_2 = (str(row[lFields.index("QYT_2")]))
#         dar_qyt_3 = (str(row[lFields.index("QYT_3")]))
#         dar_qyt_4 = (str(row[lFields.index("QYT_4")]))
#         dar_qyt_5 = (str(row[lFields.index("QYT_5")]))
#         dar_qyt_6 = (str(row[lFields.index("QTY_6")]))
#         dar_qyt_7 = (str(row[lFields.index("QTY_7")]))
#         dar_qyt_8 = (str(row[lFields.index("QTY_8")]))
#         dar_qyt_9 = (str(row[lFields.index("QTY_9")]))
#         dar_qyt_10 = (str(row[lFields.index("QTY_10")]))
#
#
#
#
#
#
#         dar_uid_1 = (str(row[lFields.index("UID1")]))
#         dar_uid_2 = (str(row[lFields.index("UID2")]))
#         dar_uid_3 = (str(row[lFields.index("UID3")]))
#         dar_uid_4 = (str(row[lFields.index("UID4")]))
#         dar_uid_5 = (str(row[lFields.index("UID5")]))
#         dar_uid_6 = (str(row[lFields.index("UID6")]))
#         dar_uid_7 = (str(row[lFields.index("UID7")]))
#         dar_uid_8 = (str(row[lFields.index("UID8")]))
#         dar_uid_9 = (str(row[lFields.index("UID9")]))
#         dar_uid_10 = (str(row[lFields.index("UID10")]))
#
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
#         # dResult.setdefault("ListOfLa311DeadAnimalRemoval", dict())
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
#         elif dar_item_1  == 'None':
#             dar_item_1 = ' '
#
#
#
#         if  dar_item_2  == '7':
#             dar_item_2 = 'Coyote '
#         elif  dar_item_2 =='1':
#              dar_item_2 = 'Alligator'
#         elif  dar_item_2 == '2':
#              dar_item_2 = 'Bat'
#         elif dar_item_2  == "3":
#             dar_item_2 = 'Bird'
#         elif  dar_item_2== '4':
#              dar_item_2  = 'Cat'
#         elif  dar_item_2  == '5':
#              dar_item_2  = 'Chicken'
#         elif  dar_item_2  == '6':
#             dar_item_2  = 'Cow'
#         elif  dar_item_2  == '8':
#             dar_item_2 = 'Crow (Pigeon Size)'
#         elif  dar_item_2 == '9':
#             dar_item_2  = 'Deer'
#         elif  dar_item_2 == '10':
#             dar_item_2 = 'Dog'
#         elif  dar_item_2  == '11':
#             dar_item_2 = 'Duck'
#         elif  dar_item_2 == '16':
#             dar_item_2  = 'Llama'
#         elif  dar_item_2 == '12':
#              dar_item_2 = 'Heater'
#         elif  dar_item_2  == '13':
#              dar_item_2 = 'Fox'
#         elif  dar_item_2 == '14':
#             dar_item_2 = 'Geese'
#         elif  dar_item_2 == '15':
#             dar_item_2  = 'Guts'
#         elif  dar_item_2 == '17':
#              dar_item_2 = 'Monkey'
#         elif dar_item_2 ==  '18':
#             dar_item_2 = 'Opposum'
#         elif dar_item_2 ==  '25':
#             dar_item_2 = 'Seal'
#         elif dar_item_2 ==  '19':
#             dar_item_2 = 'Owl'
#         elif dar_item_2 ==  '20':
#             dar_item_2 = 'Peacock'
#         elif dar_item_2 ==  '19':
#             dar_item_2 =  'Swamp Cooler'
#         elif dar_item_2 ==  '20':
#             dar_item_2 = 'Stove'
#         elif dar_item_2 ==  '21':
#             dar_item_2 ='Pig'
#         elif dar_item_2 ==  '22':
#             dar_item_2 = 'Rabbit'
#         elif dar_item_2 ==  '23':
#             dar_item_2 = 'Racoon'
#         elif dar_item_2 ==  '24':
#             dar_item_2 = 'Rats'
#         elif dar_item_2 ==  '26':
#             dar_item_2 = 'Sheep'
#         elif dar_item_2 ==  '27':
#             dar_item_2 = 'Snake'
#         elif dar_item_2 ==  '28':
#             dar_item_2 = 'Spoiled Meat'
#         elif dar_item_2 ==  '29':
#             dar_item_2 = 'Squirrel'
#         elif dar_item_2 ==  '30':
#             dar_item_2 = 'Turkey'
#         elif dar_item_2 ==  '31':
#             dar_item_2 = 'Turtle'
#         elif dar_item_2 ==  '32':
#             dar_item_2 = 'Unknown'
#         elif dar_item_2 ==  '33':
#             dar_item_2 = 'Skunk'
#         elif dar_item_2 ==  '34':
#             dar_item_2 = 'Raven (Chicken Size)'
#         elif dar_item_2 ==  '35':
#             dar_item_2 = 'Raven (Unknown Size)'
#         elif dar_item_2 ==  '36':
#             dar_item_2 = 'Other'
#         elif dar_item_2  == 'None':
#             dar_item_2 = ' '
#
#
#
#         if  dar_item_3  == '7':
#             dar_item_3 = 'Coyote '
#         elif  dar_item_3 =='1':
#              dar_item_3 = 'Alligator'
#         elif  dar_item_3 == '2':
#              dar_item_3 = 'Bat'
#         elif dar_item_3  == "3":
#             dar_item_3 = 'Bird'
#         elif  dar_item_3== '4':
#              dar_item_3  = 'Cat'
#         elif  dar_item_3  == '5':
#              dar_item_3  = 'Chicken'
#         elif  dar_item_3  == '6':
#             dar_item_3  = 'Cow'
#         elif  dar_item_3  == '8':
#             dar_item_3 = 'Crow (Pigeon Size)'
#         elif  dar_item_3 == '9':
#             dar_item_3  = 'Deer'
#         elif  dar_item_3 == '10':
#             dar_item_3 = 'Dog'
#         elif  dar_item_3  == '11':
#             dar_item_3 = 'Duck'
#         elif  dar_item_3 == '16':
#             dar_item_3  = 'Llama'
#         elif  dar_item_3 == '12':
#              dar_item_3 = 'Heater'
#         elif  dar_item_3  == '13':
#              dar_item_3 = 'Fox'
#         elif  dar_item_3 == '14':
#             dar_item_3 = 'Geese'
#         elif  dar_item_3 == '15':
#             dar_item_3  = 'Guts'
#         elif  dar_item_3 == '17':
#              dar_item_3 = 'Monkey'
#         elif dar_item_3 ==  '18':
#             dar_item_3 = 'Opposum'
#         elif dar_item_3 ==  '25':
#             dar_item_3 = 'Seal'
#         elif dar_item_3 ==  '19':
#             dar_item_3 = 'Owl'
#         elif dar_item_3 ==  '20':
#             dar_item_3 = 'Peacock'
#         elif dar_item_3 ==  '19':
#             dar_item_3 =  'Swamp Cooler'
#         elif dar_item_3 ==  '20':
#             dar_item_3 = 'Stove'
#         elif dar_item_3 ==  '21':
#             dar_item_3 ='Pig'
#         elif dar_item_3 ==  '22':
#             dar_item_3 = 'Rabbit'
#         elif dar_item_3 ==  '23':
#             dar_item_3 = 'Racoon'
#         elif dar_item_3 ==  '24':
#             dar_item_3 = 'Rats'
#         elif dar_item_3 ==  '26':
#             dar_item_3 = 'Sheep'
#         elif dar_item_3 ==  '27':
#             dar_item_3 = 'Snake'
#         elif dar_item_3 ==  '28':
#             dar_item_3 = 'Spoiled Meat'
#         elif dar_item_3 ==  '29':
#             dar_item_3 = 'Squirrel'
#         elif dar_item_3 ==  '30':
#             dar_item_3 = 'Turkey'
#         elif dar_item_3 ==  '31':
#             dar_item_3 = 'Turtle'
#         elif dar_item_3 ==  '32':
#             dar_item_3 = 'Unknown'
#         elif dar_item_3 ==  '33':
#             dar_item_3 = 'Skunk'
#         elif dar_item_3 ==  '34':
#             dar_item_3 = 'Raven (Chicken Size)'
#         elif dar_item_3 ==  '35':
#             dar_item_3 = 'Raven (Unknown Size)'
#         elif dar_item_3 ==  '36':
#             dar_item_3 = 'Other'
#
#         elif dar_item_3  == 'None':
#             dar_item_3 = ' '
#
#
#
#
#
#         if  dar_item_4  == '7':
#             dar_item_4 = 'Coyote '
#         elif  dar_item_4 =='1':
#              dar_item_4 = 'Alligator'
#         elif  dar_item_4 == '2':
#              dar_item_4 = 'Bat'
#         elif dar_item_4  == "3":
#             dar_item_4 = 'Bird'
#         elif  dar_item_4== '4':
#              dar_item_4  = 'Cat'
#         elif  dar_item_4  == '5':
#              dar_item_4  = 'Chicken'
#         elif  dar_item_4  == '6':
#             dar_item_4  = 'Cow'
#         elif  dar_item_4  == '8':
#             dar_item_4 = 'Crow (Pigeon Size)'
#         elif  dar_item_4 == '9':
#             dar_item_4  = 'Deer'
#         elif  dar_item_4 == '10':
#             dar_item_4 = 'Dog'
#         elif  dar_item_4  == '11':
#             dar_item_4 = 'Duck'
#         elif  dar_item_4 == '16':
#             dar_item_4  = 'Llama'
#         elif  dar_item_4 == '12':
#              dar_item_4 = 'Heater'
#         elif  dar_item_4  == '13':
#              dar_item_4 = 'Fox'
#         elif  dar_item_4 == '14':
#             dar_item_4 = 'Geese'
#         elif  dar_item_4 == '15':
#             dar_item_4  = 'Guts'
#         elif  dar_item_4 == '17':
#              dar_item_4 = 'Monkey'
#         elif dar_item_4 ==  '18':
#             dar_item_4 = 'Opposum'
#         elif dar_item_4 ==  '25':
#             dar_item_4 = 'Seal'
#         elif dar_item_4 ==  '19':
#             dar_item_4 = 'Owl'
#         elif dar_item_4 ==  '20':
#             dar_item_4 = 'Peacock'
#         elif dar_item_4 ==  '19':
#             dar_item_4 =  'Swamp Cooler'
#         elif dar_item_4 ==  '20':
#             dar_item_4 = 'Stove'
#         elif dar_item_4 ==  '21':
#             dar_item_4 ='Pig'
#         elif dar_item_4 ==  '22':
#             dar_item_4 = 'Rabbit'
#         elif dar_item_4 ==  '23':
#             dar_item_4 = 'Racoon'
#         elif dar_item_4 ==  '24':
#             dar_item_4 = 'Rats'
#         elif dar_item_4 ==  '26':
#             dar_item_4 = 'Sheep'
#         elif dar_item_4 ==  '27':
#             dar_item_4 = 'Snake'
#         elif dar_item_4 ==  '28':
#             dar_item_4 = 'Spoiled Meat'
#         elif dar_item_4 ==  '29':
#             dar_item_4 = 'Squirrel'
#         elif dar_item_4 ==  '30':
#             dar_item_4 = 'Turkey'
#         elif dar_item_4 ==  '31':
#             dar_item_4 = 'Turtle'
#         elif dar_item_4 ==  '32':
#             dar_item_4 = 'Unknown'
#         elif dar_item_4 ==  '33':
#             dar_item_4 = 'Skunk'
#         elif dar_item_4 ==  '34':
#             dar_item_4 = 'Raven (Chicken Size)'
#         elif dar_item_4 ==  '35':
#             dar_item_4 = 'Raven (Unknown Size)'
#         elif dar_item_4 ==  '36':
#             dar_item_4 = 'Other'
#         elif dar_item_4  == 'None':
#             dar_item_4 = ' '
#
#
#
#         if  dar_item_5  == '7':
#             dar_item_5 = 'Coyote '
#         elif  dar_item_5 =='1':
#              dar_item_5 = 'Alligator'
#         elif  dar_item_5 == '2':
#              dar_item_5 = 'Bat'
#         elif dar_item_5  == "3":
#             dar_item_5 = 'Bird'
#         elif  dar_item_5== '4':
#              dar_item_5  = 'Cat'
#         elif  dar_item_5  == '5':
#              dar_item_5  = 'Chicken'
#         elif  dar_item_5  == '6':
#             dar_item_5  = 'Cow'
#         elif  dar_item_5  == '8':
#             dar_item_5 = 'Crow (Pigeon Size)'
#         elif  dar_item_5 == '9':
#             dar_item_5  = 'Deer'
#         elif  dar_item_5 == '10':
#             dar_item_5 = 'Dog'
#         elif  dar_item_5  == '11':
#             dar_item_5 = 'Duck'
#         elif  dar_item_5 == '16':
#             dar_item_5  = 'Llama'
#         elif  dar_item_5 == '12':
#              dar_item_5 = 'Heater'
#         elif  dar_item_5  == '13':
#              dar_item_5 = 'Fox'
#         elif  dar_item_5 == '14':
#             dar_item_5 = 'Geese'
#         elif  dar_item_5 == '15':
#             dar_item_5  = 'Guts'
#         elif  dar_item_5 == '17':
#              dar_item_5 = 'Monkey'
#         elif dar_item_5 ==  '18':
#             dar_item_5 = 'Opposum'
#         elif dar_item_5 ==  '25':
#             dar_item_5 = 'Seal'
#         elif dar_item_5 ==  '19':
#             dar_item_5 = 'Owl'
#         elif dar_item_5 ==  '20':
#             dar_item_5 = 'Peacock'
#         elif dar_item_5 ==  '19':
#             dar_item_5 =  'Swamp Cooler'
#         elif dar_item_5 ==  '20':
#             dar_item_5 = 'Stove'
#         elif dar_item_5 ==  '21':
#             dar_item_5 ='Pig'
#         elif dar_item_5 ==  '22':
#             dar_item_5 = 'Rabbit'
#         elif dar_item_5 ==  '23':
#             dar_item_5 = 'Racoon'
#         elif dar_item_5 ==  '24':
#             dar_item_5 = 'Rats'
#         elif dar_item_5 ==  '26':
#             dar_item_5 = 'Sheep'
#         elif dar_item_5 ==  '27':
#             dar_item_5 = 'Snake'
#         elif dar_item_5 ==  '28':
#             dar_item_5 = 'Spoiled Meat'
#         elif dar_item_5 ==  '29':
#             dar_item_5 = 'Squirrel'
#         elif dar_item_5 ==  '30':
#             dar_item_5 = 'Turkey'
#         elif dar_item_5 ==  '31':
#             dar_item_5 = 'Turtle'
#         elif dar_item_5 ==  '32':
#             dar_item_5 = 'Unknown'
#         elif dar_item_5 ==  '33':
#             dar_item_5 = 'Skunk'
#         elif dar_item_5 ==  '34':
#             dar_item_5 = 'Raven (Chicken Size)'
#         elif dar_item_5 ==  '35':
#             dar_item_5 = 'Raven (Unknown Size)'
#         elif dar_item_5 ==  '36':
#             dar_item_5 = 'Other'
#         elif dar_item_5  == 'None':
#             dar_item_5 = ' '
#
#
#
#         if  dar_item_6  == '7':
#             dar_item_6 = 'Coyote '
#         elif  dar_item_6 =='1':
#              dar_item_6 = 'Alligator'
#         elif  dar_item_6 == '2':
#              dar_item_6 = 'Bat'
#         elif dar_item_6  == "3":
#             dar_item_6 = 'Bird'
#         elif  dar_item_6== '4':
#              dar_item_6  = 'Cat'
#         elif  dar_item_6  == '5':
#              dar_item_6  = 'Chicken'
#         elif  dar_item_6  == '6':
#             dar_item_6  = 'Cow'
#         elif  dar_item_6  == '8':
#             dar_item_6 = 'Crow (Pigeon Size)'
#         elif  dar_item_6 == '9':
#             dar_item_6  = 'Deer'
#         elif  dar_item_6 == '10':
#             dar_item_6 = 'Dog'
#         elif  dar_item_6  == '11':
#             dar_item_6 = 'Duck'
#         elif  dar_item_6 == '16':
#             dar_item_6  = 'Llama'
#         elif  dar_item_6 == '12':
#              dar_item_6 = 'Heater'
#         elif  dar_item_6  == '13':
#              dar_item_6 = 'Fox'
#         elif  dar_item_6 == '14':
#             dar_item_6 = 'Geese'
#         elif  dar_item_6 == '15':
#             dar_item_6  = 'Guts'
#         elif  dar_item_6 == '17':
#              dar_item_6 = 'Monkey'
#         elif dar_item_6 ==  '18':
#             dar_item_6 = 'Opposum'
#         elif dar_item_6 ==  '25':
#             dar_item_6 = 'Seal'
#         elif dar_item_6 ==  '19':
#             dar_item_6 = 'Owl'
#         elif dar_item_6 ==  '20':
#             dar_item_6 = 'Peacock'
#         elif dar_item_6 ==  '19':
#             dar_item_6 =  'Swamp Cooler'
#         elif dar_item_6 ==  '20':
#             dar_item_6 = 'Stove'
#         elif dar_item_6 ==  '21':
#             dar_item_6 ='Pig'
#         elif dar_item_6 ==  '22':
#             dar_item_6 = 'Rabbit'
#         elif dar_item_6 ==  '23':
#             dar_item_6 = 'Racoon'
#         elif dar_item_6 ==  '24':
#             dar_item_6 = 'Rats'
#         elif dar_item_6 ==  '26':
#             dar_item_6 = 'Sheep'
#         elif dar_item_6 ==  '27':
#             dar_item_6 = 'Snake'
#         elif dar_item_6 ==  '28':
#             dar_item_6 = 'Spoiled Meat'
#         elif dar_item_6 ==  '29':
#             dar_item_6 = 'Squirrel'
#         elif dar_item_6 ==  '30':
#             dar_item_6 = 'Turkey'
#         elif dar_item_6 ==  '31':
#             dar_item_6 = 'Turtle'
#         elif dar_item_6 ==  '32':
#             dar_item_6 = 'Unknown'
#         elif dar_item_6 ==  '33':
#             dar_item_6 = 'Skunk'
#         elif dar_item_6 ==  '34':
#             dar_item_6 = 'Raven (Chicken Size)'
#         elif dar_item_6 ==  '35':
#             dar_item_6 = 'Raven (Unknown Size)'
#         elif dar_item_6 ==  '36':
#             dar_item_6 = 'Other'
#         elif dar_item_6  == 'None':
#             dar_item_6 = ' '
#
#
#         if  dar_item_7  == '7':
#             dar_item_7 = 'Coyote '
#         elif  dar_item_7 =='1':
#              dar_item_7 = 'Alligator'
#         elif  dar_item_7 == '2':
#              dar_item_7 = 'Bat'
#         elif dar_item_7  == "3":
#             dar_item_7 = 'Bird'
#         elif  dar_item_7== '4':
#              dar_item_7  = 'Cat'
#         elif  dar_item_7  == '5':
#              dar_item_7  = 'Chicken'
#         elif  dar_item_7  == '6':
#             dar_item_7  = 'Cow'
#         elif  dar_item_7  == '8':
#             dar_item_7 = 'Crow (Pigeon Size)'
#         elif  dar_item_7 == '9':
#             dar_item_7  = 'Deer'
#         elif  dar_item_7 == '10':
#             dar_item_7 = 'Dog'
#         elif  dar_item_7  == '11':
#             dar_item_7 = 'Duck'
#         elif  dar_item_7 == '16':
#             dar_item_7  = 'Llama'
#         elif  dar_item_7 == '12':
#              dar_item_7 = 'Heater'
#         elif  dar_item_7  == '13':
#              dar_item_7 = 'Fox'
#         elif  dar_item_7 == '14':
#             dar_item_7 = 'Geese'
#         elif  dar_item_7 == '15':
#             dar_item_7  = 'Guts'
#         elif  dar_item_7 == '17':
#              dar_item_7 = 'Monkey'
#         elif dar_item_7 ==  '18':
#             dar_item_7 = 'Opposum'
#         elif dar_item_7 ==  '25':
#             dar_item_7 = 'Seal'
#         elif dar_item_7 ==  '19':
#             dar_item_7 = 'Owl'
#         elif dar_item_7 ==  '20':
#             dar_item_7 = 'Peacock'
#         elif dar_item_7 ==  '19':
#             dar_item_7 =  'Swamp Cooler'
#         elif dar_item_7 ==  '20':
#             dar_item_7 = 'Stove'
#         elif dar_item_7 ==  '21':
#             dar_item_7 ='Pig'
#         elif dar_item_7 ==  '22':
#             dar_item_7 = 'Rabbit'
#         elif dar_item_7 ==  '23':
#             dar_item_7 = 'Racoon'
#         elif dar_item_7 ==  '24':
#             dar_item_7 = 'Rats'
#         elif dar_item_7 ==  '26':
#             dar_item_7 = 'Sheep'
#         elif dar_item_7 ==  '27':
#             dar_item_7 = 'Snake'
#         elif dar_item_7 ==  '28':
#             dar_item_7 = 'Spoiled Meat'
#         elif dar_item_7 ==  '29':
#             dar_item_7 = 'Squirrel'
#         elif dar_item_7 ==  '30':
#             dar_item_7 = 'Turkey'
#         elif dar_item_7 ==  '31':
#             dar_item_7 = 'Turtle'
#         elif dar_item_7 ==  '32':
#             dar_item_7 = 'Unknown'
#         elif dar_item_7 ==  '33':
#             dar_item_7 = 'Skunk'
#         elif dar_item_7 ==  '34':
#             dar_item_7 = 'Raven (Chicken Size)'
#         elif dar_item_7 ==  '35':
#             dar_item_7 = 'Raven (Unknown Size)'
#         elif dar_item_7 ==  '36':
#             dar_item_7 = 'Other'
#
#         elif dar_item_7  == 'None':
#             dar_item_7 = ' '
#
#
#         if  dar_item_8  == '7':
#             dar_item_8 = 'Coyote '
#         elif  dar_item_8 =='1':
#              dar_item_8 = 'Alligator'
#         elif  dar_item_8 == '2':
#              dar_item_8 = 'Bat'
#         elif dar_item_8  == "3":
#             dar_item_8 = 'Bird'
#         elif  dar_item_8== '4':
#              dar_item_8  = 'Cat'
#         elif  dar_item_8  == '5':
#              dar_item_8  = 'Chicken'
#         elif  dar_item_8  == '6':
#             dar_item_8  = 'Cow'
#         elif  dar_item_8  == '8':
#             dar_item_8 = 'Crow (Pigeon Size)'
#         elif  dar_item_8 == '9':
#             dar_item_8  = 'Deer'
#         elif  dar_item_8 == '10':
#             dar_item_8 = 'Dog'
#         elif  dar_item_8  == '11':
#             dar_item_8 = 'Duck'
#         elif  dar_item_8 == '16':
#             dar_item_8  = 'Llama'
#         elif  dar_item_8 == '12':
#              dar_item_8 = 'Heater'
#         elif  dar_item_8  == '13':
#              dar_item_8 = 'Fox'
#         elif  dar_item_8 == '14':
#             dar_item_8 = 'Geese'
#         elif  dar_item_8 == '15':
#             dar_item_8  = 'Guts'
#         elif  dar_item_8 == '17':
#              dar_item_8 = 'Monkey'
#         elif dar_item_8 ==  '18':
#             dar_item_8 = 'Opposum'
#         elif dar_item_8 ==  '25':
#             dar_item_8 = 'Seal'
#         elif dar_item_8 ==  '19':
#             dar_item_8 = 'Owl'
#         elif dar_item_8 ==  '20':
#             dar_item_8 = 'Peacock'
#         elif dar_item_8 ==  '19':
#             dar_item_8 =  'Swamp Cooler'
#         elif dar_item_8 ==  '20':
#             dar_item_8 = 'Stove'
#         elif dar_item_8 ==  '21':
#             dar_item_8 ='Pig'
#         elif dar_item_8 ==  '22':
#             dar_item_8 = 'Rabbit'
#         elif dar_item_8 ==  '23':
#             dar_item_8 = 'Racoon'
#         elif dar_item_8 ==  '24':
#             dar_item_8 = 'Rats'
#         elif dar_item_8 ==  '26':
#             dar_item_8 = 'Sheep'
#         elif dar_item_8 ==  '27':
#             dar_item_8 = 'Snake'
#         elif dar_item_8 ==  '28':
#             dar_item_8 = 'Spoiled Meat'
#         elif dar_item_8 ==  '29':
#             dar_item_8 = 'Squirrel'
#         elif dar_item_8 ==  '30':
#             dar_item_8 = 'Turkey'
#         elif dar_item_8 ==  '31':
#             dar_item_8 = 'Turtle'
#         elif dar_item_8 ==  '32':
#             dar_item_8 = 'Unknown'
#         elif dar_item_8 ==  '33':
#             dar_item_8 = 'Skunk'
#         elif dar_item_8 ==  '34':
#             dar_item_8 = 'Raven (Chicken Size)'
#         elif dar_item_8 ==  '35':
#             dar_item_8 = 'Raven (Unknown Size)'
#         elif dar_item_8 ==  '36':
#             dar_item_8 = 'Other'
#
#         elif dar_item_8  == 'None':
#             dar_item_8 = ' '
#
#
#
#
#         if  dar_item_9  == '7':
#             dar_item_9 = 'Coyote '
#         elif  dar_item_9 =='1':
#              dar_item_9 = 'Alligator'
#         elif  dar_item_9 == '2':
#              dar_item_9 = 'Bat'
#         elif dar_item_9  == "3":
#             dar_item_9 = 'Bird'
#         elif  dar_item_9== '4':
#              dar_item_9  = 'Cat'
#         elif  dar_item_9  == '5':
#              dar_item_9  = 'Chicken'
#         elif  dar_item_9  == '6':
#             dar_item_9  = 'Cow'
#         elif  dar_item_9  == '8':
#             dar_item_9 = 'Crow (Pigeon Size)'
#         elif  dar_item_9 == '9':
#             dar_item_9  = 'Deer'
#         elif  dar_item_9 == '10':
#             dar_item_9 = 'Dog'
#         elif  dar_item_9  == '11':
#             dar_item_9 = 'Duck'
#         elif  dar_item_9 == '16':
#             dar_item_9  = 'Llama'
#         elif  dar_item_9 == '12':
#              dar_item_9 = 'Heater'
#         elif  dar_item_9  == '13':
#              dar_item_9 = 'Fox'
#         elif  dar_item_9 == '14':
#             dar_item_9 = 'Geese'
#         elif  dar_item_9 == '15':
#             dar_item_9  = 'Guts'
#         elif  dar_item_9 == '17':
#              dar_item_9 = 'Monkey'
#         elif dar_item_9 ==  '18':
#             dar_item_9 = 'Opposum'
#         elif dar_item_9 ==  '25':
#             dar_item_9 = 'Seal'
#         elif dar_item_9 ==  '19':
#             dar_item_9 = 'Owl'
#         elif dar_item_9 ==  '20':
#             dar_item_9 = 'Peacock'
#         elif dar_item_9 ==  '19':
#             dar_item_9 =  'Swamp Cooler'
#         elif dar_item_9 ==  '20':
#             dar_item_9 = 'Stove'
#         elif dar_item_9 ==  '21':
#             dar_item_9 ='Pig'
#         elif dar_item_9 ==  '22':
#             dar_item_9 = 'Rabbit'
#         elif dar_item_9 ==  '23':
#             dar_item_9 = 'Racoon'
#         elif dar_item_9 ==  '24':
#             dar_item_9 = 'Rats'
#         elif dar_item_9 ==  '26':
#             dar_item_9 = 'Sheep'
#         elif dar_item_9 ==  '27':
#             dar_item_9 = 'Snake'
#         elif dar_item_9 ==  '28':
#             dar_item_9 = 'Spoiled Meat'
#         elif dar_item_9 ==  '29':
#             dar_item_9 = 'Squirrel'
#         elif dar_item_9 ==  '30':
#             dar_item_9 = 'Turkey'
#         elif dar_item_9 ==  '31':
#             dar_item_9 = 'Turtle'
#         elif dar_item_9 ==  '32':
#             dar_item_9 = 'Unknown'
#         elif dar_item_9 ==  '33':
#             dar_item_9 = 'Skunk'
#         elif dar_item_9 ==  '34':
#             dar_item_9 = 'Raven (Chicken Size)'
#         elif dar_item_9 ==  '35':
#             dar_item_9 = 'Raven (Unknown Size)'
#         elif dar_item_9 ==  '36':
#             dar_item_9 = 'Other'
#
#         elif dar_item_9  == 'None':
#             dar_item_9 = ' '
#
#
#         if  dar_item_10  == '7':
#             dar_item_10 = 'Coyote '
#         elif  dar_item_10 =='1':
#              dar_item_10 = 'Alligator'
#         elif  dar_item_10 == '2':
#              dar_item_10 = 'Bat'
#         elif dar_item_10  == "3":
#             dar_item_10 = 'Bird'
#         elif  dar_item_10== '4':
#              dar_item_10  = 'Cat'
#         elif  dar_item_10  == '5':
#              dar_item_10  = 'Chicken'
#         elif  dar_item_10  == '6':
#             dar_item_10  = 'Cow'
#         elif  dar_item_10  == '8':
#             dar_item_10 = 'Crow (Pigeon Size)'
#         elif  dar_item_10 == '9':
#             dar_item_10  = 'Deer'
#         elif  dar_item_10 == '10':
#             dar_item_10 = 'Dog'
#         elif  dar_item_10  == '11':
#             dar_item_10 = 'Duck'
#         elif  dar_item_10 == '16':
#             dar_item_10  = 'Llama'
#         elif  dar_item_10 == '12':
#              dar_item_10 = 'Heater'
#         elif  dar_item_10  == '13':
#              dar_item_10 = 'Fox'
#         elif  dar_item_10 == '14':
#             dar_item_10 = 'Geese'
#         elif  dar_item_10 == '15':
#             dar_item_10  = 'Guts'
#         elif  dar_item_10 == '17':
#              dar_item_10 = 'Monkey'
#         elif dar_item_10 ==  '18':
#             dar_item_10 = 'Opposum'
#         elif dar_item_10 ==  '25':
#             dar_item_10 = 'Seal'
#         elif dar_item_10 ==  '19':
#             dar_item_10 = 'Owl'
#         elif dar_item_10 ==  '20':
#             dar_item_10 = 'Peacock'
#         elif dar_item_10 ==  '19':
#             dar_item_10 =  'Swamp Cooler'
#         elif dar_item_10 ==  '20':
#             dar_item_10 = 'Stove'
#         elif dar_item_10 ==  '21':
#             dar_item_10 ='Pig'
#         elif dar_item_10 ==  '22':
#             dar_item_10 = 'Rabbit'
#         elif dar_item_10 ==  '23':
#             dar_item_10 = 'Racoon'
#         elif dar_item_10 ==  '24':
#             dar_item_10 = 'Rats'
#         elif dar_item_10 ==  '26':
#             dar_item_10 = 'Sheep'
#         elif dar_item_10 ==  '27':
#             dar_item_10 = 'Snake'
#         elif dar_item_10 ==  '28':
#             dar_item_10 = 'Spoiled Meat'
#         elif dar_item_10 ==  '29':
#             dar_item_10 = 'Squirrel'
#         elif dar_item_10 ==  '30':
#             dar_item_10 = 'Turkey'
#         elif dar_item_10 ==  '31':
#             dar_item_10 = 'Turtle'
#         elif dar_item_10 ==  '32':
#             dar_item_10 = 'Unknown'
#         elif dar_item_10 ==  '33':
#             dar_item_10 = 'Skunk'
#         elif dar_item_10 ==  '34':
#             dar_item_10 = 'Raven (Chicken Size)'
#         elif dar_item_10 ==  '35':
#             dar_item_10 = 'Raven (Unknown Size)'
#         elif dar_item_10 ==  '36':
#             dar_item_10 = 'Other'
#
#         elif dar_item_10  == 'None':
#             dar_item_10 = ' '
#
#
#
#         if dar_qyt_1  == 'None':
#             dar_qyt_1 = "0"
#         if dar_qyt_2  == 'None':
#             dar_qyt_2 = "0"
#         if dar_qyt_3  == 'None':
#             dar_qyt_3 = "0"
#         if dar_qyt_4  == 'None':
#             dar_qyt_4 = "0"
#         if dar_qyt_5  == 'None':
#             dar_qyt_5 = "0"
#         if dar_qyt_6  == 'None':
#             dar_qyt_6 = "0"
#         if dar_qyt_7  == 'None':
#             dar_qyt_7 = "0"
#         if dar_qyt_8  == 'None':
#             dar_qyt_8 = "0"
#         if dar_qyt_9  == 'None':
#             dar_qyt_9 = "0"
#         if dar_qyt_10  == 'None':
#             dar_qyt_10 = "0"
#
#         dL311 = dict()
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("DACType", dar_item_1)
#         d.setdefault("Type", "Dead Animal Removal")
#         d.setdefault("Name", dar_uid_1 )
#         d.setdefault("DACItemCount", dar_qyt_1)
#         l311.append(d)
#         dL311 = dict()
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("DACType", dar_item_2)
#         d.setdefault("Type", "Dead Animal Removal")
#         d.setdefault("Name", dar_uid_2)
#         d.setdefault("DACItemCount", dar_qyt_2)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("DACType", dar_item_3)
#         d.setdefault("Type", "Dead Animal Removal")
#         d.setdefault("Name", dar_uid_3)
#         d.setdefault("DACItemCount", dar_qyt_3)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("DACType", dar_item_4)
#         d.setdefault("Type", "Dead Animal Removal")
#         d.setdefault("Name", dar_uid_4)
#         d.setdefault("DACItemCount", dar_qyt_4)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("DACType", dar_item_5)
#         d.setdefault("Type", "Dead Animal Removal")
#         d.setdefault("Name", dar_uid_5)
#         d.setdefault("DACItemCount", dar_qyt_5)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("DACType", dar_item_6)
#         d.setdefault("Type", "Dead Animal Removal")
#         d.setdefault("Name", dar_uid_6)
#         d.setdefault("DACItemCount", dar_qyt_6)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("DACType", dar_item_7)
#         d.setdefault("Type", "Dead Animal Removal")
#         d.setdefault("Name", dar_uid_7)
#         d.setdefault("DACItemCount", dar_qyt_7)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("DACType", dar_item_8)
#         d.setdefault("Type", "Dead Animal Removal")
#         d.setdefault("Name", dar_uid_8)
#         d.setdefault("DACItemCount", dar_qyt_8)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("DACType", dar_item_9)
#         d.setdefault("Type", "Dead Animal Removal")
#         d.setdefault("Name", dar_uid_9)
#         d.setdefault("DACItemCount", dar_qyt_9)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("DACType", dar_item_10)
#         d.setdefault("Type", "Dead Animal Removal")
#         d.setdefault("Name", dar_uid_10)
#         d.setdefault("DACItemCount", dar_qyt_10)
#         l311.append(d)
#
#
#         lIndexes = []
#         nCnt = len(l311)
#         for i in range(nCnt):
#             d = l311[i]
#             if(d['Name'].strip() == ''):
#                 del d['Name']
#
#             if(d['DACType'] == " "):
#                 lIndexes.append(i)
#
#         if(len(lIndexes)>0):
#             for i in reversed(lIndexes):
#                 del l311[i]
#
#         if(len(l311)>0):
#             dL311.setdefault("DeadAnimalRemoval", l311)
#             dResult.setdefault("ListOfLa311DeadAnimalRemoval",dL311)
#             lResults.append({"MetaData": {}, "SRData": dResult})
#             sReq = json.dumps(dResult,sort_keys=True, indent=2)
#             results = {"MetaData": {}, "SRData": dResult}
#             sReqj = json.dumps(results,sort_keys=True, indent=2)
#             print sReqj
#             # start = time.time()
#             # url = "https://myla311Test.lacity.org/myla311router/mylasrbe/1/UpsertSANSRWithCodes"
#             # headers = {'Content-type': 'text/plain', 'Accept': '/'}
#             # r = requests.post(url, data= json.dumps(results), headers=headers,  verify=False)
#             # print results
#             # print r.text
#             # print 'It took', time.time()-start, 'seconds.'
#
#             ii = ii + 1
#             print (str(ii) + " recs sent to server.",  'It took', time.time()-start, 'seconds.')
#
#
#     print("Finished")
# except Exception,e:
#     exc_type, exc_obj, exc_tb = sys.exc_info()
#     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#     print(exc_type, fname, exc_tb.tb_lineno)
#
#
#
#
#
#
#
# pyFC = "SO_SC_1"
# clauseSBE = "WHERE RESOLUTION_CODE <> '' AND Category LIKE '%1%' OR Category LIKE '%2%' OR Category LIKE '%19%' "
# if(__name__=='__main__'):
#     # sMsg = printObjects()
#     # print(sMsg)
#
#     connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
#     # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
#     conn = pyodbc.connect(connstr)
#     cursor = conn.cursor()
#     FN_SRNumber = "SRNumber"
#     lFields = [FN_SRNumber, "RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user", "last_edited_date"]
#     #lFields = ["SRNumber"]
#     sFields = ""
#     for fld in lFields:
#         if(sFields==""):
#             sFields = fld
#         else:
#             sFields = sFields + "," + fld
#     #List of the fields you'd like to exclude, like ItemCount for example.
#     lFieldsExcluded = ["RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user", "last_edited_date"]
#
#     #sSQL = "SELECT SRNumber FROM {}".format(pyFC)
#     sSQL = "SELECT {} FROM {}  {}".format(sFields, pyFC, clauseSBE)
#
#
#     cursor.execute(sSQL)
#     #columns = [column[0] for column in cursor.description]
#     columns = []
#     for column in cursor.description:
#         if not (column[0] in lFieldsExcluded):
#             columns.append(column[0])
#
#
#
#
# try:
#     ii = 0
#     bulky_item_1 = ""
#     bulky_item_2 = ""
#     bulky_item_3 = ""
#     bulky_item_4 = ""
#     bulky_item_5 = ""
#     bulky_item_6 = ""
#     bulky_item_7 = ""
#     bulky_item_8 = ""
#     bulky_item_9 = ""
#     bulky_item_10 = ""
#     bulky_qyt_1 = " "
#     bulky_qyt_2 = " "
#     bulky_qyt_3 = " "
#     bulky_qyt_4 = " "
#     bulky_qyt_5 = " "
#     bulky_qyt_6 = " "
#     bulky_qyt_7 = " "
#     bulky_qyt_8 = " "
#     bulky_qyt_9 = " "
#     bulky_qyt_10 = " "
#     bulky_uid_1 = ""
#     bulky_uid_2 = " "
#     bulky_uid_3 = ""
#     bulky_uid_4 = ""
#     bulky_uid_5 = ""
#     bulky_uid_6 = ""
#     bulky_uid_7 = ""
#     bulky_uid_8 = ""
#     bulky_uid_9 = ""
#     bulky_uid_10 = ""
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
#         bulky_item_1 = (str(row[lFields.index("ITEM_1")]))
#         bulky_item_2 = (str(row[lFields.index("ITEM_2")]))
#         bulky_item_3 = (str(row[lFields.index("ITEM_3")]))
#         bulky_item_4 = (str(row[lFields.index("ITEM_4")]))
#         bulky_item_5 = (str(row[lFields.index("ITEM_5")]))
#         bulky_item_6= (str(row[lFields.index("ITEM_6")]))
#         bulky_item_7 =(str(row[lFields.index("ITEM_7")]))
#         bulky_item_8 = (str(row[lFields.index("ITEM_8")]))
#         bulky_item_9 =(str(row[lFields.index("ITEM_9")]))
#         bulky_item_10 = (str(row[lFields.index("ITEM_10")]))
#         bulky_qyt_1 = (str(row[lFields.index("QYT_1")]))
#         bulky_qyt_2 = (str(row[lFields.index("QYT_2")]))
#         bulky_qyt_3 = (str(row[lFields.index("QYT_3")]))
#         bulky_qyt_4 = (str(row[lFields.index("QYT_4")]))
#         bulky_qyt_5 = (str(row[lFields.index("QYT_5")]))
#         bulky_qyt_6 = (str(row[lFields.index("QTY_6")]))
#         bulky_qyt_7 = (str(row[lFields.index("QTY_7")]))
#         bulky_qyt_8 = (str(row[lFields.index("QTY_8")]))
#         bulky_qyt_9 = (str(row[lFields.index("QTY_9")]))
#         bulky_qyt_10 = (str(row[lFields.index("QTY_10")]))
#
#         bulky_uid_1 = (str(row[lFields.index("UID1")]))
#         bulky_uid_2 = (str(row[lFields.index("UID2")]))
#         bulky_uid_3 = (str(row[lFields.index("UID3")]))
#         bulky_uid_4 = (str(row[lFields.index("UID4")]))
#         bulky_uid_5 = (str(row[lFields.index("UID5")]))
#         bulky_uid_6 = (str(row[lFields.index("UID6")]))
#         bulky_uid_7 = (str(row[lFields.index("UID7")]))
#         bulky_uid_8 = (str(row[lFields.index("UID8")]))
#         bulky_uid_9 = (str(row[lFields.index("UID9")]))
#         bulky_uid_10 = (str(row[lFields.index("UID10")]))
#
#
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
#         # dResult.setdefault("ListOfLa311DeadAnimalRemoval", dict())
#
#         if  bulky_item_1  == '1':
#             bulky_item_1 = 'Bags Any Size '
#         elif  bulky_item_1 =='3':
#              bulky_item_1 = 'Bed Frame (wood)'
#         elif  bulky_item_1 == '2':
#              bulky_item_1 = 'Bed Set'
#         elif bulky_item_1  == "78":
#             bulky_item_1 = 'Bicycle'
#         elif  bulky_item_1== '5':
#              bulky_item_1  = 'Bird Cage (Plastic)'
#         elif  bulky_item_1  == '6':
#              bulky_item_1  = 'Blinds'
#         elif  bulky_item_1  == '7':
#             bulky_item_1  = 'Bookcase'
#         elif  bulky_item_1  == '8':
#             bulky_item_1 = 'Box Any Size'
#         elif  bulky_item_1 == '9':
#             bulky_item_1  = 'Box Spring'
#         elif  bulky_item_1 == '10':
#             bulky_item_1 = 'Cabinet'
#         elif  bulky_item_1  == '11':
#             bulky_item_1 = 'Car Parts'
#         elif  bulky_item_1 == '12':
#             bulky_item_1  = 'Carpet'
#         elif  bulky_item_1 == '13':
#              bulky_item_1 = 'Chair'
#         elif  bulky_item_1  == '79':
#              bulky_item_1 = 'Child Day Bed'
#         elif  bulky_item_1 == '14':
#             bulky_item_1 = 'Crib'
#         elif  bulky_item_1 == '15':
#             bulky_item_1  = 'Curtain Rod'
#         elif  bulky_item_1 == '16':
#              bulky_item_1 = 'Cushions'
#         elif bulky_item_1 ==  '18':
#             bulky_item_1 = "Decorating Item "
#         if  bulky_item_1  == '19':
#             bulky_item_1 = 'Desk'
#         elif  bulky_item_1 =='20':
#              bulky_item_1 = 'Door'
#         elif  bulky_item_1 == '21':
#              bulky_item_1 = 'Dresser'
#         elif bulky_item_1  == "22":
#             bulky_item_1 = 'Entertainment Center'
#         elif  bulky_item_1== '23':
#              bulky_item_1  = 'Fan (Any Size)'
#         elif  bulky_item_1  == '24':
#              bulky_item_1  = 'Fence (Wood)'
#         elif  bulky_item_1  == '25':
#             bulky_item_1  = 'File Cabinet (Wood)'
#         elif  bulky_item_1  == '26':
#             bulky_item_1 = 'Garage Door'
#         elif  bulky_item_1 == '27':
#             bulky_item_1  = 'Garage Door Opener'
#         elif  bulky_item_1 == '80':
#             bulky_item_1 = 'Gate (Wood)'
#         elif  bulky_item_1  == '28':
#             bulky_item_1 = 'Glass'
#         elif  bulky_item_1 == '29':
#             bulky_item_1  = 'Glass Window in Frame'
#         elif  bulky_item_1 == '30':
#              bulky_item_1 = 'Headboard'
#         elif  bulky_item_1  == '31':
#              bulky_item_1 = 'Ladders (Wood & Metal)'
#         elif  bulky_item_1 == '14':
#             bulky_item_1 = 'Video/Film Cameras'
#         elif  bulky_item_1 == '32':
#             bulky_item_1  = 'Lamp'
#         elif  bulky_item_1 == '33':
#              bulky_item_1 = 'Light Fixture'
#         elif  bulky_item_1 == '34':
#              bulky_item_1 = 'Loose Debris'
#         elif  bulky_item_1 == '35':
#             bulky_item_1 = 'Mattress'
#         elif  bulky_item_1 == '36':
#             bulky_item_1 = 'Mirror'
#         elif  bulky_item_1 == '37':
#             bulky_item_1 = 'Other BI'
#         elif  bulky_item_1 == '38':
#             bulky_item_1 = 'Pallet'
#         elif  bulky_item_1 == '39':
#             bulky_item_1 = 'Patio Cover'
#         elif  bulky_item_1 == '40':
#             bulky_item_1 = 'Patio Furniture'
#         elif  bulky_item_1 == '41':
#             bulky_item_1 = 'Piano'
#         elif  bulky_item_1 == '42':
#             bulky_item_1 = 'Planter Pot'
#         elif  bulky_item_1 == '43':
#             bulky_item_1 = 'Playpen'
#         elif  bulky_item_1 == '44':
#             bulky_item_1 = 'Pool Cover'
#         elif  bulky_item_1 == '45':
#             bulky_item_1 = 'Rain Gutter'
#         elif  bulky_item_1 == '46':
#             bulky_item_1 = 'Recliner'
#         elif  bulky_item_1 == '47':
#             bulky_item_1 = 'Rug'
#         elif  bulky_item_1 == '48':
#             bulky_item_1 = 'Shelf'
#         elif  bulky_item_1 == '49':
#             bulky_item_1 = 'Shopping Cart'
#         elif  bulky_item_1 == '50':
#             bulky_item_1 = 'Shower Door'
#         elif  bulky_item_1 == '51':
#             bulky_item_1 = 'Shutter'
#         elif  bulky_item_1 == '52':
#             bulky_item_1 = 'Sink'
#         elif  bulky_item_1 == '53':
#             bulky_item_1 = 'Sliding Door'
#         elif  bulky_item_1 == '54':
#             bulky_item_1 = 'Sofa'
#         elif  bulky_item_1 == '55':
#             bulky_item_1 = 'Sofa bed'
#         elif  bulky_item_1 == '56':
#             bulky_item_1 = 'Spa Cover'
#         elif  bulky_item_1 == '57':
#             bulky_item_1 = 'Spa/Jacuzzi'
#         elif  bulky_item_1 == '58':
#             bulky_item_1 = 'Stroller'
#         elif  bulky_item_1 == '59':
#             bulky_item_1 = 'Suitcase'
#         elif  bulky_item_1 == '60':
#             bulky_item_1 = 'Table'
#         elif  bulky_item_1 == '61':
#             bulky_item_1 = 'Tank Any Size'
#         elif  bulky_item_1 == '62':
#                  bulky_item_1 = 'Tire Less Than 5'
#         elif  bulky_item_1 == '63':
#             bulky_item_1 = 'Toilet'
#         elif  bulky_item_1 == '64':
#             bulky_item_1 = 'Toys (Large Ones)'
#         elif  bulky_item_1 == '65':
#             bulky_item_1 = 'Trash Cans'
#         elif  bulky_item_1 == '66':
#              bulky_item_1 = 'Trunk'
#         elif  bulky_item_1 == '67':
#             bulky_item_1 = 'Tub (Non Metal)'
#         elif  bulky_item_1 == '68':
#             bulky_item_1 = ' Vacuum Cleaner'
#         elif  bulky_item_1 == '69':
#             bulky_item_1 = 'Vehicle Tire'
#         elif  bulky_item_1 == '70':
#             bulky_item_1 = 'Walker'
#         elif  bulky_item_1 == '71':
#                 bulky_item_1 = 'Window Blinds'
#         elif  bulky_item_1 == '72':
#                 bulky_item_1 = 'Window Frame'
#         elif  bulky_item_1 == '73':
#             bulky_item_1 = 'Windows'
#         elif  bulky_item_1 == '74':
#                 bulky_item_1 = 'Wood Boards'
#         elif  bulky_item_1 == '75':
#             bulky_item_1 = 'Wood Bundled'
#         elif  bulky_item_1 == '76':
#             bulky_item_1 = 'Wood Cabinets'
#         elif  bulky_item_1 == '77':
#             bulky_item_1 = 'XMAS TREE'
#         elif  bulky_item_1 == '2':
#             bulky_item_1 = 'Basketball Set'
#
#
#
#
#         if  bulky_item_2  == '1':
#             bulky_item_2 = 'Bags Any Size '
#         elif  bulky_item_2 =='3':
#              bulky_item_2 = 'Bed Frame (wood)'
#         elif  bulky_item_2 == '2':
#              bulky_item_2 = 'Bed Set'
#         elif bulky_item_2  == "78":
#             bulky_item_2 = 'Bicycle'
#         elif  bulky_item_2== '5':
#              bulky_item_2  = 'Bird Cage Plastic'
#         elif  bulky_item_2  == '6':
#              bulky_item_2  = 'Blinds'
#         elif  bulky_item_2  == '7':
#             bulky_item_2  = 'Bookcase'
#         elif  bulky_item_2  == '8':
#             bulky_item_2 = 'Box Any Size'
#         elif  bulky_item_2 == '9':
#             bulky_item_2  = 'Box Spring'
#         elif  bulky_item_2 == '10':
#             bulky_item_2 = 'Cabinets'
#         elif  bulky_item_2  == '11':
#             bulky_item_2 = 'Car Parts'
#         elif  bulky_item_2 == '12':
#             bulky_item_2  = 'Carpet'
#         elif  bulky_item_2 == '13':
#              bulky_item_2 = 'Chair'
#         elif  bulky_item_2  == '79':
#              bulky_item_2 = 'Child Day Bed'
#         elif  bulky_item_2 == '14':
#             bulky_item_2 = 'Crib'
#         elif  bulky_item_2 == '15':
#             bulky_item_2  = 'Curtain Rod'
#         elif  bulky_item_2 == '16':
#              bulky_item_2 = 'Cushions'
#         elif bulky_item_2 ==  '18':
#             bulky_item_2 = "Decorating Item "
#         if  bulky_item_2  == '19':
#             bulky_item_2 = 'Desk'
#         elif  bulky_item_2 =='20':
#              bulky_item_2 = 'Door'
#         elif  bulky_item_2 == '21':
#              bulky_item_2 = 'Dresser'
#         elif bulky_item_2  == "22":
#             bulky_item_2 = 'Entertainment Center'
#         elif  bulky_item_2== '23':
#              bulky_item_2  = 'Fan (Any Size)'
#         elif  bulky_item_2  == '24':
#              bulky_item_2  = 'Fence (Wood)'
#         elif  bulky_item_2  == '25':
#             bulky_item_2  = 'File Cabinet (Wood)'
#         elif  bulky_item_2  == '26':
#             bulky_item_2 = 'Garage Door'
#         elif  bulky_item_2 == '27':
#             bulky_item_2  = 'Garage Door Opener'
#         elif  bulky_item_2 == '80':
#             bulky_item_2 = 'Gate (Wood)'
#         elif  bulky_item_2  == '28':
#             bulky_item_2 = 'Glass'
#         elif  bulky_item_2 == '29':
#             bulky_item_2  = 'Glass Window in Frame'
#         elif  bulky_item_2 == '30':
#              bulky_item_2 = 'Headboard'
#         elif  bulky_item_2  == '31':
#              bulky_item_2 = 'Ladders (Wood & Metal)'
#         elif  bulky_item_2 == '14':
#             bulky_item_2 = 'Video/Film Cameras'
#         elif  bulky_item_2 == '32':
#             bulky_item_2  = 'Lamp'
#         elif  bulky_item_2 == '33':
#              bulky_item_2 = 'Light Fixture'
#         elif  bulky_item_2 == '34':
#              bulky_item_2 = 'Loose Debris'
#         elif  bulky_item_2 == '35':
#             bulky_item_2 = 'Mattress'
#         elif  bulky_item_2 == '36':
#             bulky_item_2 = 'Mirror'
#         elif  bulky_item_2 == '37':
#             bulky_item_2 = 'Other BI'
#         elif  bulky_item_2 == '38':
#             bulky_item_2 = 'Pallet'
#         elif  bulky_item_2 == '39':
#             bulky_item_2 = 'Patio Cover'
#         elif  bulky_item_2 == '40':
#             bulky_item_2 = 'Patio Furniture'
#         elif  bulky_item_2 == '41':
#             bulky_item_2 = 'Piano'
#         elif  bulky_item_2 == '42':
#             bulky_item_2 = 'Planter Pot'
#         elif  bulky_item_2 == '43':
#             bulky_item_2 = 'Playpen'
#         elif  bulky_item_2 == '44':
#             bulky_item_2 = 'Pool Cover'
#         elif  bulky_item_2 == '45':
#             bulky_item_2 = 'Rain Gutter'
#         elif  bulky_item_2 == '46':
#             bulky_item_2 = 'Recliner'
#         elif  bulky_item_2 == '47':
#             bulky_item_2 = 'Rug'
#         elif  bulky_item_2 == '48':
#             bulky_item_2 = 'Shelf'
#         elif  bulky_item_2 == '49':
#             bulky_item_2 = 'Shopping Cart'
#         elif  bulky_item_2 == '50':
#             bulky_item_2 = 'Shower Door'
#         elif  bulky_item_2 == '51':
#             bulky_item_2 = 'Shutter'
#         elif  bulky_item_2 == '52':
#             bulky_item_2 = 'Sink'
#         elif  bulky_item_2 == '53':
#             bulky_item_2 = 'Sliding Door'
#         elif  bulky_item_2 == '54':
#             bulky_item_2 = 'Sofa'
#         elif  bulky_item_2 == '55':
#             bulky_item_2 = 'Sofa bed'
#         elif  bulky_item_2 == '56':
#             bulky_item_2 = 'Spa Cover'
#         elif  bulky_item_2 == '57':
#             bulky_item_2 = 'Spa/Jacuzzi'
#         elif  bulky_item_2 == '58':
#             bulky_item_2 = 'Stroller'
#         elif  bulky_item_2 == '59':
#             bulky_item_2 = 'Suitcase'
#         elif  bulky_item_2 == '60':
#             bulky_item_2 = 'Table'
#         elif  bulky_item_2 == '61':
#             bulky_item_2 = 'Tank Any Size'
#         elif  bulky_item_2 == '62':
#                  bulky_item_2 = 'Tire Less Than 5'
#         elif  bulky_item_2 == '63':
#             bulky_item_2 = 'Toilet'
#         elif  bulky_item_2 == '64':
#             bulky_item_2 = 'Toys (Large Ones)'
#         elif  bulky_item_2 == '65':
#             bulky_item_2 = 'Trash Cans'
#         elif  bulky_item_2 == '66':
#              bulky_item_2 = 'Trunk'
#         elif  bulky_item_2 == '67':
#             bulky_item_2 = 'Tub (Non Metal)'
#         elif  bulky_item_2 == '68':
#             bulky_item_2 = ' Vacuum Cleaner'
#         elif  bulky_item_2 == '69':
#             bulky_item_2 = 'Vehicle Tire'
#         elif  bulky_item_2 == '70':
#             bulky_item_2 = 'Walker'
#         elif  bulky_item_2 == '71':
#                 bulky_item_2 = 'Window Blinds'
#         elif  bulky_item_2 == '72':
#                 bulky_item_2 = 'Window Frame'
#         elif  bulky_item_2 == '73':
#             bulky_item_2 = 'Windows'
#         elif  bulky_item_2 == '74':
#                 bulky_item_2 = 'Wood Boards'
#         elif  bulky_item_2 == '75':
#             bulky_item_2 = 'Wood Bundled'
#         elif  bulky_item_2 == '76':
#             bulky_item_2 = 'Wood Cabinets'
#         elif  bulky_item_2 == '77':
#             bulky_item_2 = 'XMAS TREE'
#         elif  bulky_item_2 == '2':
#             bulky_item_2 = 'Basketball Set'
#
#
#
#
#         if  bulky_item_3  == '1':
#             bulky_item_3 = 'Bags Any Size '
#         elif  bulky_item_3 =='3':
#              bulky_item_3 = 'Bed Frame (wood)'
#         elif  bulky_item_3 == '2':
#              bulky_item_3 = 'Bed Set'
#         elif bulky_item_3  == "78":
#             bulky_item_3 = 'Bicycle'
#         elif  bulky_item_3== '5':
#              bulky_item_3  = 'Bird Cage Plastic'
#         elif  bulky_item_3  == '6':
#              bulky_item_3  = 'Blinds'
#         elif  bulky_item_3  == '7':
#             bulky_item_3  = 'Bookcase'
#         elif  bulky_item_3  == '8':
#             bulky_item_3 = 'Box Any Size'
#         elif  bulky_item_3 == '9':
#             bulky_item_3  = 'Box Spring'
#         elif  bulky_item_3 == '10':
#             bulky_item_3 = 'Cabinets'
#         elif  bulky_item_3  == '11':
#             bulky_item_3 = 'Car Parts'
#         elif  bulky_item_3 == '12':
#             bulky_item_3  = 'Carpet'
#         elif  bulky_item_3 == '13':
#              bulky_item_3 = 'Chair'
#         elif  bulky_item_3  == '79':
#              bulky_item_3 = 'Child Day Bed'
#         elif  bulky_item_3 == '14':
#             bulky_item_3 = 'Crib'
#         elif  bulky_item_3 == '15':
#             bulky_item_3  = 'Curtain Rod'
#         elif  bulky_item_3 == '16':
#              bulky_item_3 = 'Cushions'
#         elif bulky_item_3 ==  '18':
#             bulky_item_3 = "Decorating Item "
#         if  bulky_item_3  == '19':
#             bulky_item_3 = 'Desk'
#         elif  bulky_item_3 =='20':
#              bulky_item_3 = 'Door'
#         elif  bulky_item_3 == '21':
#              bulky_item_3 = 'Dresser'
#         elif bulky_item_3  == "22":
#             bulky_item_3 = 'Entertainment Center'
#         elif  bulky_item_3== '23':
#              bulky_item_3  = 'Fan (Any Size)'
#         elif  bulky_item_3  == '24':
#              bulky_item_3  = 'Fence (Wood)'
#         elif  bulky_item_3  == '25':
#             bulky_item_3  = 'File Cabinet (Wood)'
#         elif  bulky_item_3  == '26':
#             bulky_item_3 = 'Garage Door'
#         elif  bulky_item_3 == '27':
#             bulky_item_3  = 'Garage Door Opener'
#         elif  bulky_item_3 == '80':
#             bulky_item_3 = 'Gate (Wood)'
#         elif  bulky_item_3  == '28':
#             bulky_item_3 = 'Glass'
#         elif  bulky_item_3 == '29':
#             bulky_item_3  = 'Glass Window in Frame'
#         elif  bulky_item_3 == '30':
#              bulky_item_3 = 'Headboard'
#         elif  bulky_item_3  == '31':
#              bulky_item_3 = 'Ladders (Wood & Metal)'
#         elif  bulky_item_3 == '14':
#             bulky_item_3 = 'Video/Film Cameras'
#         elif  bulky_item_3 == '32':
#             bulky_item_3  = 'Lamp'
#         elif  bulky_item_3 == '33':
#              bulky_item_3 = 'Light Fixture'
#         elif  bulky_item_3 == '34':
#              bulky_item_3 = 'Loose Debris'
#         elif  bulky_item_3 == '35':
#             bulky_item_3 = 'Mattress'
#         elif  bulky_item_3 == '36':
#             bulky_item_3 = 'Mirror'
#         elif  bulky_item_3 == '37':
#             bulky_item_3 = 'Other BI'
#         elif  bulky_item_3 == '38':
#             bulky_item_3 = 'Pallet'
#         elif  bulky_item_3 == '39':
#             bulky_item_3 = 'Patio Cover'
#         elif  bulky_item_3 == '40':
#             bulky_item_3 = 'Patio Furniture'
#         elif  bulky_item_3 == '41':
#             bulky_item_3 = 'Piano'
#         elif  bulky_item_3 == '42':
#             bulky_item_3 = 'Planter Pot'
#         elif  bulky_item_3 == '43':
#             bulky_item_3 = 'Playpen'
#         elif  bulky_item_3 == '44':
#             bulky_item_3 = 'Pool Cover'
#         elif  bulky_item_3 == '45':
#             bulky_item_3 = 'Rain Gutter'
#         elif  bulky_item_3 == '46':
#             bulky_item_3 = 'Recliner'
#         elif  bulky_item_3 == '47':
#             bulky_item_3 = 'Rug'
#         elif  bulky_item_3 == '48':
#             bulky_item_3 = 'Shelf'
#         elif  bulky_item_3 == '49':
#             bulky_item_3 = 'Shopping Cart'
#         elif  bulky_item_3 == '50':
#             bulky_item_3 = 'Shower Door'
#         elif  bulky_item_3 == '51':
#             bulky_item_3 = 'Shutter'
#         elif  bulky_item_3 == '52':
#             bulky_item_3 = 'Sink'
#         elif  bulky_item_3 == '53':
#             bulky_item_3 = 'Sliding Door'
#         elif  bulky_item_3 == '54':
#             bulky_item_3 = 'Sofa'
#         elif  bulky_item_3 == '55':
#             bulky_item_3 = 'Sofa bed'
#         elif  bulky_item_3 == '56':
#             bulky_item_3 = 'Spa Cover'
#         elif  bulky_item_3 == '57':
#             bulky_item_3 = 'Spa/Jacuzzi'
#         elif  bulky_item_3 == '58':
#             bulky_item_3 = 'Stroller'
#         elif  bulky_item_3 == '59':
#             bulky_item_3 = 'Suitcase'
#         elif  bulky_item_3 == '60':
#             bulky_item_3 = 'Table'
#         elif  bulky_item_3 == '61':
#             bulky_item_3 = 'Tank Any Size'
#         elif  bulky_item_3 == '62':
#                  bulky_item_3 = 'Tire Less Than 5'
#         elif  bulky_item_3 == '63':
#             bulky_item_3 = 'Toilet'
#         elif  bulky_item_3 == '64':
#             bulky_item_3 = 'Toys (Large Ones)'
#         elif  bulky_item_3 == '65':
#             bulky_item_3 = 'Trash Cans'
#         elif  bulky_item_3 == '66':
#              bulky_item_3 = 'Trunk'
#         elif  bulky_item_3 == '67':
#             bulky_item_3 = 'Tub (Non Metal)'
#         elif  bulky_item_3 == '68':
#             bulky_item_3 = ' Vacuum Cleaner'
#         elif  bulky_item_3 == '69':
#             bulky_item_3 = 'Vehicle Tire'
#         elif  bulky_item_3 == '70':
#             bulky_item_3 = 'Walker'
#         elif  bulky_item_3 == '71':
#                 bulky_item_3 = 'Window Blinds'
#         elif  bulky_item_3 == '72':
#                 bulky_item_3 = 'Window Frame'
#         elif  bulky_item_3 == '73':
#             bulky_item_3 = 'Windows'
#         elif  bulky_item_3 == '74':
#                 bulky_item_3 = 'Wood Boards'
#         elif  bulky_item_3 == '75':
#             bulky_item_3 = 'Wood Bundled'
#         elif  bulky_item_3 == '76':
#             bulky_item_3 = 'Wood Cabinets'
#         elif  bulky_item_3 == '77':
#             bulky_item_3 = 'XMAS TREE'
#         elif  bulky_item_3 == '2':
#             bulky_item_3 = 'Basketball Set'
#
#
#
#
#         if  bulky_item_4  == '1':
#             bulky_item_4 = 'Bags Any Size '
#         elif  bulky_item_4 =='3':
#              bulky_item_4 = 'Bed Frame (wood)'
#         elif  bulky_item_4 == '2':
#              bulky_item_4 = 'Bed Set'
#         elif bulky_item_4  == "78":
#             bulky_item_4 = 'Bicycle'
#         elif  bulky_item_4== '5':
#              bulky_item_4  = 'Bird Cage Plastic'
#         elif  bulky_item_4  == '6':
#              bulky_item_4  = 'Blinds'
#         elif  bulky_item_4  == '7':
#             bulky_item_4  = 'Bookcase'
#         elif  bulky_item_4  == '8':
#             bulky_item_4 = 'Box Any Size'
#         elif  bulky_item_4 == '9':
#             bulky_item_4  = 'Box Spring'
#         elif  bulky_item_4 == '10':
#             bulky_item_4 = 'Cabinets'
#         elif  bulky_item_4  == '11':
#             bulky_item_4 = 'Car Parts'
#         elif  bulky_item_4 == '12':
#             bulky_item_4  = 'Carpet'
#         elif  bulky_item_4 == '13':
#              bulky_item_4 = 'Chair'
#         elif  bulky_item_4  == '79':
#              bulky_item_4 = 'Child Day Bed'
#         elif  bulky_item_4 == '14':
#             bulky_item_4 = 'Crib'
#         elif  bulky_item_4 == '15':
#             bulky_item_4  = 'Curtain Rod'
#         elif  bulky_item_4 == '16':
#              bulky_item_4 = 'Cushions'
#         elif bulky_item_4 ==  '18':
#             bulky_item_4 = "Decorating Item "
#         if  bulky_item_4  == '19':
#             bulky_item_4 = 'Desk'
#         elif  bulky_item_4 =='20':
#              bulky_item_4 = 'Door'
#         elif  bulky_item_4 == '21':
#              bulky_item_4 = 'Dresser'
#         elif bulky_item_4  == "22":
#             bulky_item_4 = 'Entertainment Center'
#         elif  bulky_item_4== '23':
#              bulky_item_4  = 'Fan (Any Size)'
#         elif  bulky_item_4  == '24':
#              bulky_item_4  = 'Fence (Wood)'
#         elif  bulky_item_4  == '25':
#             bulky_item_4  = 'File Cabinet (Wood)'
#         elif  bulky_item_4  == '26':
#             bulky_item_4 = 'Garage Door'
#         elif  bulky_item_4 == '27':
#             bulky_item_4  = 'Garage Door Opener'
#         elif  bulky_item_4 == '80':
#             bulky_item_4 = 'Gate (Wood)'
#         elif  bulky_item_4  == '28':
#             bulky_item_4 = 'Glass'
#         elif  bulky_item_4 == '29':
#             bulky_item_4  = 'Glass Window in Frame'
#         elif  bulky_item_4 == '30':
#              bulky_item_4 = 'Headboard'
#         elif  bulky_item_4  == '31':
#              bulky_item_4 = 'Ladders (Wood & Metal)'
#         elif  bulky_item_4 == '14':
#             bulky_item_4 = 'Video/Film Cameras'
#         elif  bulky_item_4 == '32':
#             bulky_item_4  = 'Lamp'
#         elif  bulky_item_4 == '33':
#              bulky_item_4 = 'Light Fixture'
#         elif  bulky_item_4 == '34':
#              bulky_item_4 = 'Loose Debris'
#         elif  bulky_item_4 == '35':
#             bulky_item_4 = 'Mattress'
#         elif  bulky_item_4 == '36':
#             bulky_item_4 = 'Mirror'
#         elif  bulky_item_4 == '37':
#             bulky_item_4 = 'Other BI'
#         elif  bulky_item_4 == '38':
#             bulky_item_4 = 'Pallet'
#         elif  bulky_item_4 == '39':
#             bulky_item_4 = 'Patio Cover'
#         elif  bulky_item_4 == '40':
#             bulky_item_4 = 'Patio Furniture'
#         elif  bulky_item_4 == '41':
#             bulky_item_4 = 'Piano'
#         elif  bulky_item_4 == '42':
#             bulky_item_4 = 'Planter Pot'
#         elif  bulky_item_4 == '43':
#             bulky_item_4 = 'Playpen'
#         elif  bulky_item_4 == '44':
#             bulky_item_4 = 'Pool Cover'
#         elif  bulky_item_4 == '45':
#             bulky_item_4 = 'Rain Gutter'
#         elif  bulky_item_4 == '46':
#             bulky_item_4 = 'Recliner'
#         elif  bulky_item_4 == '47':
#             bulky_item_4 = 'Rug'
#         elif  bulky_item_4 == '48':
#             bulky_item_4 = 'Shelf'
#         elif  bulky_item_4 == '49':
#             bulky_item_4 = 'Shopping Cart'
#         elif  bulky_item_4 == '50':
#             bulky_item_4 = 'Shower Door'
#         elif  bulky_item_4 == '51':
#             bulky_item_4 = 'Shutter'
#         elif  bulky_item_4 == '52':
#             bulky_item_4 = 'Sink'
#         elif  bulky_item_4 == '53':
#             bulky_item_4 = 'Sliding Door'
#         elif  bulky_item_4 == '54':
#             bulky_item_4 = 'Sofa'
#         elif  bulky_item_4 == '55':
#             bulky_item_4 = 'Sofa bed'
#         elif  bulky_item_4 == '56':
#             bulky_item_4 = 'Spa Cover'
#         elif  bulky_item_4 == '57':
#             bulky_item_4 = 'Spa/Jacuzzi'
#         elif  bulky_item_4 == '58':
#             bulky_item_4 = 'Stroller'
#         elif  bulky_item_4 == '59':
#             bulky_item_4 = 'Suitcase'
#         elif  bulky_item_4 == '60':
#             bulky_item_4 = 'Table'
#         elif  bulky_item_4 == '61':
#             bulky_item_4 = 'Tank Any Size'
#         elif  bulky_item_4 == '62':
#                  bulky_item_4 = 'Tire Less Than 5'
#         elif  bulky_item_4 == '63':
#             bulky_item_4 = 'Toilet'
#         elif  bulky_item_4 == '64':
#             bulky_item_4 = 'Toys (Large Ones)'
#         elif  bulky_item_4 == '65':
#             bulky_item_4 = 'Trash Cans'
#         elif  bulky_item_4 == '66':
#              bulky_item_4 = 'Trunk'
#         elif  bulky_item_4 == '67':
#             bulky_item_4 = 'Tub (Non Metal)'
#         elif  bulky_item_4 == '68':
#             bulky_item_4 = ' Vacuum Cleaner'
#         elif  bulky_item_4 == '69':
#             bulky_item_4 = 'Vehicle Tire'
#         elif  bulky_item_4 == '70':
#             bulky_item_4 = 'Walker'
#         elif  bulky_item_4 == '71':
#                 bulky_item_4 = 'Window Blinds'
#         elif  bulky_item_4 == '72':
#                 bulky_item_4 = 'Window Frame'
#         elif  bulky_item_4 == '73':
#             bulky_item_4 = 'Windows'
#         elif  bulky_item_4 == '74':
#                 bulky_item_4 = 'Wood Boards'
#         elif  bulky_item_4 == '75':
#             bulky_item_4 = 'Wood Bundled'
#         elif  bulky_item_4 == '76':
#             bulky_item_4 = 'Wood Cabinets'
#         elif  bulky_item_4 == '77':
#             bulky_item_4 = 'XMAS TREE'
#         elif  bulky_item_4 == '2':
#             bulky_item_4 = 'Basketball Set'
#
#
#
#
#
#
#
#
#
#
#         if  bulky_item_5  == '1':
#             bulky_item_5 = 'Bags Any Size '
#         elif  bulky_item_5 =='3':
#              bulky_item_5 = 'Bed Frame (wood)'
#         elif  bulky_item_5 == '2':
#              bulky_item_5 = 'Bed Set'
#         elif bulky_item_5  == "78":
#             bulky_item_5 = 'Bicycle'
#         elif  bulky_item_5== '5':
#              bulky_item_5  = 'Bird Cage Plastic'
#         elif  bulky_item_5  == '6':
#              bulky_item_5  = 'Blinds'
#         elif  bulky_item_5  == '7':
#             bulky_item_5  = 'Bookcase'
#         elif  bulky_item_5  == '8':
#             bulky_item_5 = 'Box Any Size'
#         elif  bulky_item_5 == '9':
#             bulky_item_5  = 'Box Spring'
#         elif  bulky_item_5 == '10':
#             bulky_item_5 = 'Cabinets'
#         elif  bulky_item_5  == '11':
#             bulky_item_5 = 'Car Parts'
#         elif  bulky_item_5 == '12':
#             bulky_item_5  = 'Carpet'
#         elif  bulky_item_5 == '13':
#              bulky_item_5 = 'Chair'
#         elif  bulky_item_5  == '79':
#              bulky_item_5 = 'Child Day Bed'
#         elif  bulky_item_5 == '14':
#             bulky_item_5 = 'Crib'
#         elif  bulky_item_5 == '15':
#             bulky_item_5  = 'Curtain Rod'
#         elif  bulky_item_5 == '16':
#              bulky_item_5 = 'Cushions'
#         elif bulky_item_5 ==  '18':
#             bulky_item_5 = "Decorating Item "
#         if  bulky_item_5  == '19':
#             bulky_item_5 = 'Desk'
#         elif  bulky_item_5 =='20':
#              bulky_item_5 = 'Door'
#         elif  bulky_item_5 == '21':
#              bulky_item_5 = 'Dresser'
#         elif bulky_item_5  == "22":
#             bulky_item_5 = 'Entertainment Center'
#         elif  bulky_item_5== '23':
#              bulky_item_5  = 'Fan (Any Size)'
#         elif  bulky_item_5  == '24':
#              bulky_item_5  = 'Fence (Wood)'
#         elif  bulky_item_5  == '25':
#             bulky_item_5  = 'File Cabinet (Wood)'
#         elif  bulky_item_5  == '26':
#             bulky_item_5 = 'Garage Door'
#         elif  bulky_item_5 == '27':
#             bulky_item_5  = 'Garage Door Opener'
#         elif  bulky_item_5 == '80':
#             bulky_item_5 = 'Gate (Wood)'
#         elif  bulky_item_5  == '28':
#             bulky_item_5 = 'Glass'
#         elif  bulky_item_5 == '29':
#             bulky_item_5  = 'Glass Window in Frame'
#         elif  bulky_item_5 == '30':
#              bulky_item_5 = 'Headboard'
#         elif  bulky_item_5  == '31':
#              bulky_item_5 = 'Ladders (Wood & Metal)'
#         elif  bulky_item_5 == '14':
#             bulky_item_5 = 'Video/Film Cameras'
#         elif  bulky_item_5 == '32':
#             bulky_item_5  = 'Lamp'
#         elif  bulky_item_5 == '33':
#              bulky_item_5 = 'Light Fixture'
#         elif  bulky_item_5 == '34':
#              bulky_item_5 = 'Loose Debris'
#         elif  bulky_item_5 == '35':
#             bulky_item_5 = 'Mattress'
#         elif  bulky_item_5 == '36':
#             bulky_item_5 = 'Mirror'
#         elif  bulky_item_5 == '37':
#             bulky_item_5 = 'Other BI'
#         elif  bulky_item_5 == '38':
#             bulky_item_5 = 'Pallet'
#         elif  bulky_item_5 == '39':
#             bulky_item_5 = 'Patio Cover'
#         elif  bulky_item_5 == '40':
#             bulky_item_5 = 'Patio Furniture'
#         elif  bulky_item_5 == '41':
#             bulky_item_5 = 'Piano'
#         elif  bulky_item_5 == '42':
#             bulky_item_5 = 'Planter Pot'
#         elif  bulky_item_5 == '43':
#             bulky_item_5 = 'Playpen'
#         elif  bulky_item_5 == '44':
#             bulky_item_5 = 'Pool Cover'
#         elif  bulky_item_5 == '45':
#             bulky_item_5 = 'Rain Gutter'
#         elif  bulky_item_5 == '46':
#             bulky_item_5 = 'Recliner'
#         elif  bulky_item_5 == '47':
#             bulky_item_5 = 'Rug'
#         elif  bulky_item_5 == '48':
#             bulky_item_5 = 'Shelf'
#         elif  bulky_item_5 == '49':
#             bulky_item_5 = 'Shopping Cart'
#         elif  bulky_item_5 == '50':
#             bulky_item_5 = 'Shower Door'
#         elif  bulky_item_5 == '51':
#             bulky_item_5 = 'Shutter'
#         elif  bulky_item_5 == '52':
#             bulky_item_5 = 'Sink'
#         elif  bulky_item_5 == '53':
#             bulky_item_5 = 'Sliding Door'
#         elif  bulky_item_5 == '54':
#             bulky_item_5 = 'Sofa'
#         elif  bulky_item_5 == '55':
#             bulky_item_5 = 'Sofa bed'
#         elif  bulky_item_5 == '56':
#             bulky_item_5 = 'Spa Cover'
#         elif  bulky_item_5 == '57':
#             bulky_item_5 = 'Spa/Jacuzzi'
#         elif  bulky_item_5 == '58':
#             bulky_item_5 = 'Stroller'
#         elif  bulky_item_5 == '59':
#             bulky_item_5 = 'Suitcase'
#         elif  bulky_item_5 == '60':
#             bulky_item_5 = 'Table'
#         elif  bulky_item_5 == '61':
#             bulky_item_5 = 'Tank Any Size'
#         elif  bulky_item_5 == '62':
#                  bulky_item_5 = 'Tire Less Than 5'
#         elif  bulky_item_5 == '63':
#             bulky_item_5 = 'Toilet'
#         elif  bulky_item_5 == '64':
#             bulky_item_5 = 'Toys (Large Ones)'
#         elif  bulky_item_5 == '65':
#             bulky_item_5 = 'Trash Cans'
#         elif  bulky_item_5 == '66':
#              bulky_item_5 = 'Trunk'
#         elif  bulky_item_5 == '67':
#             bulky_item_5 = 'Tub (Non Metal)'
#         elif  bulky_item_5 == '68':
#             bulky_item_5 = ' Vacuum Cleaner'
#         elif  bulky_item_5 == '69':
#             bulky_item_5 = 'Vehicle Tire'
#         elif  bulky_item_5 == '70':
#             bulky_item_5 = 'Walker'
#         elif  bulky_item_5 == '71':
#                 bulky_item_5 = 'Window Blinds'
#         elif  bulky_item_5 == '72':
#                 bulky_item_5 = 'Window Frame'
#         elif  bulky_item_5 == '73':
#             bulky_item_5 = 'Windows'
#         elif  bulky_item_5 == '74':
#                 bulky_item_5 = 'Wood Boards'
#         elif  bulky_item_5 == '75':
#             bulky_item_5 = 'Wood Bundled'
#         elif  bulky_item_5 == '76':
#             bulky_item_5 = 'Wood Cabinets'
#         elif  bulky_item_5 == '77':
#             bulky_item_5 = 'XMAS TREE'
#         elif  bulky_item_5 == '2':
#             bulky_item_5 = 'Basketball Set'
#
#
#
#
#
#
#
#
#
#
#
#
#
#         if  bulky_item_6  == '1':
#             bulky_item_6 = 'Bags Any Size '
#         elif  bulky_item_6 =='3':
#              bulky_item_6 = 'Bed Frame (wood)'
#         elif  bulky_item_6 == '2':
#              bulky_item_6 = 'Bed Set'
#         elif bulky_item_6  == "78":
#             bulky_item_6 = 'Bicycle'
#         elif  bulky_item_6== '5':
#              bulky_item_6  = 'Bird Cage Plastic'
#         elif  bulky_item_6  == '6':
#              bulky_item_6  = 'Blinds'
#         elif  bulky_item_6  == '7':
#             bulky_item_6  = 'Bookcase'
#         elif  bulky_item_6  == '8':
#             bulky_item_6 = 'Box Any Size'
#         elif  bulky_item_6 == '9':
#             bulky_item_6  = 'Box Spring'
#         elif  bulky_item_6 == '10':
#             bulky_item_6 = 'Cabinets'
#         elif  bulky_item_6  == '11':
#             bulky_item_6 = 'Car Parts'
#         elif  bulky_item_6 == '12':
#             bulky_item_6  = 'Carpet'
#         elif  bulky_item_6 == '13':
#              bulky_item_6 = 'Chair'
#         elif  bulky_item_6  == '79':
#              bulky_item_6 = 'Child Day Bed'
#         elif  bulky_item_6 == '14':
#             bulky_item_6 = 'Crib'
#         elif  bulky_item_6 == '15':
#             bulky_item_6  = 'Curtain Rod'
#         elif  bulky_item_6 == '16':
#              bulky_item_6 = 'Cushions'
#         elif bulky_item_6 ==  '18':
#             bulky_item_6 = "Decorating Item "
#         if  bulky_item_6  == '19':
#             bulky_item_6 = 'Desk'
#         elif  bulky_item_6 =='20':
#              bulky_item_6 = 'Door'
#         elif  bulky_item_6 == '21':
#              bulky_item_6 = 'Dresser'
#         elif bulky_item_6  == "22":
#             bulky_item_6 = 'Entertainment Center'
#         elif  bulky_item_6== '23':
#              bulky_item_6  = 'Fan (Any Size)'
#         elif  bulky_item_6  == '24':
#              bulky_item_6  = 'Fence (Wood)'
#         elif  bulky_item_6  == '25':
#             bulky_item_6  = 'File Cabinet (Wood)'
#         elif  bulky_item_6  == '26':
#             bulky_item_6 = 'Garage Door'
#         elif  bulky_item_6 == '27':
#             bulky_item_6  = 'Garage Door Opener'
#         elif  bulky_item_6 == '80':
#             bulky_item_6 = 'Gate (Wood)'
#         elif  bulky_item_6  == '28':
#             bulky_item_6 = 'Glass'
#         elif  bulky_item_6 == '29':
#             bulky_item_6  = 'Glass Window in Frame'
#         elif  bulky_item_6 == '30':
#              bulky_item_6 = 'Headboard'
#         elif  bulky_item_6  == '31':
#              bulky_item_6 = 'Ladders (Wood & Metal)'
#         elif  bulky_item_6 == '14':
#             bulky_item_6 = 'Video/Film Cameras'
#         elif  bulky_item_6 == '32':
#             bulky_item_6  = 'Lamp'
#         elif  bulky_item_6 == '33':
#              bulky_item_6 = 'Light Fixture'
#         elif  bulky_item_6 == '34':
#              bulky_item_6 = 'Loose Debris'
#         elif  bulky_item_6 == '35':
#             bulky_item_6 = 'Mattress'
#         elif  bulky_item_6 == '36':
#             bulky_item_6 = 'Mirror'
#         elif  bulky_item_6 == '37':
#             bulky_item_6 = 'Other BI'
#         elif  bulky_item_6 == '38':
#             bulky_item_6 = 'Pallet'
#         elif  bulky_item_6 == '39':
#             bulky_item_6 = 'Patio Cover'
#         elif  bulky_item_6 == '40':
#             bulky_item_6 = 'Patio Furniture'
#         elif  bulky_item_6 == '41':
#             bulky_item_6 = 'Piano'
#         elif  bulky_item_6 == '42':
#             bulky_item_6 = 'Planter Pot'
#         elif  bulky_item_6 == '43':
#             bulky_item_6 = 'Playpen'
#         elif  bulky_item_6 == '44':
#             bulky_item_6 = 'Pool Cover'
#         elif  bulky_item_6 == '45':
#             bulky_item_6 = 'Rain Gutter'
#         elif  bulky_item_6 == '46':
#             bulky_item_6 = 'Recliner'
#         elif  bulky_item_6 == '47':
#             bulky_item_6 = 'Rug'
#         elif  bulky_item_6 == '48':
#             bulky_item_6 = 'Shelf'
#         elif  bulky_item_6 == '49':
#             bulky_item_6 = 'Shopping Cart'
#         elif  bulky_item_6 == '50':
#             bulky_item_6 = 'Shower Door'
#         elif  bulky_item_6 == '51':
#             bulky_item_6 = 'Shutter'
#         elif  bulky_item_6 == '52':
#             bulky_item_6 = 'Sink'
#         elif  bulky_item_6 == '53':
#             bulky_item_6 = 'Sliding Door'
#         elif  bulky_item_6 == '54':
#             bulky_item_6 = 'Sofa'
#         elif  bulky_item_6 == '55':
#             bulky_item_6 = 'Sofa bed'
#         elif  bulky_item_6 == '56':
#             bulky_item_6 = 'Spa Cover'
#         elif  bulky_item_6 == '57':
#             bulky_item_6 = 'Spa/Jacuzzi'
#         elif  bulky_item_6 == '58':
#             bulky_item_6 = 'Stroller'
#         elif  bulky_item_6 == '59':
#             bulky_item_6 = 'Suitcase'
#         elif  bulky_item_6 == '60':
#             bulky_item_6 = 'Table'
#         elif  bulky_item_6 == '61':
#             bulky_item_6 = 'Tank Any Size'
#         elif  bulky_item_6 == '62':
#                  bulky_item_6 = 'Tire Less Than 5'
#         elif  bulky_item_6 == '63':
#             bulky_item_6 = 'Toilet'
#         elif  bulky_item_6 == '64':
#             bulky_item_6 = 'Toys (Large Ones)'
#         elif  bulky_item_6 == '65':
#             bulky_item_6 = 'Trash Cans'
#         elif  bulky_item_6 == '66':
#              bulky_item_6 = 'Trunk'
#         elif  bulky_item_6 == '67':
#             bulky_item_6 = 'Tub (Non Metal)'
#         elif  bulky_item_6 == '68':
#             bulky_item_6 = ' Vacuum Cleaner'
#         elif  bulky_item_6 == '69':
#             bulky_item_6 = 'Vehicle Tire'
#         elif  bulky_item_6 == '70':
#             bulky_item_6 = 'Walker'
#         elif  bulky_item_6 == '71':
#                 bulky_item_6 = 'Window Blinds'
#         elif  bulky_item_6 == '72':
#                 bulky_item_6 = 'Window Frame'
#         elif  bulky_item_6 == '73':
#             bulky_item_6 = 'Windows'
#         elif  bulky_item_6 == '74':
#                 bulky_item_6 = 'Wood Boards'
#         elif  bulky_item_6 == '75':
#             bulky_item_6 = 'Wood Bundled'
#         elif  bulky_item_6 == '76':
#             bulky_item_6 = 'Wood Cabinets'
#         elif  bulky_item_6 == '77':
#             bulky_item_6 = 'XMAS TREE'
#         elif  bulky_item_6 == '2':
#             bulky_item_6 = 'Basketball Set'
#
#
#
#
#         if  bulky_item_7  == '1':
#             bulky_item_7 = 'Bags Any Size '
#         elif  bulky_item_7 =='3':
#              bulky_item_7 = 'Bed Frame (wood)'
#         elif  bulky_item_7 == '2':
#              bulky_item_7 = 'Bed Set'
#         elif bulky_item_7  == "78":
#             bulky_item_7 = 'Bicycle'
#         elif  bulky_item_7== '5':
#              bulky_item_7  = 'Bird Cage Plastic'
#         elif  bulky_item_7  == '6':
#              bulky_item_7  = 'Blinds'
#         elif  bulky_item_7  == '7':
#             bulky_item_7  = 'Bookcase'
#         elif  bulky_item_7  == '8':
#             bulky_item_7 = 'Box Any Size'
#         elif  bulky_item_7 == '9':
#             bulky_item_7  = 'Box Spring'
#         elif  bulky_item_7 == '10':
#             bulky_item_7 = 'Cabinets'
#         elif  bulky_item_7  == '11':
#             bulky_item_7 = 'Car Parts'
#         elif  bulky_item_7 == '12':
#             bulky_item_7  = 'Carpet'
#         elif  bulky_item_7 == '13':
#              bulky_item_7 = 'Chair'
#         elif  bulky_item_7  == '79':
#              bulky_item_7 = 'Child Day Bed'
#         elif  bulky_item_7 == '14':
#             bulky_item_7 = 'Crib'
#         elif  bulky_item_7 == '15':
#             bulky_item_7  = 'Curtain Rod'
#         elif  bulky_item_7 == '16':
#              bulky_item_7 = 'Cushions'
#         elif bulky_item_7 ==  '18':
#             bulky_item_7 = "Decorating Item "
#         if  bulky_item_7  == '19':
#             bulky_item_7 = 'Desk'
#         elif  bulky_item_7 =='20':
#              bulky_item_7 = 'Door'
#         elif  bulky_item_7 == '21':
#              bulky_item_7 = 'Dresser'
#         elif bulky_item_7  == "22":
#             bulky_item_7 = 'Entertainment Center'
#         elif  bulky_item_7== '23':
#              bulky_item_7  = 'Fan (Any Size)'
#         elif  bulky_item_7  == '24':
#              bulky_item_7  = 'Fence (Wood)'
#         elif  bulky_item_7  == '25':
#             bulky_item_7  = 'File Cabinet (Wood)'
#         elif  bulky_item_7  == '26':
#             bulky_item_7 = 'Garage Door'
#         elif  bulky_item_7 == '27':
#             bulky_item_7  = 'Garage Door Opener'
#         elif  bulky_item_7 == '80':
#             bulky_item_7 = 'Gate (Wood)'
#         elif  bulky_item_7  == '28':
#             bulky_item_7 = 'Glass'
#         elif  bulky_item_7 == '29':
#             bulky_item_7  = 'Glass Window in Frame'
#         elif  bulky_item_7 == '30':
#              bulky_item_7 = 'Headboard'
#         elif  bulky_item_7  == '31':
#              bulky_item_7 = 'Ladders (Wood & Metal)'
#         elif  bulky_item_7 == '14':
#             bulky_item_7 = 'Video/Film Cameras'
#         elif  bulky_item_7 == '32':
#             bulky_item_7  = 'Lamp'
#         elif  bulky_item_7 == '33':
#              bulky_item_7 = 'Light Fixture'
#         elif  bulky_item_7 == '34':
#              bulky_item_7 = 'Loose Debris'
#         elif  bulky_item_7 == '35':
#             bulky_item_7 = 'Mattress'
#         elif  bulky_item_7 == '36':
#             bulky_item_7 = 'Mirror'
#         elif  bulky_item_7 == '37':
#             bulky_item_7 = 'Other BI'
#         elif  bulky_item_7 == '38':
#             bulky_item_7 = 'Pallet'
#         elif  bulky_item_7 == '39':
#             bulky_item_7 = 'Patio Cover'
#         elif  bulky_item_7 == '40':
#             bulky_item_7 = 'Patio Furniture'
#         elif  bulky_item_7 == '41':
#             bulky_item_7 = 'Piano'
#         elif  bulky_item_7 == '42':
#             bulky_item_7 = 'Planter Pot'
#         elif  bulky_item_7 == '43':
#             bulky_item_7 = 'Playpen'
#         elif  bulky_item_7 == '44':
#             bulky_item_7 = 'Pool Cover'
#         elif  bulky_item_7 == '45':
#             bulky_item_7 = 'Rain Gutter'
#         elif  bulky_item_7 == '46':
#             bulky_item_7 = 'Recliner'
#         elif  bulky_item_7 == '47':
#             bulky_item_7 = 'Rug'
#         elif  bulky_item_7 == '48':
#             bulky_item_7 = 'Shelf'
#         elif  bulky_item_7 == '49':
#             bulky_item_7 = 'Shopping Cart'
#         elif  bulky_item_7 == '50':
#             bulky_item_7 = 'Shower Door'
#         elif  bulky_item_7 == '51':
#             bulky_item_7 = 'Shutter'
#         elif  bulky_item_7 == '52':
#             bulky_item_7 = 'Sink'
#         elif  bulky_item_7 == '53':
#             bulky_item_7 = 'Sliding Door'
#         elif  bulky_item_7 == '54':
#             bulky_item_7 = 'Sofa'
#         elif  bulky_item_7 == '55':
#             bulky_item_7 = 'Sofa bed'
#         elif  bulky_item_7 == '56':
#             bulky_item_7 = 'Spa Cover'
#         elif  bulky_item_7 == '57':
#             bulky_item_7 = 'Spa/Jacuzzi'
#         elif  bulky_item_7 == '58':
#             bulky_item_7 = 'Stroller'
#         elif  bulky_item_7 == '59':
#             bulky_item_7 = 'Suitcase'
#         elif  bulky_item_7 == '60':
#             bulky_item_7 = 'Table'
#         elif  bulky_item_7 == '61':
#             bulky_item_7 = 'Tank Any Size'
#         elif  bulky_item_7 == '62':
#                  bulky_item_7 = 'Tire Less Than 5'
#         elif  bulky_item_7 == '63':
#             bulky_item_7 = 'Toilet'
#         elif  bulky_item_7 == '64':
#             bulky_item_7 = 'Toys (Large Ones)'
#         elif  bulky_item_7 == '65':
#             bulky_item_7 = 'Trash Cans'
#         elif  bulky_item_7 == '66':
#              bulky_item_7 = 'Trunk'
#         elif  bulky_item_7 == '67':
#             bulky_item_7 = 'Tub (Non Metal)'
#         elif  bulky_item_7 == '68':
#             bulky_item_7 = ' Vacuum Cleaner'
#         elif  bulky_item_7 == '69':
#             bulky_item_7 = 'Vehicle Tire'
#         elif  bulky_item_7 == '70':
#             bulky_item_7 = 'Walker'
#         elif  bulky_item_7 == '71':
#                 bulky_item_7 = 'Window Blinds'
#         elif  bulky_item_7 == '72':
#                 bulky_item_7 = 'Window Frame'
#         elif  bulky_item_7 == '73':
#             bulky_item_7 = 'Windows'
#         elif  bulky_item_7 == '74':
#                 bulky_item_7 = 'Wood Boards'
#         elif  bulky_item_7 == '75':
#             bulky_item_7 = 'Wood Bundled'
#         elif  bulky_item_7 == '76':
#             bulky_item_7 = 'Wood Cabinets'
#         elif  bulky_item_7 == '77':
#             bulky_item_7 = 'XMAS TREE'
#         elif  bulky_item_7 == '2':
#             bulky_item_7 = 'Basketball Set'
#
#
#
#
#
#
#
#
#
#         if  bulky_item_8  == '1':
#             bulky_item_8 = 'Bags Any Size '
#         elif  bulky_item_8 =='3':
#              bulky_item_8 = 'Bed Frame (wood)'
#         elif  bulky_item_8 == '2':
#              bulky_item_8 = 'Bed Set'
#         elif bulky_item_8  == "78":
#             bulky_item_8 = 'Bicycle'
#         elif  bulky_item_8== '5':
#              bulky_item_8  = 'Bird Cage Plastic'
#         elif  bulky_item_8  == '6':
#              bulky_item_8  = 'Blinds'
#         elif  bulky_item_8  == '7':
#             bulky_item_8  = 'Bookcase'
#         elif  bulky_item_8  == '8':
#             bulky_item_8 = 'Box Any Size'
#         elif  bulky_item_8 == '9':
#             bulky_item_8  = 'Box Spring'
#         elif  bulky_item_8 == '10':
#             bulky_item_8 = 'Cabinets'
#         elif  bulky_item_8  == '11':
#             bulky_item_8 = 'Car Parts'
#         elif  bulky_item_8 == '12':
#             bulky_item_8  = 'Carpet'
#         elif  bulky_item_8 == '13':
#              bulky_item_8 = 'Chair'
#         elif  bulky_item_8  == '79':
#              bulky_item_8 = 'Child Day Bed'
#         elif  bulky_item_8 == '14':
#             bulky_item_8 = 'Crib'
#         elif  bulky_item_8 == '15':
#             bulky_item_8  = 'Curtain Rod'
#         elif  bulky_item_8 == '16':
#              bulky_item_8 = 'Cushions'
#         elif bulky_item_8 ==  '18':
#             bulky_item_8 = "Decorating Item "
#         if  bulky_item_8  == '19':
#             bulky_item_8 = 'Desk'
#         elif  bulky_item_8 =='20':
#              bulky_item_8 = 'Door'
#         elif  bulky_item_8 == '21':
#              bulky_item_8 = 'Dresser'
#         elif bulky_item_8  == "22":
#             bulky_item_8 = 'Entertainment Center'
#         elif  bulky_item_8== '23':
#              bulky_item_8  = 'Fan (Any Size)'
#         elif  bulky_item_8  == '24':
#              bulky_item_8  = 'Fence (Wood)'
#         elif  bulky_item_8  == '25':
#             bulky_item_8  = 'File Cabinet (Wood)'
#         elif  bulky_item_8  == '26':
#             bulky_item_8 = 'Garage Door'
#         elif  bulky_item_8 == '27':
#             bulky_item_8  = 'Garage Door Opener'
#         elif  bulky_item_8 == '80':
#             bulky_item_8 = 'Gate (Wood)'
#         elif  bulky_item_8  == '28':
#             bulky_item_8 = 'Glass'
#         elif  bulky_item_8 == '29':
#             bulky_item_8  = 'Glass Window in Frame'
#         elif  bulky_item_8 == '30':
#              bulky_item_8 = 'Headboard'
#         elif  bulky_item_8  == '31':
#              bulky_item_8 = 'Ladders (Wood & Metal)'
#         elif  bulky_item_8 == '14':
#             bulky_item_8 = 'Video/Film Cameras'
#         elif  bulky_item_8 == '32':
#             bulky_item_8  = 'Lamp'
#         elif  bulky_item_8 == '33':
#              bulky_item_8 = 'Light Fixture'
#         elif  bulky_item_8 == '34':
#              bulky_item_8 = 'Loose Debris'
#         elif  bulky_item_8 == '35':
#             bulky_item_8 = 'Mattress'
#         elif  bulky_item_8 == '36':
#             bulky_item_8 = 'Mirror'
#         elif  bulky_item_8 == '37':
#             bulky_item_8 = 'Other BI'
#         elif  bulky_item_8 == '38':
#             bulky_item_8 = 'Pallet'
#         elif  bulky_item_8 == '39':
#             bulky_item_8 = 'Patio Cover'
#         elif  bulky_item_8 == '40':
#             bulky_item_8 = 'Patio Furniture'
#         elif  bulky_item_8 == '41':
#             bulky_item_8 = 'Piano'
#         elif  bulky_item_8 == '42':
#             bulky_item_8 = 'Planter Pot'
#         elif  bulky_item_8 == '43':
#             bulky_item_8 = 'Playpen'
#         elif  bulky_item_8 == '44':
#             bulky_item_8 = 'Pool Cover'
#         elif  bulky_item_8 == '45':
#             bulky_item_8 = 'Rain Gutter'
#         elif  bulky_item_8 == '46':
#             bulky_item_8 = 'Recliner'
#         elif  bulky_item_8 == '47':
#             bulky_item_8 = 'Rug'
#         elif  bulky_item_8 == '48':
#             bulky_item_8 = 'Shelf'
#         elif  bulky_item_8 == '49':
#             bulky_item_8 = 'Shopping Cart'
#         elif  bulky_item_8 == '50':
#             bulky_item_8 = 'Shower Door'
#         elif  bulky_item_8 == '51':
#             bulky_item_8 = 'Shutter'
#         elif  bulky_item_8 == '52':
#             bulky_item_8 = 'Sink'
#         elif  bulky_item_8 == '53':
#             bulky_item_8 = 'Sliding Door'
#         elif  bulky_item_8 == '54':
#             bulky_item_8 = 'Sofa'
#         elif  bulky_item_8 == '55':
#             bulky_item_8 = 'Sofa bed'
#         elif  bulky_item_8 == '56':
#             bulky_item_8 = 'Spa Cover'
#         elif  bulky_item_8 == '57':
#             bulky_item_8 = 'Spa/Jacuzzi'
#         elif  bulky_item_8 == '58':
#             bulky_item_8 = 'Stroller'
#         elif  bulky_item_8 == '59':
#             bulky_item_8 = 'Suitcase'
#         elif  bulky_item_8 == '60':
#             bulky_item_8 = 'Table'
#         elif  bulky_item_8 == '61':
#             bulky_item_8 = 'Tank Any Size'
#         elif  bulky_item_8 == '62':
#                  bulky_item_8 = 'Tire Less Than 5'
#         elif  bulky_item_8 == '63':
#             bulky_item_8 = 'Toilet'
#         elif  bulky_item_8 == '64':
#             bulky_item_8 = 'Toys (Large Ones)'
#         elif  bulky_item_8 == '65':
#             bulky_item_8 = 'Trash Cans'
#         elif  bulky_item_8 == '66':
#              bulky_item_8 = 'Trunk'
#         elif  bulky_item_8 == '67':
#             bulky_item_8 = 'Tub (Non Metal)'
#         elif  bulky_item_8 == '68':
#             bulky_item_8 = ' Vacuum Cleaner'
#         elif  bulky_item_8 == '69':
#             bulky_item_8 = 'Vehicle Tire'
#         elif  bulky_item_8 == '70':
#             bulky_item_8 = 'Walker'
#         elif  bulky_item_8 == '71':
#                 bulky_item_8 = 'Window Blinds'
#         elif  bulky_item_8 == '72':
#                 bulky_item_8 = 'Window Frame'
#         elif  bulky_item_8 == '73':
#             bulky_item_8 = 'Windows'
#         elif  bulky_item_8 == '74':
#                 bulky_item_8 = 'Wood Boards'
#         elif  bulky_item_8 == '75':
#             bulky_item_8 = 'Wood Bundled'
#         elif  bulky_item_8 == '76':
#             bulky_item_8 = 'Wood Cabinets'
#         elif  bulky_item_8 == '77':
#             bulky_item_8 = 'XMAS TREE'
#         elif  bulky_item_8 == '2':
#             bulky_item_8 = 'Basketball Set'
#
#
#
#
#
#
#         if  bulky_item_9  == '1':
#             bulky_item_9 = 'Bags Any Size '
#         elif  bulky_item_9 =='3':
#              bulky_item_9 = 'Bed Frame (wood)'
#         elif  bulky_item_9 == '2':
#              bulky_item_9 = 'Bed Set'
#         elif bulky_item_9  == "78":
#             bulky_item_9 = 'Bicycle'
#         elif  bulky_item_9== '5':
#              bulky_item_9  = 'Bird Cage Plastic'
#         elif  bulky_item_9  == '6':
#              bulky_item_9  = 'Blinds'
#         elif  bulky_item_9  == '7':
#             bulky_item_9  = 'Bookcase'
#         elif  bulky_item_9  == '8':
#             bulky_item_9 = 'Box Any Size'
#         elif  bulky_item_9 == '9':
#             bulky_item_9  = 'Box Spring'
#         elif  bulky_item_9 == '10':
#             bulky_item_9 = 'Cabinets'
#         elif  bulky_item_9  == '11':
#             bulky_item_9 = 'Car Parts'
#         elif  bulky_item_9 == '12':
#             bulky_item_9  = 'Carpet'
#         elif  bulky_item_9 == '13':
#              bulky_item_9 = 'Chair'
#         elif  bulky_item_9  == '79':
#              bulky_item_9 = 'Child Day Bed'
#         elif  bulky_item_9 == '14':
#             bulky_item_9 = 'Crib'
#         elif  bulky_item_9 == '15':
#             bulky_item_9  = 'Curtain Rod'
#         elif  bulky_item_9 == '16':
#              bulky_item_9 = 'Cushions'
#         elif bulky_item_9 ==  '18':
#             bulky_item_9 = "Decorating Item "
#         if  bulky_item_9  == '19':
#             bulky_item_9 = 'Desk'
#         elif  bulky_item_9 =='20':
#              bulky_item_9 = 'Door'
#         elif  bulky_item_9 == '21':
#              bulky_item_9 = 'Dresser'
#         elif bulky_item_9  == "22":
#             bulky_item_9 = 'Entertainment Center'
#         elif  bulky_item_9== '23':
#              bulky_item_9  = 'Fan (Any Size)'
#         elif  bulky_item_9  == '24':
#              bulky_item_9  = 'Fence (Wood)'
#         elif  bulky_item_9  == '25':
#             bulky_item_9  = 'File Cabinet (Wood)'
#         elif  bulky_item_9  == '26':
#             bulky_item_9 = 'Garage Door'
#         elif  bulky_item_9 == '27':
#             bulky_item_9  = 'Garage Door Opener'
#         elif  bulky_item_9 == '80':
#             bulky_item_9 = 'Gate (Wood)'
#         elif  bulky_item_9  == '28':
#             bulky_item_9 = 'Glass'
#         elif  bulky_item_9 == '29':
#             bulky_item_9  = 'Glass Window in Frame'
#         elif  bulky_item_9 == '30':
#              bulky_item_9 = 'Headboard'
#         elif  bulky_item_9  == '31':
#              bulky_item_9 = 'Ladders (Wood & Metal)'
#         elif  bulky_item_9 == '14':
#             bulky_item_9 = 'Video/Film Cameras'
#         elif  bulky_item_9 == '32':
#             bulky_item_9  = 'Lamp'
#         elif  bulky_item_9 == '33':
#              bulky_item_9 = 'Light Fixture'
#         elif  bulky_item_9 == '34':
#              bulky_item_9 = 'Loose Debris'
#         elif  bulky_item_9 == '35':
#             bulky_item_9 = 'Mattress'
#         elif  bulky_item_9 == '36':
#             bulky_item_9 = 'Mirror'
#         elif  bulky_item_9 == '37':
#             bulky_item_9 = 'Other BI'
#         elif  bulky_item_9 == '38':
#             bulky_item_9 = 'Pallet'
#         elif  bulky_item_9 == '39':
#             bulky_item_9 = 'Patio Cover'
#         elif  bulky_item_9 == '40':
#             bulky_item_9 = 'Patio Furniture'
#         elif  bulky_item_9 == '41':
#             bulky_item_9 = 'Piano'
#         elif  bulky_item_9 == '42':
#             bulky_item_9 = 'Planter Pot'
#         elif  bulky_item_9 == '43':
#             bulky_item_9 = 'Playpen'
#         elif  bulky_item_9 == '44':
#             bulky_item_9 = 'Pool Cover'
#         elif  bulky_item_9 == '45':
#             bulky_item_9 = 'Rain Gutter'
#         elif  bulky_item_9 == '46':
#             bulky_item_9 = 'Recliner'
#         elif  bulky_item_9 == '47':
#             bulky_item_9 = 'Rug'
#         elif  bulky_item_9 == '48':
#             bulky_item_9 = 'Shelf'
#         elif  bulky_item_9 == '49':
#             bulky_item_9 = 'Shopping Cart'
#         elif  bulky_item_9 == '50':
#             bulky_item_9 = 'Shower Door'
#         elif  bulky_item_9 == '51':
#             bulky_item_9 = 'Shutter'
#         elif  bulky_item_9 == '52':
#             bulky_item_9 = 'Sink'
#         elif  bulky_item_9 == '53':
#             bulky_item_9 = 'Sliding Door'
#         elif  bulky_item_9 == '54':
#             bulky_item_9 = 'Sofa'
#         elif  bulky_item_9 == '55':
#             bulky_item_9 = 'Sofa bed'
#         elif  bulky_item_9 == '56':
#             bulky_item_9 = 'Spa Cover'
#         elif  bulky_item_9 == '57':
#             bulky_item_9 = 'Spa/Jacuzzi'
#         elif  bulky_item_9 == '58':
#             bulky_item_9 = 'Stroller'
#         elif  bulky_item_9 == '59':
#             bulky_item_9 = 'Suitcase'
#         elif  bulky_item_9 == '60':
#             bulky_item_9 = 'Table'
#         elif  bulky_item_9 == '61':
#             bulky_item_9 = 'Tank Any Size'
#         elif  bulky_item_9 == '62':
#                  bulky_item_9 = 'Tire Less Than 5'
#         elif  bulky_item_9 == '63':
#             bulky_item_9 = 'Toilet'
#         elif  bulky_item_9 == '64':
#             bulky_item_9 = 'Toys (Large Ones)'
#         elif  bulky_item_9 == '65':
#             bulky_item_9 = 'Trash Cans'
#         elif  bulky_item_9 == '66':
#              bulky_item_9 = 'Trunk'
#         elif  bulky_item_9 == '67':
#             bulky_item_9 = 'Tub (Non Metal)'
#         elif  bulky_item_9 == '68':
#             bulky_item_9 = ' Vacuum Cleaner'
#         elif  bulky_item_9 == '69':
#             bulky_item_9 = 'Vehicle Tire'
#         elif  bulky_item_9 == '70':
#             bulky_item_9 = 'Walker'
#         elif  bulky_item_9 == '71':
#                 bulky_item_9 = 'Window Blinds'
#         elif  bulky_item_9 == '72':
#                 bulky_item_9 = 'Window Frame'
#         elif  bulky_item_9 == '73':
#             bulky_item_9 = 'Windows'
#         elif  bulky_item_9 == '74':
#                 bulky_item_9 = 'Wood Boards'
#         elif  bulky_item_9 == '75':
#             bulky_item_9 = 'Wood Bundled'
#         elif  bulky_item_9 == '76':
#             bulky_item_9 = 'Wood Cabinets'
#         elif  bulky_item_9 == '77':
#             bulky_item_9 = 'XMAS TREE'
#         elif  bulky_item_9 == '2':
#             bulky_item_9 = 'Basketball Set'
#
#
#
#         if  bulky_item_10  == '1':
#             bulky_item_10 = 'Bags Any Size '
#         elif  bulky_item_10 =='3':
#              bulky_item_10 = 'Bed Frame (wood)'
#         elif  bulky_item_10 == '2':
#              bulky_item_10 = 'Bed Set'
#         elif bulky_item_10  == "78":
#             bulky_item_10 = 'Bicycle'
#         elif  bulky_item_10== '5':
#              bulky_item_10  = 'Bird Cage (Plastic)'
#         elif  bulky_item_10  == '6':
#              bulky_item_10  = 'Blinds'
#         elif  bulky_item_10  == '7':
#             bulky_item_10  = 'Bookcase'
#         elif  bulky_item_10  == '8':
#             bulky_item_10 = 'Box Any Size'
#         elif  bulky_item_10 == '9':
#             bulky_item_10  = 'Box Spring'
#         elif  bulky_item_10 == '10':
#             bulky_item_10 = 'Cabinets'
#         elif  bulky_item_10  == '11':
#             bulky_item_10 = 'Car Parts'
#         elif  bulky_item_10 == '12':
#             bulky_item_10  = 'Carpet'
#         elif  bulky_item_10 == '13':
#              bulky_item_10 = 'Chair'
#         elif  bulky_item_10  == '79':
#              bulky_item_10 = 'Child Day Bed'
#         elif  bulky_item_10 == '14':
#             bulky_item_10 = 'Crib'
#         elif  bulky_item_10 == '15':
#             bulky_item_10  = 'Curtain Rod'
#         elif  bulky_item_10 == '16':
#              bulky_item_10 = 'Cushions'
#         elif bulky_item_10 ==  '18':
#             bulky_item_10 = "Decorating Item "
#         if  bulky_item_10  == '19':
#             bulky_item_10 = 'Desk (Wood)'
#         elif  bulky_item_10 =='20':
#              bulky_item_10 = 'Door'
#         elif  bulky_item_10 == '21':
#              bulky_item_10 = 'Dresser'
#         elif bulky_item_10  == "22":
#             bulky_item_10 = 'Entertainment Center'
#         elif  bulky_item_10== '23':
#              bulky_item_10  = 'Fan (Any Size)'
#         elif  bulky_item_10  == '24':
#              bulky_item_10  = 'Fence (Wood)'
#         elif  bulky_item_10  == '25':
#             bulky_item_10  = 'File Cabinet (Wood)'
#         elif  bulky_item_10  == '26':
#             bulky_item_10 = 'Garage Door'
#         elif  bulky_item_10 == '27':
#             bulky_item_10  = 'Garage Door Opener'
#         elif  bulky_item_10 == '80':
#             bulky_item_10 = 'Gate (Wood)'
#         elif  bulky_item_10  == '28':
#             bulky_item_10 = 'Glass'
#         elif  bulky_item_10 == '29':
#             bulky_item_10  = 'Glass Window in Frame'
#         elif  bulky_item_10 == '30':
#              bulky_item_10 = 'Headboard'
#         elif  bulky_item_10  == '31':
#              bulky_item_10 = 'Ladders (Wood & Metal)'
#         elif  bulky_item_10 == '14':
#             bulky_item_10 = 'Video/Film Cameras'
#         elif  bulky_item_10 == '32':
#             bulky_item_10  = 'Lamp'
#         elif  bulky_item_10 == '33':
#              bulky_item_10 = 'Light Fixture'
#         elif  bulky_item_10 == '34':
#              bulky_item_10 = 'Loose Debris'
#         elif  bulky_item_10 == '35':
#             bulky_item_10 = 'Mattress'
#         elif  bulky_item_10 == '36':
#             bulky_item_10 = 'Mirror'
#         elif  bulky_item_10 == '37':
#             bulky_item_10 = 'Other BI'
#         elif  bulky_item_10 == '38':
#             bulky_item_10 = 'Pallet'
#         elif  bulky_item_10 == '39':
#             bulky_item_10 = 'Patio Cover'
#         elif  bulky_item_10 == '40':
#             bulky_item_10 = 'Patio Furniture'
#         elif  bulky_item_10 == '41':
#             bulky_item_10 = 'Piano'
#         elif  bulky_item_10 == '42':
#             bulky_item_10 = 'Planter Pot'
#         elif  bulky_item_10 == '43':
#             bulky_item_10 = 'Playpen'
#         elif  bulky_item_10 == '44':
#             bulky_item_10 = 'Pool Cover'
#         elif  bulky_item_10 == '45':
#             bulky_item_10 = 'Rain Gutter'
#         elif  bulky_item_10 == '46':
#             bulky_item_10 = 'Recliner'
#         elif  bulky_item_10 == '47':
#             bulky_item_10 = 'Rug'
#         elif  bulky_item_10 == '48':
#             bulky_item_10 = 'Shelf'
#         elif  bulky_item_10 == '49':
#             bulky_item_10 = 'Shopping Cart'
#         elif  bulky_item_10 == '50':
#             bulky_item_10 = 'Shower Door'
#         elif  bulky_item_10 == '51':
#             bulky_item_10 = 'Shutter'
#         elif  bulky_item_10 == '52':
#             bulky_item_10 = 'Sink'
#         elif  bulky_item_10 == '53':
#             bulky_item_10 = 'Sliding Door'
#         elif  bulky_item_10 == '54':
#             bulky_item_10 = 'Sofa'
#         elif  bulky_item_10 == '55':
#             bulky_item_10 = 'Sofa bed'
#         elif  bulky_item_10 == '56':
#             bulky_item_10 = 'Spa Cover'
#         elif  bulky_item_10 == '57':
#             bulky_item_10 = 'Spa/Jacuzzi'
#         elif  bulky_item_10 == '58':
#             bulky_item_10 = 'Stroller'
#         elif  bulky_item_10 == '59':
#             bulky_item_10 = 'Suitcase'
#         elif  bulky_item_10 == '60':
#             bulky_item_10 = 'Table'
#         elif  bulky_item_10 == '61':
#             bulky_item_10 = 'Tank Any Size'
#         elif  bulky_item_10 == '62':
#                  bulky_item_10 = 'Tire Less Than 5'
#         elif  bulky_item_10 == '63':
#             bulky_item_10 = 'Toilet'
#         elif  bulky_item_10 == '64':
#             bulky_item_10 = 'Toys (Large Ones)'
#         elif  bulky_item_10 == '65':
#             bulky_item_10 = 'Trash Cans'
#         elif  bulky_item_10 == '66':
#              bulky_item_10 = 'Trunk'
#         elif  bulky_item_10 == '67':
#             bulky_item_10 = 'Tub (Non Metal)'
#         elif  bulky_item_10 == '68':
#             bulky_item_10 = ' Vacuum Cleaner'
#         elif  bulky_item_10 == '69':
#             bulky_item_10 = 'Vehicle Tire'
#         elif  bulky_item_10 == '70':
#             bulky_item_10 = 'Walker'
#         elif  bulky_item_10 == '71':
#                 bulky_item_10 = 'Window Blinds'
#         elif  bulky_item_10 == '72':
#                 bulky_item_10 = 'Window Frame'
#         elif  bulky_item_10 == '73':
#             bulky_item_10 = 'Windows'
#         elif  bulky_item_10 == '74':
#                 bulky_item_10 = 'Wood Boards'
#         elif  bulky_item_10 == '75':
#             bulky_item_10 = 'Wood Bundled'
#         elif  bulky_item_10 == '76':
#             bulky_item_10 = 'Wood Cabinets'
#         elif  bulky_item_10 == '77':
#             bulky_item_10 = 'XMAS TREE'
#         elif  bulky_item_10 == '2':
#             bulky_item_10 = 'Basketball Set'
#
#         dL311 = dict()
#         l311 = []
#
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("BulkyItemType", bulky_item_1)
#         d.setdefault("Type", "Bulky Items")
#         d.setdefault("Name", bulky_uid_1 )
#         d.setdefault("BulkyItemCount", bulky_qyt_1)
#         l311.append(d)
#         dL311 = dict()
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("BulkyItemType", bulky_item_2)
#         d.setdefault("Type", "Bulky Items")
#         d.setdefault("Name", bulky_uid_2)
#         d.setdefault("BulkyItemCount", bulky_qyt_2)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("BulkyItemType", bulky_item_3)
#         d.setdefault("Type", "Bulky Items")
#         d.setdefault("Name", bulky_uid_3)
#         d.setdefault("BulkyItemCount", bulky_qyt_3)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("BulkyItemType", bulky_item_4)
#         d.setdefault("Type", "Bulky Items")
#         d.setdefault("Name", bulky_uid_4)
#         d.setdefault("BulkyItemCount", bulky_qyt_4)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("BulkyItemType", bulky_item_5)
#         d.setdefault("Type", "Bulky Items")
#         d.setdefault("Name", bulky_uid_5)
#         d.setdefault("BulkyItemCount", bulky_qyt_5)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("BulkyItemType", bulky_item_6)
#         d.setdefault("Type", "Bulky Items")
#         d.setdefault("Name", bulky_uid_6)
#         d.setdefault("BulkyItemCount", bulky_qyt_6)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("BulkyItemType", bulky_item_7)
#         d.setdefault("Type", "Bulky Items")
#         d.setdefault("Name", bulky_uid_7)
#         d.setdefault("BulkyItemCount", bulky_qyt_7)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("BulkyItemType", bulky_item_8)
#         d.setdefault("Type", "Bulky Items")
#         d.setdefault("Name", bulky_uid_8)
#         d.setdefault("BulkyItemCount", bulky_qyt_8)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("BulkyItemType", bulky_item_9)
#         d.setdefault("Type", "Bulky Items")
#         d.setdefault("Name", bulky_uid_9)
#         d.setdefault("BulkyItemCount", bulky_qyt_9)
#         l311.append(d)
#         d = dict()
#        d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("BulkyItemType", bulky_item_10)
#         d.setdefault("Type", "Bulky Items")
#         d.setdefault("Name", bulky_uid_10)
#         d.setdefault("BulkyItemCount", bulky_qyt_10)
#         l311.append(d)
#
#
#         lIndexes = []
#         nCnt = len(l311)
#         for i in range(nCnt):
#             d = l311[i]
#             if(d['Name'].strip() == ''):
#                 del d['Name']
#
#             if(d['BulkyItemCount'] == "None"):
#                 lIndexes.append(i)
#         if(len(lIndexes)>0):
#             for i in reversed(lIndexes):
#                 del l311[i]
#
#         if(len(l311)>0):
#             dL311.setdefault("BulkyItem", l311)
#             dResult.setdefault("ListOfLa311BulkyItem",dL311)
#             lResults.append({"MetaData": {}, "SRData": dResult})
#             sReq = json.dumps(lResults,sort_keys=True, indent=2)
#             results = {"MetaData": {}, "SRData": dResult}
#
#             start = time.time()
#             url = "https://myla311Test.lacity.org/myla311router/mylasrbe/1/UpsertSANSRWithCodes"
#             headers = {'Content-type': 'text/plain', 'Accept': '/'}
#             # r = requests.post(url, data= json.dumps(results), headers=headers,  verify=False)
#             print results
#             print r.text
#             print 'It took', time.time()-start, 'seconds.'
#
#             ii = ii + 1
#             print (str(ii) + " recs sent to server.",  'It took', time.time()-start, 'seconds.')
#
#
#     print("Finished")
# except Exception,e:
#     exc_type, exc_obj, exc_tb = sys.exc_info()
#     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#     print(exc_type, fname, exc_tb.tb_lineno)




#
#
# pyFC = "sc_bkup"
# clauseSBE = "WHERE CATEGORY = 4 OR CATEGORY =  18 OR CATEGORY = 5 AND RESOLUTION_CODE <> ''  AND RESOLUTION_CODE <> '-1' AND UID1 = '080620151821182201'"
# if(__name__=='__main__'):
#     # sMsg = printObjects()
#     # print(sMsg)
#
#     connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
#     # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
#     conn = pyodbc.connect(connstr)
#     cursor = conn.cursor()
#     FN_SRNumber = "SRNumber"
#     lFields = [FN_SRNumber, "RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user", "last_edited_date"]
#     #lFields = ["SRNumber"]
#     sFields = ""
#     for fld in lFields:
#         if(sFields==""):
#             sFields = fld
#         else:
#             sFields = sFields + "," + fld
#     #List of the fields you'd like to exclude, like ItemCount for example.
#     lFieldsExcluded = ["ContactFirstName", "ContactLastName", "RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user", "last_edited_date"]
#
#     #sSQL = "SELECT SRNumber FROM {}".format(pyFC)
#     sSQL = "SELECT {} FROM {}  {}".format(sFields, pyFC, clauseSBE)
#
#
#     cursor.execute(sSQL)
#     #columns = [column[0] for column in cursor.description]
#     columns = []
#     for column in cursor.description:
#         if not (column[0] in lFieldsExcluded):
#             columns.append(column[0])
#
#
#
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
#     ewaste_qyt_1 = " "
#     ewaste_qyt_2 = " "
#     ewaste_qyt_3 = " "
#     ewaste_qyt_4 = " "
#     ewaste_qyt_5 = " "
#     ewaste_qyt_6 = " "
#     ewaste_qyt_7 = " "
#     ewaste_qyt_8 = " "
#     ewaste_qyt_9 = " "
#     ewaste_qyt_10 = " "
#     ewaste_uid_1 = ""
#     ewaste_uid_2 = " "
#     ewaste_uid_3 = ""
#     ewaste_uid_4 = ""
#     ewaste_uid_5 = ""
#     ewaste_uid_6 = ""
#     ewaste_uid_7 = ""
#     ewaste_uid_8 = ""
#     ewaste_uid_9 = ""
#     ewaste_uid_10 = ""
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
#         ewaste_item_1 = (str(row[lFields.index("ITEM_1")]))
#         ewaste_item_2 = (str(row[lFields.index("ITEM_2")]))
#         ewaste_item_3 = (str(row[lFields.index("ITEM_3")]))
#         ewaste_item_4 = (str(row[lFields.index("ITEM_4")]))
#         ewaste_item_5 = (str(row[lFields.index("ITEM_5")]))
#         ewaste_item_6= (str(row[lFields.index("ITEM_6")]))
#         ewaste_item_7 =(str(row[lFields.index("ITEM_7")]))
#         ewaste_item_8 = (str(row[lFields.index("ITEM_8")]))
#         ewaste_item_9 =(str(row[lFields.index("ITEM_9")]))
#         ewaste_item_10 = (str(row[lFields.index("ITEM_10")]))
#         ewaste_qyt_1 = (str(row[lFields.index("QYT_1")]))
#         ewaste_qyt_2 = (str(row[lFields.index("QYT_2")]))
#         ewaste_qyt_3 = (str(row[lFields.index("QYT_3")]))
#         ewaste_qyt_4 = (str(row[lFields.index("QYT_4")]))
#         ewaste_qyt_5 = (str(row[lFields.index("QYT_5")]))
#         ewaste_qyt_6 = (str(row[lFields.index("QTY_6")]))
#         ewaste_qyt_7 = (str(row[lFields.index("QTY_7")]))
#         ewaste_qyt_8 = (str(row[lFields.index("QTY_8")]))
#         ewaste_qyt_9 = (str(row[lFields.index("QTY_9")]))
#         ewaste_qyt_10 = (str(row[lFields.index("QTY_10")]))
#
#
#
#         ewaste_uid_1 = (str(row[lFields.index("UID1")]))
#         ewaste_uid_2 = (str(row[lFields.index("UID2")]))
#         ewaste_uid_3 = (str(row[lFields.index("UID3")]))
#         ewaste_uid_4 = (str(row[lFields.index("UID4")]))
#         ewaste_uid_5 = (str(row[lFields.index("UID5")]))
#         ewaste_uid_6 = (str(row[lFields.index("UID6")]))
#         ewaste_uid_7 = (str(row[lFields.index("UID7")]))
#         ewaste_uid_8 = (str(row[lFields.index("UID8")]))
#         ewaste_uid_9 = (str(row[lFields.index("UID9")]))
#         ewaste_uid_10 = (str(row[lFields.index("UID10")]))
#
#
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
#         dResult.setdefault("UpdatedByUserLogin", "SANSTAR1")
#
#
#         # dResult.setdefault("ListOfLa311DeadAnimalRemoval", dict())
#         l311 = []
#         if  ewaste_item_1  == '1':
#             ewaste_item_1 = 'Copier/Scanner'
#         elif  ewaste_item_1 =='2':
#              ewaste_item_1 = 'Electronic Equipment'
#         elif  ewaste_item_1 == '3':
#              ewaste_item_1 = 'Laptops/Tablets'
#         elif ewaste_item_1  == "4":
#             ewaste_item_1 = 'Microwaves'
#         elif  ewaste_item_1== '5':
#              ewaste_item_1  = 'Monitors'
#         elif  ewaste_item_1  == '6':
#              ewaste_item_1  = 'Other Ewaste'
#         elif  ewaste_item_1  == '7':
#             ewaste_item_1  = 'Computers'
#         elif  ewaste_item_1  == '8':
#             ewaste_item_1 = 'Printer/Fax Machine'
#         elif  ewaste_item_1 == '9':
#             ewaste_item_1  = 'Stereo/Radios'
#         elif  ewaste_item_1 == '10':
#             ewaste_item_1 = 'Speakers'
#         elif  ewaste_item_1  == '11':
#             ewaste_item_1 = 'Telephone'
#         elif  ewaste_item_1 == '12':
#             ewaste_item_1  = 'TV (Any Size)'
#         elif  ewaste_item_1 == '13':
#              ewaste_item_1 = 'VCR/DVD Player'
#         elif  ewaste_item_1  == '13':
#              ewaste_item_1 = 'Child Day Bed'
#         elif  ewaste_item_1 == '14':
#             ewaste_item_1 = 'Video/Film Cameras'
#         elif  ewaste_item_1 == '15':
#             ewaste_item_1  = 'Video/Games Components'
#         elif  ewaste_item_1 == '16':
#              ewaste_item_1 = 'Cell Phone'
#         elif ewaste_item_1 ==  '17':
#             ewaste_item_1 = "Vacuum Cleaner"
#
#
#
#
#         l311 = []
#         if  ewaste_item_2  == '1':
#             ewaste_item_2 = 'Copier/Scanner'
#         elif  ewaste_item_2 =='2':
#              ewaste_item_2 = 'Electronic Equipment'
#         elif  ewaste_item_2 == '3':
#              ewaste_item_2 = 'Laptops/Tablets'
#         elif ewaste_item_2  == "4":
#             ewaste_item_2 = 'Microwaves'
#         elif  ewaste_item_2== '5':
#              ewaste_item_2  = 'Monitors'
#         elif  ewaste_item_2  == '6':
#              ewaste_item_2  = 'Other Ewaste'
#         elif  ewaste_item_2  == '7':
#             ewaste_item_2  = 'Computers'
#         elif  ewaste_item_2  == '8':
#             ewaste_item_2 = 'Printer/Fax Machine'
#         elif  ewaste_item_2 == '9':
#             ewaste_item_2  = 'Stereo/Radios'
#         elif  ewaste_item_2 == '10':
#             ewaste_item_2 = 'Speakers'
#         elif  ewaste_item_2  == '11':
#             ewaste_item_2 = 'Telephone'
#         elif  ewaste_item_2 == '12':
#             ewaste_item_2  = 'TV (Any Size)'
#         elif  ewaste_item_2 == '13':
#              ewaste_item_2 = 'VCR/DVD Player'
#         elif  ewaste_item_2  == '13':
#              ewaste_item_2 = 'Child Day Bed'
#         elif  ewaste_item_2 == '14':
#             ewaste_item_2 = 'Video/Film Cameras'
#         elif  ewaste_item_2 == '15':
#             ewaste_item_2  = 'Video/Games Components'
#         elif  ewaste_item_2 == '16':
#              ewaste_item_2 = 'Cell Phone'
#         elif ewaste_item_2 ==  '17':
#             ewaste_item_2 = "Vacuum Cleaner"
#
#
#
#
#
#
#         l311 = []
#         if  ewaste_item_3  == '1':
#             ewaste_item_3 = 'Copier/Scanner'
#         elif  ewaste_item_3 =='2':
#              ewaste_item_3 = 'Electronic Equipment'
#         elif  ewaste_item_3 == '3':
#              ewaste_item_3 = 'Laptops/Tablets'
#         elif ewaste_item_3  == "4":
#             ewaste_item_3 = 'Microwaves'
#         elif  ewaste_item_3== '5':
#              ewaste_item_3  = 'Monitors'
#         elif  ewaste_item_3  == '6':
#              ewaste_item_3  = 'Other Ewaste'
#         elif  ewaste_item_3  == '7':
#             ewaste_item_3  = 'Computers'
#         elif  ewaste_item_3  == '8':
#             ewaste_item_3 = 'Printer/Fax Machine'
#         elif  ewaste_item_3 == '9':
#             ewaste_item_3  = 'Stereo/Radios'
#         elif  ewaste_item_3 == '10':
#             ewaste_item_3 = 'Speakers'
#         elif  ewaste_item_3  == '11':
#             ewaste_item_3 = 'Telephone'
#         elif  ewaste_item_3 == '12':
#             ewaste_item_3  = 'TV (Any Size)'
#         elif  ewaste_item_3 == '13':
#              ewaste_item_3 = 'VCR/DVD Player'
#         elif  ewaste_item_3  == '13':
#              ewaste_item_3 = 'Child Day Bed'
#         elif  ewaste_item_3 == '14':
#             ewaste_item_3 = 'Video/Film Cameras'
#         elif  ewaste_item_3 == '15':
#             ewaste_item_3  = 'Video/Games Components'
#         elif  ewaste_item_3 == '16':
#              ewaste_item_3 = 'Cell Phone'
#         elif ewaste_item_3 ==  '17':
#             ewaste_item_3 = "Vacuum Cleaner"
#
#
#
#
#         l311 = []
#         if  ewaste_item_4  == '1':
#             ewaste_item_4 = 'Copier/Scanner'
#         elif  ewaste_item_4 =='2':
#              ewaste_item_4 = 'Electronic Equipment'
#         elif  ewaste_item_4 == '3':
#              ewaste_item_4 = 'Laptops/Tablets'
#         elif ewaste_item_4  == "4":
#             ewaste_item_4 = 'Microwaves'
#         elif  ewaste_item_4== '5':
#              ewaste_item_4  = 'Monitors'
#         elif  ewaste_item_4  == '6':
#              ewaste_item_4  = 'Other Ewaste'
#         elif  ewaste_item_4  == '7':
#             ewaste_item_4  = 'Computers'
#         elif  ewaste_item_4  == '8':
#             ewaste_item_4 = 'Printer/Fax Machine'
#         elif  ewaste_item_4 == '9':
#             ewaste_item_4  = 'Stereo/Radios'
#         elif  ewaste_item_4 == '10':
#             ewaste_item_4 = 'Speakers'
#         elif  ewaste_item_4  == '11':
#             ewaste_item_4 = 'Telephone'
#         elif  ewaste_item_4 == '12':
#             ewaste_item_4  = 'TV (Any Size)'
#         elif  ewaste_item_4 == '13':
#              ewaste_item_4 = 'VCR/DVD Player'
#         elif  ewaste_item_4  == '13':
#              ewaste_item_4 = 'Child Day Bed'
#         elif  ewaste_item_4 == '14':
#             ewaste_item_4 = 'Video/Film Cameras'
#         elif  ewaste_item_4 == '15':
#             ewaste_item_4  = 'Video/Games Components'
#         elif  ewaste_item_4 == '16':
#              ewaste_item_4 = 'Cell Phone'
#         elif ewaste_item_4 ==  '17':
#             ewaste_item_4 = "Vacuum Cleaner"
#
#
#         l311 = []
#         if  ewaste_item_5  == '1':
#             ewaste_item_5 = 'Copier/Scanner'
#         elif  ewaste_item_5 =='2':
#              ewaste_item_5 = 'Electronic Equipment'
#         elif  ewaste_item_5 == '3':
#              ewaste_item_5 = 'Laptops/Tablets'
#         elif ewaste_item_5  == "4":
#             ewaste_item_5 = 'Microwaves'
#         elif  ewaste_item_5== '5':
#              ewaste_item_5  = 'Monitors'
#         elif  ewaste_item_5  == '6':
#              ewaste_item_5  = 'Other Ewaste'
#         elif  ewaste_item_5  == '7':
#             ewaste_item_5  = 'Computers'
#         elif  ewaste_item_5  == '8':
#             ewaste_item_5 = 'Printer/Fax Machine'
#         elif  ewaste_item_5 == '9':
#             ewaste_item_5  = 'Stereo/Radios'
#         elif  ewaste_item_5 == '10':
#             ewaste_item_5 = 'Speakers'
#         elif  ewaste_item_5  == '11':
#             ewaste_item_5 = 'Telephone'
#         elif  ewaste_item_5 == '12':
#             ewaste_item_5  = 'TV (Any Size)'
#         elif  ewaste_item_5 == '13':
#              ewaste_item_5 = 'VCR/DVD Player'
#         elif  ewaste_item_5  == '13':
#              ewaste_item_5 = 'Child Day Bed'
#         elif  ewaste_item_5 == '14':
#             ewaste_item_5 = 'Video/Film Cameras'
#         elif  ewaste_item_5 == '15':
#             ewaste_item_5  = 'Video/Games Components'
#         elif  ewaste_item_5 == '16':
#              ewaste_item_5 = 'Cell Phone'
#         elif ewaste_item_5 ==  '17':
#             ewaste_item_5 = "Vacuum Cleaner"
#
#
#
#         l311 = []
#         if  ewaste_item_6  == '1':
#             ewaste_item_6 = 'Copier/Scanner'
#         elif  ewaste_item_6 =='2':
#              ewaste_item_6 = 'Electronic Equipment'
#         elif  ewaste_item_6 == '3':
#              ewaste_item_6 = 'Laptops/Tablets'
#         elif ewaste_item_6  == "4":
#             ewaste_item_6 = 'Microwaves'
#         elif  ewaste_item_6== '5':
#              ewaste_item_6  = 'Monitors'
#         elif  ewaste_item_6  == '6':
#              ewaste_item_6  = 'Other Ewaste'
#         elif  ewaste_item_6  == '7':
#             ewaste_item_6  = 'Computers'
#         elif  ewaste_item_6  == '8':
#             ewaste_item_6 = 'Printer/Fax Machine'
#         elif  ewaste_item_6 == '9':
#             ewaste_item_6  = 'Stereo/Radios'
#         elif  ewaste_item_6 == '10':
#             ewaste_item_6 = 'Speakers'
#         elif  ewaste_item_6  == '11':
#             ewaste_item_6 = 'Telephone'
#         elif  ewaste_item_6 == '12':
#             ewaste_item_6  = 'TV (Any Size)'
#         elif  ewaste_item_6 == '13':
#              ewaste_item_6 = 'VCR/DVD Player'
#         elif  ewaste_item_6  == '13':
#              ewaste_item_6 = 'Child Day Bed'
#         elif  ewaste_item_6 == '14':
#             ewaste_item_6 = 'Video/Film Cameras'
#         elif  ewaste_item_6 == '15':
#             ewaste_item_6  = 'Video/Games Components'
#         elif  ewaste_item_6 == '16':
#              ewaste_item_6 = 'Cell Phone'
#         elif ewaste_item_6 ==  '17':
#             ewaste_item_6 = "Vacuum Cleaner"
#
#
#         l311 = []
#         if  ewaste_item_7  == '1':
#             ewaste_item_7 = 'Copier/Scanner'
#         elif  ewaste_item_7 =='2':
#              ewaste_item_7 = 'Electronic Equipment'
#         elif  ewaste_item_7 == '3':
#              ewaste_item_7 = 'Laptops/Tablets'
#         elif ewaste_item_7  == "4":
#             ewaste_item_7 = 'Microwaves'
#         elif  ewaste_item_7== '5':
#              ewaste_item_7  = 'Monitors'
#         elif  ewaste_item_7  == '6':
#              ewaste_item_7  = 'Other Ewaste'
#         elif  ewaste_item_7  == '7':
#             ewaste_item_7  = 'Computers'
#         elif  ewaste_item_7  == '8':
#             ewaste_item_7 = 'Printer/Fax Machine'
#         elif  ewaste_item_7 == '9':
#             ewaste_item_7  = 'Stereo/Radios'
#         elif  ewaste_item_7 == '10':
#             ewaste_item_7 = 'Speakers'
#         elif  ewaste_item_7  == '11':
#             ewaste_item_7 = 'Telephone'
#         elif  ewaste_item_7 == '12':
#             ewaste_item_7  = 'TV (Any Size)'
#         elif  ewaste_item_7 == '13':
#              ewaste_item_7 = 'VCR/DVD Player'
#         elif  ewaste_item_7  == '13':
#              ewaste_item_7 = 'Child Day Bed'
#         elif  ewaste_item_7 == '14':
#             ewaste_item_7 = 'Video/Film Cameras'
#         elif  ewaste_item_7 == '15':
#             ewaste_item_7  = 'Video/Games Components'
#         elif  ewaste_item_7 == '16':
#              ewaste_item_7 = 'Cell Phone'
#         elif ewaste_item_7 ==  '17':
#             ewaste_item_7 = "Vacuum Cleaner"
#
#
#
#         l311 = []
#         if  ewaste_item_7  == '1':
#             ewaste_item_7 = 'Copier/Scanner'
#         elif  ewaste_item_7 =='2':
#              ewaste_item_7 = 'Electronic Equipment'
#         elif  ewaste_item_7 == '3':
#              ewaste_item_7 = 'Laptops/Tablets'
#         elif ewaste_item_7  == "4":
#             ewaste_item_7 = 'Microwaves'
#         elif  ewaste_item_7== '5':
#              ewaste_item_7  = 'Monitors'
#         elif  ewaste_item_7  == '6':
#              ewaste_item_7  = 'Other Ewaste'
#         elif  ewaste_item_7  == '7':
#             ewaste_item_7  = 'Computers'
#         elif  ewaste_item_7  == '8':
#             ewaste_item_7 = 'Printer/Fax Machine'
#         elif  ewaste_item_7 == '9':
#             ewaste_item_7  = 'Stereo/Radios'
#         elif  ewaste_item_7 == '10':
#             ewaste_item_7 = 'Speakers'
#         elif  ewaste_item_7  == '11':
#             ewaste_item_7 = 'Telephone'
#         elif  ewaste_item_7 == '12':
#             ewaste_item_7  = 'TV (Any Size)'
#         elif  ewaste_item_7 == '13':
#              ewaste_item_7 = 'VCR/DVD Player'
#         elif  ewaste_item_7  == '13':
#              ewaste_item_7 = 'Child Day Bed'
#         elif  ewaste_item_7 == '14':
#             ewaste_item_7 = 'Video/Film Cameras'
#         elif  ewaste_item_7 == '15':
#             ewaste_item_7  = 'Video/Games Components'
#         elif  ewaste_item_7 == '16':
#              ewaste_item_7 = 'Cell Phone'
#         elif ewaste_item_7 ==  '17':
#             ewaste_item_7 = "Vacuum Cleaner"
#
#
#
#         l311 = []
#         if  ewaste_item_9  == '1':
#             ewaste_item_9 = 'Copier/Scanner'
#         elif  ewaste_item_9 =='2':
#              ewaste_item_9 = 'Electronic Equipment'
#         elif  ewaste_item_9 == '3':
#              ewaste_item_9 = 'Laptops/Tablets'
#         elif ewaste_item_9  == "4":
#             ewaste_item_9 = 'Microwaves'
#         elif  ewaste_item_9== '5':
#              ewaste_item_9  = 'Monitors'
#         elif  ewaste_item_9  == '6':
#              ewaste_item_9  = 'Other Ewaste'
#         elif  ewaste_item_9  == '7':
#             ewaste_item_9  = 'Computers'
#         elif  ewaste_item_9  == '8':
#             ewaste_item_9 = 'Printer/Fax Machine'
#         elif  ewaste_item_9 == '9':
#             ewaste_item_9  = 'Stereo/Radios'
#         elif  ewaste_item_9 == '10':
#             ewaste_item_9 = 'Speakers'
#         elif  ewaste_item_9  == '11':
#             ewaste_item_9 = 'Telephone'
#         elif  ewaste_item_9 == '12':
#             ewaste_item_9  = 'TV (Any Size)'
#         elif  ewaste_item_9 == '13':
#              ewaste_item_9 = 'VCR/DVD Player'
#         elif  ewaste_item_9  == '13':
#              ewaste_item_9 = 'Child Day Bed'
#         elif  ewaste_item_9 == '14':
#             ewaste_item_9 = 'Video/Film Cameras'
#         elif  ewaste_item_9 == '15':
#             ewaste_item_9  = 'Video/Games Components'
#         elif  ewaste_item_9 == '16':
#              ewaste_item_9 = 'Cell Phone'
#         elif ewaste_item_9 ==  '17':
#             ewaste_item_9 = "Vacuum Cleaner"
#
#         l311 = []
#         if  ewaste_item_10  == '1':
#             ewaste_item_10 = 'Copier/Scanner'
#         elif  ewaste_item_10 =='2':
#              ewaste_item_10 = 'Electronic Equipment'
#         elif  ewaste_item_10 == '3':
#              ewaste_item_10 = 'Laptops/Tablets'
#         elif ewaste_item_10  == "4":
#             ewaste_item_10 = 'Microwaves'
#         elif  ewaste_item_10== '5':
#              ewaste_item_10  = 'Monitors'
#         elif  ewaste_item_10  == '6':
#              ewaste_item_10  = 'Other Ewaste'
#         elif  ewaste_item_10  == '7':
#             ewaste_item_10  = 'Computers'
#         elif  ewaste_item_10  == '8':
#             ewaste_item_10 = 'Printer/Fax Machine'
#         elif  ewaste_item_10 == '9':
#             ewaste_item_10  = 'Stereo/Radios'
#         elif  ewaste_item_10 == '10':
#             ewaste_item_10 = 'Speakers'
#         elif  ewaste_item_10  == '11':
#             ewaste_item_10 = 'Telephone'
#         elif  ewaste_item_10 == '12':
#             ewaste_item_10  = 'TV (Any Size)'
#         elif  ewaste_item_10 == '13':
#              ewaste_item_10 = 'VCR/DVD Player'
#         elif  ewaste_item_10  == '13':
#              ewaste_item_10 = 'Child Day Bed'
#         elif  ewaste_item_10 == '14':
#             ewaste_item_10 = 'Video/Film Cameras'
#         elif  ewaste_item_10 == '15':
#             ewaste_item_10  = 'Video/Games Components'
#         elif  ewaste_item_10 == '16':
#              ewaste_item_10 = 'Cell Phone'
#         elif ewaste_item_10 ==  '17':
#             ewaste_item_10 = "Vacuum Cleaner"
#
#         if last_edited_user == "SA":
#             last_edited_user = "Sanstar Proxy"
#
#         if last_edited_user == "Manuel P Rodriguez":
#             last_edited_user = "Manuel Rodriguez"
#
#         firstName, lastName = last_edited_user.split()
#
#         print firstName
#         print lastName
#
#
#
#         dL311 = dict()
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName)
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("ElectronicWestType", ewaste_item_1)
#         d.setdefault("Type", "Electronic Waste")
#         d.setdefault("Name", ewaste_uid_1 )
#         d.setdefault("ItemCount", ewaste_qyt_1)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         dL311 = dict()
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("ElectronicWestType", ewaste_item_2)
#         d.setdefault("Type", "Electronic Waste")
#         d.setdefault("Name", ewaste_uid_2)
#         d.setdefault("ItemCount", ewaste_qyt_2)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("ElectronicWestType", ewaste_item_3)
#         d.setdefault("Type", "Electronic Waste")
#         d.setdefault("Name", ewaste_uid_3)
#         d.setdefault("ItemCount", ewaste_qyt_3)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("ElectronicWestType", ewaste_item_4)
#         d.setdefault("Type", "Electronic Waste")
#         d.setdefault("Name", ewaste_uid_4)
#         d.setdefault("ItemCount", ewaste_qyt_4)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("ElectronicWestType", ewaste_item_5)
#         d.setdefault("Type", "Electronic Waste")
#         d.setdefault("Name", ewaste_uid_5)
#         d.setdefault("ItemCount", ewaste_qyt_5)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("ElectronicWestType", ewaste_item_6)
#         d.setdefault("Type", "Electronic Waste")
#         d.setdefault("Name", ewaste_uid_6)
#         d.setdefault("ItemCount", ewaste_qyt_6)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#
#
#
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("ElectronicWestType", ewaste_item_7)
#         d.setdefault("Type", "Electronic Waste")
#         d.setdefault("Name", ewaste_uid_7)
#         d.setdefault("ItemCount", ewaste_qyt_7)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("ElectronicWestType", ewaste_item_8)
#         d.setdefault("Type", "Electronic Waste")
#         d.setdefault("Name", ewaste_uid_8)
#         d.setdefault("ItemCount", ewaste_qyt_8)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",last_edited_user)
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("ElectronicWestType", ewaste_item_9)
#         d.setdefault("Type", "Electronic Waste")
#         d.setdefault("Name", ewaste_uid_9)
#         d.setdefault("ItemCount", ewaste_qyt_9)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",last_edited_user)
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("ElectronicWestType", ewaste_item_10)
#         d.setdefault("Type", "Electronic Waste")
#         d.setdefault("Name", ewaste_uid_10)
#         d.setdefault("ItemCount", ewaste_qyt_10)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#
#         lIndexes = []
#         nCnt = len(l311)
#         for i in range(nCnt):
#             d = l311[i]
#             if(d['Name'].strip() == '') or (d['Name'].strip() == "None"):
#                 del d['Name']
#
#             if(d['ElectronicWestType'] == "None"):
#                 lIndexes.append(i)
#
#         if(len(lIndexes)>0):
#             for i in reversed(lIndexes):
#                 del l311[i]
#
#         if(len(l311)>0):
#                 dL311.setdefault("La311ElectronicWaste", l311)
#                 dResult.setdefault("ListOfLa311ElectronicWaste",dL311)
#                 lResults.append({"MetaData": {}, "SRData": dResult})
#                 sReq = json.dumps(dResult,sort_keys=True, indent=2)
#                 results = {"MetaData": {}, "SRData": dResult}
#                 print lFields[0]
#                 # print results
#                 sReqj = json.dumps(results,sort_keys=True, indent=2)
#
#                 # start = time.time()
#                 # url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSRWithCodes"
#                 # headers = {'Content-type': 'text/plain', 'Accept': '/'}
#                 # r = requests.post(url, data= json.dumps(results), headers=headers,  verify=False)
#                 # # print results
#                 # print r.text
#                 # print 'It took', time.time()-start, 'seconds.'
#
#                 ii = ii + 1
#                 # print (str(ii) + " recs sent to server.",  'It took', time.time()-start, 'seconds.')
#
#
#                 # ii = ii + 1
#                 # print (str(ii) + " recs sent to server.",  'It took', time.time()-start, 'seconds.')
#
#     print("Finished")
# except Exception,e:
#     exc_type, exc_obj, exc_tb = sys.exc_info()
#     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#     print(exc_type, fname, exc_tb.tb_lineno)
#


pyFC = "sc_bkup_mha_D"
clauseSBE = "WHERE RESOLUTION_CODE <> '' AND Category LIKE '%6%' OR Category LIKE '%7%'OR Category LIKE '%20%'   "
if(__name__=='__main__'):
    # sMsg = printObjects()
    # print(sMsg)

    connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
    # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
    conn = pyodbc.connect(connstr)
    cursor = conn.cursor()
    FN_SRNumber = "SRNumber"
    lFields = [FN_SRNumber, "RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user", "last_edited_date"]
    #lFields = ["SRNumber"]
    sFields = ""
    for fld in lFields:
        if(sFields==""):
            sFields = fld
        else:
            sFields = sFields + "," + fld
    #List of the fields you'd like to exclude, like ItemCount for example.
    lFieldsExcluded = ["RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user", "last_edited_date"]

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
    mha_item_1 = ""
    mha_item_2 = ""
    mha_item_3 = ""
    mha_item_4 = ""
    mha_item_5 = ""
    mha_item_6 = ""
    mha_item_7 = ""
    mha_item_8 = ""
    mha_item_9 = ""
    mha_item_10 = ""
    mha_qyt_1 = " "
    mha_qyt_2 = " "
    mha_qyt_3 = " "
    mha_qyt_4 = " "
    mha_qyt_5 = " "
    mha_qyt_6 = " "
    mha_qyt_7 = " "
    mha_qyt_8 = " "
    mha_qyt_9 = " "
    mha_qyt_10 = " "
    mha_uid_1 = ""
    mha_uid_2 = " "
    mha_uid_3 = ""
    mha_uid_4 = ""
    mha_uid_5 = ""
    mha_uid_6 = ""
    mha_uid_7 = ""
    mha_uid_8 = ""
    mha_uid_9 = ""
    mha_uid_10 = ""
    rescode = ""
    reasoncode = " "
    mha_uid = ""


    for row in cursor.fetchall():
        lResults = []    #make sure lResults are initiated here
        lValues = []
        for i in range(len(columns)):
            lValues.append( str(row[i]))
        mha_item_1 = (str(row[lFields.index("ITEM_1")]))
        mha_item_2 = (str(row[lFields.index("ITEM_2")]))
        mha_item_3 = (str(row[lFields.index("ITEM_3")]))
        mha_item_4 = (str(row[lFields.index("ITEM_4")]))
        mha_item_5 = (str(row[lFields.index("ITEM_5")]))
        mha_item_6= (str(row[lFields.index("ITEM_6")]))
        mha_item_7 =(str(row[lFields.index("ITEM_7")]))
        mha_item_8 = (str(row[lFields.index("ITEM_8")]))
        mha_item_9 =(str(row[lFields.index("ITEM_9")]))
        mha_item_10 = (str(row[lFields.index("ITEM_10")]))
        mha_qyt_1 = (str(row[lFields.index("QYT_1")]))
        mha_qyt_2 = (str(row[lFields.index("QYT_2")]))
        mha_qyt_3 = (str(row[lFields.index("QYT_3")]))
        mha_qyt_4 = (str(row[lFields.index("QYT_4")]))
        mha_qyt_5 = (str(row[lFields.index("QYT_5")]))
        mha_qyt_6 = (str(row[lFields.index("QTY_6")]))
        mha_qyt_7 = (str(row[lFields.index("QTY_7")]))
        mha_qyt_8 = (str(row[lFields.index("QTY_8")]))
        mha_qyt_9 = (str(row[lFields.index("QTY_9")]))
        mha_qyt_10 = (str(row[lFields.index("QTY_10")]))



        mha_uid_1 = (str(row[lFields.index("UID1")]))
        mha_uid_2 = (str(row[lFields.index("UID2")]))
        mha_uid_3 = (str(row[lFields.index("UID3")]))
        mha_uid_4 = (str(row[lFields.index("UID4")]))
        mha_uid_5 = (str(row[lFields.index("UID5")]))
        mha_uid_6 = (str(row[lFields.index("UID6")]))
        mha_uid_7 = (str(row[lFields.index("UID7")]))
        mha_uid_8 = (str(row[lFields.index("UID8")]))
        mha_uid_9 = (str(row[lFields.index("UID9")]))
        mha_uid_10 = (str(row[lFields.index("UID10")]))


        rescode = (str(row[lFields.index("RESOLUTION_CODE")]))

        last_edited_user = (str(row[lFields.index("last_edited_user")]))

        #dResult = dict(zip(columns, row))
        dResult = dict(zip(columns, lValues))

        # Adding additional items  ******************************
        dResult.setdefault("ReasonCode", rescode if rescode.isdigit() else "")
        dResult.setdefault("ResolutionCode",rescode if not rescode.isdigit() else "")
        dResult.setdefault("UpdatedByUserLogin", "SANSTAR1")
        # dResult.setdefault("ListOfLa311DeadAnimalRemoval", dict())
        l311 = []
        if  mha_item_1  == '1':
            mha_item_1 = 'Air Conditioner'
        elif  mha_item_1 =='2':
             mha_item_1 = 'BBQ'
        elif  mha_item_1 == '3':
             mha_item_1 = 'Bed Frame (Metal)'
        elif mha_item_1  == "4":
            mha_item_1 = 'Bicycle Parts'
        elif  mha_item_1== '5':
             mha_item_1  = 'Bird Cage (Metal)'
        elif  mha_item_1  == '6':
             mha_item_1  = 'Cooler'
        elif  mha_item_1  == '7':
            mha_item_1  = 'Dishwasher'
        elif  mha_item_1  == '8':
            mha_item_1 = 'Dryer'
        elif  mha_item_1 == '9':
            mha_item_1  = 'Fence (Metal)'
        elif  mha_item_1 == '10':
            mha_item_1 = 'File Cabinet (Metal)'
        elif  mha_item_1  == '11':
            mha_item_1 = 'Freezer'
        elif  mha_item_1 == '12':
            mha_item_1  = 'Heater'
        elif  mha_item_1 == '13':
             mha_item_1 = 'Iron Tub'
        elif  mha_item_1 == '14':
            mha_item_1 = 'Metal Cabinet'
        elif  mha_item_1 == '15':
            mha_item_1  = 'Other'
        elif  mha_item_1 == '16':
             mha_item_1 = 'Ovens'
        elif mha_item_1 ==  '17':
            mha_item_1 = "Pipes (Metal)"
        elif mha_item_1 ==  '24':
            mha_item_1 = "Water Heater"
        elif mha_item_1 ==  '23':
            mha_item_1 = "Washing Machine"
        elif mha_item_1 ==  '22':
            mha_item_1 = "Trash Compactor"
        elif mha_item_1 ==  '21':
            mha_item_1 = "Swamp Cooler"
        elif mha_item_1 ==  '20':
            mha_item_1 = "Stove"
        elif mha_item_1 ==  '19':
            mha_item_1 = "Scrap Metal"
        elif mha_item_1 ==  '25':
            mha_item_1 = "Refrigerator"

        elif mha_item_1 ==  '18':
            mha_item_1 ='Pool Heater/Pump/Filter (metal) '
        elif mha_item_1 ==  '33':
            mha_item_1 ='Window Frame (Metal)'
        elif mha_item_1 ==  '32':
            mha_item_1 ='Tub (Metal)'
        elif mha_item_1 ==  '31':
            mha_item_1 ='Shelf (Metal)'
        elif mha_item_1 ==  '31':
            mha_item_1 ='Shelf (Metal)'
        elif mha_item_1 ==  '30':
            mha_item_1 ='Rain Gutter (Metal)'
        elif mha_item_1 ==  '28':
            mha_item_1 ='Headboard (Metal)'
        elif mha_item_1 ==  '27':
            mha_item_1 ='Garage Door (Metal)'
        elif mha_item_1 ==  '26':
            mha_item_1 ='Desk (Metal)'





        l311 = []
        if  mha_item_2 == '1':
            mha_item_2= 'Air Conditioner'
        elif  mha_item_2=='2':
             mha_item_2= 'BBQ'
        elif  mha_item_2== '3':
             mha_item_2= 'Bed Frame (Metal)'
        elif mha_item_2 == "4":
            mha_item_2= 'Bicycle Parts'
        elif  mha_item_1== '5':
             mha_item_2 = 'Bird Cage (Metal)'
        elif  mha_item_2 == '6':
             mha_item_2 = 'Cooler'
        elif  mha_item_2 == '7':
            mha_item_2 = 'Dishwasher'
        elif  mha_item_2 == '8':
            mha_item_2= 'Dryer'
        elif  mha_item_2== '9':
            mha_item_2 = 'Fence (Metal)'
        elif  mha_item_2== '10':
            mha_item_2= 'File Cabinet (Metal)'
        elif  mha_item_2 == '11':
            mha_item_2= 'Freezer'
        elif  mha_item_2== '12':
            mha_item_2 = 'Heater'
        elif  mha_item_2== '13':
             mha_item_2= 'Iron Tub'
        elif  mha_item_2== '14':
            mha_item_2= 'Metal Cabinet'
        elif  mha_item_2== '15':
            mha_item_2 = 'Other'
        elif  mha_item_2== '16':
             mha_item_2= 'Ovens'
        elif mha_item_2==  '17':
            mha_item_2= "Pipes (Metal)"
        elif mha_item_2==  '24':
            mha_item_2= "Water Heater"
        elif mha_item_2==  '23':
            mha_item_2= "Washing Machine"
        elif mha_item_2==  '22':
            mha_item_2= "Trash Compactor"
        elif mha_item_2==  '21':
            mha_item_2= "Swamp Cooler"
        elif mha_item_2==  '20':
            mha_item_2= "Stove"
        elif mha_item_2==  '19':
            mha_item_2= "Scrap Metal"
        elif mha_item_2==  '25':
            mha_item_2= "Refrigerator"



        l311 = []
        if  mha_item_3 == '1':
            mha_item_3= 'Air Conditioner'
        elif  mha_item_3=='2':
             mha_item_3= 'BBQ'
        elif  mha_item_3== '3':
             mha_item_3= 'Bed Frame (Metal)'
        elif mha_item_3 == "4":
            mha_item_3= 'Bicycle Parts'
        elif  mha_item_1== '5':
             mha_item_3 = 'Bird Cage (Metal)'
        elif  mha_item_3 == '6':
             mha_item_3 = 'Cooler'
        elif  mha_item_3 == '7':
            mha_item_3 = 'Dishwasher'
        elif  mha_item_3 == '8':
            mha_item_3= 'Dryer'
        elif  mha_item_3== '9':
            mha_item_3 = 'Fence (Metal)'
        elif  mha_item_3== '10':
            mha_item_3= 'File Cabinet (Metal)'
        elif  mha_item_3 == '11':
            mha_item_3= 'Freezer'
        elif  mha_item_3== '12':
            mha_item_3 = 'Heater'
        elif  mha_item_3== '13':
             mha_item_3= 'Iron Tub'
        elif  mha_item_3== '14':
            mha_item_3= 'Metal Cabinet'
        elif  mha_item_3== '15':
            mha_item_3 = 'Other'
        elif  mha_item_3== '16':
             mha_item_3= 'Ovens'
        elif mha_item_3==  '17':
            mha_item_3= "Pipes (Metal)"
        elif mha_item_3==  '24':
            mha_item_3= "Water Heater"
        elif mha_item_3==  '23':
            mha_item_3= "Washing Machine"
        elif mha_item_3==  '22':
            mha_item_3= "Trash Compactor"
        elif mha_item_3==  '21':
            mha_item_3= "Swamp Cooler"
        elif mha_item_3==  '20':
            mha_item_3= "Stove"
        elif mha_item_3==  '19':
            mha_item_3= "Scrap Metal"
        elif mha_item_3==  '25':
            mha_item_3= "Refrigerator"




        l311 = []
        if  mha_item_4 == '1':
            mha_item_4= 'Air Conditioner'
        elif  mha_item_4=='2':
             mha_item_4= 'BBQ'
        elif  mha_item_4== '3':
             mha_item_4= 'Bed Frame (Metal)'
        elif mha_item_4 == "4":
            mha_item_4= 'Bicycle Parts'
        elif  mha_item_1== '5':
             mha_item_4 = 'Bird Cage (Metal)'
        elif  mha_item_4 == '6':
             mha_item_4 = 'Cooler'
        elif  mha_item_4 == '7':
            mha_item_4 = 'Dishwasher'
        elif  mha_item_4 == '8':
            mha_item_4= 'Dryer'
        elif  mha_item_4== '9':
            mha_item_4 = 'Fence (Metal)'
        elif  mha_item_4== '10':
            mha_item_4= 'File Cabinet (Metal)'
        elif  mha_item_4 == '11':
            mha_item_4= 'Freezer'
        elif  mha_item_4== '12':
            mha_item_4 = 'Heater'
        elif  mha_item_4== '13':
             mha_item_4= 'Iron Tub'
        elif  mha_item_4== '14':
            mha_item_4= 'Metal Cabinet'
        elif  mha_item_4== '15':
            mha_item_4 = 'Other'
        elif  mha_item_4== '16':
             mha_item_4= 'Ovens'
        elif mha_item_4==  '17':
            mha_item_4= "Pipes (Metal)"
        elif mha_item_4==  '24':
            mha_item_4= "Water Heater"
        elif mha_item_4==  '23':
            mha_item_4= "Washing Machine"
        elif mha_item_4==  '22':
            mha_item_4= "Trash Compactor"
        elif mha_item_4==  '21':
            mha_item_4= "Swamp Cooler"
        elif mha_item_4==  '20':
            mha_item_4= "Stove"
        elif mha_item_4==  '19':
            mha_item_4= "Scrap Metal"
        elif mha_item_4==  '25':
            mha_item_4= "Refrigerator"







        l311 = []
        if  mha_item_5 == '1':
            mha_item_5= 'Air Conditioner'
        elif  mha_item_5=='2':
             mha_item_5= 'BBQ'
        elif  mha_item_5== '3':
             mha_item_5= 'Bed Frame (Metal)'
        elif mha_item_5 == "4":
            mha_item_5= 'Bicycle Parts'
        elif  mha_item_1== '5':
             mha_item_5 = 'Bird Cage (Metal)'
        elif  mha_item_5 == '6':
             mha_item_5 = 'Cooler'
        elif  mha_item_5 == '7':
            mha_item_5 = 'Dishwasher'
        elif  mha_item_5 == '8':
            mha_item_5= 'Dryer'
        elif  mha_item_5== '9':
            mha_item_5 = 'Fence (Metal)'
        elif  mha_item_5== '10':
            mha_item_5= 'File Cabinet (Metal)'
        elif  mha_item_5 == '11':
            mha_item_5= 'Freezer'
        elif  mha_item_5== '12':
            mha_item_5 = 'Heater'
        elif  mha_item_5== '13':
             mha_item_5= 'Iron Tub'
        elif  mha_item_5== '14':
            mha_item_5= 'Metal Cabinet'
        elif  mha_item_5== '15':
            mha_item_5 = 'Other'
        elif  mha_item_5== '16':
             mha_item_5= 'Ovens'
        elif mha_item_5==  '17':
            mha_item_5= "Pipes (Metal)"
        elif mha_item_5==  '24':
            mha_item_5= "Water Heater"
        elif mha_item_5==  '23':
            mha_item_5= "Washing Machine"
        elif mha_item_5==  '22':
            mha_item_5= "Trash Compactor"
        elif mha_item_5==  '21':
            mha_item_5= "Swamp Cooler"
        elif mha_item_5==  '20':
            mha_item_5= "Stove"
        elif mha_item_5==  '19':
            mha_item_5= "Scrap Metal"
        elif mha_item_5==  '25':
            mha_item_5= "Refrigerator"



        l311 = []
        if  mha_item_6 == '1':
            mha_item_6= 'Air Conditioner'
        elif  mha_item_6=='2':
             mha_item_6= 'BBQ'
        elif  mha_item_6== '3':
             mha_item_6= 'Bed Frame (Metal)'
        elif mha_item_6 == "4":
            mha_item_6= 'Bicycle Parts'
        elif  mha_item_1== '5':
             mha_item_6 = 'Bird Cage (Metal)'
        elif  mha_item_6 == '6':
             mha_item_6 = 'Cooler'
        elif  mha_item_6 == '7':
            mha_item_6 = 'Dishwasher'
        elif  mha_item_6 == '8':
            mha_item_6= 'Dryer'
        elif  mha_item_6== '9':
            mha_item_6 = 'Fence (Metal)'
        elif  mha_item_6== '10':
            mha_item_6= 'File Cabinet (Metal)'
        elif  mha_item_6 == '11':
            mha_item_6= 'Freezer'
        elif  mha_item_6== '12':
            mha_item_6 = 'Heater'
        elif  mha_item_6== '13':
             mha_item_6= 'Iron Tub'
        elif  mha_item_6== '14':
            mha_item_6= 'Metal Cabinet'
        elif  mha_item_6== '15':
            mha_item_6 = 'Other'
        elif  mha_item_6== '16':
             mha_item_6= 'Ovens'
        elif mha_item_6==  '17':
            mha_item_6= "Pipes (Metal)"
        elif mha_item_6==  '24':
            mha_item_6= "Water Heater"
        elif mha_item_6==  '23':
            mha_item_6= "Washing Machine"
        elif mha_item_6==  '22':
            mha_item_6= "Trash Compactor"
        elif mha_item_6==  '21':
            mha_item_6= "Swamp Cooler"
        elif mha_item_6==  '20':
            mha_item_6= "Stove"
        elif mha_item_6==  '19':
            mha_item_6= "Scrap Metal"
        elif mha_item_6==  '25':
            mha_item_6= "Refrigerator"







        l311 = []
        if  mha_item_7 == '1':
            mha_item_7= 'Air Conditioner'
        elif  mha_item_7=='2':
             mha_item_7= 'BBQ'
        elif  mha_item_7== '3':
             mha_item_7= 'Bed Frame (Metal)'
        elif mha_item_7 == "4":
            mha_item_7= 'Bicycle Parts'
        elif  mha_item_1== '5':
             mha_item_7 = 'Bird Cage (Metal)'
        elif  mha_item_7 == '6':
             mha_item_7 = 'Cooler'
        elif  mha_item_7 == '7':
            mha_item_7 = 'Dishwasher'
        elif  mha_item_7 == '8':
            mha_item_7= 'Dryer'
        elif  mha_item_7== '9':
            mha_item_7 = 'Fence (Metal)'
        elif  mha_item_7== '10':
            mha_item_7= 'File Cabinet (Metal)'
        elif  mha_item_7 == '11':
            mha_item_7= 'Freezer'
        elif  mha_item_7== '12':
            mha_item_7 = 'Heater'
        elif  mha_item_7== '13':
             mha_item_7= 'Iron Tub'
        elif  mha_item_7== '14':
            mha_item_7= 'Metal Cabinet'
        elif  mha_item_7== '15':
            mha_item_7 = 'Other'
        elif  mha_item_7== '16':
             mha_item_7= 'Ovens'
        elif mha_item_7==  '17':
            mha_item_7= "Pipes (Metal)"
        elif mha_item_7==  '24':
            mha_item_7= "Water Heater"
        elif mha_item_7==  '23':
            mha_item_7= "Washing Machine"
        elif mha_item_7==  '22':
            mha_item_7= "Trash Compactor"
        elif mha_item_7==  '21':
            mha_item_7= "Swamp Cooler"
        elif mha_item_7==  '20':
            mha_item_7= "Stove"
        elif mha_item_7==  '19':
            mha_item_7= "Scrap Metal"
        elif mha_item_7==  '25':
            mha_item_7= "Refrigerator"



        l311 = []
        if  mha_item_8 == '1':
            mha_item_8= 'Air Conditioner'
        elif  mha_item_8=='2':
             mha_item_8= 'BBQ'
        elif  mha_item_8== '3':
             mha_item_8= 'Bed Frame (Metal)'
        elif mha_item_8 == "4":
            mha_item_8= 'Bicycle Parts'
        elif  mha_item_1== '5':
             mha_item_8 = 'Bird Cage (Metal)'
        elif  mha_item_8 == '6':
             mha_item_8 = 'Cooler'
        elif  mha_item_8 == '7':
            mha_item_8 = 'Dishwasher'
        elif  mha_item_8 == '8':
            mha_item_8= 'Dryer'
        elif  mha_item_8== '9':
            mha_item_8 = 'Fence (Metal)'
        elif  mha_item_8== '10':
            mha_item_8= 'File Cabinet (Metal)'
        elif  mha_item_8 == '11':
            mha_item_8= 'Freezer'
        elif  mha_item_8== '12':
            mha_item_8 = 'Heater'
        elif  mha_item_8== '13':
             mha_item_8= 'Iron Tub'
        elif  mha_item_8== '14':
            mha_item_8= 'Metal Cabinet'
        elif  mha_item_8== '15':
            mha_item_8 = 'Other'
        elif  mha_item_8== '16':
             mha_item_8= 'Ovens'
        elif mha_item_8==  '17':
            mha_item_8= "Pipes (Metal)"
        elif mha_item_8==  '24':
            mha_item_8= "Water Heater"
        elif mha_item_8==  '23':
            mha_item_8= "Washing Machine"
        elif mha_item_8==  '22':
            mha_item_8= "Trash Compactor"
        elif mha_item_8==  '21':
            mha_item_8= "Swamp Cooler"
        elif mha_item_8==  '20':
            mha_item_8= "Stove"
        elif mha_item_8==  '19':
            mha_item_8= "Scrap Metal"
        elif mha_item_8==  '25':
            mha_item_8= "Refrigerator"


        l311 = []
        if  mha_item_9 == '1':
            mha_item_9= 'Air Conditioner'
        elif  mha_item_9=='2':
             mha_item_9= 'BBQ'
        elif  mha_item_9== '3':
             mha_item_9= 'Bed Frame (Metal)'
        elif mha_item_9 == "4":
            mha_item_9= 'Bicycle Parts'
        elif  mha_item_1== '5':
             mha_item_9 = 'Bird Cage (Metal)'
        elif  mha_item_9 == '6':
             mha_item_9 = 'Cooler'
        elif  mha_item_9 == '7':
            mha_item_9 = 'Dishwasher'
        elif  mha_item_9 == '8':
            mha_item_9= 'Dryer'
        elif  mha_item_9== '9':
            mha_item_9 = 'Fence (Metal)'
        elif  mha_item_9== '10':
            mha_item_9= 'File Cabinet (Metal)'
        elif  mha_item_9 == '11':
            mha_item_9= 'Freezer'
        elif  mha_item_9== '12':
            mha_item_9 = 'Heater'
        elif  mha_item_9== '13':
             mha_item_9= 'Iron Tub'
        elif  mha_item_9== '14':
            mha_item_9= 'Metal Cabinet'
        elif  mha_item_9== '15':
            mha_item_9 = 'Other'
        elif  mha_item_9== '16':
             mha_item_9= 'Ovens'
        elif mha_item_9==  '17':
            mha_item_9= "Pipes (Metal)"
        elif mha_item_9==  '24':
            mha_item_9= "Water Heater"
        elif mha_item_9==  '23':
            mha_item_9= "Washing Machine"
        elif mha_item_9==  '22':
            mha_item_9= "Trash Compactor"
        elif mha_item_9==  '21':
            mha_item_9= "Swamp Cooler"
        elif mha_item_9==  '20':
            mha_item_9= "Stove"
        elif mha_item_9==  '19':
            mha_item_9= "Scrap Metal"
        elif mha_item_9==  '25':
            mha_item_9= "Refrigerator"

        l311 = []
        if  mha_item_10 == '1':
            mha_item_10= 'Air Conditioner'
        elif  mha_item_10=='2':
             mha_item_10= 'BBQ'
        elif  mha_item_10== '3':
             mha_item_10= 'Bed Frame (Metal)'
        elif mha_item_10 == "4":
            mha_item_10= 'Bicycle Parts'
        elif  mha_item_1== '5':
             mha_item_10 = 'Bird Cage (Metal)'
        elif  mha_item_10 == '6':
             mha_item_10 = 'Cooler'
        elif  mha_item_10 == '7':
            mha_item_10 = 'Dishwasher'
        elif  mha_item_10 == '8':
            mha_item_10= 'Dryer'
        elif  mha_item_10== '9':
            mha_item_10 = 'Fence (Metal)'
        elif  mha_item_10== '10':
            mha_item_10= 'File Cabinet (Metal)'
        elif  mha_item_10 == '11':
            mha_item_10= 'Freezer'
        elif  mha_item_10== '12':
            mha_item_10 = 'Heater'
        elif  mha_item_10== '13':
             mha_item_10= 'Iron Tub'
        elif  mha_item_10== '14':
            mha_item_10= 'Metal Cabinet'
        elif  mha_item_10== '15':
            mha_item_10 = 'Other'
        elif  mha_item_10== '16':
             mha_item_10= 'Ovens'
        elif mha_item_10==  '17':
            mha_item_10= "Pipes (Metal)"
        elif mha_item_10==  '24':
            mha_item_10= "Water Heater"
        elif mha_item_10==  '23':
            mha_item_10= "Washing Machine"
        elif mha_item_10==  '22':
            mha_item_10= "Trash Compactor"
        elif mha_item_10==  '21':
            mha_item_10= "Swamp Cooler"
        elif mha_item_10==  '20':
            mha_item_10= "Stove"
        elif mha_item_10==  '19':
            mha_item_10= "Scrap Metal"
        elif mha_item_10==  '25':
            mha_item_10= "Refrigerator"


        if last_edited_user == "SA":
            last_edited_user = "Sanstar Proxy"

        if last_edited_user == "Manuel P Rodriguez":
            last_edited_user = "Manuel Rodriguez"

        print last_edited_user



        firstName, lastName = last_edited_user.split()

        print firstName
        print lastName

        dL311 = dict()
        l311 = []
        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("HouseholdItem", mha_item_1)
        d.setdefault("Type", "Metal/Household Appliances")
        d.setdefault("Name", mha_uid_1 )
        d.setdefault("HouseHoldItemCount", mha_qyt_1)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)

        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("HouseholdItem", mha_item_2)
        d.setdefault("Type", "Metal/Household Appliances")
        d.setdefault("Name", mha_uid_2)
        d.setdefault("HouseHoldItemCount", mha_qyt_2)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")

        l311.append(d)

        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("HouseholdItem", mha_item_3)
        d.setdefault("Type", "Metal/Household Appliances")
        d.setdefault("Name", mha_uid_3)
        d.setdefault("HouseHoldItemCount", mha_qyt_3)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)

        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("HouseholdItem", mha_item_4)
        d.setdefault("Type", "Metal/Household Appliances")
        d.setdefault("Name", mha_uid_4)
        d.setdefault("HouseHoldItemCount", mha_qyt_4)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)
        d = dict()

        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("HouseholdItem", mha_item_5)
        d.setdefault("Type", "Metal/Household Appliances")
        d.setdefault("Name", mha_uid_5)
        d.setdefault("HouseHoldItemCount", mha_qyt_5)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")





        l311.append(d)

        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("HouseholdItem", mha_item_6)
        d.setdefault("Type", "Metal/Household Appliances")
        d.setdefault("Name", mha_uid_6)
        d.setdefault("HouseHoldItemCount", mha_qyt_6)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)

        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("HouseholdItem", mha_item_7)
        d.setdefault("Type", "Metal/Household Appliances")
        d.setdefault("Name", mha_uid_7)
        d.setdefault("HouseHoldItemCount", mha_qyt_7)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)

        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("ElectronicWestType", mha_item_8)
        d.setdefault("Type", "Metal/Household Appliances")
        d.setdefault("Name", mha_uid_8)
        d.setdefault("HouseHoldItemCount", mha_qyt_8)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)

        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("HouseholdItem", mha_item_9)
        d.setdefault("Type", "Metal/Household Appliances")
        d.setdefault("Name", mha_uid_9)
        d.setdefault("HouseHoldItemCount", mha_qyt_9)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)

        d = dict()
        d.setdefault("DriverFirstName",firstName )
        d.setdefault("DriverLastName",lastName )
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("HouseholdItem", mha_item_10)
        d.setdefault("Type", "Metal/Household Appliances")
        d.setdefault("Name", mha_uid_10)
        d.setdefault("HouseHoldItemCount", mha_qyt_10)
        d.setdefault("ContactFirstName", "Sanstar1")
        d.setdefault("ContactLastName", "Integration")
        d.setdefault("LastUpdatedBy", "SANSTAR1")
        d.setdefault("PurposeofSR", "Cutover Activity")
        l311.append(d)




        lIndexes = []
        nCnt = len(l311)
        for i in range(nCnt):
            d = l311[i]
            if(d['Name'].strip() == ''):
                del d['Name']
            if(d['HouseHoldItemCount'] == "None"):
                lIndexes.append(i)

        if(len(lIndexes)>0):
            for i in reversed(lIndexes):
                del l311[i]




        if(len(l311)>0):
                dL311.setdefault("La311MetalHouseholdAppliancesPickup", l311)
                dResult.setdefault("ListOfLa311MetalHouseholdAppliancesPickup",dL311)
                sReq = json.dumps(dResult,sort_keys=True, indent=2)
                results = {"MetaData": {}, "SRData": dResult}
                sReqj = json.dumps(results,sort_keys=True, indent=2)
                print sReqj
                start = time.time()
                url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSRWithCodes"
                headers = {'Content-type': 'text/plain', 'Accept': '/'}
                r = requests.post(url, data= json.dumps(results), headers=headers,  verify=False)
                # # print results
                print r.text
                print 'It took', time.time()-start, 'seconds.'

                ii = ii + 1
                print (str(ii) + " recs sent to server.",  'It took', time.time()-start, 'seconds.')



    print("Finished")
except Exception,e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)

#
#
#
# 
# pyFC = "import_311"
# clauseSBE = "WHERE RESOLUTION_CODE <> ''  AND Category LIKE '%10%'"
# if(__name__=='__main__'):
#     # sMsg = printObjects()
#     # print(sMsg)
# 
#     connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
#     # connstr = 'DRIVER={SQL Server};SERVER=zye8;DATABASE=LA2015; UID=sa;PWD=sapassword'
#     conn = pyodbc.connect(connstr)
#     cursor = conn.cursor()
#     FN_SRNumber = "SRNumber"
#     lFields = [FN_SRNumber, "RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user", "last_edited_date", "ItemLoc_1","ItemLoc_2", "ItemLoc_3", "ItemLoc_4", "ItemLoc_5", "ItemLoc_6", "ItemLoc_7", "ItemLoc_8", "ItemLoc_9", "ItemLoc_10" ]
#     #lFields = ["SRNumber"]
#     sFields = ""
#     for fld in lFields:
#         if(sFields==""):
#             sFields = fld
#         else:
#             sFields = sFields + "," + fld
#     #List of the fields you'd like to exclude, like ItemCount for example.
#     lFieldsExcluded = ["RESOLUTION_CODE", "ITEM_1","ITEM_2", "ITEM_3", "ITEM_4", "ITEM_5", "ITEM_6","ITEM_7","ITEM_8", "ITEM_9", "ITEM_10", "UID1","UID2", "UID3", "UID4", "UID5", "UID6", "UID7", "UID8", "UID9", "UID10","QYT_1", "QYT_2", "QYT_3", "QYT_4", "QYT_5", "QTY_6", "QTY_7", "QTY_8", "QTY_9", "QTY_10", "last_edited_user",  "last_edited_date", "ItemLoc_1","ItemLoc_2", "ItemLoc_3", "ItemLoc_4", "ItemLoc_5", "ItemLoc_6", "ItemLoc_7", "ItemLoc_8", "ItemLoc_9", "ItemLoc_10"]
# 
#     #sSQL = "SELECT SRNumber FROM {}".format(pyFC)
#     sSQL = "SELECT {} FROM {}  {}".format(sFields, pyFC, clauseSBE)
# 
# 
#     cursor.execute(sSQL)
#     #columns = [column[0] for column in cursor.description]
#     columns = []
#     for column in cursor.description:
#         if not (column[0] in lFieldsExcluded):
#             columns.append(column[0])
# 
# 
# try:
#     ii = 0
# 
#     abw_uid_1 = ""
#     abw_uid_2 = " "
#     abw_uid_3 = ""
#     abw_uid_4 = ""
#     abw_uid_5 = ""
#     abw_uid_6 = ""
#     abw_uid_7 = ""
#     abw_uid_8 = ""
#     abw_uid_9 = ""
#     abw_uid_10 = ""
#     rescode = ""
#     reasoncode = " "
#     abw_uid = ""
# 
# 
#     for row in cursor.fetchall():
#         lResults = []    #make sure lResults are initiated here
#         lValues = []
#         for i in range(len(columns)):
#             lValues.append( str(row[i]))
# 
# 
#         abw_uid_1 = (str(row[lFields.index("UID1")]))
#         abw_uid_2 = (str(row[lFields.index("UID2")]))
#         abw_uid_3 = (str(row[lFields.index("UID3")]))
#         abw_uid_4 = (str(row[lFields.index("UID4")]))
#         abw_uid_5 = (str(row[lFields.index("UID5")]))
#         abw_uid_6 = (str(row[lFields.index("UID6")]))
#         abw_uid_7 = (str(row[lFields.index("UID7")]))
#         abw_uid_8 = (str(row[lFields.index("UID8")]))
#         abw_uid_9 = (str(row[lFields.index("UID9")]))
#         abw_uid_10 = (str(row[lFields.index("UID10")]))
# 
#         ItemLoc_1 = (str(row[lFields.index("ItemLoc_1")]))
#         ItemLoc_2 = (str(row[lFields.index("ItemLoc_2")]))
#         ItemLoc_3 = (str(row[lFields.index("ItemLoc_3")]))
#         ItemLoc_4 = (str(row[lFields.index("ItemLoc_4")]))
#         ItemLoc_5 = (str(row[lFields.index("ItemLoc_5")]))
#         ItemLoc_6= (str(row[lFields.index("ItemLoc_6")]))
#         ItemLoc_7 =(str(row[lFields.index("ItemLoc_7")]))
#         ItemLoc_8 = (str(row[lFields.index("ItemLoc_8")]))
#         ItemLoc_9 =(str(row[lFields.index("ItemLoc_9")]))
#         ItemLoc_10 = (str(row[lFields.index("ItemLoc_10")]))
# 
# 
# 
#         rescode = (str(row[lFields.index("RESOLUTION_CODE")]))
# 
#         last_edited_user = (str(row[lFields.index("last_edited_user")]))
# 
#         #dResult = dict(zip(columns, row)) number of columns = field names, lva
#         dResult = dict(zip(columns, lValues))
# 
#         # Adding additional items  ******************************
#         dResult.setdefault("ReasonCode", rescode if rescode.isdigit() else "")
#         dResult.setdefault("ResolutionCode",rescode if not rescode.isdigit() else "")
#         dResult.setdefault("UpdatedByUserLogin", "SANSTAR1")
# 
# 
# 
# 
#         firstName, lastName = last_edited_user.split()
# 
#         print firstName
#         print lastName
# 
# 
#         # dResult.setdefault("ListOfLa311DeadAnimalRemoval", dict())
#         l311 = []
#         dL311 = dict()
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName)
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("Type", "Illegal Dumping Pickup")
#         d.setdefault("Name", abw_uid_1 )
#         d.setdefault("CollectionLocation", ItemLoc_1)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         dL311 = dict()
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("Type", "Illegal Dumping Pickup")
#         d.setdefault("Name", abw_uid_2 )
#         d.setdefault("CollectionLocation", ItemLoc_2)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         # l311.append(d)
#         # d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("Type", "Illegal Dumping Pickup")
#         d.setdefault("Name", abw_uid_3 )
#         d.setdefault("CollectionLocation", ItemLoc_3)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("Type", "Illegal Dumping Pickup")
#         d.setdefault("Name", abw_uid_4 )
#         d.setdefault("CollectionLocation", ItemLoc_4)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("Type", "Illegal Dumping Pickup")
#         d.setdefault("Name", abw_uid_5 )
#         d.setdefault("CollectionLocation", ItemLoc_5)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("Type", "Illegal Dumping Pickup")
#         d.setdefault("Name", abw_uid_6 )
#         d.setdefault("CollectionLocation", ItemLoc_6)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("Type", "Illegal Dumping Pickup")
#         d.setdefault("Name", abw_uid_7 )
#         d.setdefault("CollectionLocation", ItemLoc_7)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("Type", "Illegal Dumping Pickup")
#         d.setdefault("Name", abw_uid_8 )
#         d.setdefault("CollectionLocation", ItemLoc_8)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("Type", "Illegal Dumping Pickup")
#         d.setdefault("Name", abw_uid_9 )
#         d.setdefault("CollectionLocation", ItemLoc_9)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
#         d = dict()
#         d.setdefault("DriverFirstName",firstName )
#         d.setdefault("DriverLastName",lastName )
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("Type", "Illegal Dumping Pickup")
#         d.setdefault("Name", abw_uid_10 )
#         d.setdefault("CollectionLocation", ItemLoc_10)
#         d.setdefault("ContactFirstName", "Sanstar1")
#         d.setdefault("ContactLastName", "Integration")
#         d.setdefault("LastUpdatedBy", "SANSTAR1")
#         d.setdefault("PurposeofSR", "Cutover Activity")
#         l311.append(d)
# 
# 
#         lIndexes = []
#         nCnt = len(l311)
#         for i in range(nCnt):
#             d = l311[i]
#             if(d['Name'].strip() == '') or (d['Name'].strip() == "None"):
#                 del d['Name']
# 
#             if(d['CollectionLocation'] == " "):
#                 lIndexes.append(i)
# 
#         if(len(lIndexes)>0):
#             for i in reversed(lIndexes):
#                 del l311 [i]
# 
# 
#         for d in l311:
#             if(d['Name'].strip() == ''):
#                 del d['Name']
# 
# 
# 
# 
# 
#         if(len(l311)>0):
#             dL311.setdefault("La311IllegalDumpingPickup", l311)
#             dResult.setdefault("ListOfLa311IllegalDumpingPickup",dL311)
#             lResults.append({"MetaData": {}, "SRData": dResult})
#             sReq = json.dumps(dResult,sort_keys=True, indent=2)
#             results = {"MetaData": {}, "SRData": dResult}
#             # print results
#             sReqj = json.dumps(results,sort_keys=True, indent=2)
#             print sReqj
#             start = time.time()
#             # url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSRWithCodes"
#             # headers = {'Content-type': 'text/plain', 'Accept': '/'}
#             # r = requests.post(url, data= json.dumps(results), headers=headers,  verify=False)
#             # # # print results
#             # print r.text
#             # print 'It took', time.time()-start, 'seconds.'
# 
#             ii = ii + 1
#             print (str(ii) + " recs sent to server.",  'It took', time.time()-start, 'seconds.')
# 
# 
# 
#     print("Finished")
# except Exception,e:
#     exc_type, exc_obj, exc_tb = sys.exc_info()
#     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#     print(exc_type, fname, exc_tb.tb_lineno)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


























