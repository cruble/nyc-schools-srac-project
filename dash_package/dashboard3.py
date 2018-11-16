# from dash_package import app3
# from dash_package.dashboard2 import *
# import pdb
#
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash_package.dashboard3 import *
# import pandas as pd
# import plotly.plotly as py
# import plotly.graph_objs as go
# from dash_package.models import *
#
#
# def generate_table(School, max_rows=100):
#     return html.Table(
#         # Header
#         [html.Tr([html.Th(col) for col in school.columns])] +
#
#         # Body
#         [html.Tr([
#             html.Td(dataframe.iloc[i][col]) for col in school.columns
#         ]) for i in range(min(len(dataframe), max_rows))]
#     )
#
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div(children=[
#     html.H4(children='school'),
#     generate_table(school)
# ])
# #
# # # if __name__ == '__main__':
# # #     app.run_server(debug=True)
