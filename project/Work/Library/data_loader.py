#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Загрузка базы данных, проверка на корректность базы данных

@author: pavel
"""

import numpy as np
import pandas as pd

def get_database(filename):
    """
    Загрузка датасета с диска

    Parameters
    ----------
    filename : str
        Название файла.

    Returns
    -------
    df : Dataframe
        База данных.

    """
    _df = pd.read_csv('../Data/'+filename, delimiter=',')
    return _df

def get_reference():
    """
    Правильные занчения датасета

    Returns
    -------
    result : DataFrame
        База данных.

    """
    result = pd.Series({
'Rank':np.int64,'Name':np.object,'Ranked2021':np.object,'Ranked2020':np.object,
'Country':np.object,'Sector':np.object, 'CAGR':np.float64,
'Revenue2020':np.int64,'Revenue2017':np.int64, 'Employees2020':np.int64, 
'Employees2017':np.int64,'FoundingYear':np.int64})
    return result

def check_dataset(_df):
    """
    Проверка на валидность

    Parameters
    ----------
    df : DataFrame
        База данных.

    Returns
    -------
    result : bool
        Значение правильности.

    """
    info = _df.dtypes
    result = (len(info.keys())==len(get_reference().keys())) and min(info==get_reference())
    return result

if __name__=="__main__":
    df = get_database("FT1000.csv")
    print(check_dataset(df))