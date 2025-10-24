# Overview
This is an expense tracker which leverages Gemini to get AI insights.
Please find the detailed flow below of how this project works:
- Create a user and log in (it creates a session using JWT)
- Add your expenses
- Ask AI about your expense like, give total spendings in last month, which area should I work on to save more


# Backend
## Start
- python -m venv venv (if not already done)
- myenv\Scripts\activate 
- pip install uvicorn
- pip install "fastapi[standard]" uvicorn
- python -m uvicorn app.main:app --reload // ignores the broken uvicorn.exe launcher runs through curr env OR uvicorn app.main:app --reload

