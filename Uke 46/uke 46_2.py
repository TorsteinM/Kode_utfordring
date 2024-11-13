from math import factorial as f
class Pascal_Rad:
    def __init__(self, N):
        self.rad = [f(x + i)//(f(x)*f(i)) for x, i in enumerate(range(N,-1,-1), 0)]
    def __repr__(self, sep=" "):
        return sep.join([str(x) for x in self.rad])