import json
from app.adapter.CustomerAdapter import CustomerAdapter
from app.domain.customer import Customer
from app.db.mongodb_connector import customer_collection
from app.adapter.serializers import customers_serializer
from starlette.exceptions import HTTPException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/all/customers", tags=["print statement"],)
async def get_all_customers():
    all_customers = customer_collection.find({})
    return customers_serializer(all_customers)

@app.get("/create/customer/lastname={lastname}/firstname={firstname}", tags=["create customer"],)
async def create_customer(lastname: str, firstname: str):

    if isinstance(lastname, str) and isinstance(firstname, str):
        adapter = CustomerAdapter()

        customer = Customer(lastname, firstname, adapter)

        customer = adapter.create_user(customer)
        
        return customer
    else:
        raise HTTPException(status_code=422, detail="Veuillez entrer des chaines de caractères s'il vous plaît")

@app.post("/deposit/{amount}/by/lastname={lastname}/firstname={firstname}", tags=["make deposit"],)
async def deposit(amount: int, lastname: str, firstname: str):
    if isinstance(lastname, str) and isinstance(firstname, str) and isinstance(amount, int):
        adapter = CustomerAdapter()

        customer = Customer(lastname, firstname, adapter)

        account_state = customer.deposit(amount)

        return account_state
    else:
        raise HTTPException(status_code=422, detail="Veuillez entrer un montant de type entier et des prénom et nom de type chaînes de caractères!")
    

@app.post("/withdrawal/{amount}/by/lastname={lastname}/firstname={firstname}", tags=["make withdrawal"],)
async def withdrawal(amount: int, lastname: str, firstname: str):
    if isinstance(lastname, str) and isinstance(firstname, str) and isinstance(amount, int):
        adapter = CustomerAdapter()

        customer = Customer(lastname, firstname, adapter)

        account_state = customer.withdrawal(amount)

        return account_state
    else:
        raise HTTPException(status_code=422, detail="Veuillez entrer un montant de type entier et des prénom et nom de type chaînes de caractères!")

@app.get("/statement/of/lastname={lastname}/firstname={firstname}/account", tags=["print statement"],)
async def statement_print(lastname: str, firstname: str):
    if isinstance(lastname, str) and isinstance(firstname, str):
        adapter = CustomerAdapter()

        customer = Customer(lastname, firstname, adapter)

        account_state = customer.statement_print()
        return account_state
    else:
        raise HTTPException(status_code=422, detail="Veuillez entrer des chaines de caractères s'il vous plaît")

@app.post("/account/statement/for/lastname={lastname}/firstname={firstname}", tags=["make account statement"],)
async def account_statement(lastname: str, firstname: str):
    if isinstance(lastname, str) and isinstance(firstname, str):
        adapter = CustomerAdapter()

        customer = Customer(lastname, firstname, adapter)

        account_state = customer.account_statement()

        return account_state
    else:
        raise HTTPException(status_code=422, detail="Veuillez entrer des chaines de caractères s'il vous plaît")

@app.get("/print/history/account/of={lastname}/firstname={firstname}", tags=["make print history account"],)
async def print_history(lastname: str, firstname: str):
    if isinstance(lastname, str) and isinstance(firstname, str):
        adapter = CustomerAdapter()

        customer = Customer(lastname, firstname, adapter)

        list_operation = customer.print_history()
        return list_operation
    else:
        raise HTTPException(status_code=422, detail="Veuillez entrer des chaines de caractères s'il vous plaît")

