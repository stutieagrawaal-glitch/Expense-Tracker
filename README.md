# Beginner Expense Planner

This repository contains a beginner-friendly expense planner written in Python. The program enables users to track their expenses and incomes, set budgets, and review their savings through a console-based menu interface.

## Features

- **Expense Management**: Add, view, and delete expenses with details such as date, amount, category, and description.
- **Income Tracking**: Add incomes, view total income for specified periods.
- **Budgeting**: Define monthly budgets, check budget status, and see budget vs. spending details.
- **Savings Calculation**: Compare monthly income and expenses to determine savings.
- **Category Analytics**: List expense categories and get totals per category.
- **Search & Organisation**: Search for expenses by keyword, and list all categories used.
- **User Menu**: Interactive menu for easy navigation of all features.

## How It Works

The main logic is implemented in `expense.py`, presented as a looping menu-based interface:
- Users interact by selecting numbered options.
- Expenses and incomes are stored in lists, while budgets are managed using a dictionary keyed by month and year.
- Functions provide all core actions (add/view/delete expenses, set/view budgets, calculate totals, etc.)
- Input is taken via prompts, making it approachable for beginners.

## Getting Started

### Requirements

- Python 3.x

### Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/stutieagrawaal-glitch/Expense-Tracker.git
    cd Expense-Tracker
    ```
2. Run the planner:
    ```bash
    python expense.py
    ```
3. Follow the console menu to add expenses, incomes, set budgets, and review your financial activity.

### Example Menu

```
Expense Planner Menu
1. Add Expense
2. View Expenses
3. Delete Expense
4. Total Expense
5. Category Totals
6. Add Income
7. Total Income
8. Set Budget
9. Get Budget
10. Budget Status
11. Savings
12. Search Expenses
13. List Categories
0. Exit
```

## Contributing

Beginners or those interested in personal finance programming are encouraged to contribute! Please fork the repository and open a pull request with your improvements.

## License

This project is open source under the [MIT License](LICENSE).

## Author

Developed by [stutieagrawaal-glitch](https://github.com/stutieagrawaal-glitch).
