from flask import Flask
from flask_restful import Api, Resource
from flask import render_template
import requests

app = Flask(__name__)
api = Api()
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=3fd71f50684a58f9c310b7a4e5df243f'

class Main(Resource):
    def get(self, city):
        res = requests.get(url.format(city)).json()
        try:
            city_info = {
                'city': res['name'],                       # Название города 
                'temp': res['main']['temp'],               # Температура в городе
                'temp_feels': res['main']['feels_like'],   # Температура по ощущениям
                'wind_speed': res['wind']['speed'],        # Скорость ветра (вроде м/c)
            }
        except KeyError:
            return 'Incorect name'    #Если неверное имя города, то возвращает эту строку 
        return city_info

@app.route('/')
def index():
    return render_template('index.html')



api.add_resource(Main, '/api/main/<string:city>')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=3000)