# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            # Video Game Sales Project


            ## I have enjoyed video games since I was a teenager.
            ## On Kaggle I saw this set of data shrubbed from the website vgsales.


            - ### Want to see if there was a relationship between your favorite 
              ### platforms, publishers and consols in determining sales?

            """
        ),
        dcc.Link(dbc.Button('Go to predict', color='primary'), href='/predictions')
    ],
    md=12,
)



# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#           hover_name="country", log_x=True, size_max=60)

# column2 = dbc.Col(
#    [
#        dcc.Graph(figure=fig),
#    ]
#)
layout = dbc.Row([column1])
