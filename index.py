from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)

# Configura la conexión a MongoDB
client = MongoClient('mongodb://nico:password@monguito:27017/miapp?authSource=admin')
db = client.miapp
animal_collection = db.animales

# Endpoint para listar animales
@app.route('/', methods=['GET'])
async def list_animals():
    print('listando... chanchitos...')
    animals = animal_collection.find()
    return dumps(animals), 200

# Endpoint para crear un nuevo animal
@app.route('/crear', methods=['GET'])
async def create_animal():
    print('creando...')
    animal_collection.insert_one({ 'tipo': 'Chanchito', 'estado': 'Feliz' })
    return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
