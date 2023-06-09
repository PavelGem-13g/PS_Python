#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Работа с нейросетью

@author: pavel
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

import data_loader

def normalize(df):
    """
    Нормализация данных

    Parameters
    ----------
    df : DataFrame
        База данных.

    Returns
    -------
    result : DataFrame
        База данных.

    """
    result = pd.DataFrame()
    
    for i in df.columns:
        if df[i].dtype.name != 'object':
            result[i] = df[i].copy()
            result.loc[result[i].isna(), i] = result[i].median()
        else:
            result[i] = pd.factorize(df[i])[0]
            
    return result


def get_X(df):
    """
    Получение входных данных для обучения

    Parameters
    ----------
    df : DataFrame
        База данных.

    Returns
    -------
    result : DataFrame
        База данных входных значений для обучения.

    """
    col = ['Ranked2020', 'Ranked2021', 'Country', 'Sector', 'CAGR',
           'Revenue2017', 'Employees2017' ,'Employees2020', 'FoundingYear']
    result = df[col]
    return result


def get_Y(df):
    """
    Получение выходных данных для обучения

    Parameters
    ----------
    df : DataFrame
        База данных.

    Returns
    -------
    result : DataFrame
        База данных выходных значений для обучения.

    """
    return df['Revenue2020']


def train_model(df):
    """
    Обучение модели

    Parameters
    ----------
    df : DataFrame
        База данных.

    Returns
    -------
    resutl : RandomForestRegressor
        Обученная модель.

    """
    resutl = RandomForestRegressor(n_estimators=300)
    X = get_X(df)[:-20]
    y = get_Y(df)[:-20]
    resutl.fit(X, y)
    return resutl

def test_model(df, model):
    """
    Проверка точности

    Parameters
    ----------
    df : DataFrame
        База данных.
    model : RandomForestRegressor
        Модель.

    Returns
    -------
    None.

    """
    predictions = model.predict(get_X(df))
    print('Score is', model.score(get_X(df)[:-20], get_Y(df)[:-20]))

def predict(model, data):
    """
    Предсказание

    Parameters
    ----------
    model : RandomForestRegressor
        Модель.
    data : DataFrame
        Входные значения.

    Returns
    -------
    prediction : DataFrame
        Выходные значения.

    """
    prediction = model.predict(data)
    return prediction

if __name__ == "__main__":
    """
    Тестирование модуля на работу
    """
    df = data_loader.get_database()
    df = normalize(df)
    X = get_X(df)
    Y = get_Y(df)
    model = train_model(df)
    test_model(df, model)
    prediction = predict(model, get_X(df).tail(20))
    print('Prediction is\n', prediction)
    print('Real value is\n', df.tail(20)['Revenue2020'])