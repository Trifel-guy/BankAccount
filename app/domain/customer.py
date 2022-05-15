
from app.domain.operation import Operation
from app.domain.account import Account
from typing import List, TYPE_CHECKING
from dataclasses import dataclass, field
import uuid

# if TYPE_CHECKING:
    # This is necessary to prevent circular imports
from app.domain.manager import ManagerInterface

@dataclass
class Customer:
    id: str
    lastname = str
    firstname = str
    def __init__(self, lastname: str, firstname: str, manager: ManagerInterface):
        self.id = str(uuid.uuid4())
        self.lastname = lastname
        self.firstname = firstname
        self.manager = manager
        self.account = None
    
    def account_statement(self) -> Account:
        return self.manager.account_statement(self)
    

    def withdrawal(self, amount: int) -> Account:
        return self.manager.withdrawal(self,amount)
    
    def deposit(self, amount: int) -> Account:
        return self.manager.deposit(self, amount)
    
    def statement_print(self) -> Account:
        return self.manager.statement_print(self)

    def print_history(self, account: Account) -> List[Operation]:
        return self.manager.print_history(self,account)
    
    def __hash__(self):
        return hash(self.id)