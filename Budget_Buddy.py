print("Welcome to Budget Buddy 💰")
income = []
expenses = []

# Option 1: Add Income
def add_income():
    while True:
        income_amount = input("Income amount: ")
        if income_amount.replace('.', '', 1).isdigit():
            income_amount = float(income_amount)  
            break
        else:
            print("Invalid income amount! Please enter a valid number.")
    
    while True:
        income_type = input("Income type |ex. 'Work'|: ")
        if income_type.isalpha():
            break
        else:
            print("Invalid income type! Please enter a valid string.")

    income.append({
        "income_type": income_type,
        "income_amount": income_amount
    })

# Option 2: Add Expense
def add_expense():
    while True:
        expense_amount = input("Expense amount: ")
        if expense_amount.replace('.', '', 1).isdigit():
            expense_amount = float(expense_amount)  
            break
        else:
            print("Invalid expense amount! Please enter a valid number.")
    
    while True:
        expense_type = input("Expense type |ex. 'Rent'|: ")
        if expense_type.isalpha():
            break
        else:
            print("Invalid expense type! Please enter a valid string.")
    
    expenses.append({
        "expense_type": expense_type,
        "expense_amount": expense_amount
    })

# Option 3: View Balance
def view_balance():
    income_amount = 0
    expenses_amount = 0

    for entry in income:
        income_amount += entry["income_amount"]
    for payments in expenses:
        expenses_amount += payments["expense_amount"]
    
    balance = income_amount - expenses_amount
    if balance == 0:
        print("You have 0$ in your account")
    elif balance < 0:
        print(f"You are negative {balance}$ 😥")
    else:
        print(f"{balance}$ in your account")

# Option 4: Category Breakdown
def category_breakdown():
    categories = []
    for items in expenses:
        if items["expense_type"] not in categories:
            categories.append(items["expense_type"])
    
    print("Your expenses based on the type: ")
    for category in categories:
        total = 0
        for expense in expenses:
            if expense["expense_type"] == category:
                total += expense["expense_amount"]
        print(f"{category}: {total}")

# Main Loop
while True:
    print("-" * 20)
    # User Choices
    print("1. ➕ Add Income")
    print("2. ➖ Add Expense")
    print("3. 📊 View Balance")
    print("4. 🗂️ View Category Breakdown")
    print("5. ❌ Exit")

    # User Input
    user_choice = input("👉 Enter your choice: ")

    if user_choice == "1":
        add_income()
    elif user_choice == "2":
        add_expense()
    elif user_choice == "3":
        view_balance()
    elif user_choice == "4":
        category_breakdown()
    elif user_choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid choice! Please select a valid option.")
