from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class  ExpenseBase(BaseModel):
    title: str
    category: str
    amount: float
    date: str

class ExpenseOut(ExpenseBase):
    id: int
    class Config:
        orm_mode = True
