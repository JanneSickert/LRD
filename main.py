from LinearRegressionData import LinearRegressionData
from Konstanten import Konstanten
import numpy as np
import math
import matplotlib.pyplot as plt

CONST = Konstanten()
length = None

def test_function(a, x, d):
    return (np.add(np.multiply(x, a), d))

def calculate_distance(a, d, data):
    return np.sum(np.sqrt(np.power(np.subtract(test_function(a, data.feature["data"], d), data.target["data"]), 2)))

def calculate_mittelwert(data):
    summe = np.sum(data.target["data"])
    average = summe / length
    return average

def calculate_average_increase(data):
    s = (np.sum(np.divide(data.target["data"], data.feature["data"]))) / length
    return s

def create_formula(a, d):
    formular_string = "f(x) = " + str(a) + " * x " + str(d)
    return formular_string

def make_my_values(a, d, x):
    return (a*x+d)

def show_graph(data, min_value, a, x, d):
    plt.figure()
    plt.title(create_formula(a, d, min_value))
    foooo = [data.feature["data"][length - 1], make_my_values(a, d, x)]
    plt.plot([[0, d], foooo])
    plt.scatter(data.feature["data"], data.target["data"])
    plt.show()

def winkel_berechnen(average_increase, data, max_feature):
    # --------------------------------------
    # Hypotenuse: a² + b² = C²
    # cos(α) = (Ankathete / Hypotenuse)
    # -------------------------------------
        i = 0
        cos = []
        while i < data.target["data"].size:
            a2, b2 = data.target["data"][i] ** 2, data.feature["data"][i] ** 2
            c2 = a2 + b2
            c = c2 ** (0.5)
            a = max_feature / c
            cos.append(a)
            i = i + 1
        return cos

class MyRange:
    def __init__(self, p_from : int, p_to : int, p_step : int):
        self.p_from = p_from
        self.p_to = p_to
        self.p_step = p_step
        self.len = 0
        self.arr_nr = []
        self.arr_i = []

    def get_data(self):
        i = 0
        n = self.p_from
        while i < length:
            self.arr_nr.append(n)
            self.arr_i.append(i)
            i = i + 1
            n = n + self.p_step
        return [self.arr_i, self.arr_nr]

def hat_diffrent_weniger_abstand(diffrent, value):
    d = (diffrent ** 2) ** (0.5)
    m = (value) ** (0.5)
    return (d < m)

if __name__ == '__main__':
    print("start LRD")
    data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
    length = data.target["data"].size
    mittelwert = calculate_mittelwert(data)
    min_value = {"index": 0, "value": math.inf, "plus_or_minus": None}  # min_value object
    min_value_a = {"index": 0, "value": math.inf, "plus_or_minus": None}
    min_value["value"] = calculate_distance(1, mittelwert, data)    # y = x + d
    average_increase = calculate_average_increase(data)
    max_target, max_feature = max(data.target["data"]), max(data.feature["data"])
    step_d = max_target / average_increase / CONST.get_accuracy()
    steps_a = winkel_berechnen(average_increase, data, max_feature)
    max_increased = average_increase / CONST.get_accuracy()
    r = MyRange(-(length / 2), (length / 2), 1)
    z = r.get_data()
    k = 0
    vorzeichen = 1
    while k < length:
        a = steps_a
        diffrent = calculate_distance(a, mittelwert, data)
        if hat_diffrent_weniger_abstand(diffrent, min_value["value"]):
            min_value_a["value"] = diffrent
            min_value_a["index"] = k
            min_value_a["plus_or_minus"] = "+"
        k = k + 1
        if k % 10 == 0:
            vorzeichen = vorzeichen * (-1)
    k = 0
    vorzeichen = 1
    while k < length:
        d = mittelwert - (((k - length) / 2) * step_d)
        diffrent = calculate_distance(0, d, data)
        if hat_diffrent_weniger_abstand(diffrent, min_value["value"]):
            min_value["value"] = diffrent
            min_value["index"] = k
            min_value["plus_or_minus"] = "+"
        k = k + 1
        if k % 10 == 0:
            vorzeichen = vorzeichen * (-1)
    formula = create_formula(2, d)
    ppd = mittelwert - (min_value["index"] * step_d)
    px = data.feature["data"][min_value["index"]]
    pd = mittelwert - (min_value["index"] * step_d)
    show_graph(data, min_value, steps_a[min_value_a["index"]], px, pd)
    print(formula)
    print("end LRD")