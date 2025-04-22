# -*- coding: utf-8 -*-


#Current weather in Poznań (API). The program uses OpenWeather API to 
#gather information about the temperature in a given city expressed 
#in degrees Celsius


import requests, json
ApiKey_current = '9d3bd1708e400127c779ca11909c210c'
BaseURL_current = 'https://api.openweathermap.org/data/2.5/weather?q='

CityName = input('Enter Your city name. If the city is in Poland write its'
                ' name in Polish: ')

CompleteURL_current = (BaseURL_current + CityName + '&appid=' + 
                      ApiKey_current + '&units=metric')
response_current = requests.get(CompleteURL_current)
data_current = response_current.json()
print(data_current['main']['temp'])


# %%


#Scraping new recepies. The program scrapes all new recepies being on display
#of "https://www.kwestiasmaku.com/" website and repeating the process every 24
#hours. Recepies are being stored in seperate txt file along with the date
#of their apperance in the file.


def find_recepies():
    print('Function will append all recepies from front page every '
          '24 hours\n\n')
    from bs4 import BeautifulSoup
    import requests
    import datetime
    import time
    url = 'https://www.kwestiasmaku.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')
    
    texts_all = (soup.find_all('a'))
    texts = [t.text for t in texts_all]
    indices = [i for i, x in enumerate(texts) if x == "ZAPISZ"]
    
    new_recepies = []
    a = 0
    while a < 1:
        for i in indices:
            new_recepies.append(texts[i - 1])
        print(new_recepies)
        with open('recepies.txt', 'a') as file:
            for recepie in new_recepies:
                date_now = str(datetime.datetime.now())
                print (recepie + ', ' + date_now[0:10], file=file)
        print('\n\nFunction will now wait 24 hours before appending recepies '
              'from front page\n\n')
        time.sleep(86400)
        print('It has been 24 hours since last appending. '
              'New data will appear.\n\n')

find_recepies()
