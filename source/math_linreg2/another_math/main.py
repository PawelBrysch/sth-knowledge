"""
openpyxl -  o czym pamiętac? ->                                                           `workbook.save(path)` na koncu
"""


import numpy as np
import random
import copy
import openpyxl

PATH_TO_EXCEL = rf"C:\Users\Lenovo\Desktop\PROJECTS\django_top2\sth-knowledge\source\another_math\output.xlsx"
SHEET_NAME = "Sheet1"


def write_array(path_, sheet_name, origin_row, origin_column, array):
    workbook = openpyxl.load_workbook(path_)
    sheet = workbook[sheet_name]
    for row in range(0, 4):
        for column in range(0, 4):
            sheet.cell( origin_row + row, origin_column + column).value = array[row, column]
    workbook.save(path_)


def get_random_4x4():
    return np.array([random.randint(1, 4) for i in range(16)]).reshape(4, 4)


def get_dets(array_):
    array_as_list = []
    for row in range(0, 4):
        for column in range(0, 4):
            array_as_list.append(
                np.linalg.det(
                    np.delete(
                        np.delete(array_, column, 1),
                        row, 0
                    )
                )
            )
    return np.array(array_as_list).reshape(4, 4)


def minus(array):
    result = copy.deepcopy(array)
    for row in range(0, 4):
        for column in range(0, 4):
            result[row, column] = ((-1) ** (row + column)) * array[row, column]
    return result


class Matrix:
    def __init__(self, base):
        self.base = base
        self.dets_raw = get_dets(self.base)
        self.dets_minus = minus(self.dets_raw)
        self.elems_raw = self.base * self.dets_raw
        self.elems_minus = minus(self.elems_raw)

    def save_to_excel(self, origin_row):
        arrays = [self.base, self.dets_raw, self.dets_minus, self.elems_raw, self.elems_minus]
        column = 3
        for array in arrays:
            write_array(PATH_TO_EXCEL, SHEET_NAME, origin_row, column, array)
            column += 6

a = Matrix(get_random_4x4())
b = Matrix(get_random_4x4())
c = Matrix(np.matmul(a.base, b.base))

# array = a.dets_raw
# write_array(PATH_TO_EXCEL, SHEET_NAME, 6, 7, a.base)

# a.save_to_excel(3)
# b.save_to_excel(9)
# c.save_to_excel(15)
