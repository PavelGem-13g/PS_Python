#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:31:19 2023

@author: pavel
"""

import os
import pandas

def saveDataFrameToCSV(name, df):
    df.to_csv("../Outputs/"+name)