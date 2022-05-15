import datetime
import uuid
from app.domain.customer import Customer
from app.domain.manager import ManagerInterface
from app.domain.account import Account
from app.domain.operation import Operation
from app.adapter.serializers import  single_operation_serializer
from typing import Dict, List
import pymongo
from app.db.mongodb_connector import customer_collection, account_collection
from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_422_UNPROCESSABLE_ENTITY
)


class CustomerAdapter(ManagerInterface):
        
    def create_user(self, customer: Customer) -> Customer:
        try:
            customer_collection.insert_one({"lastname":customer.lastname,"firstname":customer.firstname, "_id": customer.id})
            customer_created = customer_collection.find_one({"lastname": customer.lastname, "firstname":customer.firstname})

            list_operation = []
            operation = {"type":"creation","amount":0, "balance":0}

            list_operation.append(operation)
            account = Account(customer.id)
            account_collection.insert_one({"_id":account.id,"balance": account.balance,"created_at": account.created_at,"account_owner": account.account_owner, "list_operation":list_operation})
            
            # account_created = account_collection.find_one({"account_owner": customer.id})
            return customer_created
        except pymongo.errors.DuplicateKeyError as e:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Utilisateur déjà existant"
            )

    def account_statement(self, customer: Customer) -> Account:
        """
            Déclarer un compte
        """
        exist_customer = customer_collection.find_one({"lastname": customer.lastname, "firstname":customer.firstname})
        if not exist_customer:
            list_operation = []
            operation ={"type":"creation", "amount":0, "balance":0, "time": datetime.datetime.utcnow()}

            list_operation.append(operation)

            customer_collection.insert_one({"lastname":customer.lastname,"firstname":customer.firstname, "_id": customer.id})
            
            account = Account(customer.id)
            account_collection.insert_one({"_id":account.id,"balance": account.balance,"created_at": account.created_at,"account_owner": account.account_owner, "list_operation":list_operation})
            account_created = account_collection.find_one({"account_owner": customer.id})
            return account_created
        else:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="account_statement: Cet utilisateur existe déjà et possède un compte"
            )

    def withdrawal(self,customer: Customer, amount: int) -> Account:
        """
            Faire un retrait
        """
        exist_customer = customer_collection.find_one({"lastname": customer.lastname, "firstname":customer.firstname})
        amount_good = abs(amount)
        if exist_customer:
            
            exist_account = account_collection.find_one({"account_owner": exist_customer["_id"]})
            if exist_account:
                operation = {"type":"withdrawal","amount":amount_good,"balance": exist_account["balance"], "time": datetime.datetime.utcnow()}

                exist_account["list_operation"].append(operation)
                account_collection.update_one({"account_owner": exist_customer["_id"]}, {"$set": {"balance":exist_account["balance"] - amount_good, "list_operation":exist_account["list_operation"] }})
                account_updated = account_collection.find_one({"account_owner": exist_customer["_id"]})
                return account_updated
            else:
               raise HTTPException(status_code=404, detail="withdrawal: Compte inexistant!")
        else:
            raise HTTPException(status_code=404, detail="Withdrawal: Customer inexistant!")
       
    
    def deposit(self,customer: Customer, amount: int) -> Account:
        """
            Faire un dépôt
        """
        amount_good = abs(amount)
        exist_customer = customer_collection.find_one({"lastname": customer.lastname, "firstname":customer.firstname})
        
        if exist_customer:
            exist_account = account_collection.find_one({"account_owner": exist_customer["_id"]})

            if exist_account:
                operation = {"type":"deposit","amount":amount_good, "balance":exist_account["balance"], "time": datetime.datetime.utcnow()}

                exist_account["list_operation"].append(operation)
                account_collection.update_one({"account_owner": exist_customer["_id"]}, {"$set": {"balance":exist_account["balance"] + amount_good, "list_operation":exist_account["list_operation"] }})
                account_updated = account_collection.find_one({"account_owner": exist_customer["_id"]})
                return account_updated
            else:
                raise HTTPException(status_code=404, detail="deposit: Compte inexistant!")
        else:
            raise HTTPException(status_code=404, detail="Deposit: Customer inexistant!")
    
    def statement_print(self,customer: Customer) -> Account:
        """
            Afficher l'état d'un compte
        """
        exist_customer = customer_collection.find_one({"lastname": customer.lastname, "firstname":customer.firstname})
        
        if exist_customer != None:
            exist_account = account_collection.find_one({"account_owner": exist_customer["_id"]})
            if exist_account:
                return exist_account
        else:
            raise HTTPException(status_code=404, detail="statement_print: Customer inexistant!")

    def print_history(self,customer: Customer) -> List[Operation]:
        """
            Afficher l'historique des opération
        """
        exist_customer = customer_collection.find_one({"lastname": customer.lastname, "firstname":customer.firstname})
        
        if exist_customer:
            exist_account = account_collection.find_one({"account_owner": exist_customer["_id"]})
            if exist_account:
                return exist_account["list_operation"]
            else:
                raise HTTPException(status_code=404, detail="print_history: Compte inexistant!")
        else:
            raise HTTPException(status_code=404, detail="print_history: Customer inexistant!")

    
