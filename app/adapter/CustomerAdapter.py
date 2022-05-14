from app.domain.customer import Customer
from app.domain.manager import ManagerInterface
from app.domain.account import Account
from app.domain.operation import Operation
from app.adapter.serializers import single_customer_serializer
from typing import Dict, List
import pymongo
from app.db.mongodb_connector import customer_collection, account_collection
from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_404_NOT_FOUND,
)
import json
from bson import ObjectId


class CustomerAdapter(ManagerInterface):
        
    def create_user(self, customer: Customer) -> Customer:
        try:
            customer_collection.insert_one({"lastname":customer.lastname,"firstname":customer.firstname, "_id": customer.id})
            return customer
        except pymongo.errors.DuplicateKeyError as e:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Utilisateur déjà existant"
            )
            
    def account_statement(self, customer: Customer) -> Account:
        exist_customer = customer_collection.find_one({"_id": customer.id})

        if exist_customer == None:
            customer_collection.insert_one({"lastname":customer.lastname,"firstname":customer.firstname, "_id": customer.id})
            account = Account(customer.id)
            account_collection.insert_one({"_id":account.id,"balance": account.balance,"created_at": account.created_at,"account_owner": account.account_owner})
            return account
        else:
            account = Account(customer.id)
            account_collection.insert_one({"_id":account.id,"balance": account.balance,"created_at": account.created_at,"account_owner": account.account_owner})
            return account

    def withdrawal(amount: int, account_id: str) -> Account:
        raise NotImplementedError()
    
    def deposit(amount: int, account_id: str) -> Account:
        raise NotImplementedError()
    
    def statement_print(account_id: str) -> Account:
        raise NotImplementedError()

    def print_history(account_id: str) -> List[Operation]:
        raise NotImplementedError()
    
