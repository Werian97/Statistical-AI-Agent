import csv
import os
import shutil

from data.filepath_to_data import TMP_FILEPATH

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


def save_csv(table: Table):
    n = count_temporary() + 1
    if n < 10:
        file_name: str = "tmp_0" + str(n) + ".csv"
    else:
        file_name: str = "tmp_" + str(n) + ".csv"

    relative_file_path: str = os.path.join(TMP_FILEPATH, file_name)

    abs_file_path: str = os.path.join(os.path.abspath("."), relative_file_path)
    with open(abs_file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(table.fields)
        for row in table.rows:
            writer.writerow(row)
    return relative_file_path
    

def count_temporary() -> int:
    if not os.path.isdir(TMP_FILEPATH):
        os.mkdir(TMP_FILEPATH)
        return 0
    return len(os.listdir(TMP_FILEPATH))

def clean_temporary() -> None:
    if os.path.isdir(TMP_FILEPATH):
        shutil.rmtree(TMP_FILEPATH)
    return
