from flask import Flask, jsonify, request
import json

app = Flask(__name__)

stores = [
{ 'name':'My favorite store',
  'items':[
    {'name':'The book', 'price':15.99}
]
}
]

people = []



# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
       'name':request_data['name'],
       'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def show_store(name):
    for store in stores:
        if store['name'] == name :
            return jsonify(store)
    return(jsonify({'message':'store not found'}))
# GET /stores
@app.route('/store')
def get_stores():
    return(jsonify({'stores':stores}))

# POST store/<string:name >/item {name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    request_data = request.get_json()
    new_item ={
    "name":request_data["name"],
    "price":request_data["price"]
    }
    for store in stores:
        if store["name"] == name:
            store["items"].append(new_item)
            return(jsonify(store))
    return(jsonify({'message':'store not found'}))
# GET store/<string:name> /item/<string:item_name>
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return(jsonify({'items':store['items']}))
    return(jsonify({'message':'store not found'}))

#POST method to make a new person
@app.route('/person/new', methods=['POST'])
def create_person():
    request_data = request.get_json()
    new_person = {

      "name": request_data["name"],
      "family" : request_data["family"]
    }
    people.append(new_person)
    return(jsonify({"people":people}))
@app.route('/person')
def find_person():
    name = request.args.get('name')
    family = request.args.get('family')
    for person in people:
        if person["name"]== name and person["family"]== family:
            return(jsonify({"name":name, "family":family}))
    return(jsonify({"message":"person not found"}))
    
app.run(port=5000)
