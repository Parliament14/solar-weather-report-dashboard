from dash import Dash, html, dcc 
import plotly.express as px 
import pandas as pd 
import datetime 
from nasa_api import get_neo_object_properties, get_neo_object_value, get_neo_data, sort_neo_data_by_velocity
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

colors = {
    'background': '#000000',
    'text': '#8C6BBE'

}
neo_data = sort_neo_data_by_velocity()

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

names = get_asteroid_names()
velocity = get_neo_velocity()
hazard = get_hazard_status()
df = pd.DataFrame({
    "Object Name": names,
    "Velocity (mph)": velocity,
    "Hazard": hazard,
})

df = df.sort_values(by=["Velocity (mph)"])
fig1 = px.bar(df, x="Object Name", y="Velocity (mph)", color="Hazard", barmode="group")

fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig2 = px.scatter(
    df, x="Object Name", y="Velocity (mph)", color="Hazard", log_x=True, size_max=60
)
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children="Near Earth Objects", 
        style={
            'textAlign': 'center',
            'background': colors['background'], 
            'color': colors['text']
        }
    ), 

    html.Div(
        children=
            '''
            Currently a dashboard displaying near-earth objects and their relative velocity. 
            Also note, the graphs will indicate if the asteroid is marked as potentially hazardous or not. 
            ''', 
        style={
            'textAlign': 'center', 
            'color': colors['text']
        }
    ), 

    dcc.Graph(
        id="neo-bar-chart", 
        figure=fig1
    ),
    dcc.Graph(
        id="neo-scatter-plot", 
        figure=fig2
    )
])

if __name__ == '__main__': 
    app.run_server(host="127.0.0.1", port="8050", debug=True)