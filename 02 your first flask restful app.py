from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

# defining our resource (in this case student is a resource )
class Student (Resource):
    def get(self,name): # defining the methods in this case a get method
        return {'student':name} # desiding what method is going to do when endpoint is called

api.add_resource(Student, '/student/<string:name>') #http://127.0.0.1.5000/student/Ram

app.run(port=5000)
