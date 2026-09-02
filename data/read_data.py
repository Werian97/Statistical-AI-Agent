import csv
import os

Row = list[str]
Rows = list[Row]

class Table():
    def __init__(self, fields: Row, rows: Rows):
        if len(fields) == 0:
            raise ValueError("Can't create a table with no fields")
        if len(rows) == 0:
            raise ValueError("Can't create a table with no rows")
        if len(fields) != len(rows[0]):
            raise ValueError("fields and rows must have same lenght")
        self.fields: Row = fields
        self.rows: Rows = rows

    def get_field_index(self, field: str):
        if not (field in self.fields):
            raise ValueError("this field does not exist")
        return self.fields.index(field)

    def get_column(self, field: str) -> list[str]:
        i: int = self.get_field_index(field)
        column: list[str] = []
        for row in self.rows:
            column.append(row[i])
        return column

    def __add__(self, other):
        if not all(x == y for x, y in zip(self.fields, other.fields)):
            raise ValueError("You can add two table with identical fields")
        sum_rows: Rows = self.rows.copy()
        sum_rows.extend(other.rows)
        return Table(self.fields, sum_rows)


def get_table(file_path: str) -> Table:
    rows: Rows = []
    fields: Row = []
    if not os.path.isfile(file_path):
        raise ValueError(f"{file_path} is not a valid target file")

    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return Table(fields, rows)
