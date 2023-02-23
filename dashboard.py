import dash 
from dash import dcc
from dash import html
import plotly.express as px 
import pandas as pd 
import numpy as np 
from nasa_utils.nasa_api import get_neo_data

# Globals 
nasa_api_key = "xfgp244Iz1GK1Bbk1eG32doMCb9NgafoW0efmNqt" ## Please don't abuse me :) 

def build_datetime(): 
    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=1)
    time = {'today': str(today), 'last_week': str(last_week)}
    return time


app = dash.Dash()
time = build_datetime() 
data = pd.read_json(get_neo_data(nasa_api_key,time))

fig = px.scatter(
    data, 
    x="x axis",
    y="y axis",
    size="size",
    color="color", 
    hover_name="hover_name",
    log_x=True,
    size_max=100,
)




app.layout = html.Div([dcc.Graph(id="graph_id", figure=fig)])

