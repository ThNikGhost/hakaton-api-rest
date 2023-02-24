from flask import Flask
from flask_restful import Api, Resource, reqparse
from work_db import *
import sqlite3 as sq

app = Flask(__name__)
api = Api()
parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('id', type=int)
courses = {
    1: {'name': 'Python', 'vid': 15},
    2: {'name': 'JS', 'vid': 13},
    3: {'name': 'php', 'vid': 150},
}

#Проверка наличия БД, создания при отсутствии
check_db()




#РАЗОБРАТЬСЯ С ПОЛУЧЕНИЕМ ДАННЫХ ИЗ БД 
#ВРОДЕ ПРОБЛЕМА В ФОРМАТЕ ВЫХОДНЫХ ДАННЫХ
#БД ВЫДАЁТ МАССИВ, А НАДО JSON

class Main(Resource):
    
    """    def get(self, city_id):
        '''Для получения данных из БД'''
        if city_id == 0:
            return getfulldata()
        else:
            return getdata(city_id)"""
    
    @app.route('/')
    def get(self, city_id):

        def check_data_in_db(city_id):
            with sq.connect('db.sqlite3') as con:
                cur = con.cursor()
                cur.execute('''SELECT city_id, city_name
                            FROM Cities
                            ''')
                data = cur.fetchall()
            for i in data:
                if city_id in i:
                    return True
            return False
        if city_id == 0:
            sql_get = 'SELECT city_id, city_name FROM Cities'
            
        # Проверка наличия city_id в БД
        elif check_data_in_db(city_id) == False:
            return 'Данного объекта нет в БД'

        else:
            sql_get = f'SELECT city_id, city_name FROM Cities WHERE city_id = {city_id}'
        with sq.connect("db.sqlite3") as con:
            cur = con.cursor()
            cur.execute(f'{sql_get}')
            data = cur.fetchall()
        return data

    def delete(self, city_id):
        '''Для удаления данных из БД'''
        if city_id == 0:
            sql_get = (f'''DELETE FROM Cities''')

        elif str(city_id).isnumeric() == False:
            city_name = city_id
            sql_get = (f'''DELETE FROM Cities
            WHERE city_name = '{city_name}';
            ''')
        elif str(city_id).isnumeric() == True:
            sql_get = (f'''DELETE FROM Cities
            WHERE city_id = '{city_id}' 
            ''')
        with sq.connect("db.sqlite3") as con:
            cur = con.cursor()
            cur.execute(f'{sql_get}')
            cur.execute('''SELECT city_id, city_name
                        FROM Cities
                        ''')
            data = cur.fetchall()
        return data

    def post(self, city_id):
        '''Для добавления данных в БД'''
        data_json = (parser.parse_args())

        with sq.connect("db.sqlite3") as con:
            cur = con.cursor()
            cur.execute('SELECT city_id, city_name FROM Cities')
            data = cur.fetchall()
            for i in data:
                if (data_json['id'] in i) or (data_json['name'] in i[1]):
                    return "Такой объект уже существует"

            cur.execute(f"""INSERT INTO Cities (
                       city_id,
                       city_name
                   )
                   VALUES (
                       '{data_json['id']}',
                       '{data_json['name']}'
                   );
                        """)
            con.commit()
            cur.execute('SELECT city_id, city_name FROM Cities')
            return cur.fetchall()

    def put(self, city_id):
        '''Для изменения данных в БД'''
        data_json = (parser.parse_args())

        with sq.connect("db.sqlite3") as con:
            cur = con.cursor()
            cur.execute('SELECT city_id FROM Cities')
            data = cur.fetchall()
            for i in data:
                if (data_json['id'] in i):
                    try:
                        cur.execute(f"""UPDATE Cities
                        SET city_name = '{data_json['name']}'
                        WHERE city_id = '{data_json['id']}'
                        """)
                    except IndentationError:
                        return 'Такой город уже существует'

                    con.commit()
                    cur.execute('SELECT city_id, city_name FROM Cities')
                    return cur.fetchall()
            return 'Такого объекта нет!'
            

api.add_resource(Main, '/api/city-info/<int:city_id>')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=3000)
