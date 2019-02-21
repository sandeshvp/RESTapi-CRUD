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
        """
        Get method for retrieving particular user details by specifying the name
        """
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        """
        Post method for creating a new user
        """
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name" : name,
            "age" : args["age"],
            "occupation" : args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        """
        Put method is used to update details of the user, or create a new one if it does not exist.
        """
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name" : name,
            "age" : args["age"]
            "occupation" : args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):

if __name__ == '__main__':
    app.run()
