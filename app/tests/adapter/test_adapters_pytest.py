from app.domain.customer import Customer
from app.domain.account import Account
from app.adapter.CustomerAdapter import CustomerAdapter
import uuid
import pytest
from starlette.exceptions import HTTPException

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
    adapter = CustomerAdapter()

    customer = Customer("vege","ta", adapter)

    account = Account(customer.id)

    account2 = customer.account_statement()

    assert account.account_owner == account2.account_owner

def test_withdrawal():
    adapter = CustomerAdapter()

    customer = Customer("yaya","yiyi", adapter)

    account = Account(customer.id)

    customer.withdrawal(200, account.id)

    assert account.balance == -200

def test_deposit():
    adapter = CustomerAdapter()

    customer = Customer("toto","tata", adapter)

    account = Account(customer.id)

    customer.deposit(350, account.id)

    assert account.balance == 350

def test_statement_print():
    adapter = CustomerAdapter()

    customer = Customer("guy","trifel", adapter)

    account = Account(customer.id)

    account_printed = customer.statement_print(account.id)

    assert account.account_owner == account_printed.account_owner

# def test_database_():
#     conn = get_mysql_database()
#     try:
#         with conn.cursor() as cur:

#             cur.execute('SELECT VERSION()')

#             version = cur.fetchone()
#             assert version != None
#             # print(f'Database version: {version[0]}')
#     finally:
#         conn.close()
