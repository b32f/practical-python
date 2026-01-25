# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    cost = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            try:
                cost += int(row[1]) * float(row[2])
            except ValueError as e:
                print(f"Warning: could not read line: {row}")
    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
    filename = "Data/missing.csv"

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")
