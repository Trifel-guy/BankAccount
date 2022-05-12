from app.domain.manager import ManagerInterface
from app.domain.account import Account
from app.domain.operation import Operation
from typing import List

class CustomerAdapter(ManagerInterface):
    def account_statement(self, owner_id: str) -> Account:
        raise NotImplementedError()
    
    def withdrawal(self, amount: int, account_id: str) -> Account:
        raise NotImplementedError()
    
    def deposit(self, amount: int, account_id: str) -> Account:
        raise NotImplementedError()
    
    def statement_print(self, account_id: str) -> Account:
        raise NotImplementedError()

    def print_history(self, account_id: str) -> List[Operation]:
        raise NotImplementedError()
    
