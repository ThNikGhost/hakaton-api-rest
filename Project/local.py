import requests

while True:
    text = input('Что хотите?')
    if text == 'qq':
        break
    elif text == 'get':
        while True:
                text = input()
                if text == 'qq':
                    break
                res = requests.get(f"http://127.0.0.1:3000/api/city-info/{text}")
                print(res.json())
    elif text == 'delete':
        while True:
                text = input()
                if text == 'qq':
                    break
                res = requests.delete(f"http://127.0.0.1:3000/api/city-info/{text}")
                print(res.json())
    elif text == 'post':
        while True:
                id = input('Введите id города:')
                name = input('Введите название города:')
                if name == 'qq':
                    break
                res = requests.post(f"http://127.0.0.1:3000/api/city-info/{id}", json={'name': name, 'id': id})
                print(res.json())
    elif text == 'put':
        while True:
                id = input('Введите id города, который вы хотите изменить:')
                name = input('Введите новое название города:')
                if name == 'qq':
                    break
                res = requests.put(f"http://127.0.0.1:3000/api/city-info/{id}", json={'name': name, 'id': id})
                print(res.json())

