import React, { useState } from "react";
import API from "../api";

const ExpenseCard = ({ expense, onUpdate, onDelete }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editForm, setEditForm] = useState({ ...expense });

  const handleChange = (e) => setEditForm({ ...editForm, [e.target.name]: e.target.value });

  const handleSave = async () => {
    await API.put(`/expenses/${expense.id}`, {title: editForm.title, category: editForm.category, amount: Number(editForm.amount), date: editForm.date});
    setIsEditing(false);
    onUpdate();
  };

  const handleDelete = async () => {
    await API.delete(`/expenses/${expense.id}`);
    onDelete(expense.id);
  };

  return (
    <div className="expense-card">
      {isEditing ? (
        <>
          <input name="title" value={editForm.title} onChange={handleChange} />
          <input name="category" value={editForm.category} onChange={handleChange} />
          <input name="amount" type="number" value={editForm.amount} onChange={handleChange} />
          <input name="date" value={editForm.date} onChange={handleChange} />
          <button onClick={handleSave}>💾 Save</button>
          <button onClick={() => setIsEditing(false)}>❌ Cancel</button>
        </>
      ) : (
        <>
          <h4>{expense.title}</h4>
          <p><strong>Category:</strong> {expense.category}</p>
          <p><strong>Amount:</strong> ₹{expense.amount}</p>
          <p><strong>Date:</strong> {expense.date}</p>

          <div className="actions">
            <button onClick={() => setIsEditing(true)}>✏️ Edit</button>
            <button onClick={handleDelete}>🗑️ Delete</button>
          </div>
        </>
      )}
    </div>
  );
};

export default ExpenseCard;
