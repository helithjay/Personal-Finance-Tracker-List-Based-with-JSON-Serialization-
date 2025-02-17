Personal Finance Tracker
A simple Python-based command-line application to track personal finances. This tool allows users to add, view, update, delete, and summarize their income and expenses. Transactions are stored in a JSON file for persistence.

Features
Add Transaction: Record new income or expenses with details like amount, description, type (income/expense), and date.

View Transactions: Display all recorded transactions in a readable format.

Update Transaction: Modify existing transactions.

Delete Transaction: Remove unwanted transactions.

Display Summary: View total income, total expenses, and net balance.

Installation
Clone the Repository:


git clone (https://github.com/helithjay/Personal-Finance-Tracker-List-Based-with-JSON-Serialization-.git)

cd personal-finance-tracker

Ensure Python is Installed:

This project requires Python 3.x. You can download it from python.org.

Run the Application:
Execute the Python script to start the finance tracker:


python finance_tracker.py
Usage
Main Menu:
When you run the program, you'll see a menu with the following options:


1. Add Transaction
2. View Transactions
3. Update Transaction
4. Delete Transaction
5. Display Summary
6. Exit
Adding a Transaction:

Select option 1 from the menu.

Enter the amount (use a negative value for expenses).

Provide a description, type (Income/Expense), and date.

Viewing Transactions:

Select option 2 to see all recorded transactions.

Updating a Transaction:

Select option 3 and follow the prompts to update an existing transaction.

Deleting a Transaction:

Select option 4 and enter the index of the transaction you want to delete.

Displaying Summary:

Select option 5 to view the total income, total expenses, and net balance.

Exiting the Program:

Select option 6 to exit the application.

File Structure
finance_tracker.py: The main Python script containing the logic for the finance tracker.

SampleJSONFile.json: A JSON file used to store transaction data.

Example JSON File
The SampleJSONFile.json file stores transactions in the following format:

json
Copy
[
  [
    30000.0,
    "Salary",
    "Income",
    "2024-01-01"
  ],
  [
    -2000.0,
    "Groceries",
    "Expense",
    "2024-01-02"
  ]
]
Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Commit your changes.

Submit a pull request.

License
This project is open-source and available under the MIT License.

Contact
For questions or feedback, feel free to reach out:

Helith Jayasuriya: helithjayasuriya77@gmail.com

GitHub: helithjay
