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

connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=SCData; UID=SA;PWD=70SR30ssD'
conn = pyodbc.connect(connstr)
cursor = conn.cursor()

cursor.execute("""SELECT    SRNumber FROM SO_SC_1 WHERE SRNumber LIKE '%1-%' """)
columns = [column[0] for column in cursor.description]

for row in cursor.fetchall():
    results = []
    result = dict(zip(columns, row))
    results.append({"MetaData": {}, "SRData": result})
    print(json.dumps(results, sort_keys=True, indent=4))
    for outputs in results:
        url = "https://myla311.lacity.org/myla311router/mylasrbe/1/UpsertSANSR"
        headers = {'Content-type': 'text/plain', 'Accept': '/'}
        r = requests.post(url, data= json.dumps(outputs), headers=headers,  verify=False)
        print 'It took', time.time()-start, 'seconds.'
        print r.text

