from fastapi import APIRouter, Depends
from app import models, schemas
from app.database import SessionLocal
from app.core.security import get_current_user

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/")
def create_expense(expense: schemas.ExpenseBase, user=Depends(get_current_user)):
    try:
        db = SessionLocal()
        new_exp = models.Expense(**expense.dict(), user_id=user.id)
        db.add(new_exp)
        db.commit()
        db.refresh(new_exp)
        return new_exp
    except Exception as e:
        print(e)

@router.get("/")
def get_expenses(user=Depends(get_current_user)):
    db = SessionLocal()
    return db.query(models.Expense).filter(models.Expense.user_id == user.id).all()
