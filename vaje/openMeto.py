
import requests

#izpiši trenutno temperaturo za poljubni kraj
https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&current=temperature_2m

def temperatura_temp(lat, lon):
    base_url = f""
    call = requests,get(base_url).json()
    print(call["current"]["temperature_2m"])

trenutna_temp(45.12, 14.5)
