from ast import Is
from decimal import ROUND_DOWN
from msilib.schema import PublishComponent
from re import A
from LinearRegressionData import LinearRegressionData
from Konstanten import Konstanten
import numpy as np
import math
import matplotlib.pyplot as plt

CONST = Konstanten()
length = 0

matrix_list = [
    [], # index             0
    [], # feature           1
    [], # target            2
    [], # a                 3
    [], # d                 4
    [], # sum diffrence     5
    [], # my finding        6
    [], # difference        7
    [], # positiv target    8
    [], # x for plot        9
    []  # y for plot        10
]

class UserInterface:
    def __init__(self, a = 1, d = 0):
        self.a = a
        self.d = d

    @classmethod
    def show_graph():
        plt.figure()
        plt.plot(matrix[9], matrix[10])
        plt.scatter(matrix[1], matrix[2])
        plt.show()

    @classmethod
    def print_function(self):
        print("f(x) = " + str(self.a) + " * x " + str(self.d))

matrix = np.array

class MathFunction(UserInterface):
    def __init__(self, a = 1, d = 0):
        super().__init__(a, d)
        self.print_func = lambda x: super()._print_function()
    
    def set_d(self, d):
        self.d = d
    
    def set_a(self, a):
        self.a = a

    def calculate_graph(self, x : np.array):
        matrix[10] = np.add(np.multiply(self.a, x), self.d)
        matrix[9]  = np.copy(x)

math_function = MathFunction()

def show_all():
    UserInterface.print_function()
    UserInterface.show_graph()

def init_list():
    data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
    length = data.target["data"].size
    i = 0
    while i < length:
        matrix_list[0].append(int(i))
        i = i + 1
    matrix_list[1] = data.feature["data"]
    matrix_list[2] = data.target["data"]
    i = 3
    matrix[4] = data.target["data"]
    while i < 11:
        matrix_list[i].append(0)
        i = i + 1
        if i == 4:
            continue
    matrix = np.array(matrix_list)
    i = 0
    while i < matrix.size:
        np.array(matrix[i])
        i = i + 1

def init_a():
    i = 1
    half = int(length * 0.5)
    while i < half:
        matrix[3][i] = math.pow(matrix[3][i - 1], 2) * (-1)
        i = i + 1
    while i < length:
        matrix[3][i] = math.pow(matrix[3][i - 1], 2)
        i = i + 1
    while i < length:
        matrix[3][i] = math.pow(0.0001)
        i = i + 1

def init_d():
    pass

def make_row_plus(ind):
    return np.sqrt(np.power(matrix[ind], 2))

def init_differences(i):
    matrix[6] = np.add(np.multiply(matrix[3][i], matrix[1]), matrix[4][i])
    matrix[6] = make_row_plus(6)
    matrix[8] = make_row_plus(2)
    matrix[7] = np.subtract(matrix[6], matrix[8])
    matrix[7] = make_row_plus(7)

def get_key_by_value(value, index_search, index_result = 0):
    for i, v in np.arange(matrix[0]), np.arange(matrix[index_search]):
        if value == v:
            return float(matrix[index_result][i])
        else:
            return -1

def init_all_diffs():
    for i in range(0, length, 1):
        init_differences(i)
        matrix[5][i] = sum(matrix[7])
    ind_copy = np.array(matrix[0], dtype='int')
    max_diff = np.array(matrix[5], dtype=float)
    ld = get_key_by_value(max_diff, 5, index_result = 2)
    math_function.set_d(ld)

if __name__ == "__main__":
    execute = [init_list, init_a, init_d, init_all_diffs, show_all]
    for foo in execute:
        print(str(foo))
        try:
            foo()
        except NameError:
            print("error in: " + str(foo))
            print(str(NameError))