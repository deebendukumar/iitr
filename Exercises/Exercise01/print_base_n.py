#
import math
from tabulate import tabulate

def base_table(base, max_numbers):
    if base > 16:
        return False

    table = []
    for index in range(max_numbers):
        if is_valid(base, index):
            table.append(index)
    return table

def is_valid(base, number) -> bool:
    array = ""
    for index in range(base):
        array += str(index)
    return all(digit in array for digit in str(number))

def print_table(base, table):
    table_str = ""
    for index, item in enumerate(table):
        table_str += ("%6d" % item) + "\t"
        if (index + 1) % base == 0:
            table_str += "\n"
    return table_str

base = 8
result = base_table(base, 100)
print(print_table(base, result))