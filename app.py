from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

users = [
    {
        "name" : "Sandesh",
        "age" : 24,
        "occupation" : "Software Engineer"
    },
    {
        "name" : "Sumit",
        "age" : 25,
        "occupation" : "Wireless Protocol Engineer"
    },
    {
        "name": "Abhilash",
        "age" : 26,
        "occupation" : "Cloud Engineer"
    }
]

class User(Resource):

    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):

    def put(self, name):

    def delete(self, name):

if __name__ == '__main__':
    app.run()
