from ast import IsNot
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

def create_formula(a, d, min_value):
    if d < 0:
        d = " - " + str(d)
    elif d > 0:
        d = " + " + str(d)
    else:
        d = ""
    formular_string = "f(x) = " + min_value["plus_or_minus"] + " " + str(a) + " * x " + str(d)
    return formular_string

def make_my_values(a, d, x):
    return (a*x+d)

def show_graph(data, min_value, a = 1, x = 1, d = 0):
    plt.figure()
    plt.title(create_formula(a, d, min_value))
    foooo = [data.feature["data"][length - 1], make_my_values(a, d, x)]
    plt.plot([[0, d], foooo])
    plt.scatter(data.feature["data"], data.target["data"])
    plt.show()

def winkel_berechnen(average_increase, data, max_feature):
    # --------------------------------------
    # cos(α) = (Ankathete / Hypotenuse)
    # -------------------------------------
        i = 0
        cos = []
        while i < data.target["data"].size:
            t, f = data.target["data"][i] ** 2, data.feature["data"][i] ** 2
            e = max_feature / (math.sqrt(t) + math.sqrt(f))
            print(average_increase)
            cos.append(e)
            i = i + 1
        return cos

if __name__ == '__main__':
    print("start LRD")
    data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
    length = data.target["data"].size
    mittelwert = calculate_mittelwert(data)
    min_value = {"index": 0, "value": math.inf, "plus_or_minus": None}  # min_value object
    min_value["value"] = calculate_distance(1, mittelwert, data)    # y = x + d
    average_increase = calculate_average_increase(data)
    max_target, max_feature = max(data.target["data"]), max(data.feature["data"])
    step_d = max_target / average_increase / CONST.get_accuracy()
    steps_a = winkel_berechnen(average_increase, data, max_feature)
    max_increased = average_increase / CONST.get_accuracy()
    b = True
    step = 0
    while b:    # function rise
        a, d = steps_a[step] * step, mittelwert - (step * step_d)
        diffrent = calculate_distance(a, d, data)
        if diffrent < min_value["value"]:
            min_value["value"] = diffrent
            min_value["index"] = step
            min_value["plus_or_minus"] = "+"
        if step <= len(steps_a):
            b = False
        else:
            step = step + 1
    b = True
    step = 0
    while b:    # function fall
        a, d = steps_a[step] * step, mittelwert - (step * step_d)
        diffrent = calculate_distance(a, d, data)
        if diffrent < min_value["value"]:
            min_value["value"] = diffrent
            min_value["index"] = step
            min_value["plus_or_minus"] = "-"
        if step >= ((-1) * len(steps_a)):
            b = False
        else:
            step = step - 1
    formula = create_formula(a, d, min_value)
    pa, pd = steps_a[min_value["index"]] * step, mittelwert - (min_value["index"] * step_d)
    px = data.feature["data"][min_value["index"]]
    show_graph(data, min_value, a = pa, x = pa, d = pd)
    print(formula)
    print("end LRD")