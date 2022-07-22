import pandas as pd

class LinearRegressionData:
    def __start(self, dataObj, path):
        self.feature = {"name": dataObj["feature"]}    # T3
        self.target = {"name": dataObj["target"]}     # T4
        df = pd.read_csv(path)
        df = df.head(df.size)
        self.feature["data"] = df[dataObj["feature"]]
        self.target["data"] = df[dataObj["target"]]

    def __init__(self, *args):
        self.feature = None
        self.target = None
        var = []
        for e in args:
            if isinstance(e, dict):
                var.append(e)
            elif isinstance(e, str):
                var.append(e)
        self.__start(var[0], var[1])