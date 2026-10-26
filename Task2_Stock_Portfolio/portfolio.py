
import csv
from datetime import datetime
import yfinance as yf

SUMMARY_FILE = "portfolio_summary.csv"


def get_current_price(ticker):
    """Fetch the latest available daily closing price."""
    stock = yf.Ticker(ticker)
    data = stock.history(period="5d")

    if data.empty:
        raise ValueError("Price data unavailable")

    closes = data["Close"].dropna()

    if closes.empty:
        raise ValueError("Closing price unavailable")

    return float(closes.iloc[-1])


def main():
    portfolio = {}

    print("\n=== STOCK PORTFOLIO TRACKER ===")
    print("Enter DONE when finished adding stocks.")

    while True:
        ticker = input("\nEnter ticker: ").strip().upper()

        if ticker == "DONE":
            break

        if not ticker:
            print("Ticker cannot be empty.")
            continue

        try:
            buy_price = float(input("Enter buy price: "))
            quantity = int(input("Enter quantity: "))

            if buy_price <= 0 or quantity <= 0:
                print("Price and quantity must be positive.")
                continue

            current_price = get_current_price(ticker)

            if ticker not in portfolio:
                portfolio[ticker] = {
                    "quantity": 0,
                    "invested": 0.0,
                    "current_price": current_price
                }

            item = portfolio[ticker]
            item["quantity"] += quantity
            item["invested"] += buy_price * quantity
            item["current_price"] = current_price

            print(f"{ticker} added successfully!")

        except ValueError as e:
            print("Invalid input or unavailable price:", e)
        except Exception as e:
            print("Could not retrieve stock data:", e)

    if not portfolio:
        print("\nNo valid holdings entered.")
        return

    total_invested = 0.0
    total_value = 0.0
    timestamp = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )

    rows = []

    print("\n========== PORTFOLIO SUMMARY ==========")

    for ticker, item in portfolio.items():
        quantity = item["quantity"]
        invested = item["invested"]
        current = item["current_price"]

        market_value = quantity * current
        profit_loss = market_value - invested
        gain_loss_pct = (profit_loss / invested) * 100

        total_invested += invested
        total_value += market_value

        print(f"\nStock: {ticker}")
        print(f"Quantity: {quantity}")
        print(f"Invested: {invested:.2f}")
        print(f"Latest available close: {current:.2f}")
        print(f"Market value: {market_value:.2f}")
        print(f"Profit/Loss: {profit_loss:.2f}")
        print(f"Return: {gain_loss_pct:.2f}%")

        rows.append([
            timestamp,
            ticker,
            quantity,
            round(invested, 2),
            round(current, 2),
            round(market_value, 2),
            round(profit_loss, 2),
            round(gain_loss_pct, 2)
        ])

    total_profit = total_value - total_invested
    overall_return = total_profit / total_invested * 100

    print("\n========== TOTAL ==========")
    print(f"Total invested: {total_invested:.2f}")
    print(f"Current value: {total_value:.2f}")
    print(f"Total Profit/Loss: {total_profit:.2f}")
    print(f"Overall return: {overall_return:.2f}%")

    # Append each run's snapshot to the CSV log
    headers = [
        "Timestamp", "Ticker", "Quantity", "Invested",
        "Latest_Close", "Market_Value", "Profit_Loss",
        "Return_Percent"
    ]

    with open(SUMMARY_FILE, "a", newline="",
              encoding="utf-8") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(headers)

        writer.writerows(rows)

    print(f"\nPerformance log saved to {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
