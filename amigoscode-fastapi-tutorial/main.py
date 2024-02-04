from re import L
from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User, UserUpdateRequest

app = FastAPI()

db: List[User] = [
  User(
    id="230d8054-a2df-496d-80f1-bfb39d8c8b8c",
    first_name="Jamila",
    last_name="Ahmed",
    gender=Gender.female,
    roles=[Role.student]
  ),
  User(
    id="f78646d3-bf2b-416d-b888-6b5295e7e1e2",
    first_name="Alex",
    last_name="Jones",
    gender=Gender.male,
    roles=[Role.admin]
  )
]

@app.get("/")
def root():
  return {"Hello" : "Shafie"}


@app.get("/api/v1/users")
async def fetch_users():
  return db

@app.post("/api/v1/users")
async def register_user(user: User):
  # something wrong, 422 unprocessable entity
  db.append(user)
  return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
  for user in db:
    if user.id == user.id:
      db.remove(user)
      return
  raise HTTPException(
    status_code=404,
    detail=f'user with id: {user_id} does not exists'
  )

@app.put ("/api/v1/users/{user_id}")
async def update_user (user_update: UserUpdateRequest, user_id: UUID):
  for user in db:
    if user. id == user_id:
      if user_update. first_name is not None:
        user.first_name = user_update. first_name
      if user_update. last_name is not None:
        user. last_name = user_update. last_name
      if user_update. middle_name is not None:
        user.middle_name = user_update.middle_name
      if user_update. roles is not None:
        user. roles = user_update. roles
    return
  raise HTTPException(
    status_code=404,
    detail=f"user with id: {user_id} does not exists"
  )

    