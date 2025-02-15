from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI()
# @app.get("/welcome/{name}")
# async def welcome(name):
#     return{"Hello " + name + " Welcome to ISDB Saudi Arabia"}


# bank = FastAPI()
# @bank.get("/bank/default")
# async def bankapp():
#     return "ISDB Saudi Arabia"
# @bank.get("/bankaccount/{account_id}/{account_name}")
# async def bankapp(account_id : int, account_name):
#     return "Account ID: " + str(account_id) + ": Account Name: " + account_name


#User data model
class User(BaseModel):
    id:int
    name: str
    email: str
    
#Fake database (in-memory list)
users_db = []

#create new user
@app.post("/users", response_model=User)
def create_user(user: User):
    for u in users_db:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User ID already exists")
        users_db.append(user)
        return user
    
    #Get all users
    @app.get("/users/", response_model=List[User])
    def get_users():
        return users_db
    
    
# Get a user by ID
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Update a user
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db[i] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# Delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(i)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
