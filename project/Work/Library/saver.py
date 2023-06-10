#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Сохранение оперируемых объектов

@author: pavel
"""

import pickle


def saveDataFrameToCSV(name, _df):
    """
    Сохранение датасета в внутреннюю директорию

    Parameters
    ----------
    name : str
        Название выходного файла.
    df : DataFrame
        База данных.

    Returns
    -------
    None.

    """
    _df.to_csv("../Outputs/"+name+".csv")


def save_model(name, model):
    """
    Сохранение модели в внутреннюю директорию

    Parameters
    ----------
    name : str
        Название выходного файла.
    model : RandomForestRegressor
        Модель.

    Returns
    -------
    None.

    """
    with open('../Outputs/'+name+'.pkl', 'wb') as _f:
        pickle.dump(model, _f)
