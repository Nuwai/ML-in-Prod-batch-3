from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str


# Fake storage for demonstration purposes
users = {1: User(name="Alice"), 2: User(name="Bob")}



@app.get("/users")
def get_user():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return users[user_id]



@app.post("/users")
def create_user(user: User):
    user_id = max(users.keys()) + 1 if users else 1
    users[user_id] = user.dict()

    return {"id": user_id, "user": user}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = user.dict()
    return {"id": user_id, "user": user}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    deleted = users.pop(user_id)
    return {"deleted": deleted}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




    