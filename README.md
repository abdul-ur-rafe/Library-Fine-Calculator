# Library Fine Calculator

A Python command-line application that processes library borrowing records from a CSV file,
validates borrower email addresses, calculates overdue fines, and generates a summary report.

## Features

- Reads borrowing records from a CSV file
- Validates borrower email addresses using regular expressions
- Calculates overdue fines
  - $0.25 per overdue day
  - Maximum fine of $10.00 per book
- Handles invalid or missing data gracefully
- Generates a report (`report.txt`)
- Calculates the total fines collected
- Identifies the borrower appearing most frequently in the records


## Project Structure

```
library-fine-calculator/
│── library.py
│── test_library.py
│── books.csv
│── report.txt
└── README.md
```

## Input

Example CSV:

```csv
title,borrower_email,days_overdue
Harry Potter,alice@example.com,5
1984,bob@example.net,12
```

## Output

```
alice@example.com's copy of Harry Potter owes $1.25
bob@example.net's copy of 1984 owes $3.00

The Total Fines of the Library is $4.25
```

## Concepts Demonstrated

- Object-Oriented Programming
- Classes and Properties
- File Handling
- CSV Processing
- Regular Expressions
- Error Handling
- Command-Line Arguments
- Data Aggregation using Counter
