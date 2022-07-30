from LinearRegressionData import LinearRegressionData
from Konstanten import Konstanten
import numpy as np
import matplotlib.pyplot as plt

CONST = Konstanten()

def create_formula(x0, a):
    formular_string = "f(x) = " + str(x0) + " + (x * "  + str(a) + ")"
    return formular_string

def show_graph(arr_x, arr_Y, raw_x, raw_y, formel):
    plt.figure()
    plt.title(formel)
    plt.plot(arr_x, arr_Y)
    plt.scatter(raw_x, raw_y)
    plt.show()

class Funktions:
    def __init__(self):
        self.raw_data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
        self.length = self.raw_data.get_size()
        self.raw_x = np.sort(self.raw_data.feature["data"])
        self.raw_y = np.sort(self.raw_data.target["data"])
        self.avg_x = np.average(self.raw_x)
        self.avg_y = np.average(self.raw_y)

    def fb(self, avg_x, avg_y, raw_x, raw_y):
        a1, a2 = 0, 0
        for i in range(0, len(raw_x), 1):
            a1 += (raw_x[i] - avg_x) * (raw_y[i] - avg_y)
        for i in range(0, len(raw_x), 1):
            a2 += (raw_x[i] - avg_x) ** 2
        return (a1 / a2)

    def start_lrs(self):
        b = self.fb(self.avg_x, self.avg_y, self.raw_x, self.raw_y)
        a = self.avg_y - b * self.avg_x
        x1 = 0
        x2 = max(self.raw_x)
        y1 = a + b * x1
        y2 = a + b * x2
        formel = create_formula(x1, a)
        print(formel)
        show_graph([x1, x2], [y1, y2], self.raw_x, self.raw_y, formel)

if __name__ == "__main__":
    f = Funktions()
    f.start_lrs()