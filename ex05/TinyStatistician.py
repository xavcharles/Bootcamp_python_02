import numpy as np

class TinyStatistician:
    def __init__(self):
        return
    

    def mean(self, x):
        if (isinstance(x, list) and x) or (isinstance(x, np.ndarray) and x.size > 0):
            mean = float(sum(val for val in x) / len(x))
        else:
            return None
        return mean

    def median(self, x):
        if (isinstance(x, list) and x) or (isinstance(x, np.ndarray) and x.size > 0):
            y = x
            y.sort()
            if len(x) % 2 == 1:
                return float(y[int(len(y) / 2)])
            else:
                return (self.mean([y[int((len(y) / 2) - 1)], y[int(len(y) / 2)]]))
        else:
            return None

    def quartiles(self, x):
        if (isinstance(x, list) and x) or (isinstance(x, np.ndarray) and x.size > 0):
            y = x
            y.sort()
            if len(x) % 2 == 1:
                if ((len(x) / 2) % 2 == 1):
                    return (float(y[]))
