# Personal Finance Tracker

## Overview
Personal Finance Tracker is a simple Python application that allows users to manage their financial transactions. Users can add, view, update, and delete transactions, as well as display a summary of their income and expenses.

## Features
- Add transactions (Income or Expense)
- View transaction history
- Update existing transactions
- Delete transactions
- Display a summary of total income, total expenses, and net balance
- Data persistence using JSON file

## Technologies Used
- Python
- JSON (for data storage)

## Installation
1. Clone this repository:
   ```sh
   https://github.com/helithjay/Personal-Finance-Tracker-List-Based-with-JSON-Serialization-.git
   ```
2. Navigate to the project directory:
   ```sh
   cd finance-tracker
   ```
3. Install required dependencies (if needed):
   ```sh
   pip install json
   ```

## Usage
1. Run the Python script:
   ```sh
   python code.py
   ```
2. Select an option from the menu to perform various actions:
   - Add a transaction
   - View all transactions
   - Update an existing transaction
   - Delete a transaction
   - Display a financial summary
   - Exit the program

## File Structure
```
finance-tracker/
│-- code.py            # Main application script
│-- SampleJSONFile.json  # JSON file containing transaction data
│-- README.md          # Project documentation
```

## Sample Data
The application loads transaction data from `SampleJSONFile.json`:
```json
[
  [
    30000.0,
    "Salary",
    "Income",
    "2024-01-01"
  ],
  [
    2000.0,
    "Keels",
    "Expense",
    "2024-01-02"
  ],
  [
    200000.0,
    "Gift",
    "Income",
    "2024-03-01"
  ],
  [
    220.0,
    "Gift",
    "Income",
    "2024-03-03"
  ]
]
```

## Contributions
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

