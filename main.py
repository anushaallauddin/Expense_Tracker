from tracker import ExpenseTracker
from expense import Expense


tracker = ExpenseTracker()


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Show Total Income")
    print("4. Show Total Expenses")
    print("5. Show Balance")
    print("6. Search by Category")
    print("7. Search by Type")
    print("8. Category-wise Summary")
    print("9. Monthly Summary")
    print("10. Delete Transaction")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        transaction_id = len(tracker.expenses) + 1

        transaction_date = input("Enter Date (YYYY-MM-DD): ")
        category = input("Enter Category: ")
        description = input("Enter Description: ")
        amount = float(input("Enter Amount: "))

        print("\nSelect Transaction Type:")
        print("1. Income")
        print("2. Expense")

        transaction_choice = input("Enter choice: ")

        if transaction_choice == "1":
            transaction_type = "Income"

        elif transaction_choice == "2":
            transaction_type = "Expense"

        else:
            print("Invalid transaction type!")
            continue

        new_expense = Expense(
            transaction_id,
            transaction_date,
            category,
            description,
            amount,
            transaction_type
        )

        tracker.add_expense(new_expense)

    elif choice == "2":

        tracker.view_expenses()

    elif choice == "3":

        total_income = sum(
            expense.amount
            for expense in tracker.expenses
            if expense.transaction_type == "Income"
        )

        print(f"\nTotal Income: {total_income}")

    elif choice == "4":

        total_expenses = sum(
            expense.amount
            for expense in tracker.expenses
            if expense.transaction_type == "Expense"
        )

        print(f"\nTotal Expenses: {total_expenses}")

    elif choice == "5":

        total_income = sum(
            expense.amount
            for expense in tracker.expenses
            if expense.transaction_type == "Income"
        )

        total_expenses = sum(
            expense.amount
            for expense in tracker.expenses
            if expense.transaction_type == "Expense"
        )

        balance = total_income - total_expenses

        print(f"\nCurrent Balance: {balance}")

    elif choice == "6":

        category = input("Enter Category to Search: ")

        tracker.search_by_category(category)

    elif choice == "7":

        print("\n1. Income")
        print("2. Expense")

        type_choice = input("Enter choice: ")

        if type_choice == "1":

            tracker.search_by_type("Income")

        elif type_choice == "2":

            tracker.search_by_type("Expense")

        else:

            print("Invalid choice!")

    elif choice == "8":

        tracker.category_summary()

    elif choice == "9":

        tracker.monthly_summary()

    elif choice == "10":

        expense_id = int(input("Enter Transaction ID to Delete: "))

        tracker.delete_expense(expense_id)

    elif choice == "11":

        print("Thank you for using the Expense Tracker!")