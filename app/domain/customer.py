
from app.domain.account import Account
from typing import Optional, TYPE_CHECKING
from dataclasses import dataclass, field
import uuid

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.customer_repository import CustomerRepository

@dataclass
class Customer():
    def __init__(self, lastname, firstname):
        self.id = str(uuid.uuid4())
        self.lastname = lastname
        self.firstname = firstname
    
    def withdrawal(self, account: Account , amount: int) -> Account:
        return CustomerRepository.withdrawal(account, amount)
    
    def deposit(self, account: Account , amount: int) -> Account:
        return CustomerRepository.deposit(account, amount )
    
    def account_statement(self) -> Account:
        return CustomerRepository.account_statement(self.id)
    
    def statement_print(self, account: Account) -> Account:
        return CustomerRepository.statement_print(account)

    def print_history(self, account: Account):
        return CustomerRepository.print_history(account)

    def __hash__(self):
        return hash(self.id)