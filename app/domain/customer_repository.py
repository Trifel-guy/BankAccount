import abc, six
from app.domain.account import Account

@six.add_metaclass(abc.ABCMeta)
class CustomerRepository():
    @abc.abstractmethod
    def withdrawal(self, account: Account, amount: int) -> Account:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def deposit(self, account: Account , amount: int) -> Account:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def account_statement(self, owner_id: str) -> Account:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def statement_print(self, account: Account) -> Account:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def print_history(self, account: Account):
        raise NotImplementedError()