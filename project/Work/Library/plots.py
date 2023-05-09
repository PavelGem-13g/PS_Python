# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import plotly.express as px
import plotly.io as pio
pio.renderers.default='svg'
import plotly.graph_objects as go
from plotly import tools


import data_loader


def generate_plots(df):
    fig = px.histogram(df, x='Country',color='Country',marginal='box',hover_data=df.columns,title= 'The most common countries', width=1000, height=500,template='plotly_dark')
    fig.show()
    
    fig=px.choropleth(data_frame=df,locations=df['Country'],locationmode='country names',color=df['Revenue2020'],animation_frame=df['FoundingYear'],animation_group=df['CAGR'] ,template='plotly_dark')
    fig.update_layout(dict1={'title':'Revenue distribution relative to countries for 2020 on the map'})
    fig.show() 
    
    fig = px.box(df, x='Sector', color='Sector', y='Employees2017', title='Distribution and analysis of the number of employees by sector in 2017', width=1200, height=600 ,template='plotly_dark')
    fig.show()

    

if __name__ == "__main__":
    df = data_loader.get_database()
    generate_plots(df)