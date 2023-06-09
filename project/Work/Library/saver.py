#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Сохранение оперируемых объектов

@author: pavel
"""

import pickle


def saveDataFrameToCSV(name, df):
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
    df.to_csv("../Outputs/"+name+".csv")


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
    with open('../Outputs/'+name+'.pkl', 'wb') as f:
        pickle.dump(model, f)
