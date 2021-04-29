# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Imports from this application
from app import app
from joblib import load
pipeline = load('assets/pipeline.joblib')



# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Choose the parameter for your favorite video game

            """
        ),
        dcc.Markdown('', id='prediction_content')
    ],  
)

platform_list = ['PC', 'PSP', 'Wii', 'DS', '3DS', 'PS3', 'PSV', 'X360', 'PS2', 'WiiU', 'PS4', 'XOne'] 
genre_list = ['Strategy', 'Action', 'Fighting', 'Shooter', 'Simulation', 'Misc', 'Sports', 'Adventure', 'Platform', 'Role-Playing', 'Racing', 'Puzzle']
publisher_list = ['Other', 'Konami Digital Entertainment', 'Namco Bandai Games', 'Square Enix', 'THQ', 'Sony Computer Entertainment', 'Sega', 'Electronic Arts', 'Warner Bros. Interactive Entertainment', 'Take-Two Interactive', '505 Games', 'Ubisoft', 'Disney Interactive Studios', 'Activision', 'Tecmo Koei', 'Capcom', 'Nintendo', 'Atari', 'Microsoft Game Studios']

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
            
            #### platform
            
            """),
        dcc.Dropdown(
            id='platform',
            options=[
                {'label': i, 'value': i} for i in platform_list
            ],
            value='PC',
            className='mb-4'
        ),
        dcc.Markdown(
            '''
            
            #### genre
             
            '''),
        dcc.Dropdown(
            id='genre',
            options=[
                {'label': i, 'value': i} for i in genre_list
            ],
            value='Strategy',
            className='mb-4'
        ),
        dcc.Markdown(
            '''

            #### publisher

            '''
        ),
        dcc.Dropdown(
            id='publisher',
            options=[
                {'label': i, 'value': i} for i in publisher_list
            ],
            value='Konami Digital Entertainment',
            className='mb-4'
        )
    ]
)
# @app.callback(
#     Output(component_id='my-platform', component_property='children'),
#     [Input(component_id='platform',component_property='value')]
# )
# def update_platform_div(input_value):
#     return 'The platform is {}'.format(input_value)

# @app.callback(
#     Output(component_id='my-genre', component_property='children'),
#     [Input(component_id='genre', component_property='value')]
# )
# def update_platform_div(input_value):
#     return 'The genre is {}'.format(input_value)

# @app.callback(
#     Output(component_id='my-publisher', component_property='children'),
#     [Input(component_id='publisher', component_property='value')]
# )
# def update_platform_div(input_value):
#     return 'The publisher is {}'.format(input_value)

@app.callback(
     Output('prediction_content', 'children'),
     [Input('platform', 'value'),
      Input('genre', 'value'),
      Input('publisher', 'value')]
)   
def predict(platform, genre, publisher):
    df = pd.DataFrame(
        columns=['Platform', 'Genre', 'Publisher'],
        data=[[platform, genre, publisher]]
    )
    y_pred = pipeline.predict(df)[0]
    return 'The Video Game Sales Prediction {} millions'.format(round(y_pred,6))

layout = dbc.Row([column1, column2])
