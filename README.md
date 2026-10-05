# 💰 Expense Tracker with AI Assistant

An intelligent, interactive, and user-friendly command-line application built using Python to track daily expenses, perform data analysis, and provide smart financial recommendations using generative AI.

---

## 📌 Problem Statement
Many people find it difficult to track their daily expenses and analyze their spending habits. There is a crucial need for a simple application that can seamlessly record expenses, generate comprehensive reports, and provide smart AI-based budget suggestions.

## 🎯 Project Objectives
* **Track Daily Expenses:** Easily record and manage daily expenditures.
* **Secure Storage:** Store data safely in structured local formats.
* **Data Insights:** Generate automated category-wise financial reports.
* **AI Assistance:** Provide personalized, intelligent financial advice based on user spending habits.

---

## ✨ Features
* ➕ **Add Expenses:** Input custom amounts, categories (Food, Travel, Shopping, etc.), and dates.
* 🔍 **View Expenses:** Display a clean tabular view of all recorded historical expenditures with automated totals.
* 📊 **Category Report:** Generate automated reports calculating total expenses per category powered by data aggregation.
* 🤖 **AI Suggestions:** Integrated with advanced Large Language Models to read expense trends and deliver realistic budget insights.
* 💾 **Auto Save to CSV:** Continuous data persistence using standard CSV file handling.

---

## 🛠️ Technologies Used
* **Language:** Python
* **Data Analysis:** Pandas library for structured group-by reporting
* **Database/Storage:** CSV File Handling
* **Artificial Intelligence:** Groq AI API (`llama-3.3-70b-versatile` model)

---

## 📂 Project Structure & Architecture
```text
expense_project/
│
├── Main.py          # Main executable interface (Menu system)
├── expense.py       # Data model (Expense class structure)
├── File_handler.py  # Read/Write operations for data persistence
├── analysis.py      # Pandas logic for generating insights
├── Ai_helper.py     # Groq API client configuration & prompting
└── data.csv         # Local storage file containing transaction data
```

### Component Breakdown
* **`expense.py`:** Handles initialization of fields: `amount`, `category`, and `date`.
* **`File_handler.py`:** Implements safe read/write blocks utilizing path joins (`os.path.join`) to prevent data loss.
* **`analysis.py`:** Leverages Pandas DataFrames (`pd.read_csv`) to run grouped aggregations like `df.groupby("Category")["Amount"].sum()`.
* **`Ai_helper.py`:** Establishes the asynchronous client request structure communicating directly with the Groq inference engine.

---

## 💻 Sample Terminal Workflow

### 1. Adding an Expense
```bash
===== FINANCE TRACKER WITH AI ASSISTANCE =====
1. Add Expense
Enter amount: 500
Enter category: Food
Enter date (DD-MM-YYYY): 05-05-2026
Expense added successfully!
```

### 2. Tabular Reports & Summary
```bash
2. View Expenses
+---------------+---------------+---------------+

| Amount        | Category      | Date          |
+---------------+---------------+---------------+

| 500           | Food          | 05-05-2026    |
| 1200          | Shopping      | 07-05-2026    |
+---------------+---------------+---------------+
TOTAL Expenses: 4050
```

### 3. AI Insights Output
```bash
AI Suggestion:
+----------------------------------------------+

| You are spending the most on shopping (1200).|
| Try reducing unnecessary purchases.          |
|                                              |
| Your Food expenses are also high.            |
| Consider cooking at home to save more.       |
+----------------------------------------------+
```

---

## ⚠️ Challenges Faced & Overcoming Them
* **Path Discrepancies:** Resolved structural CSV loading errors across environments by moving from static strings to dynamic `os.path.dirname(__file__)` paths.
* **Data Serialization:** Tackled runtime type crashes during calculations by enforcing strict cast operations (`float()`) on raw data parsed from text rows.
* **API Integration:** Managed continuous streaming exceptions and secure credentials handling during the Groq AI integration lifecycle.

---

## 🚀 Future Enhancements
* 📊 Integration of visual UI charts using dynamic graphical dashboards.
* ☁️ Porting localized data engines to secure Cloud Database infrastructure.
* 🔐 User profile authentication frameworks for individual multi-tenant isolation.
* 🎤 Smart voice-enabled interaction for recording financial inputs.

---
*Developed by **Aman** as part of the Python Programming Curriculum.*
