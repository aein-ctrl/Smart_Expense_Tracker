import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
            df.to_csv(self.filename, index=False)

    def add_expense(self, category, amount, description=""):
        try:
            date = datetime.now().strftime("%Y-%m-%d")
            df = pd.read_csv(self.filename)
            new_data = {
                "Date": date,
                "Category": category,
                "Amount": float(amount),
                "Description": description
            }
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(self.filename, index=False)
            print("Expense added successfully!")
        except ValueError:
            print("Invalid amount entered.")

    def view_summary(self):
        df = pd.read_csv(self.filename)
        print("\nTotal Expenses:")
        print(df.groupby("Category")["Amount"].sum())

    def plot_expenses(self):
        df = pd.read_csv(self.filename)
        summary = df.groupby("Category")["Amount"].sum()
        summary.plot(kind="bar", title="Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. View Summary")
        print("3. Plot Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Category: ")
            amount = input("Amount: ")
            description = input("Description: ")
            tracker.add_expense(category, amount, description)

        elif choice == "2":
            tracker.view_summary()

        elif choice == "3":
            tracker.plot_expenses()

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
