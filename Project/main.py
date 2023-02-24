from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()

some_dict = {
    'name': 'Omsk',
    'clouds': 56,
    'temp': 0.97,
}

class Main(Resource):

    def get(self):
        return some_dict


api.add_resource(Main, '/api/main')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=3000)
