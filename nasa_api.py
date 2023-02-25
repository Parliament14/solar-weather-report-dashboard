#!/usr/bin/python3
from colorama import Fore, Back, Style
import requests
import json 
import datetime
import os 
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path 
import logging 


## Todo: 
#   Build API key gen
#   Build poller 
#   Integrate voice-command functionality  // possibly // maybe jsut dashboard
#   Speed up request + response time 
#   Figure out a better way to store all this data
#   See if you can obfuscate the requests to nasa into a single function. Then you need to pass just the endpoint, time, and api key (See NTB) 

# Globals 
path = str(Path.cwd()) + "/api_key.txt" 
with open(path) as f: 
    nasa_api_key = f.read()
logging.basicConfig(filename="nasa_api.log", level=logging.CRITICAL)
logging.info("Started")
    
    
def build_datetime(): 
    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=1)
    time = {'today': str(today), 'last_week': str(last_week)}
    return time

def send_nasa_request(nasa_api_key: str, endpoint: str): 
    time = build_datetime()
    if endpoint == 'neo': 
        try: 
            data = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=' + time['last_week'] + '&end_date=' + time['today'] + '&api_key=' + nasa_api_key)
        except ConnectionError: 
            print("Are you connected to the internet, forehead?")
    elif endpoint == 'cme': 
        try: 
            data = requests.get('https://api.nasa.gov/DONKI/CME?startDate=' + time['last_week'] + '&endDate=' + time['today'] + '&api_key=' + nasa_api_key)
        except ConnectionError: 
            print("Are you connected to the internet, forehead?")
    elif endpoint == 'flr': 
        try: 
            data = requests.get('https://api.nasa.gov/DONKI/FLR?startDate=' + time['last_week'] + '&endDate=' + time['today'] + '&api_key=' + nasa_api_key)
        except ConnectionError: 
            print("Are you connected to the internet, forehead?")
    elif endpoint == 'gst': 
        try: 
            data = requests.get("https://api.nasa.gov/DONKI/GST?startDate=" + time['last_week'] + '&endDate=' + time['today'] + '&api_key=' + nasa_api_key)
        except ConnectionError:
            print("Are you connected to the internet, forehead?")
    elif endpoint == 'ips': 
        try: 
            data = requests.get("https://api.nasa.gov/DONKI/IPS?startDate=" + time['last_week'] + "&endDate=" + time['today'] + "&api_key=" + nasa_api_key)
        except ConnectionError: 
                print("Are you connected to the internet, forehead?")
    data = data.json()
    return data 

def get_neo_data(nasa_api_key: str) -> dict:
    logging.info(f'Fetching near-earth object data...')
    print("test")
    data = send_nasa_request(endpoint="neo", nasa_api_key=nasa_api_key)
    logging.info(f'near earth object data retrieved.')
    return data

def get_cme_data(nasa_api_key: str, time: dict) -> dict: 
    logging.info(Fore.RED + "Fetching Coronal Mass Ejection Data...")
    data = send_nasa_request(endpoint="cme", nasa_api_key=nasa_api_key)
    logging.info(Fore.YELLOW + "Solar Flare data retrieved")
    logging.info(Style.RESET_ALL)
    return data

def get_solar_flare_data(nasa_api_key: str, time: dict) -> dict: 
    logging.info(Fore.RED + "Fetching Solar Flare Data...")
    data = send_nasa_request(endpoint='flr', nasa_api_key=nasa_api_key)
    logging.info(Fore.YELLOW + "CME data retrieved")
    logging.info(Style.RESET_ALL)
    return data
    
def get_nasa_api_key() -> dict: 
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://api.nasa.gov/")
    firstname_element = browser.find_element(By.NAME, "user_first_name")
    firstname_element.clear()
    firstname_element.send_keys("testing dashboard")
    firstname_element.send_keys(Keys.RETURN)
    browser.close()

def get_neo_object_value(time: dict, neo_data: dict) -> list: 
    values = []
    for item in time.values():
        for i in range(len(neo_data['near_earth_objects'][item])):
            result = neo_data['near_earth_objects'][item][i]
            values.append(result)
    return values
        
def get_neo_object_properties() -> dict:
    '''
    This function will fetch neo data and return a formatted, 
    enumerated dictionary. The keys (starting at 0) represent the 
    number of near-earth objects and the values can be accessed
    by the subequent key detailed on NASA's API documentation. 
    
    ex. 
    
    >>> objects = get_neo_object_properties()
    >>> objects.keys()
    dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])
    >>> objects[0]["name"]
    '37638 (1993 VB)'
    '''
    neo_data = get_neo_data(nasa_api_key=nasa_api_key)
    data = get_neo_object_value(neo_data=neo_data, time=build_datetime())
    objects = dict(list(enumerate(data)))
    return objects