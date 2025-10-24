import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_expenses(expenses, user_query):
    expense_summary = "\n".join(
        [f"{e.date} | {e.category}: ₹{e.amount} - {e.title}" for e in expenses]
    )
    prompt = f"""
    You are a personal finance AI assistant.
    Here are the user's expenses:
    {expense_summary}

    User's question: {user_query}
    Analyze and respond with financial insights.
    """
    model = genai.GenerativeModel("gemini-2.0-flash")
    res = model.generate_content(prompt)
    return res.text
