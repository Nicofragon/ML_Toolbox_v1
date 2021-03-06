import sys
import urllib.parse
import datetime
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    url = BASE_URI + '/api/location/search/?query=' + query
    response = requests.get(url).json()
    if len(response) == 0:
        return None
    if len(response) == 1:
        return response[0]
    for i, city in enumerate(response):
        print(f"{i + 1}. {city['title']}")
    index = int(input("Oops, which one did you mean?")) - 1
    return response[index]


def weather_forecast(woeid):
    url_full_data = BASE_URI + '/api/location/' + str(woeid)
    weather = requests.get(url_full_data).json()

    return weather['consolidated_weather']


def get_weather_in():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    if city is None:
        print(f"Sorry, Metaweather does not know about {query}...")
    else:
        print(f"Here's the weather in {city['title']}")
        weather = weather_forecast(city['woeid'])
        for i in range(len(weather)):
            if weather[i]['applicable_date'] < str(datetime.date.today() +
                                                   datetime.timedelta(days=5)):
                date = weather[i]['applicable_date']
                forecast = weather[i]['weather_state_name']
                max_temp = weather[i]['max_temp']
                print(f"{date}: {forecast} {round(max_temp,1)} °C")


# -------------------


import numpy as np
import pandas as pd
import yfinance as yf


def get_stock(stock, days):
    data = yf.download(tickers=stock, period=days)
    return data


def stock_price():
    stock = input('Stock Name?\n> ')
    period = input('Period in days?\n> ')
    per = str(period) + 'd'

    data = get_stock(stock, per)

    print(data)
