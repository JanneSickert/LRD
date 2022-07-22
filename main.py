from LinearRegressionData import LinearRegressionData
from Konstanten import Konstanten
import numpy as np
import math

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

def create_formula(step_a, step_d, mittelwert, min_value):
    a, d = step_a * min_value["index"], mittelwert - (min_value["index"] * step_d)
    if d < 0:
        d = " - " + str(d)
    elif d > 0:
        d = " + " + str(d)
    else:
        d = ""
    formular_string = "f(x) = " + min_value["plus_or_minus"] + " " + str(a) + " * x " + str(d)
    return formular_string

if __name__ == '__main__':
    print("start LRD")
    data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
    length = data.target["data"].size
    mittelwert = calculate_mittelwert(data)
    min_value = {"index": 0, "value": math.inf, "plus_or_minus": None}  # min_value object
    min_value["value"] = calculate_distance(1, mittelwert, data)    # y = x + d
    average_increase = calculate_average_increase(data)
    max_target = max(data.target["data"])
    step_d = max_target / average_increase / CONST.get_accuracy()
    step_a = step_d / max_target
    max_increased = average_increase / CONST.get_accuracy()
    b = True
    step = 1
    while b:    # function rise
        a, d = step_a * step, mittelwert - (step * step_d)
        diffrent = calculate_distance(a, d, data)
        if diffrent < min_value["value"]:
            min_value["value"] = diffrent
            min_value["index"] = step
            min_value["plus_or_minus"] = "+"
        if test_function(a, max(data.feature["data"]), d) > (max_target * 2):
            b = False
        else:
            step = step + 1
    b = True
    step = -1
    while b:    # function fall
        a, d = step_a * step, mittelwert - (step * step_d)
        diffrent = calculate_distance(a, d, data)
        if diffrent < min_value["value"]:
            min_value["value"] = diffrent
            min_value["index"] = step
            min_value["plus_or_minus"] = "-"
        if test_function(a, min(data.feature["data"]), d) < (min(data.target["data"]) * 2):
            b = False
        else:
            step = step - 1
    formula = create_formula(step_a, step_d, mittelwert, min_value)
    print(formula)
    print("end LRD")