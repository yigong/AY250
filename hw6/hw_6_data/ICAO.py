# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:04:41 2013

@author: Yigong
"""
import sqlite3
import pandas as pd
import numpy as np
connection = sqlite3.connect('airport.db')
cursor = connection.cursor()
drop_cmd = 'DROP TABLE IF EXISTS ICAO'
cursor.execute(drop_cmd)
sql_cmd = '''CREATE TABLE IF NOT EXISTS ICAO(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, latitude REAL, longitude REAL, iata_code TEXT)'''
cursor.execute(sql_cmd)
data_df = pd.read_csv('ICAO_airports.csv')
for i in data_df.index:
    info = ['name', 'latitude_deg', 'longitude_deg', 'iata_code']
    temp_row = list(data_df.iloc[i,3:6].values)
    temp_row = tuple(temp_row+[str(data_df.iloc[i,-5])])
    #temp_row = tuple(temp_row)
    #info_temp = 'City, FAA, IATA, ICAO, Airport, Role, Enplanements'
    #print temp_row, '@@'
    #airport = tuple(airport)
    sql_cmd = ("INSERT INTO ICAO (name, latitude, longitude, iata_code) VALUES"+str(temp_row))
    #print sql_cmd
    cursor.execute(sql_cmd)
    
sql_cmd = 'SELECT * FROM ICAO where id = 1'
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
    