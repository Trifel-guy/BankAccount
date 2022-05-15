from app.domain.customer import Customer
from app.domain.account import Account
from app.adapter.CustomerAdapter import CustomerAdapter
from app.db.mongodb_connector import account_collection, customer_collection
import uuid
import pytest
from starlette.exceptions import HTTPException
import pymongo.errors

def test_create_user_exception():
    """
        test if user already exit and raise exception if he exist in database
    """
    adapter = CustomerAdapter()

    customer = Customer("san","goku", adapter)
    with pytest.raises(HTTPException) as e_info:
        adapter.create_user(customer)
        adapter.create_user(customer)

def test_account_statement():
    """
        test account statement
    """
    adapter = CustomerAdapter()

    customer = Customer("hi","nata", adapter)

    account = Account(customer.id)
    # with pytest.raises(pymongo.errors.DuplicateKeyError) as e_info:
    account2 = customer.account_statement()

    assert account.account_owner == customer.id

def test_withdrawal():
    """
        test withdrawal method
    """
    adapter = CustomerAdapter()

    customer = Customer("na","ruto", adapter)
    customer.account_statement()

    customer.withdrawal(200)
    account = account_collection.find_one({"account_owner":customer.id})

    assert account["balance"] == -200

def test_deposit():
    adapter = CustomerAdapter()

    customer = Customer("ne","ji", adapter)
    customer.account_statement()

    customer.deposit(350)
    account = account_collection.find_one({"account_owner":customer.id})

    assert account["balance"] == 350

def test_statement_print():
    adapter = CustomerAdapter()

    customer = Customer("i","no", adapter)

    account_declared = customer.account_statement()

    account_printed = customer.statement_print()

    assert account_printed["_id"] == account_declared.id
