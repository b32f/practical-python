# fileparse.py
#
# Exercise 3.3

import csv
import logging

log  = logging.getLogger(__name__)


def parse_csv(lines, select = None, types = None, has_headers=True, delimiter=",", silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    if not has_headers and select is not None:
        raise RuntimeError("select argument requieres column headers")
    
    rows = csv.reader(lines, delimiter=delimiter)
    headers = next(rows) if has_headers else []

    if select is not None:
        indices  =  [headers.index(colname) for colname in select]
        headers = select
            
    records = []
    for i, row in enumerate(rows, start=1):
        if not row:
            continue

        if select:
            row = [row[i] for i in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", i, row)
                    log.debug("Row %d: Reason %s", i, e)
                continue
        
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)        
        records.append(record)

    return records