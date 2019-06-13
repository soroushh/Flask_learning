from flask import Flask
import json

app = Flask(__name__)

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}

# GET /store/<string:name>

# GET /stores

# POST store/<string:name >/item {name:,price:}

# GET store/<string:name> /item/<string name:>


app.run(port=5000)
