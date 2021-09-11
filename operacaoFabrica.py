from soma import Soma
from subtracao import Subtracao
from divisao import Divisao
from multiplicacao import Multiplicacao


class OperacaoFabrica(object):

    def criar(self, operador):
        if(operador == "soma"):
            return Soma()
        elif (operador == "subtracao"):
            return Subtracao()
        elif (operador == "divisao"):
            return Divisao()
        elif (operador == "multiplicacao"):
            return Multiplicacao()
