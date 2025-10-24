from fastapi import FastAPI
from app.routes import auth, expenses, ai
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Expense Tracker")

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(auth.router)
app.include_router(expenses.router)
app.include_router(ai.router)

@app.get("/")
def root():
    return {"message": "AI Expense Tracker API is live 🔥"}
