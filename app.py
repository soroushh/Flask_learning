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
    pass
# GET store/<string:name> /item/<string:item_name>
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return(jsonify({'items':store['items']}))
    return(jsonify({'message':'store not found'}))

app.run(port=5000)
