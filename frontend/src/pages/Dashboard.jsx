import React, { useState, useEffect } from "react";
import API from "../api";
import ExpenseCard from "../components/ExpenseCard";

const Dashboard = () => {
  const [expenses, setExpenses] = useState([]);
  const [form, setForm] = useState({ title: "", category: "", amount: "", date: "" });
  const [query, setQuery] = useState("");
  const [aiResponse, setAiResponse] = useState("");

  useEffect(() => { fetchExpenses(); }, []);

  const fetchExpenses = async () => {
    const res = await API.get("/expenses/");
    setExpenses(res.data);
  };

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await API.post("/expenses/", form);
    fetchExpenses();
  };

  const handleAIQuery = async () => {
    const res = await API.post("/ai/query", { query });
    setAiResponse(res.data.response);
  };

  return (
    <div className="dashboard">
      <header>
        <h2>AI Expense Tracker 💸</h2>
      </header>

      <div className="expense-form">
        <form onSubmit={handleSubmit}>
          <input name="title" placeholder="Title" onChange={handleChange} required />
          <input name="category" placeholder="Category" onChange={handleChange} required />
          <input name="amount" type="number" placeholder="Amount" onChange={handleChange} required />
          <input name="date" placeholder="01-Oct-25" onChange={handleChange} required />
          <button type="submit">Add Expense</button>
        </form>
      </div>

      <div className="expense-list">
        {expenses.map((e) => <ExpenseCard key={e.id} expense={e} />)}
      </div>

      <div className="ai-box">
        <textarea value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Ask AI something about your expenses..." />
        <button onClick={handleAIQuery}>Ask AI</button>
        {aiResponse && <div className="ai-response">{aiResponse}</div>}
      </div>
      <div className="logout-button">
        <button onClick={() => { localStorage.removeItem("token"); window.location.href = "/login"; }}>Logout</button>
      </div>
    </div>
  );
};

export default Dashboard;
