import datetime
from dataclasses import dataclass
import uuid

@dataclass
class Operation():
    
    def __init__(self, type, amount, balance):
        self.id = str(uuid.uuid4())
        self.type = type
        self.created_at = datetime.date.today()
        self.amount = amount
        self.balance = balance

    def __hash__(self):
        return hash(self.id)