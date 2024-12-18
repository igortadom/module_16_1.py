from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def input() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def welcome() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id(user_id:str) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{user_name}/{age}")
async def user_inf(user_name:str, age: str) -> dict:
    return {"message": f"Информация о пользователе. Имя: {user_name}, Возраст: {age}"}