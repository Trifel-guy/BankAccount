from app.domain.customer import Customer
from app.domain.account import Account
from app.adapter.CustomerAdapter import CustomerAdapter
import uuid

def test_account_existing_owner_id():
    owner_id = str(uuid.uuid4())

    assert Account(owner_id).account_owner == owner_id


def test_account_defaults():
    adapter = CustomerAdapter()

    customer = Customer("guy","trifel", adapter)
    assert uuid.UUID(Account(customer.id).id)

def test_customer_defaults():
    adapter = CustomerAdapter()
    assert uuid.UUID(Customer("guy","trifel", adapter).id)