#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:58:37 2023

@author: pavel
"""

import pandas as pd

import saver

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
    describtion = df.describe()
    saver.saveDataFrameToCSV("Describtion", describtion)
    saver.saveDataFrameToCSV(
        "Top companies from top 5 countries",
        filter(
            df,
            {"Country":{"UK", "Germany", "France", "Italy", "Spain"}},
            ["Name", "Sector"]))
    saver.saveDataFrameToCSV(
        "Companies with eployees greater than 200",
        filterByValue(
        df,
        "Employees2017", 
        200,
        ">"))