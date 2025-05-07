from fastapi import FastAPI
from database.userservice import add_user
from database import Base, engine
app = FastAPI(docs_url="/")
# первичная миграция
Base.metadata.create_all(bind=engine)
@app.post("/")
async def login_register(username: str, phone_number: str):
    result = add_user(username, phone_number)
    return {"message": result}
# uvicorn main:app --reload