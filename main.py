from LinearRegressionData import LinearRegressionData
from Konstanten import Konstanten
import numpy as np
import math
import matplotlib.pyplot as plt

CONST = Konstanten()
length = None

def betrag(nr):
    return (math.sqrt(math.pow(nr, 2)))

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

def create_formula(**vars):
    formular_string = "f(x) = " + str(vars["a"]) + " * x + " + str(vars["y_achsenabschnitt"])
    return formular_string

def make_my_values(a, d, x):
    return (a*x+d)

def show_graph(data, **vars):
    plt.figure()
    plt.title(create_formula(a = vars["a"], y_achsenabschnitt = vars["y_achsenabschnitt"]))
    x, y = [], []
    x.append(0)
    y.append(vars["y_achsenabschnitt"])
    for e in data.feature["data"]:
        x.append(float(e))
        y.append(float(make_my_values(vars["a"], vars["y_achsenabschnitt"], e)))
    for i in range(len(x)):
        print("x:", x[i], "y:", y[i])
    plt.plot(x, y)
    plt.scatter(data.feature["data"], data.target["data"])
    plt.show()

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
    return (betrag(diffrent) < betrag(value))

def y_achse_berechnen(target):
    target = np.array(target)
    sort = np.sort(target)
    return sort

def winkel_berechnen(data, max_feature):
    # --------------------------------------
    # Hypotenuse: a² + b² = C²
    # cos(α) = (Ankathete / Hypotenuse)
    # -------------------------------------
    i = 0
    cos = []
    while i < length:
        a2, b2 = data.target["data"][i] ** 2, data.feature["data"][i] ** 2
        c2 = a2 + b2
        c = c2 ** (0.5)
        a = max_feature / c
        cos.append(a)
        i = i + 1
    return cos

min_value = {"index": 0, "value": math.inf, "a": 0.0, "d": 0, "y_achsenabschnitt": 0}

def rotate(data, ka, kd, steps_a, steps_d):
    k = 0
    while k < length:
        a = steps_a[ka]
        d = steps_d[kd]
        diffrent = calculate_distance(a, d, data)
        if hat_diffrent_weniger_abstand(diffrent, min_value["value"]):
            min_value["value"] = diffrent
            min_value["index"] = k
            min_value["a"] = a
            min_value["d"] = d
            min_value["y_achsenabschnitt"] = d
        k = k + 1

if __name__ == '__main__':
    print("start LRD")
    data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
    length = data.target["data"].size
    mittelwert = calculate_mittelwert(data)
    min_value["value"] = calculate_distance(1, mittelwert, data)    # y = x + d
    average_increase = calculate_average_increase(data)
    max_target, max_feature = max(data.target["data"]), max(data.feature["data"])
    steps_d = y_achse_berechnen(data.target["data"])
    steps_a = winkel_berechnen(data, max_feature)
    max_increased = average_increase
    r = MyRange(-(length / 2), (length / 2), 1)
    z = r.get_data()
    ka, kd = 0, 0
    zbf = length ** 2
    print("zu berechnende functionen: ", zbf)
    while kd < length:
        while ka < length:
            rotate(data, ka, kd, steps_a, steps_d)
            ka = ka + 1
            zbf = zbf - 1
            print("zu berechnende functionen: ", zbf)
            if ka % 10 == 0:
                print(create_formula(a = min_value["a"], y_achsenabschnitt = min_value["y_achsenabschnitt"]))
        ka = 0
        kd = kd + 1
    print(str(min_value))
    show_graph(data, a = min_value["a"], y_achsenabschnitt = min_value["y_achsenabschnitt"])