import abc
from unittest import TestCase, main

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def executar(self, valor1, valor2):
        pass