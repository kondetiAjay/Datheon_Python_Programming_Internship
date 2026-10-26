# Datheon Python Programming Internship

## About
This repository contains my Python programming internship projects completed as part of the Datheon internship program.

## Task 1: Hangman Word Guessing Game (Console)

### Description
A terminal-based word guessing game developed using Python. The user guesses a hidden word one letter at a time within a limited number of attempts.

### Features
- Random secret word selection
- Letter-by-letter guessing
- ASCII gallows art
- Tracks previously guessed letters
- Prevents duplicate guesses from reducing attempts
- Maximum of 6 incorrect attempts
- Victory and defeat messages

### Technologies
- Python 3
- Random module
- String manipulation
- Control flow

### How to Run
```bash
python hangman.py
```

## Task 2: Stock Portfolio Performance Tracker

### Description
A Python application that tracks stock investments, calculates portfolio value and profit/loss, and saves portfolio performance records to a CSV file.

### Features
- Accepts stock ticker symbols
- Accepts purchase prices and share quantities
- Retrieves available stock price history
- Calculates invested capital and market value
- Calculates profit/loss and percentage returns
- Maintains timestamped CSV performance logs

### Technologies
- Python 3
- yfinance
- CSV module
- File handling
- Dictionaries

### How to Run
Install dependencies:
```bash
python -m pip install -r Task2_Stock_Portfolio/requirements.txt
```

Run the program from the main project folder:
```bash
python Task2_Stock_Portfolio/portfolio.py
```

Enter stock ticker symbols, purchase prices, and quantities. Enter `DONE` to finish and view the portfolio summary.

### Output
The program generates `portfolio_summary.csv` containing portfolio performance records.

## Project Structure
```text
hangman_internship/
├── hangman.py
├── words.txt
├── README.md
└── Task2_Stock_Portfolio/
    ├── portfolio.py
    ├── requirements.txt
    └── portfolio_summary.csv
```

## Author
Ajay Kondeti
