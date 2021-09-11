from calculadora import Calculadora
from teste import Testes
from unittest import TestCase, main

calculador = Calculadora()
res_soma = calculador.calcular(4, 5, 'soma')
print(res_soma)

if __name__ == '__main__':
    main()
