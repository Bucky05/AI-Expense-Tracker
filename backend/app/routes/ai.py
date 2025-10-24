from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app import models
from app.services.gemini_service import analyze_expenses
from app.core.security import get_current_user

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/query")
def ai_query(query: dict, user=Depends(get_current_user)):
    db = SessionLocal()
    expenses = db.query(models.Expense).filter(models.Expense.user_id == user.id).all()
    response = analyze_expenses(expenses, query["query"])
    return {"response": response}
