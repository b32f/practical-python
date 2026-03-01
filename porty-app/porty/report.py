# report.py
#
# Exercise 2.4
import sys
from . import fileparse
from . import tableformat
from .portfolio import Portfolio
import logging

def read_portfolio(filename, **opts):
    """
    Read a stock portfolio into a list of dictionaries with keys:
    `name`, `shares`, and `price`.
    """
    with open(filename, "rt") as f:
        # portdicts = fileparse.parse_csv(f, select=["name", "shares", "price"], types=[str, int, float], **opts)
        # portfolio = [stock.Stock(**s) for s in portdicts]
        return Portfolio.from_csv(f)
    

def read_prices(filename):
    with open(filename, "rt") as f:
        return dict(fileparse.parse_csv(f, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        price_new = prices[s.name]
        change = round((price_new - s.price), 2)

        report.append((s.name, s.shares, price_new, change))
    return report


def print_report(report, formatter):
    formatter.headings(("Name", "Shares", "Price", "Change"))

    for name, shares, price, change in report:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio, prices, fmt="txt"):
    portfolio = read_portfolio(portfolio)
    prices = read_prices(prices)
    report = make_report(portfolio, prices)

    if fmt == "txt":
        formatter = tableformat.TextTableFormatter()
    elif fmt == "csv":
        formatter = tableformat.CSVTableFormatter()
    elif fmt == "html":
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f"Unknown format {fmt}")
    print_report(report, formatter)


def main(args):
    print(args)
    if len(args) == 3:
        l_args = [None, args[0], args[1]]
        args = l_args
    if len(args) != 4:
        raise SystemExit("Usage: %s portfile pricefile" % args[0])
    portfolio_report(args[1], args[2], args[3])


if __name__ == "__main__":
    logging.basicConfig(
        filename = "app.log",
        filemode="w",
        level = logging.warning
    )
    main(sys.argv)


# portfolio_report("Data/portfolio.csv", "Data/prices.csv")
