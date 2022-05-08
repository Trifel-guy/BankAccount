from app.domain.customer import Customer
from app.domain.account import Account
import uuid

def test_account_existing_owner_id():
    owner_id = str(uuid.uuid4())

    assert Account(owner_id).account_owner == owner_id


def test_account_defaults():
    customer = Customer("guy","trifel")
    assert uuid.UUID(Account(customer.id).id)

def test_customer_defaults():
    assert uuid.UUID(Customer("guy","trifel").id)