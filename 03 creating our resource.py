from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

items = []

# defining our resource 
class Item (Resource):
    def get(self,name):
        for item in items:
            if item['name'] == name:
                return name
        return {'items': None }, 404

    def post(self,name):
        item = {'name': name, 'price': 12.50}
        items.append(item) 
        return item, 201

api.add_resource(Item, '/item/<string:name>')

app.run(port=5000)
