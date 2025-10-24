import React from "react";

const ExpenseCard = ({ expense }) => {
  return (
    <div className="expense-card">
      <h4>{expense.title}</h4>
      <p>Category: {expense.category}</p>
      <p>Amount: ₹{expense.amount}</p>
      <p>Date: {expense.date}</p>
    </div>
  );
};

export default ExpenseCard;
