#!/usr/bin/python3
from colorama import Fore, Back, Style
import requests
import json 
import urllib3
import pyttsx3
import datetime
from gtts import gTTS
import os 

## Todo: 
#   Build API 
#   Build poller 
#   Integrate voice-command functionality  
#   Speed up request + response time 
#   Figure out a better way to store all this data

nasa_api_key = "xfgp244Iz1GK1Bbk1eG32doMCb9NgafoW0efmNqt"

print(Fore.GREEN + f'NASA API Key: {nasa_api_key}')
print(Style.RESET_ALL)

def build_datetime(): 
    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=7)
    time = {'today': str(today), 'last_week': str(last_week)}
    return time

def get_neo_data(nasa_api_key: str, time: dict) -> dict:
    print(f'Fetching near-earth object data...')
    try: 
        data = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=' + time['last_week'] + '&end_date=' + time['today'] + '&api_key=' + nasa_api_key)
    except ConnectionError: 
        print("Are you connected to the internet, forehead?")
    data = data.json
    print(f'near earth object data retrieved.')
    return data

def get_cme_data(nasa_api_key: str, time: dict) -> dict: 
    print(Fore.RED + "Fetching Coronal Mass Ejection Data...")
    try: 
        data = requests.get('https://api.nasa.gov/DONKI/CME?startDate=' + time['last_week'] + '&endDate=' + time['today'] + '&api_key=' + nasa_api_key)
    except ConnectionError: 
        print(f'ARe you connected to the internet, forehead?') 
    data = data.json
    print(Fore.YELLOW + "Solar Flare data retrieved")
    print(Style.RESET_ALL)
    return data

def get_solar_flare_data(nasa_api_key: str, time: dict) -> dict: 
    print(Fore.RED + "Fetching Solar Flare Data...")
    try: 
        data = requests.get('https://api.nasa.gov/DONKI/FLR?startDate=' + time['last_week'] + '&endDate=' + time['today'] + '&api_key=' + nasa_api_key)
    except ConnectionError: 
        print(f'ARe you connected to the internet, forehead?') 
    data = data.json
    print(Fore.YELLOW + "CME data retrieved")
    print(Style.RESET_ALL)
    return data


def speak_text(text: str): 
    audio = gTTS(text=text, lang="en", slow=False)
    audio.save("speech.mp3") 
    os.system("mpg321 speech.mp3")
    