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
                res = requests.get(f"http://127.0.0.1:3000/api/courses/{text}")
                print(res.json())
    elif text == 'delete':
        while True:
                text = input()
                if text == 'qq':
                    break
                res = requests.delete(f"http://127.0.0.1:3000/api/courses/{int(text)}")
                print(res.json())
    elif text == 'post':
        while True:
                id = int(input('Введите id курса:'))
                name = input('Введите имя курса:')
                vid = int(input('Введите кол-во видео в курсе:'))
                if name == 'qq':
                    break
                res = requests.post(f"http://127.0.0.1:3000/api/courses/{id}", json={'name': name, 'vid': vid})
                print(res.json())
    elif text == 'put':
        while True:
                id = int(input('Введите id курса:'))
                name = input('Введите имя курса:')
                vid = int(input('Введите кол-во видео в курсе:'))
                if name == 'qq':
                    break
                res = requests.post(f"http://127.0.0.1:3000/api/courses/{id}", json={'name': name, 'vid': vid})
                print(res.json())

