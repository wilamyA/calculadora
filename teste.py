from calculadora import Calculadora
from unittest import TestCase


class Testes(TestCase):
    def teste_soma(self):
        calculador = Calculadora()
        resultado = calculador.calcular(6, 6, 'soma')
        print(resultado)
        self.assertEqual(resultado, 12)
    
    def teste_multiplicacao(self):
        calculador = Calculadora()
        resultado = calculador.calcular(6, 6, 'multiplicacao')
        print(resultado)
        self.assertEqual(resultado, 36)
    
    def teste_subtracao(self):
        calculador = Calculadora()
        resultado = calculador.calcular(6, 5, 'subtracao')
        print(resultado)
        self.assertEqual(resultado, 1)
    
    def teste_divisao(self):
        calculador = Calculadora()
        resultado = calculador.calcular(6, 2, 'divisao')
        print(resultado)
        self.assertEqual(resultado, 3)
    
    def test_operacao_invalida(self):
        calculador = Calculadora()
        resultado = calculador.calcular(6, 6, 'multiplicação')
        print(resultado)
        self.assertEqual(resultado, 0)
