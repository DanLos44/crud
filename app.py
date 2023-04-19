from bson import ObjectId
from flask import Flask, render_template, request, redirect, send_from_directory
from pymongo import MongoClient
import os
import logging

app = Flask(__name__)
password = os.environ['MONGO_PASSWORD']
client = MongoClient(f'mongodb+srv://daniellosev95:{password}@cluster0.9w7khno.mongodb.net/test')
db = client['mydatabase']
collection = db['mycollection']
logging.basicConfig(filename='/home/daniel/infinityprojects/CRUD-project/logs/record.log')



@app.route('/')
def index():
    data = list(collection.find())
    app.logger.error("user entered website")
    return render_template('index.html', data=data)



@app.route('/create', methods=['POST'])
def create():
    record = {
        'name': request.form.get('name'),
        'age': request.form.get('age')
    }
    collection.insert_one(record)
    return redirect('/')

@app.route('/update/<id>', methods=['POST'])
def update(id):
    record = {
        'name': request.form.get('name'),
        'age': request.form.get('age')
    }
    collection.update_one({'_id': ObjectId(id)}, {'$set': record})
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    collection.delete_one({'_id': ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
