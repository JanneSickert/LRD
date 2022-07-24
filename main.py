from LinearRegressionData import LinearRegressionData
from Konstanten import Konstanten
import numpy as np
import matplotlib.pyplot as plt

CONST = Konstanten()

length = 0
matrix = None

if __name__ == "__main__":
    raw_data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
    length = raw_data.get_size()
    matrix = np.array(np.zeros((3, 2, 3, length), dtype = np.float64))
    for i in range(length):
        matrix[0][0][0][i] = np.float64(raw_data.feature["data"][i])
    for i in range(length):
        matrix[0][0][1][i] = np.float64(raw_data.target["data"][i])
    matrix[0][0][1][0] = np.sum(matrix[0][0][0])
    matrix[0][1][1][0] = np.sum(matrix[0][0][1])
    matrix[0][0][2][0] = np.divide(matrix[0][1][1][0], np.float64(length))
    matrix[0][1][2][0] = np.divide(matrix[0][0][1][0], np.float64(length))
    for x, y in matrix[0, 0]:
        matrix[1, 0, 0] = [xx - matrix[0, 0, 2] for xx in x]
        matrix[1, 1, 0] = [yy - matrix[0, 1, 2] for yy in y]
    for x, y in matrix[0, 0]:
        matrix[1, 0, 1] = [xx - matrix[0, 0, 2] for xx in x]
        matrix[1, 1, 1] = [yy - matrix[0, 1, 2] for yy in y]
    for i in range(length):
        matrix[1][0][2][i] = matrix[1][0][1][i] - matrix[1][1][1][i]
        matrix[1][1][2][i] = matrix[1][0][1][i] ** 2
        matrix[2][1][0][0] = np.sum(matrix[1][0][2])
        matrix[2][1][1][0] = np.sum(matrix[1][1][2])