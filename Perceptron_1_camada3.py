# Teste de rede neural perceptron de 1 camada para tabela verdade do tipo AND

import numpy as np

entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([0, 0, 0, 1])
pesos = np.array([0.0, 0.0])
taxa_aprendizagem = 0.1

def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1

    while erroTotal != 0:
        erroTotal = 0

        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro

            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxa_aprendizagem * entradas[i][j] * erro)
                print(f'Peso {j} atualizado: {pesos[j]}')

        print(f'Total de erros: {erroTotal}')

treinar()

try:
    entrada1 = int(input('Primeira entrada> '))

    if entrada1 > 1 or entrada1 < 0:
        raise ValueError

    entrada2 = int(input('Segunda entrada> '))    

    if entrada2 > 1 or entrada2 < 0:
        raise ValueError
    
    print(calculaSaida(np.asarray([entrada1, entrada2])))
except ValueError:
    raise ValueError('Somente valores 0 e 1 são aceitos!!')
                

                


