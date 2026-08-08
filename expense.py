class Expense:
    def __init__(self, expense_id, date, category, description, amount, transaction_type):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type

    def to_dict(self):
        return {
            "ID": self.expense_id,
            "Date": self.date,
            "Category": self.category,
            "Description": self.description,
            "Amount": self.amount,
            "Type": self.transaction_type
        }