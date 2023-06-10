#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Работа с нейросетью

@author: pavel
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

import data_loader


def normalize(_df):
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

    for i in _df.columns:
        if _df[i].dtype.name != 'object':
            result[i] = _df[i].copy()
            result.loc[result[i].isna(), i] = result[i].median()
        else:
            result[i] = pd.factorize(_df[i])[0]

    return result


def get_x(_df):
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
           'Revenue2017', 'Employees2017', 'Employees2020', 'FoundingYear']
    result = _df[col]
    return result


def get_y(_df):
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
    return _df['Revenue2020']


def train_model(_df):
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
    _x = get_x(_df)[:-20]
    _y = get_y(_df)[:-20]
    resutl.fit(_x, _y)
    return resutl


def test_model(_df, model):
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
    predictions = model.predict(get_x(_df))
    print('Score is', model.score(get_x(_df)[:-20], get_y(_df)[:-20]))


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
    _df = data_loader.get_database('FT1000.csv')
    _df = normalize(_df)
    X = get_x(_df)
    Y = get_y(_df)
    model = train_model(_df)
    test_model(_df, model)
    prediction = predict(model, get_x(_df).tail(20))
    print('Prediction is\n', prediction)
    print('Real value is\n', _df.tail(20)['Revenue2020'])
