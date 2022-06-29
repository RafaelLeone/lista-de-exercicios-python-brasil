"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

    >>> ler_5_valores()

"""


def ler_5_valores():
    """Escreva aqui em baixo a sua solução"""
    lista = []
    
    for i in range(5):
        numero = float(input('Digite: '))
        lista.append(numero)

    print(lista)

ler_5_valores()


# Resolução do ex2:
#     lista = []
    
#     for i in range(10):
#         numero = float(input('Digite: '))
#         lista.append(numero)

#     lista.reverse()
#     print(lista)

#resolucao da 15 em outra branch

#resolucao da 16:
#   contagem_de_assalariados_por_faixa = [0] * 9
#   for salario in salarios: essa é a lista que a função vai passar (ou por input)
#       indice = salario // 100 - 2
#       indice_maximo = len(contagem_de_assalariados_por_faixa) - 1
#       indice = min(indice, indice_maximo)
#       contagem_de_assalariados_por_faixa[indice] += 1