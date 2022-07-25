from LinearRegressionData import LinearRegressionData
from Konstanten import Konstanten
import numpy as np
import matplotlib.pyplot as plt

CONST = Konstanten()

length = 0
matrix = None

def create_formula(y_achse):
    formular_string = "f(x) = " + str(matrix[2][0][1][0]) + " * x + " + str(y_achse)
    return formular_string

def make_my_values(a, b, x):
    return (a + b * x)

def show_graph():
    plt.figure()
    plt.title(create_formula(0))
    plt.plot(matrix[0][0][0], matrix[2][0][2])
    plt.scatter(matrix[0][0][0], matrix[0][1][0])
    plt.show()

def foo_b(avg_x, avg_y, raw_x, raw_y):
    a = 0
    for i in range(1, length):
        a += (raw_x[i] - avg_x) * (raw_y[i] - avg_y)
    for i in range(1, length):
        a += (raw_x[i] - avg_x) ** 2
    return a

if __name__ == "__main__":
    raw_data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
    length = raw_data.get_size()
    print("length : ", length)
    matrix = np.array(np.zeros((3, 2, 3, length), dtype = np.float64))
    # ------------------------- Dimension 0
    for i in range(length):
        matrix[0][0][0][i] = np.float64(raw_data.feature["data"][i])
    for i in range(length):
        matrix[0][0][1][i] = np.float64(raw_data.target["data"][i])
    raw_x = matrix[0][0][0]
    raw_y = matrix[0][1][0]
    avg_x = np.average(raw_x)
    avg_y = np.average(raw_y)
    matrix[2][0][0][0] = foo_b(avg_x, avg_y, raw_x, raw_y)
    matrix[2][0][2][0] = avg_y - matrix[2][0][0][0] * avg_x
    matrix[2][0][2][0] = matrix[2][0][0][0] * matrix[0][0][0][0] + matrix[2][0][2][0]
    show_graph()