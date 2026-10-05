import os
from expense import Expense

def save_to_file(expenses):
    try:
        path = os.path.join(os.path.dirname(__file__), "data.csv")

        print("Saving to:", path)

        with open(path, "w") as file:
            for e in expenses:
                file.write(f"{e.amount},{e.category},{e.date}\n")

    except Exception as e:
        print("Save Error:", e)


def load_from_file():
    expenses = []
    try:
        path = os.path.join(os.path.dirname(__file__), "data.csv")

        print("Loading from:", path)

        with open(path, "r") as file:
            for line in file:
                data = line.strip().split(",")
                expenses.append(Expense(float(data[0]), data[1], data[2]))

    except:
        print("File not found")

    return expenses
