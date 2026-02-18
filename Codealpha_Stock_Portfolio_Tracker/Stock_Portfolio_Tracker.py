stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0
portfolio = {}

print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity.")
        continue

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

print("\nPortfolio Summary:-\n")

for stock, qty in portfolio.items():
    total = stock_prices[stock] * qty
    print(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${total}")
    total_investment += total

print(f"\nTOTAL VALUE: ${total_investment}")

save = input("\nDo you want to save to file? (y/n): ").lower()

if save == "y":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Portfolio Summary:-\n")

        for stock, qty in portfolio.items():
            total = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${total}\n")

        file.write("--------------------------------------------\n")
        file.write(f"TOTAL VALUE: ${total_investment}")

    print("Portfolio saved to portfolio_summary.txt")
