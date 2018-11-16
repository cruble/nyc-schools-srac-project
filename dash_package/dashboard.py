from dash_package import app
import dash_core_components as dcc
import dash_html_components as html
from dash_package.query import *


import dash
import plotly.graph_objs as go
import plotly.plotly as py
import pandas as pd 

from dash_package.mega_data import mega_list_2012, mega_list_2013, mega_list_2014, mega_list_2015, mega_list_2016, mega_list_2017

# school_rating = [i.overall for i in db.session.query(Rating).all()]
# school_sat= School=[i.math_avg for i in db.session.query(SchoolSAT).all()]

# def sat_avg():
#     name=[]
#     math=[]
#     for school in School.query.all():
#         if school.sats[0].math_avg:
#             name.append(school.name)
#             math.append(school.sats[0].math_avg)
#     return {'x': name, 'y': math, 'type': 'bar', 'name': 'Math Avgs'}


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('../Schools2013-3.csv', sep='\t')


app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['Rating'] == i]['Math_Avg'],
                    y=df[df['Rating'] == i]['Attendance_Ratio'],
                    text=df[df['Rating'] == i]['Name'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=str(i)
                ) for i in df.Rating.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Math Average'},
                yaxis={'title': 'Attendance_Ratio'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])




# app.layout= html.Div('It\'s here...')
# #working to here
# app.layout = html.Div(
#     children=[
#     dcc.Tabs(id="tabs", children=[
#         dcc.Tab(id='sat', label='sat for 2012',
#             children=[
#             dcc.Graph(figure=
#             {'data': sat_avg(),
#             'layout': {}})
#             ]
#         ),
#         dcc.Tab(id='rating', label='School Ratings',
#             children=[
#             dcc.Graph(figure=
#             {'data': overall_rating(),
#             'layout': {}})
#             ]
#         )

#         ])
#     ]
# )
