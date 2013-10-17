# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:37:07 2013

@author: Yigong
"""
from urllib import urlopen
import pandas as pd
import numpy as np
import sqlite3

def toStandardTime(columns):
    daylight_time = ['AKDT','ADT', 'CDT','HADT','MDT','PDT', 'EDT','AKST', 'AST', 'CST', 'HAST', 'MST', 'PST', 'EST']  
    for i, col in enumerate(columns):
        if col in daylight_time:
            columns[i] = 'date'
        else:
            pass
    return columns

def toDataFrame(url):
    '''
    convert data in a url into pandas.DataFrame
    '''
    lines_temp = urlopen(url).readlines()
    month_temp = []
    for entry in lines_temp[1:]:
        line_splitted = entry.split(',')
        month_temp.append(line_splitted)
    col = toStandardTime(month_temp[0])
    month_df = pd.DataFrame(month_temp[1:], columns = col)
    return month_df

yrs = np.arange(2008,2009)
months = np.arange(1,2)



read_ICAO = 'SELECT ICAO FROM top50_joined;'
connection = sqlite3.connect('airport.db')
cursor = connection.cursor()
url_pre = 'http://www.wunderground.com/history/airport/'
url_end = 'MonthlyHistory.html?format=1'

ICAO_df = pd.io.sql.read_frame(read_ICAO, connection)
for i in ICAO_df.index:
    ICAO, = ICAO_df.iloc[i].values
    url_airport = ICAO
    airport_temp = pd.DataFrame()
    for Year in yrs:
        url_yr = '/'+str(Year)
        year_temp = pd.DataFrame()
        for Month in months:
            if (Year == 2013) & (Month > 9):
                print Year
                print Month
            
            else:
                url_mon = '/'+str(Month)+'/1/'
                url = url_pre+url_airport+url_yr+url_mon+url_end
                year_temp = year_temp.append(toDataFrame(url))
        airport_temp = airport_temp.append(year_temp)
    db_name = ICAO +'_corr'
    drop_cmd = 'DROP TABLE IF EXISTS ' + db_name
    cursor.execute(drop_cmd)
    #create_table = 'CREATE TABLE IF NOT EXISTS '+ICAO+' (id INTEGER PRIMARY KEY AUTOINCREMENT, min_temp INTEGER, max_temp INTEGER,\
    #humid INTEGER, precipitation REAL, cloud_cover INTEGER)'
    #cursor.execute(create_table)
    info = ['date','Min TemperatureF','Max TemperatureF',' Mean Humidity','PrecipitationIn',' CloudCover']
    pd.io.sql.write_frame(airport_temp[info], db_name, connection )
connection.commit()
connection.close()


