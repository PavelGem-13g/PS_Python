#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:31:53 2023

@author: pavel
"""

import numpy as np
import pandas as pd

def get_database(filename):
    df = pd.read_csv('../Data/'+filename, delimiter=',')
    return df

def get_reference():
    result = pd.Series({
        'Rank':np.int64,
        'Name':np.object,
        'Ranked2021':np.object,
        'Ranked2020':np.object,
        'Country':np.object, 
        'Sector':np.object, 
        'CAGR':np.float64, 
        'Revenue2020':np.int64, 
        'Revenue2017':np.int64, 
        'Employees2020':np.int64, 
        'Employees2017':np.int64, 
        'FoundingYear':np.int64
            })
    return result

def check_dataset(df):
    info = df.dtypes
    # print(info.keys())
    # print(get_reference().keys())
    # print(len(info.keys()), len(get_reference().keys()))
    result = (len(info.keys())==len(get_reference().keys())) and min(info==get_reference())
    return result
# =============================================================================
#     data = data.to_numpy()
#     
#     country = sorted(list(set(data[:,4])))
#     country = dict(sorted([[str(country[i]),i] for i in range(len(country))]))
#         
#     sectors = sorted(list(set(data[:,5])))
#     sectors = dict(sorted([[str(sectors[i]),i] for i in range(len(sectors))]))
# 
#     date = sorted(list(set(data[:,11])))
#     date = dict(sorted([[str(date[i]),i] for i in range(len(date))]))
#     
#     ranked_values = sorted(list(set(data[:,2])))
#     ranked_values = dict(sorted([[str(ranked_values[i]),i] for i in range(len(ranked_values))]))
#     
#     return data, country, sectors, date, ranked_values
# =============================================================================

# =============================================================================
# def normalize(data, country, sectors, date, ranked_values):
#     for i in range(1, len(data)):
#         data[i][4] = country[str(data[i][4])]
#     
#     for i in range(1, len(data)):
#         data[i][5] = sectors[str(data[i][5])]
#         
#     for i in range(1, len(data)):
#         data[i][11] = date[str(data[i][11])]
#         
#     for i in range(1, len(data)):
#         data[i][2] = ranked_values[str(data[i][2])]
#         data[i][3] = ranked_values[str(data[i][3])]
#         
# def get_database():
#     data, country, sectors, date, ranked_values = load_data()
#     normalize(data, country, sectors, date, ranked_values)
#     return data, country, sectors, date, ranked_values
# =============================================================================

if __name__=="__main__":
    df = get_database("FT1000.csv")
    print(check_dataset(df))