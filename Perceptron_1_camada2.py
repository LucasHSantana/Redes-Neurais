# Dado 3 entradas e seus pesos, calcular a saída
# Otimizado

import numpy as np

entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma(e, p):
# dot product / produto escalar
# Já faz a multiplicação e a soma de todos os itens automaticamente
# Cálculo é otimizado pelo numpy
    return e.dot(p)

def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

s = soma(entradas, pesos)
r = stepFunction(s)

print(r)