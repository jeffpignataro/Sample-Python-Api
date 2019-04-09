from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017')
db = client.sampleDb
sampleCollection = db.sampleCollection

sampleCollection.insert_one({"hello": "world"})
helloworld = sampleCollection.find({"hello": "world"})

for item in helloworld:
    print(item.hello)


for item in sampleCollection.find():
    print(item)


def getDataFromMongo(key, value):
    return sampleCollection.find({key: value})


def getData():
    with open('./Data/tasks.json', "r") as jsonFile:
        data = json.load(jsonFile)
        return data


sampleCollection.insert_many(getData())

dataFromMongo = getDataFromMongo("title", "Learn Python")
print((dataFromMongo[0])["title"])
