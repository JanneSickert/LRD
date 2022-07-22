class Konstanten:
    def __init__(self):
        self.__PATH_TO_CSV = "data.csv"
        self.ACCURACY = 10

    def get_path_to_csv(self):
        return self.__PATH_TO_CSV

    def get_accuracy(self):
        return self.ACCURACY