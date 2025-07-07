from fastapi import FastAPI
from pymongo import MongoClient
from routes.route import router
app=FastAPI()

app.include_router(router)

