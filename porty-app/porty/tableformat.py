class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()
    
    def row(self, rowdata):
        raise NotImplementedError()

class FormatError(Exception):
    pass

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ")*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10}", end= " ")
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>", end="")
        for h in headers:
            print(f"<th>{h}</th>", end="")
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end="")
        for d in rowdata:
            print(f"<td>{d}</td>", end="")
        print("</tr>")
        

def create_formatter(fmt="txt"):
    if fmt == "txt":
        return TextTableFormatter()
    elif fmt == "csv":
        return CSVTableFormatter()
    elif fmt == "html":
        return HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown format {fmt}")
    

def print_table(portfolio, cols, formatter):
    formatter.headings(cols)
    for row in portfolio:
        formatter.row([getattr(row, s) for s in cols])


