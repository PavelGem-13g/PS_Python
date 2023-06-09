#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Сортировка значений, формирование отчетов

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
    """
    Сортировка по значению

    Parameters
    ----------
    df : DataFrame
        База данных.
    column : List
        Колонки.
    value : int
        Ключевое значение.
    sign : string
        Знак.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if sign=='>':
        return df.loc[df[column]>value]
    elif sign=='<':
        return df.loc[df[column]<value]
    elif sign=='>=':
        return df.loc[df[column]>=value]
    else:
        return df.loc[df[column]<=value]
    
def crosstab(df, attribute1, attribute2):
    """
    Пересечение талблиц

    Parameters
    ----------
    df : DataFrame
        База данных.
    attribute1 : str
        Атрибут 1.
    attribute2 : str
        Атрибут 2.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    print(type(df['Name']), type(df['Country']))
    return pd.crosstab(df[attribute1], df[attribute2])

def makeOutputs(df):
    """
    Сохранение стандартных отчетов

    Parameters
    ----------
    df : DataFrame
        База данных.

    Returns
    -------
    result : List
        Базовые таблицы для анализа.

    """
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
    """
    Тестирование
    """
    df = data_loader.get_database("FT1000.csv")
    res = makeOutputs(df)
    print(crosstab(df, 'Sector', 'Country'))