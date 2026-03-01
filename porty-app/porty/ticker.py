
from .follow import follow
import csv
from . import report

from . import tableformat


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
    
    # yield dict(zip(headers,row)) for row in rows


def filter_symbols(rows, names):
    for row in rows:
        if row["name"] in names:
            yield row
    

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])

    # rows = make_dicts(rows, ["name", "price", "change"])
    rows = (dict(zip(["name", "price", "change"], row)) for row in rows)

    return rows


def ticker(portfile, logfile, fmt):
    port = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)

    # rows = filter_symbols(rows, port)
    # equivalent to filter_symbols()
    rows = (row for row in rows if row["name"] in port)
    
    tf = tableformat.create_formatter(fmt)
    tf.headings(["Name", "Price", "Change"])
    for row in rows:
        tf.row(row.values())
        # print(row)

if __name__ == "__main__":
    portfile = "Data/portfolio.csv"
    logile = "Data/stocklog.csv"
    ticker(portfile, logile, fmt="txt")
    
    