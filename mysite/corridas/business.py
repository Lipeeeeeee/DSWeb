

class CalculaCorrida:
    def __init__(self, km, precoKm = 5):
        self.km = km
        self.precoKm = precoKm

    def getValor(self):
        return self.km * self.precoKm

class CalculaCorridaUberX(CalculaCorrida):
    ...

class CalculaCorridaUberMoto(CalculaCorrida):
    def getValor(self):
        return 0.9 * super().getValor()

class CalculaCorridaUberBlack(CalculaCorrida):
    def getValor(self):
        return 1.1 * super().getValor()

class CalculaCorridaUberPool(CalculaCorrida):
    def __init__(self, km, precoKm = 5, numPassageiros = 1):
        self.numPassageiros = numPassageiros
        super().__init__(km, precoKm)

    def getValor(self):
        return super().getValor() / self.numPassageiros