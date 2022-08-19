import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://paaiz:Akusara2020@cluster0.4i3g2d6.mongodb.net/?retryWrites=true&w=majority")
db = client.sicassweek8
my_collections = db.assweek8

speed1 = {
    "kecepatan": 90,
    "latitude": 6.2088,
    "longitude": 106.8456
}
speed2 = {
    "kecpatan": 60,
    "latitude": -6.193125,
    "longitude": 106.821810
}

results = my_collections.insert_many([speed1,speed2])
print(results.inserted_ids)