from dash_package import app
import dash_core_components as dcc
import dash_html_components as html
from dash_package.query import *



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


# app.layout= html.Div('It\'s here...')

app.layout = html.Div(
    children=[
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(id='sat', label='sat for 2012',
            children=[
            dcc.Graph(figure=
            {'data': overall_rating(),
            'layout': {}})
            ]
        ),
        dcc.Tab(id='rating', label='School Ratings',
            children=[
            dcc.Graph(figure=
            {'data': overall_rating(),
            'layout': {}})
            ]
        )

        ])
    ]
)
