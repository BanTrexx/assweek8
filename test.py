from flask import Flask, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://paaiz:Akusara2020@cluster0.4i3g2d6.mongodb.net/?retryWrites=true&w=majority")
db = client.akusara
my_collections = db.sic

@app.route('/')
def display():
	payload = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
	body = request.get_json{my_collections.find(), params = payload)
	print(r.json())

if __name__ == '__main__':
	app.run(debug==True)