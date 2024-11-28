class DiaFunctions:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dodav(self):
        return self.a + self.b

    def vidniman(self):
        return self.a - self.b

    def dilena(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Ділити на нуль не можна!"

    def mnozena(self):
        return self.a * self.b
