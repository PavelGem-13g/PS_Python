#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:58:37 2023

@author: pavel
"""

import pandas as pd

import saver
import data_loader

def filter(df, keys, col):
    """
    Фильтрация данных

    Parameters
    ----------
    df : DataFrame
        База данных.
    keys : Dictionary
        Ключи их их значения, по которым идет фильтрация данных.
    col : List
        Список требуемых колонок.

    Returns
    -------
    Dataframe
        Возращает отфильтрованные данные.

    """
    for i in keys:
        select = (df[i].isin(keys[i]))
        df = df.loc[select, :]
    return df.loc[select, col]

def filterByValue(df, column, value, sign):
    if sign=='>':
        return df.loc[df[column]>value]
    elif sign=='<':
        return df.loc[df[column]<value]
    elif sign=='>=':
        return df.loc[df[column]>=value]
    else:
        return df.loc[df[column]<=value]

def makeOutputs(df):
    result = []
    describtion = df.describe()
    saver.saveDataFrameToCSV("Describtion", describtion)
    table1 = filter(
        df,
        {"Country":{"UK", "Germany", "France", "Italy", "Spain"}},
        ["Name", "Sector"])
    saver.saveDataFrameToCSV(
        "Top companies from top 5 countries",
        filter(
            df,
            {"Country":{"UK", "Germany", "France", "Italy", "Spain"}},
            ["Name", "Sector"]))
    table2 = filterByValue(
    df,
    "Employees2017", 
    200,
    ">")
    saver.saveDataFrameToCSV(
        "Companies with employees greater than 200",
        filterByValue(
        df,
        "Employees2017", 
        200,
        ">"))
    result.append("Describtion")
    result.append("Top companies from top 5 countries")
    result.append("Companies with employees greater than 200")
    print(result)
    return result


if __name__=="__main__":
    df = data_loader.get_database("FT1000.csv")
    res = makeOutputs(df)