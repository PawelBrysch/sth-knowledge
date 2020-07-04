""" slicing not always works"""
import numpy as np


def print_first_row(arr, message):
    try:
        arr[0, :]
    except:
        print(message)


def print_first_column(arr, message):
    try:
        arr[:, 0]
    except:
        print(message)


quadratic = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
row = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
column = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])

print_first_column(quadratic, "quadratic")
print_first_column(row, "row")
print_first_column(column, "column")

print_first_row(quadratic, "quadratic")
print_first_row(row, "row")
print_first_row(column, "column")

"""
dlaczego tak jest-?                                                               wskazówka: przeczytaj komunikat erroru
"""