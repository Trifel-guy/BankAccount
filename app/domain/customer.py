
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

    def __init__(self, lastname: str, firstname: str, manager: ManagerInterface):
        self.id = str(uuid.uuid4())
        self.lastname = lastname
        self.firstname = firstname
        self.manager = manager
    
    def account_statement(self) -> Account:
        return self.manager.account_statement(self.id)
    

    def withdrawal(self, amount: int, account_id: str) -> Account:
        return self.manager.withdrawal(self, amount, account_id)
    
    def deposit(self, amount: int, account_id: str) -> Account:
        return self.manager.deposit(self, amount , account_id)
    
    def statement_print(self, account_id: str) -> Account:
        return self.manager.statement_print(self, account_id)

    def print_history(self, account_id: str) -> List[Operation]:
        return self.manager.print_history(self, account_id)
    
    def __hash__(self):
        return hash(self.id)