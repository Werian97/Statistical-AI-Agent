import csv
import os

Row = list[str]
Rows = list[Row]

class Table():
    def __init__(self, fields: Row, rows: Rows):
        self.fields: Row = fields
        self.rows: Rows = rows

    def get_field_index(self, field: str):
        if not (field in self.fields):
            raise ValueError("this field does not exist")
        return self.fields.index(field)

    def pick_rows(self, field: str, value: str):
        # Return a subtable containing only the rows having 'value'
        # in the corresponding field column.
        # The fields remain the same
        i = self.get_field_index(field)
        new_rows: Rows = []
        for row in self.rows:
            if row[i] == value:
                new_rows.append(row)

        return Table(self.fields, new_rows)

    def get_column(self, field: str):
        i = self.get_field_index(field)
        column: list[str] = []
        for row in self.rows:
            column.append(row[i])
        return column


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