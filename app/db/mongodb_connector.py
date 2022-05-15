import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
DATABASE_URL_CONNECTION = os.getenv("DATABASE_URL_CONNECTION")


try:
    client = MongoClient(DATABASE_URL_CONNECTION)
    db = client.bankaccount
    customer_collection = db.customer
    customer_collection.create_index("lastname", unique=True )

    account_collection = db.account

    operation_collection = db.operation
except KeyError:
    client = MongoClient()
    db = client.bankaccount
    customer_collection = db.customer
    customer_collection.create_index("lastname", unique=True)

    account_collection = db.account
    
    operation_collection = db.operation