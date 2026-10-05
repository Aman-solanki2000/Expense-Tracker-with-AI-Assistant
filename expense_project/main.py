from expense import Expense
from file_handler import save_to_file, load_from_file
from analysis import analyze, category_report
from ai_helper import ai_suggestion
expenses = load_from_file()
    



def menu():
    print("\n1. Add Expenses")
    print("2. View Expenses")
    print("3. Report")
    print("4. AI Suggestion")
    print("5. Exit")


def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date: ")

        exp = Expense(amount, category, date)
        expenses.append(exp)

    except:
        print("Invalid input")


def view_expense(expenses):
    for e in expenses:
        print(e.amount, e.category, e.date)



while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense(expenses)
        save_to_file(expenses)

    elif choice == "2":
        view_expense(expenses)

    elif choice == "3":
        category_report(expenses)
        analyze()

    elif choice == "4":
        ai_suggestion(expenses)

    elif choice == "5":
        save_to_file(expenses)
        print("Exit")
        break
    

    else:
        print("Invalid choice")



        
    

        
            


