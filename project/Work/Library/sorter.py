#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Сортировка значений, формирование отчетов

@author: pavel
"""

import pandas as pd

import saver
import data_loader

def filter(_df, keys, col):
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
        select = (_df[i].isin(keys[i]))
        _df = _df.loc[select, :]
    return _df.loc[select, col]

def filterByValue(_df, column, value, sign):
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
        return _df.loc[_df[column]>value]
    elif sign=='<':
        return _df.loc[_df[column]<value]
    elif sign=='>=':
        return _df.loc[_df[column]>=value]
    else:
        return _df.loc[_df[column]<=value]
    
def crosstab(_df, attribute1, attribute2):
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
    print(type(_df['Name']), type(_df['Country']))
    return pd.crosstab(_df[attribute1], _df[attribute2])

def makeOutputs(_df):
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
    describtion = _df.describe()
    saver.saveDataFrameToCSV("Describtion", describtion)
    table1 = filter(
        _df,
        {"Country":{"UK", "Germany", "France", "Italy", "Spain"}},
        ["Name", "Sector"])
    saver.saveDataFrameToCSV(
        "Top companies from top 5 countries",
        filter(
            _df,
            {"Country":{"UK", "Germany", "France", "Italy", "Spain"}},
            ["Name", "Sector"]))
    table2 = filterByValue(
    _df,
    "Employees2017", 
    200,
    ">")
    saver.saveDataFrameToCSV(
        "Companies with employees greater than 200",
        filterByValue(
        _df,
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
