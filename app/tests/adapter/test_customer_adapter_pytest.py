from app.adapter.customer_adapter import CustomerAdapter
from app.domain.customer import Customer
from app.domain.account import Account


def test_withdrawal():
    customer = Customer("guy","trifel")
    customer_repository = CustomerAdapter()
    account = Account(customer.id)

    customer_repository.withdrawal(account, 200)
    assert account.balance == -200

def test_deposit():
    customer = Customer("guy","trifel")
    customer_repository = CustomerAdapter()
    account = Account(customer.id)

    customer_repository.deposit(account, 350)
    assert account.balance == 350

def test_account_statement():
    customer = Customer("guy","trifel")
    customer_repository = CustomerAdapter()
    account = Account(customer.id)

    customer_repository.account_statement(customer.id)

    assert account.account_owner == customer.id

def test_statement_print():
    customer = Customer("guy","trifel")
    customer_repository = CustomerAdapter()
    account = Account(customer.id)

    account_printed = customer_repository.statement_print(account)

    assert account.account_owner == account_printed.account_owner