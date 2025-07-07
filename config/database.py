from pymongo import MongoClient
client =MongoClient("mongodb+srv://suryamurikinjeri:987654321@pymongo.w0agsot.mongodb.net/?retryWrites=true&w=majority&appName=PyMongo"
)
db=client.todo_db
coll_name=db["todo_collection"]