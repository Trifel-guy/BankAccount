import datetime
from dataclasses import dataclass, field
import uuid
from typing import List
from app.domain.operation import Operation

@dataclass
class Account():
    id: field(default_factory=lambda: str(uuid.uuid4()))
    balance: float
    date: datetime.date
    account_owner: str
    list_operation: List[Operation]
    
    def __init__(self, account_owner):
        self.id = str(uuid.uuid4())
        self.balance = 0.0
        self.date = datetime.date.today()
        self.account_owner = account_owner
        self.list_operation = []

    def __hash__(self):
        return hash(self.id)