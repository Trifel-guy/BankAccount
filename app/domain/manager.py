import abc, six

from app.domain.operation import Operation
from app.domain.account import Account
from typing import List, TYPE_CHECKING

# if TYPE_CHECKING:
#     from app.domain.customer import Customer
    
@six.add_metaclass(abc.ABCMeta)
class ManagerInterface():
    @abc.abstractmethod
    def account_statement(self) -> Account:
        pass
    
    @abc.abstractmethod
    def withdrawal(amount: int, account_id: str) -> Account:
        pass
    
    @abc.abstractmethod
    def deposit( amount: int, account_id: str) -> Account:
        pass
    
    @abc.abstractmethod
    def statement_print( account_id: str) -> Account:
        pass
    
    @abc.abstractmethod
    def print_history(account_id: str) -> List[Operation]:
        pass
    
    