from flask import Flask
from flask_restful import Api, Resource, reqparse
from work_db import *


app = Flask(__name__)
api = Api()
parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('vid', type=int)
courses = {
    1: {'name': 'Python', 'vid': 15},
    2: {'name': 'JS', 'vid': 13},
    3: {'name': 'php', 'vid': 150},
}

#Проверка наличия БД, создания при отсутствии
#check_db()

#РАЗОБРАТЬСЯ С ПОЛУЧЕНИЕМ ДАННЫХ ИЗ БД 
#ВРОДЕ ПРОБЛЕМА В ФОРМАТЕ ВЫХОДНЫХ ДАННЫХ
#БД ВЫДАЁТ МАССИВ, А НАДО JSON

class Main(Resource):
    
    def get(self, city_id):
        '''Для получения данных из БД'''
        if city_id == 0:
            return getfulldata()
        else:
            return getdata(city_id)
        

        """if city_id == 0:
            return courses
        elif city_id not in courses:
            return 'Ошибка ввода, введите корректное число'
        else:
            return courses[city_id]"""


    def delete(self, course_id):
        '''Для удаления данных из БД'''
        del courses[course_id]
        return courses

    def post(self, course_id):
        '''Для добавления данных в БД'''
        if course_id in courses:
            return 'Такой id уже присутствует'
        courses[course_id] = parser.parse_args()
        return courses

    def put(self, course_id):
        '''Для изменения данных в БД'''
        courses[course_id] = parser.parse_args()
        return courses

api.add_resource(Main, '/api/courses/<int:city_id>')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=3000)
