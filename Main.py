from fastapi import FastAPI
app = FastAPI()
@app.get("/welcome/{name}")
async def welcome(name):
    return{"Hello " + name + " Welcome to ISDB Saudi Arabia"}


bank = FastAPI()
@bank.get("/bank/default")
async def bankapp():
    return "ISDB Saudi Arabia"
@bank.get("/bankaccount/{account_id}/{account_name}")
async def bankapp(account_id : int, account_name):
    return "Account ID: " + str(account_id) + ": Account Name: " + account_name