from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27013/")

db = client["db0"]

collection = db["products"]

# products = collection.find()

# for product in products:
#     print(product)
