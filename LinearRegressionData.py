import pandas as pd

class LinearRegressionData:
    def start(self, dataObj, path):
        self.feature = {"name": dataObj["feature"]}    # T3
        self.target = {"name": dataObj["target"]}     # T4
        df = pd.read_csv(path)
        print(df)
        df = df.head(df.size)
        self.feature["data"] = df[dataObj["feature"]].tolist()
        self.target["data"] = df[dataObj["target"]].tolist()
        print(self.feature)
        print(self.target)

    def __init__(self, *args):
        self.feature = None
        self.target = None
        var = []
        for e in args:
            if isinstance(e, dict):
                var.append(e)
            elif isinstance(e, str):
                var.append(e)
        self.start(var[0], var[1])