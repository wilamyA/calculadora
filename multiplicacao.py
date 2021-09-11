from operacao import Operacao


class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 * valor2