from app.domain.customer_repository import CustomerRepository
from app.domain.account import Account

class CustomerAdapter(CustomerRepository):

    def withdrawal(self, account: Account, amount: int) -> Account:
        return super().withdrawal(account, amount)
    
    def deposit(self, account: Account, amount: int) -> Account:
        return super().deposit(account, amount)
    
    def account_statement(self, owner_id: str) -> Account:
        return super().account_statement(owner_id)
    
    def statement_print(self, account: Account) -> Account:
        return super().statement_print(account)
    
    def print_history(self, account: Account):
        return super().print_history(account)