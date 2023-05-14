# -*- coding: utf-8 -*-

# import matplotlib.pyplot as plt

import plotly
import plotly.express as px
import plotly.io as pio
pio.renderers.default='svg'
# pio.renderers.default='browser'
# import plotly.graph_objects as go
# from plotly import tools


import data_loader


def generate_html_image(fig, name):
    fig.write_image("../Graphics/"+name)
    result = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    fig.show()
    return result


def generate_plots(df):
    result = ''
    
    fig = px.bar(df, x='CAGR', y='Ranked2020', color='Ranked2021', title='Relation between CAGR and Ranked2020', width=1000, height=500, template='plotly_white')
    result += generate_html_image(fig, "r2021.svg")

    fig = px.histogram(df, x='Sector', color='Sector', title="The most common sectors", width=1000, height=500, template='plotly_white').update_xaxes(categoryorder="total descending")
    result += generate_html_image(fig, "sector.svg")
    
    fig = px.scatter(df, x='Revenue2017', y='Revenue2020', color='Sector', size="CAGR",animation_frame=df['Sector'], width=1000, height=500, template='plotly_white')
    result += generate_html_image(fig, "CAGRRevenue2020Sector.svg")

    fig = px.histogram(df, x='Country',color='Country', title= 'The most common countries', width=1000, height=500,template='plotly_white').update_xaxes(categoryorder="total descending")
    result += generate_html_image(fig, "countries.svg")
    
    df = df.sort_values(by="FoundingYear")
    fig=px.choropleth(data_frame=df,locations=df['Country'],locationmode='country names',color=df['Revenue2020'],animation_frame=df['FoundingYear'],animation_group=df['CAGR'], width=1000, height=500, template='plotly_white')
    fig.update_layout(dict1={'title':'Revenue distribution relative to countries for 2020 on the map'})
    result += generate_html_image(fig, "Revenue2020 FoundingYear.svg")
    
    fig = px.line(df.sort_values(by="FoundingYear"), x='FoundingYear', y='CAGR', title='Relation between CAGR and Founding Year', width=1000, height=500, template='plotly_white')
    result += generate_html_image(fig, "FoundingCagr.svg")
    
    fig = px.box(df, x='Sector', color='Sector', y='Employees2017', title='Distribution and analysis of the number of employees by sector in 2017', width=1000, height=500, template='plotly_white')
    result += generate_html_image(fig, "Sector Employees2017.svg")
    
    fig = px.imshow(df[["Name","Ranked2021","Ranked2020","Country","Sector","CAGR","Revenue2020","Revenue2017","Employees2020","Employees2017","FoundingYear"]].corr(),title="Correlations", width=1000, height=500, template='plotly_white')
    result += generate_html_image(fig, "Correlation.svg")

    return result

    

if __name__ == "__main__":
    df = data_loader.get_database()
    html = '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>'
    html += generate_plots(df)
    