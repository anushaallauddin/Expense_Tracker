import csv
from expense import Expense


class ExpenseTracker:

    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open("expenses.csv", "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    expense = Expense(
                        int(row["ID"]),
                        row["Date"],
                        row["Category"],
                        row["Description"],
                        float(row["Amount"]),
                        row["Type"]
                    )

                    self.expenses.append(expense)

        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open("expenses.csv", "w", newline="") as file:

            fieldnames = [
                "ID",
                "Date",
                "Category",
                "Description",
                "Amount",
                "Type"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for expense in self.expenses:
                writer.writerow(expense.to_dict())

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

        print("Transaction Added Successfully!")

    def view_expenses(self):

        if len(self.expenses) == 0:
            print("No transactions available.")
            return

        print("\n========== TRANSACTIONS ==========")

        for expense in self.expenses:

            print(f"ID          : {expense.expense_id}")
            print(f"Date        : {expense.date}")
            print(f"Category    : {expense.category}")
            print(f"Description : {expense.description}")
            print(f"Amount      : {expense.amount}")
            print(f"Type        : {expense.transaction_type}")
            print("-" * 35)

    def search_by_category(self, category):

        found = False

        print(f"\n===== {category.upper()} TRANSACTIONS =====")

        for expense in self.expenses:

            if expense.category.lower() == category.lower():

                print(f"ID          : {expense.expense_id}")
                print(f"Date        : {expense.date}")
                print(f"Category    : {expense.category}")
                print(f"Description : {expense.description}")
                print(f"Amount      : {expense.amount}")
                print(f"Type        : {expense.transaction_type}")
                print("-" * 35)

                found = True

        if not found:
            print("No transactions found for this category.")

    def search_by_type(self, transaction_type):

        found = False

        print(f"\n===== {transaction_type.upper()} TRANSACTIONS =====")

        for expense in self.expenses:

            if expense.transaction_type.lower() == transaction_type.lower():

                print(f"ID          : {expense.expense_id}")
                print(f"Date        : {expense.date}")
                print(f"Category    : {expense.category}")
                print(f"Description : {expense.description}")
                print(f"Amount      : {expense.amount}")
                print(f"Type        : {expense.transaction_type}")
                print("-" * 35)

                found = True

        if not found:
            print("No transactions found.")

    def category_summary(self):

        summary = {}

        for expense in self.expenses:

            if expense.transaction_type == "Expense":

                category = expense.category

                if category in summary:
                    summary[category] += expense.amount
                else:
                    summary[category] = expense.amount

        print("\n===== EXPENSE BY CATEGORY =====")

        for category, amount in summary.items():
            print(f"{category}: {amount:.2f}")

    def monthly_summary(self):

        summary = {}

        for expense in self.expenses:

            month = expense.date[:7]

            if month not in summary:
                summary[month] = {
                    "Income": 0,
                    "Expense": 0
                }

            summary[month][expense.transaction_type] += expense.amount

        print("\n===== MONTHLY SUMMARY =====")

        for month, data in sorted(summary.items()):

            income = data["Income"]
            expenses = data["Expense"]
            balance = income - expenses

            print(f"\nMonth: {month}")
            print(f"Income  : {income:.2f}")
            print(f"Expenses: {expenses:.2f}")
            print(f"Balance : {balance:.2f}")
            print("-" * 35)

    def delete_expense(self, expense_id):

        for expense in self.expenses:

            if expense.expense_id == expense_id:

                self.expenses.remove(expense)
                self.save_expenses()

                print("Transaction Deleted Successfully!")
                return

        print("Transaction not found.")