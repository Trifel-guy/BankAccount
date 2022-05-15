from app.domain.customer import Customer
from app.domain.account import Account
from app.adapter.CustomerAdapter import CustomerAdapter
from app.db.mongodb_connector import account_collection
from app.main import app
import pytest
from starlette.exceptions import HTTPException
import pymongo.errors
from fastapi.testclient import TestClient

def test_create_user_exception():
    """
        test if user already exit and raise exception if he exist in database
    """
    adapter = CustomerAdapter()

    customer = Customer("so","prano", adapter)
    with pytest.raises(HTTPException) as e_info:
        adapter.create_user(customer)
        adapter.create_user(customer)

def test_account_statement():
    """
        test account statement
    """
    adapter = CustomerAdapter()

    customer = Customer("li","no", adapter)

    account = Account(customer.id)
    # with pytest.raises(pymongo.errors.DuplicateKeyError) as e_info:
    account2 = customer.account_statement()

    assert account.account_owner == customer.id

def test_withdrawal():
    """
        test withdrawal method
    """
    adapter = CustomerAdapter()

    customer = Customer("ninho","maness", adapter)
    customer.account_statement()

    customer.withdrawal(200)
    account = account_collection.find_one({"account_owner":customer.id})

    assert account["balance"] == -200

def test_deposit():
    adapter = CustomerAdapter()

    customer = Customer("cabrel","musique", adapter)
    customer.account_statement()

    customer.deposit(350)
    account = account_collection.find_one({"account_owner":customer.id})

    assert account["balance"] == 350

def test_statement_print():
    adapter = CustomerAdapter()

    customer = Customer("fu","tur", adapter)

    account_declared = customer.account_statement()

    account_printed = customer.statement_print()

    assert account_printed["_id"] == account_declared["_id"]

client = TestClient(app)


def test_get_allcustomers():
    response = client.get("/all/customers")
    assert response.status_code == 200