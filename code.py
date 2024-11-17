import json


# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    global transactions
    try:
        with open("SampleJSONFile.json", "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:
        pass
def save_transactions():
    with open('SampleJSONFile.json', 'w') as file:
        json.dump(transactions, file, indent = 2)

# Feature implementations
def add_transaction():
    try:
            amount=float(input("Enter amount here(If Expense use (-)):"))
            description=input("Enter description here:")
            income_or_expence=input("Income or Expense:")
            date=input("Enter date YYYY-MM-DD:")
            transaction=[amount,description,income_or_expence,date]
            transactions.append(transaction)
            print("Transaction added successfully")
            save_transactions()

    except ValueError:
            print("Enter valid data")

def view_transactions():
    if not transactions:
        print("There are no transactions here")
    else:
        print("Transactions History:")
        index=0
        for transaction in transactions:
            index +=1
            print(index,transaction)

def update_transaction():
    # Placeholder for update transaction logic
    # Remember to use save_transactions() after updating
    view_transactions()
    try:
        index=int(input("Enter index number you want to update:"))-1
        new_amount=float(input("Enter new amount here:"))
        new_description=input("Enter new description here:")
        new_Income_or_Expense=input("Enter Income or Expense:")
        new_date=input("Enter date here:")
        transactions[index]=[new_amount,new_description,new_Income_or_Expense,new_date]
        save_transactions()
        print("Update successfully")

    except ValueError:
        print("Enter valid data")
    
def delete_transaction():
    # Placeholder for delete transaction logic
    # Remember to use save_transactions() after deleting
    view_transactions()
    try:
        index=int(input("Enter index number here:"))-1
        del transactions[index]
        save_transactions()
        print("Deleted")

    except ValueError:
        print("Enter valid index number")

def display_summary():
    # Placeholder for summary display logic
    total_income = sum(transaction[0] for transaction in transactions if transaction[0] > 0)
    total_expense = sum(transaction[0] for transaction in transactions if transaction[0] < 0)
    print("Total Income:",total_income)
    print("Total Expense:",total_expense)
    print("Net Balance", total_income+total_expense)
def main_menu():
    load_transactions()  # Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

# if you are paid to do this assignment please delete this line of comment 

