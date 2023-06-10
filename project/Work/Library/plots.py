# -*- coding: utf-8 -*-
"""
Формирования графиков
"""

import plotly
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'svg'

import data_loader


def generate_html_image(fig, name):
    """
    Одновременная генерация html и скачивание в файл

    Parameters
    ----------
    fig : plot
        График.
    name : string
        Название.

    Returns
    -------
    result : str
        HTML-код.

    """
    fig.write_image("../Graphics/" + name)
    result = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    return result


def generate_plots(_df):
    """
    Генерация графиков по умолчанию

    Parameters
    ----------
    _df : DataFrmae
        База данныъ.

    Returns
    -------
    result : List
        Графики в формате HTML.

    """
    result = []

    fig = px.bar(_df, x='CAGR', y='Ranked2020', color='Ranked2021',
                 title='Relation between CAGR and Ranked2020',
                 width=1000, height=500, template='plotly_white')
    result.append(generate_html_image(fig, "r2021.svg"))

    fig = px.histogram(
        _df,
        x='Sector',
        color='Sector',
        title="The most common sectors",
        width=1000,
        height=500,
        template='plotly_white').update_xaxes(categoryorder="total descending")
    result.append(generate_html_image(fig, "sector.svg"))

    fig = px.scatter(
        _df,
        x='Revenue2017',
        y='Revenue2020',
        color='Sector',
        size="CAGR",
        animation_frame=_df['Sector'],
        width=1000, height=500, template='plotly_white')
    result.append(generate_html_image(fig, "CAGRRevenue2020Sector.svg"))

    fig = px.histogram(
        _df, x='Country',
        color='Country',
        title='The most common countries', width=1000, height=500,
        template='plotly_white').update_xaxes(categoryorder="total descending")
    result.append(generate_html_image(fig, "countries.svg"))

    _df = _df.sort_values(by="FoundingYear")
    fig = px.choropleth(
        data_frame=_df,
        locations=_df['Country'],
        locationmode='country names',
        color=_df['Revenue2020'],
        animation_frame=_df['FoundingYear'],
        animation_group=_df['CAGR'], width=1000, height=500,
        template='plotly_white')
    fig.update_layout(
        dict1=
        {'title':
         'Revenue distribution relative to countries for 2020 on the map'})
    result.append(generate_html_image(fig, "Revenue2020 FoundingYear.svg"))

    fig = px.line(_df.sort_values(by="FoundingYear"),
                  x='FoundingYear', y='CAGR',
                  title='Relation between CAGR and Founding Year',
                  width=1000, height=500, template='plotly_white')
    result.append(generate_html_image(fig, "FoundingCagr.svg"))

    fig = px.box(_df,
                 x='Sector',
                 color='Sector',
                 y='Employees2017',
title='Distribution and analysis of the number of employees by sector in 2017',
 width=1000, height=500,
                 template='plotly_white')
    result.append(generate_html_image(fig, "Sector Employees2017.svg"))

    fig = px.imshow(_df[["Name", "Ranked2021", "Ranked2020", "Country",
                        "Sector", "CAGR", "Revenue2020", "Revenue2017",
                        "Employees2020", "Employees2017", "FoundingYear"]
                       ].corr(), title="Correlations", width=1000,
                    height=500, template='plotly_white')
    result.append(generate_html_image(fig, "Correlation.svg"))

    return result


def common_plot(_df, name):
    """
    Генерация гистограммы 

    Parameters
    ----------
    df : DataFrame
        База данных.
    name : str
        Атрибут 1.

    Returns
    -------
    fig : Plot
        График Plotly.

    """
    fig = px.histogram(_df, x=name, color=name, title='The most common ' +
                       name, width=1000, height=500,
                       template='plotly_white'
                       ).update_xaxes(categoryorder="total descending")
    return fig


def box_plot(_df, name1, name2):
    """
    Генерация графика box

    Parameters
    ----------
    df : DataFrame
        База данных.
    name1 : str
        Атрибут 1.
    name2 : str
        Атрибут 2.

    Returns
    -------
    fig : Plot
        График Plotly.

    """
    fig = px.box(_df, x=name1, color=name1, y=name2,
                 title='Distribution and analysis of the ' +
                 name1 + ' by ' + name2,
                 width=1000, height=500, template='plotly_white')
    return fig


def scatter_plot(_df, x_name, y_name, color_name, size_name, animation_name):
    """
    Генерация графика scatter

    Parameters
    ----------
    df : DataFrame
        База данных.
    x_name :  str
        Атрибут 1.
    y_name : str
        Атрибут 2.
    color_name : str
        Атрибут 3.
    size_name : str
        Атрибут 4.
    animation_name : str
        Атрибут 5.

    Returns
    -------
    fig : Plot
        График Plotly.

    """
    _df = _df.sort_values(by=animation_name)
    fig = px.scatter(_df, x=x_name, y=y_name, color=color_name, size=size_name,
                     animation_frame=_df[animation_name],
                     width=1000, height=500, template='plotly_white')
    return fig


def pie_plot(_df, names):
    """
    Генерация кругового графика

    Parameters
    ----------
    df : DataFrame
        База данных.
    names :  str
        Атрибут 1.

    Returns
    -------
    fig : Plot
        График Plotly.

    """
    fig = px.pie(_df, names, width=1000, height=500, template='plotly_white')
    return fig


if __name__ == "__main__":
    df = data_loader.get_database('FT1000.csv')
    page = generate_plots(df)
