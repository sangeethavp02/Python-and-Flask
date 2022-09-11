import sys
sys.path.append('C:/Users/SangeethaVP/AppData/Local/Programs/Python/Python37/Lib/site-packages') 

from flask import Flask, jsonify, request
from flask_cors import CORS
from bson.objectid import ObjectId
import pymongo
  
connection_url = "mongodb+srv://sangeethavp02:sangeethavp02@cluster0.bx4sfzh.mongodb.net/?retryWrites=true&w=majority"
app = Flask(__name__)
client = pymongo.MongoClient(connection_url) 
Database = client.get_database('API')
SampleTable = Database.SampleTable
user_collection = pymongo.collection.Collection(Database, 'SampleTable')

@app.route('/insert-one/<name>/<id>/', methods=['GET'])
def insertOne(name, id):
    queryObject = {
        'Name': name,
        'ID': id
    }
    query = SampleTable.insert_one(queryObject)
    return "Query inserted...!!!"

@app.route('/find-one/<argument>/<value>/', methods=['POST'])
def findOne(argument, value):
    queryObject = {argument: value}
    query = SampleTable.find_one(queryObject)
    query.pop('_id')
    return jsonify(query)

@app.route('/find/', methods=['POST'])
def findAll():
    query = SampleTable.find()
    output = {}
    i = 0
    for x in query:
        output[i] = x
        output[i].pop('_id')
        i += 1
    return jsonify(output)
  
@app.route('/update/<key>/<value>/<element>/<updateValue>/', methods=['PUT'])
def update(key, value, element, updateValue):
    queryObject = {key: value}
    updateObject = {element: updateValue}
    query = SampleTable.update_one(queryObject, {'$set': updateObject})
    if query.acknowledged:
        return "Update Successful"
    else:
        return "Update Unsuccessful"

@app.route('/delete/<name>/<id>/', methods=['DELETE'])
def delete(name, id):
    queryObject = {
        'Name': name,
        'ID': id
    }
    query = SampleTable.delete_one(queryObject)
    return "Query deleted...!!!"
  
if __name__ == '__main__':
    app.run(debug=True)

