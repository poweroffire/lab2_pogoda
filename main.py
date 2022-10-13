# Вывести в текущем и недельном прогнозе скорость ветра и видимость.
import requests
city = "Moscow,RU"
appid = "9808dc4bcd301e2b8e47a60e96618aa4"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print(f'Скорость ветра: {data["wind"]["speed"]}.')
print(f'Видимость: {data["visibility"]}')


res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Данные о скорости ветра и видимости на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nСкорость ветра <",(i['wind']['speed']), "> \r\nВидимость <", i['visibility'], ">")
    print("*****************************")