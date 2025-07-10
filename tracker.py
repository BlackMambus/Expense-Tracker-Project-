import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.transactions = []
        self.load_data()

    def add_transaction(self, amount, category, description):
        transaction = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transactions.append(transaction)
        self.save_data()

    def view_summary(self):
        print("\n📋 Transaction History:")
        for t in self.transactions:
            sign = "+" if t["amount"] > 0 else "-"
            print(f"{t['date']} | {t['category']} | {sign}₹{abs(t['amount'])} | {t['description']}")
        print(f"\n💼 Current Balance: ₹{self.get_balance():.2f}")

    def get_balance(self):
        return sum(t["amount"] for t in self.transactions)

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.transactions, f, indent=4)

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                self.transactions = json.load(f)
        except FileNotFoundError:
            self.transactions = []

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: ₹"))
            category = input("Enter income category: ")
            description = input("Enter description: ")
            tracker.add_transaction(amount, category, description)

        elif choice == "2":
            amount = float(input("Enter expense amount: ₹"))
            category = input("Enter expense category: ")
            description = input("Enter description: ")
            tracker.add_transaction(-amount, category, description)

        elif choice == "3":
            tracker.view_summary()

        elif choice == "4":
            print("👋 Exiting Expense Tracker. Stay financially wise!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



