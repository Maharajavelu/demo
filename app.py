from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access Database
db = client["testdb"]

# Access Collection
collection = db["users"]

# Insert a Document
user = {"name": {name}, "email": "john.doe@example.com"}
collection.insert_one(user)

# Retrieve and Print Documents
for doc in collection.find():
    print(doc)

# Close the Connection
client.close()
