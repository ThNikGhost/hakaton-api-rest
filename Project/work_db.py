import sqlite3
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

def check_db():
    sql('''SELECT name 
    FROM sqlite_master 
    WHERE type='table'
    ''')
    table = cursor.fetchall()
    if 'Cities' not in table:
        create_base_table()

def check_data_in(num):
    data = getfulldata()
    for i in data:
        print(i)
        if num in i:
            return True
    return False

def create_base_table():
    sql('''
    CREATE TABLE Cities( 
    city_id INTEGER UNIQUE, 
    city_name TEXT UNIQUE
    )''')

# Упрощаю ввод SQL запросов и при ошибке, выводит введённый запрос
def sql(text: str):
    try:
        cursor.execute(text)
    except:
        print(text)

# Получает данные из введённой таблицы
# Делает получение инфы легче
def getdata(num):
    sql(f'''SELECT city_id, city_name 
    FROM Cities
    WHERE city_id = {num}
    ''')
    return cursor.fetchall()

def getfulldata():
    sql('''SELECT city_id, city_name
    FROM Cities
    ''')
    return cursor.fetchall()

# Преобразует полученные данные в массив для удобства
def get_list_db(name: str, sort: bool = False):
    data = getdata(name)
    new_list = []
    if sort == True:
        data = sorted(data)
    for i in data:
        for k in i:
            new_list.append(k)
    return new_list

# Закрывает конект БД
def Close():
    conn.close()
