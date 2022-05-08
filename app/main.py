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

@app.get("/")
async def home():
    return {"msg": "Hello World"}

@app.post("/deposit/{amount}/account/{id}")
async def deposit():
    raise NotImplementedError()

@app.post("/withdrawal/{amount}/account/{id}")
async def withdrawal():
    raise NotImplementedError()

@app.post("/account/statement/{owner_id}")
async def account_statement():
    raise NotImplementedError()

@app.get("/statement/{id}")
async def statement_print():
    raise NotImplementedError()