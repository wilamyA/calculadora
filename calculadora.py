from operacaoFabrica import OperacaoFabrica

class Calculadora (object):

    def calcular(self, valor1, valor2, operador):
        operacao_fabrica = OperacaoFabrica()
        operacao = operacao_fabrica.criar(operador)
        if(operacao == None):
            return 0
        else:
            return operacao.executar(valor1, valor2)
