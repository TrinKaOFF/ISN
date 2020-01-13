from datetime import *
import requests
from newsapi import *

r = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=ab0b9935472a05bf72192f5d3f36cb11&q=Saint-Vaast-la-Hougue&lang=fr")
data=r.json()
t=data['main']['temp']
g = round(t , 2)
w=data['name']
weather=data['weather'][0]['description']
print("La ville est {}".format(w))
print("La témpérature est de {} degrés C°".format(round(g-273.15)))
print(weather)
print("#-------------------------------------------")
heure = datetime.now().time()
print(heure.hour, ':', heure.minute)
print("#-------------------------------------------")
print("Actu du jour")
newsapi = NewsApiClient(api_key='3dc1dd43f9914d8891b0c45875f34882')
data = all_articles = newsapi.get_everything(q='a',
                                      language='fr',
                                      domains='lemonde.fr,',
                                      sort_by='publishedAt',
                                      page=2)
a = 0
for loop in range(20):
    print(a+1, " ", data['articles'][a]['title'])
    print(data['articles'][a]['url'])
    print("#-------------------------------------------")
    a += 1


print("#-------------------------------------------")
p = input("Pour continuer, pressez Entrée ... ")
print("#-------------------------------------------")

