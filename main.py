from LinearRegressionData import LinearRegressionData
from Konstanten import Konstanten

CONST = Konstanten()

if __name__ == '__main__':
    data = LinearRegressionData({"feature" : "T3", "target" : "T4"}, CONST.get_path_to_csv())
    print(data)