import csv
from typing import Callable
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


def filter(table: Table, filters: dict):
    filter_list: list[tuple[dict | None, Callable]] = [
        (filters.get("exact_value"), filter_by_exact_value),
        (filters.get("numerical_range"), filter_by_numerical_range),
        (filters.get("alphabetical_range"), filter_by_alphabetical_range),
        (filters.get("exact_value_remove"), remove_exact_value),
        (filters.get("numerical_range_remove"),remove_numerical_range),
        (filters.get("alphabetical_range_remove"), remove_alphabetical_range)
    ]
    filtered_table: Table = table
    for i, item in enumerate(filter_list):
        if item[0] is not None:
            if i%3 == 0:
                for field in item[0]:
                    value = item[0].get(field)
                    filtered_table = item[1](filtered_table, field, value)
            else:
                for field in item[0]:
                    min_max: dict = item[0][field]
                    filtered_table = item[1](filtered_table, field, **min_max)
    save_csv(filtered_table)
    return filtered_table

def save_csv(table: Table):
    pass
            

    


filters: dict = {
    "exact_value": {
        "price": "550000.0",
        "bedrooms": "3.0"
    },
    "numerical_range": {
        "yr_built": {
            "min_value": 1950,
            "max_value": float("+inf")
        }
    }
}
