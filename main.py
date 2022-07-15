from LinearRegressionData import LinearRegressionData
from Konstanten import Konstanten

CONST = Konstanten()

def ersteFormel():
    m = len(data.feature["data"])
    a = 1 / (2 * m)
    s = []
    for i in range(0, m):
        unquadriert = foo(data.feature["data"][i]) - data.target["data"][i]
        s.append(unquadriert * unquadriert)
    min = a * sum(s)
    return min

def foo(p):
    return (650 / 400) * p

if __name__ == '__main__':
    data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
    print(ersteFormel())