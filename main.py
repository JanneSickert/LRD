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

def create_formula(a, d):
    formular_string = "f(x) = " + str(a) + " * x " + str(d)
    return formular_string

def make_my_values(a, d, x):
    return (a*x+d)

def show_graph(data, a, x, d):
    plt.figure()
    plt.title(create_formula(a, d))
    x, y = [], []
    for e in data.feature["data"]:
        x.append(float(e))
        y.append(float(make_my_values(a, d, e)))
    plt.plot(x, y)
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
    return (betrag(diffrent) < betrag(value))

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
    step_d = max_target / average_increase
    steps_a = winkel_berechnen(average_increase, data, max_feature)
    max_increased = average_increase
    r = MyRange(-(length / 2), (length / 2), 1)
    z = r.get_data()
    k = 0
    vorzeichen = 1
    while k < length:
        a = steps_a[k]
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
        diffrent = calculate_distance(steps_a[min_value_a["index"]], d, data)
        if hat_diffrent_weniger_abstand(diffrent, min_value["value"]):
            min_value["value"] = diffrent
            min_value["index"] = k
            min_value["plus_or_minus"] = "+"
        k = k + 1
        if k % 10 == 0:
            vorzeichen = vorzeichen * (-1)
    formula = create_formula(steps_a[min_value_a["index"]], d)
    ppd = mittelwert - (min_value["index"] * step_d)
    px = data.feature["data"][min_value["index"]]
    pd = mittelwert - (min_value["index"] * step_d)
    search = []
    ka = 0
    for e in data.target["data"]:
         o = {"index": ka, "y-achsenabschnitt": e, "a": steps_a[min_value_a["index"]], "d": pd, "y-achsenabschnitt": e, "value": 0}
         o["value"] = calculate_distance(o["a"], o["d"], data)
         search.append(o)
         ka = ka + 1
    minimum, search_index = 640000, 0
    for e in search:
        if e["value"] < minimum:
            minimum = e["value"]
            search_index = e["index"]
    print(formula)
    show_graph(data, steps_a[min_value["index"]], px, search[search_index]["y-achsenabschnitt"])
    print("end LRD")