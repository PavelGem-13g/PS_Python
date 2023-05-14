#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:31:19 2023

@author: pavel
"""

def saveDataFrameToCSV(name, df):
    df.to_csv("../Outputs/"+name+".csv")
