from dash import Dash, html, dcc 
import plotly.express as px 
import pandas as pd 
import datetime 
from nasa_api import get_neo_object_properties, get_neo_object_value, get_neo_data
from pathlib import Path


def build_datetime(): 
    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=1)
    time = {'today': str(today), 'last_week': str(last_week)}
    return time

path = str(Path.cwd()) + "/api_key.txt" 
with open(path) as f: 
    nasa_api_key = f.read()

app = Dash(__name__) 

neo_data = get_neo_object_properties()

def get_asteroid_names() -> list: 
    neo_data = get_neo_object_properties()
    names = []
    for i in range(len(neo_data)):
        names.append(neo_data[i]["name"])
    return names

def get_hazard_status() -> list: 
    neo_data = get_neo_object_properties()
    hazard = []
    for i in range(len(neo_data)): 
        hazard.append(neo_data[i]['is_potentially_hazardous_asteroid'])
    return hazard 

def get_neo_velocity() -> list: 
    neo_data = get_neo_object_properties()
    velocity = []
    for i in range(len(neo_data)): 
        velocity.append(neo_data[i]['close_approach_data'][0]['relative_velocity']['miles_per_hour'])
    return velocity 


df = pd.DataFrame({
    "Object Name": get_asteroid_names(),
    "Velocity (mph)": get_neo_velocity(),
    "Hazard": get_hazard_status()
})
fig = px.bar(df, x="Object Name", y="Velocity (mph)", color="Hazard", barmode="group")

app.layout = html.Div(children=[
    html.H1(children="Near Earth Objects"), 

    html.Div(children='''
        Currently a dashboard displaying near-earth objects and their relative velocity. 
        Also note, the graphs will indicate if the asteroid is marked as potentially hazardous or not. 
    '''), 

    dcc.Graph(
        id="example-graph", 
        figure=fig
    )
])

if __name__ == '__main__': 
    app.run_server(debug=True)