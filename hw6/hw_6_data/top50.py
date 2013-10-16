# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:23:43 2013

@author: Yigong
"""
import sqlite3
import pandas as pd
import numpy as np
connection = sqlite3.connect('airport.db')
cursor = connection.cursor()
sql_cmd = '''CREATE TABLE IF NOT EXISTS top50(id INTEGER PRIMARY KEY AUTOINCREMENT, City TEXT, FAA TEXT, IATA TEXT, ICAO TEXT, Airport TEXT, Role TEXT, Enplanements INTEGER) '''
cursor.execute(sql_cmd)
data_df = pd.read_csv('top_airports.csv')
for i in data_df.index:
    temp_row = tuple(data_df.iloc[i,:].values)
    #info_temp = 'City, FAA, IATA, ICAO, Airport, Role, Enplanements'
    print temp_row, '@@'
    #airport = tuple(airport)
    sql_cmd = ("INSERT INTO top50 (City, FAA, IATA, ICAO, Airport, Role, Enplanements) VALUES"+str(temp_row))
    print sql_cmd
    cursor.execute(sql_cmd)
    
sql_cmd = 'SELECT * FROM top50'
cursor.execute(sql_cmd)    
db_info = cursor.fetchall()
print db_info
connection.commit()
connection.close()
#sql_cmd = "SELECT * FROM top50"
#cursor.execute(sql_cmd)
#top50_info = cursor.fetchall()
#for entry in top50_info:
#    print entry
    