# pcost.py
#
# Exercise 1.27
import sys
from . import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename=filename)
    return portfolio.total_cost

if __name__ == "__main__":
    cost = portfolio_cost(sys.argv[1])
    print("Total cost:", cost)



# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = "Data/portfolio.csv"
#     filename = "Data/missing.csv"
#     filename = "Data/portfoliodate.csv"

# cost = portfolio_cost(filename)
# print(f"Total cost: {cost}")
