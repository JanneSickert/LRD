from LinearRegressionData import LinearRegressionData
from Konstanten import Konstanten
import numpy as np
import math
import matplotlib.pyplot as plt

CONST = Konstanten()
length = None
a_feature = None
a_target = None
min_value = {"index": 0, "value": math.inf, "a": 0.0, "d": 0, "y_achsenabschnitt": 0}

def betrag(nr):
    return (math.sqrt(math.pow(nr, 2)))

def test_function(a, x, d):
    return (np.add(np.multiply(x, a), d))

def calculate_distance(a, d):
    return np.sum(np.sqrt(np.power(np.subtract(test_function(a, a_feature, d), a_target), 2)))

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

def y_achse_berechnen():
    sort = np.sort(a_target)
    return sort

def winkel_berechnen():
    # --------------------------------------
    # Hypotenuse: a² + b² = C²
    # cos(α) = (Ankathete / Hypotenuse)
    # -------------------------------------
    i = 0
    cos = []
    while i < length:
        a2, b2 = a_target[i] ** 2, a_feature[i] ** 2
        c2 = a2 + b2
        c = c2 ** (0.5)
        a = np.max(a_feature) / c
        cos.append(float(a))
        i = i + 1
    cos = np.array(cos)
    np.sort(cos)
    return cos

def rotated_over_function_line(data, ka, kd, steps_a, steps_d):
    k = 0
    while k < length:
        a = steps_a[ka]
        d = steps_d[kd]
        diffrent = calculate_distance(a, d)
        if (betrag(diffrent) < betrag(min_value["value"])):
            min_value["value"] = diffrent
            min_value["index"] = k
            min_value["a"] = a
            min_value["d"] = d
            min_value["y_achsenabschnitt"] = d
        k = k + 1

def rotate_over_x_is_null(steps_a, steps_d):
    ka, kd = 0, 0
    zbf = length ** 2
    print("zu berechnende functionen: ", zbf)
    while kd < length:
        while ka < length:
            rotated_over_function_line(data, ka, kd, steps_a, steps_d)
            ka = ka + 1
            zbf = zbf - 1
            if ka % 10 == 0:
                print(create_formula(
                    a = min_value["a"], 
                    y_achsenabschnitt = min_value["y_achsenabschnitt"])
                )
                print("zu berechnende functionen: ", zbf)
        ka = 0
        kd = kd + 1

if __name__ == '__main__':
    print("start LRD")
    data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
    length = data.target["data"].size
    a_feature = np.array(data.feature["data"])
    a_target =  np.array(data.target["data"])
    steps_a, steps_d = winkel_berechnen(), y_achse_berechnen()
    print(steps_a, steps_d)
    rotate_over_x_is_null(steps_a, steps_d)
    steps_d = np.multiply(steps_d, (-1))
    rotate_over_x_is_null(steps_a, steps_d)
    print(str(min_value))
    show_graph(data, a = min_value["a"], y_achsenabschnitt = min_value["y_achsenabschnitt"])
    create_formula(a = min_value["index"], y_achsenabschnitt = min_value["y_achsenabschnitt"])
    print("ende")