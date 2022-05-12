import abc, six
from app.domain.operation import Operation
from app.domain.account import Account
from typing import List

@six.add_metaclass(abc.ABCMeta)
class ManagerInterface():

    @abc.abstractmethod
    def account_statement(self, owner_id: str) -> Account:
        pass
    
    @abc.abstractmethod
    def withdrawal(self, amount: int, account_id: str) -> Account:
        pass
    
    @abc.abstractmethod
    def deposit(self, amount: int, account_id: str) -> Account:
        pass
    
    @abc.abstractmethod
    def statement_print(self, account_id: str) -> Account:
        pass
    
    @abc.abstractmethod
    def print_history(self, account_id: str) -> List[Operation]:
        pass
    
    