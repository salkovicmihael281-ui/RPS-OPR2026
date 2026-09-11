import requests


def povprecna_temp_7dni(lat, lon):
    # vstavim lon in lat v link in ne direktne podatke za lažjo kasnejšo obdelavo
    base_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_mean'

    # pridobimo podatke v json formatu
    call = requests.get(base_url).json()

    #klici spremenjlivke
    dni = call['daily']['time']
    temp = call['daily']['temperature_2m_mean']

    #koda
    for i in range(len(dni)):
        print(dni[i], temp[i], '°C')


povprecna_temp_7dni(46.0833, 15)