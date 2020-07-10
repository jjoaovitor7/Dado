import random

class Dado(object):
    def __init__(self, cor="vermelho", lado=6):
        self._cor = cor
        self._lado = lado

    def setCor(self, cor):
        self._cor = cor

    def getCor(self):
        return self._cor

    def setLado(self, qtde):
        self._lado = random.randint(1, qtde)

    def getLado(self):
        return self._lado
