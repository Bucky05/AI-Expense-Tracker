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


@router.put("/{expense_id}")
def update_expense(expense_id: str, expense: schemas.ExpenseBase):
    try:
        db = SessionLocal()
        db_exp = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
        if not db_exp:
            return {"error": "Expense not found"}
        for key, value in expense.dict().items():
            setattr(db_exp, key, value)
        db.commit()
        db.refresh(db_exp)
        return db_exp   
    except Exception as e:
        print(e)


@router.delete("/{expense_id}")
def delete_expense(expense_id: str, user=Depends(get_current_user)):
    db = SessionLocal()
    db_exp = db.query(models.Expense).filter(models.Expense.id == expense_id, models.Expense.user_id == user.id).first()
    if not db_exp:
        return {"error": "Expense not found"}
    db.delete(db_exp)
    db.commit()
    return {"message": "Expense deleted"}