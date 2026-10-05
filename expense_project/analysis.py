import pandas as pd
import os 

def category_report(expenses):
    report = {}

    for e in expenses:
        if e.category in report:
            report[e.category] += e.amount
        else:
            report[e.category] = e.amount

    print("\n--- Category Report ---")
    print(report)


def analyze():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "data.csv")

        df = pd.read_csv(file_path, names=["Amount", "Category", "Date"])

        print("\n--- Category Wise Total Expense ---")
        print(df.groupby("Category")["Amount"].sum())

    except Exception as e:
        print("Error:", e)
