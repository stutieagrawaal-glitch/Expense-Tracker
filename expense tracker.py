# Expense Planner with User Input

expenses = []
incomes = []
categories = []
budgets = {}

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    if category not in categories:
        categories.append(category)
    expenses.append({"date": date, "amount": amount, "category": category, "description": description})
    print("Expense added!")

def view_expenses():
    for i, e in enumerate(expenses):
        print(i, e)

def delete_expense():
    index = int(input("Enter expense index to delete: "))
    if 0 <= index < len(expenses):
        expenses.pop(index)
        print("Expense deleted.")
    else:
        print("Invalid index.")

def total_expense():
    print("Total expense:", sum(e["amount"] for e in expenses))

def category_totals():
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]
    print("Category totals:", totals)

def add_income():
    date = input("Enter income date (YYYY-MM-DD): ")
    source = input("Enter income source: ")
    amount = float(input("Enter income amount: "))
    incomes.append({"date": date, "source": source, "amount": amount})
    print("Income added!")

def total_income():
    print("Total income:", sum(i["amount"] for i in incomes))

def set_budget():
    year = input("Enter year (YYYY): ")
    month = input("Enter month (MM): ")
    amount = float(input("Enter budget amount: "))
    budgets[f"{year}-{month}"] = amount
    print("Budget set!")

def get_budget():
    year = input("Enter year (YYYY): ")
    month = input("Enter month (MM): ")
    key = f"{year}-{month}"
    print("Budget:", budgets.get(key, "No budget set"))

def budget_status():
    year = input("Enter year (YYYY): ")
    month = input("Enter month (MM): ")
    key = f"{year}-{month}"
    budget = budgets.get(key, 0)
    spent = sum(e["amount"] for e in expenses if e["date"].startswith(key))
    print("Budget:", budget, "Spent:", spent, "Remaining:", budget - spent)

def savings():
    year = input("Enter year (YYYY): ")
    month = input("Enter month (MM): ")
    key = f"{year}-{month}"
    income = sum(i["amount"] for i in incomes if i["date"].startswith(key))
    spent = sum(e["amount"] for e in expenses if e["date"].startswith(key))
    print("Income:", income, "Expense:", spent, "Savings:", income - spent)

def search_expenses():
    word = input("Enter search word: ").lower()
    for e in expenses:
        if word in e["description"].lower() or word in e["category"].lower():
            print(e)

def list_categories():
    print("Categories:", categories)

# ---- Menu Loop ----
while True:
    print("\nExpense Planner Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Expense")
    print("5. Category Totals")
    print("6. Add Income")
    print("7. Total Income")
    print("8. Set Budget")
    print("9. Get Budget")
    print("10. Budget Status")
    print("11. Savings")
    print("12. Search Expenses")
    print("13. List Categories")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1": add_expense()
    elif choice == "2": view_expenses()
    elif choice == "3": delete_expense()
    elif choice == "4": total_expense()
    elif choice == "5": category_totals()
    elif choice == "6": add_income()
    elif choice == "7": total_income()
    elif choice == "8": set_budget()
    elif choice == "9": get_budget()
    elif choice == "10": budget_status()
    elif choice == "11": savings()
    elif choice == "12": search_expenses()
    elif choice == "13": list_categories()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
