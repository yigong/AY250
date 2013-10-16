# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:44:50 2013

@author: Yigong
"""
import sqlite3
import pandas as pd
import numpy as np
connection = sqlite3.connect('airport.db')
cursor = connection.cursor()
DROP_cmd = 'DROP TABLE IF EXISTS top50_joined'
cursor.execute(DROP_cmd)
#join_cmd = 'CREATE TABLE top50_joined(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, city TEXT, ICAO TEXT, latitude REAL, longitude REAL)'+\
#            ' AS SELECT Airport, City, ICAO, latitude, longitude From'+\
#            ' top50 LEFT JOIN ICAO on top50.Airport = ICAO.name'
join_cmd = '''CREATE TABLE top50_joined AS SELECT Airport, City, ICAO, latitude,
             longitude FROM top50 LEFT JOIN ICAO on top50.IATA = ICAO.iata_code'''
cursor.execute(join_cmd)
read_cmd = 'SELECT * FROM top50_joined'
cursor.execute(read_cmd)
joined_info = cursor.fetchall()
for entry in joined_info:
    print entry
connection.commit()
connection.close()