# Backend
## Start
- python -m venv venv (if not already done)
- myenv\Scripts\activate 
- pip install uvicorn
- pip install "fastapi[standard]" uvicorn
- python -m uvicorn app.main:app --reload // ignores the broken uvicorn.exe launcher runs through curr env OR uvicorn app.main:app --reload

