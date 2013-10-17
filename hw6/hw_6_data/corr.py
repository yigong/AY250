# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:42:30 2013

@author: Yigong
"""

import sqlite3
import pandas as pd
from pandas.io import sql
connection = sqlite3.connect('airport.db')
cursor = connection.cursor()
table_cmd = '.tables'
cursor.execute(table_cmd)
tables_info = cursor.fetchall()
for irow, ICAO_row in ICAO_df.itertuples():
    for icol, ICAO_col in ICAO_df.itertuples():
        row_cmd = 'SELECT Max_TemperatureF FROM '+ICAO_row
        cursor.execute(row_cmd)
        row_df = cursor.fetchall()
        col_cmd = 'SELECT Max_TemperatureF FROM '+ICAO_col
        cursor.execute(col_cmd)
        col_df = cursor.fetchall()
#sql.read_frame()