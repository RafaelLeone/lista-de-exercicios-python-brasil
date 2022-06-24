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

