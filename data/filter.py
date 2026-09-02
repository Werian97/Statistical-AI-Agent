import csv
from data.read_data import Table

Row = list[str]
Rows = list[Row]

def filter_by_exact_value(table: Table, field: str, value: str):
    # Return a subtable containing only the rows having 'value'
    # in the corresponding field column.
    # The fields remain the same
    i = table.get_field_index(field)
    new_rows: Rows = []
    for row in table.rows:
        if row[i] == value:
            new_rows.append(row.copy())

    return Table(table.fields, new_rows)

def filter_by_numerical_range(table: Table, field: str, min_value: float, max_value: float):
    i: int = table.get_field_index(field)
    new_rows: Rows = []
    for row in table.rows:
        try:
            row_value_floated: float = float(row[i])
        except Exception:
            raise ValueError("You can filter by range only numerical values")
        if min_value < row_value_floated and row_value_floated < max_value:
            new_rows.append(row.copy())
    return Table(table.fields, new_rows)

def filter_by_alphabetical_range(table: Table, field: str, min_value: str, max_value: str):
    i: int = table.get_field_index(field)
    new_rows: Rows = []
    for row in table.rows:
        if min_value < row[i] and row[i] < max_value:
            new_rows.append(row.copy())
    return Table(table.fields, new_rows)

def remove_exact_value(table: Table, field: str, value: str):
    removed_at_least_once: bool = False
    i = table.get_field_index(field)
    new_rows: Rows = []
    for row in table.rows:
        if row[i] != value:
            new_rows.append(row.copy())
        else:
            removed_at_least_once = True
    if removed_at_least_once:
        return Table(table.fields, new_rows)
    raise ValueError(f"The value: {value} is not present in the column {field}")

def remove_numerical_range(table: Table, field: str, min_value: float, max_value: float):
    removed_at_least_once: bool = False
    i: int = table.get_field_index(field)
    new_rows: Rows = []
    for row in table.rows:
        try:
            row_value_floated: float = float(row[i])
        except Exception:
            raise ValueError("You can filter by range only numerical values")
        if min_value >= row_value_floated or row_value_floated >= max_value:
            new_rows.append(row.copy())
        else:
            removed_at_least_once = True
    if removed_at_least_once:
        return Table(table.fields, new_rows)
    raise ValueError(f"There are no values between {min_value} and {max_value} in the column {field}")

def remove_alphabetical_range(table: Table, field: str, min_value: str, max_value: str):
    removed_at_least_once: bool = False
    i: int = table.get_field_index(field)
    new_rows: Rows = []
    for row in table.rows:
        if min_value >= row[i] or row[i] >= max_value:
            new_rows.append(row.copy())
        else:
            removed_at_least_once = True
    if removed_at_least_once:
        return Table(table.fields, new_rows)
    raise ValueError(f"There are no values between {min_value} and {max_value} in the column {field}")
