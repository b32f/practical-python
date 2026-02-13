# report.py
#
# Exercise 2.4
import csv
from pprint import pprint


def portfolio_cost(filename):
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            # total_cost += nshares * price
            # holding = (row[0], nshares, price)
            # portfolio.append(holding)
            portfolio.append({"name": row[0], "shares": nshares, "price": price})
    return portfolio


def read_prices(filename):
    f = open(filename, "r")
    rows = csv.reader(f)

    stock_price = {}
    for row in rows:
        try:
            stock_price[row[0]] = float(row[1])
        except IndexError:
            pass
    return stock_price


def gain_loss(portfolio, prices):
    pf = []
    for row in portfolio:
        price_bought = row["price"]
        nshares = row["shares"]
        price_new = prices[row["name"]]
        row["gain/loss"] = round((price_bought - price_new) * nshares, 2)
        pf.append(row)
    return pf


portfolio = portfolio_cost("Work/Data/portfolio.csv")
prices = read_prices("Work/Data/prices.csv")
pf_gl = gain_loss(portfolio, prices)
pprint(pf_gl)
