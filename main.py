from LinearRegressionData import LinearRegressionData
from Konstanten import Konstanten
import numpy as np
import matplotlib.pyplot as plt

CONST = Konstanten()

length = 0
matrix = None
a_a, a_b = 0, 0

def print_vars():
    print(a_a, a_b)

def create_formula():
    formular_string = "f(x) = " + str(a_a) + " + (x * "  + str(a_b) + ")"
    return formular_string

def make_my_values(a, b, x):
    return (a + b * x)

def show_graph(arr_x, arr_Y, raw_x, raw_y):
    fff = create_formula()
    plt.figure()
    plt.title(fff)
    plt.plot(arr_x, arr_Y)
    plt.scatter(raw_x, raw_y)
    plt.show()
    return fff

def foo_b(avg_x, avg_y, raw_x, raw_y):
    a1, a2 = 0, 0
    for i in range(0, length, 1):
        a1 += (raw_x[i] - avg_x) * (raw_y[i] - avg_y)
    for i in range(0, length), 1:
        a2 += (raw_x[i] - avg_x) ** 2
    return (a1 / a2)

def start_lrs():
    raw_data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
    length = raw_data.get_size()
    raw_x = np.sort(raw_data.feature["data"])
    raw_y = np.sort(raw_data.target["data"])
    avg_x = np.average(raw_x)
    avg_y = np.average(raw_y)
    a_b = foo_b(avg_x, avg_y, raw_x, raw_y)
    a_a = avg_y - (a_b * avg_x)
    x = [0, raw_data.feature["data"][int(length / 2)]]
    y = avg_x + a_b * avg_x
    arr_x = [0,  max(raw_x)]
    arr_y = [a_b, y]
    math_function_as_string = show_graph(arr_x, arr_y, raw_x, raw_y)
    return math_function_as_string

if __name__ == "__main__":
    start_lrs()