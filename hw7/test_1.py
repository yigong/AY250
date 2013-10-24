# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:14:15 2013

@author: Yigong
"""

#1) Make a DataFrame with one row per issue with the following columns extracted from the issue data:
#ntitle, created_at, labels, closed_at, user, id

import json
jFile = open('closed.json')
jData = json.load(jFile)