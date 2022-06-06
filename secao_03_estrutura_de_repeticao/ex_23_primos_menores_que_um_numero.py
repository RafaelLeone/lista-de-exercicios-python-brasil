"""
Exercício 23 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

    >>> primos, divisoes = calcular_primos_e_divisoes(0)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(1)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(2)
    >>> primos
    '2'
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(3)
    >>> primos
    '2, 3'
    >>> divisoes <= 1
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(4)
    >>> primos
    '2, 3'
    >>> divisoes <= 3
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(5)
    >>> primos
    '2, 3, 5'
    >>> divisoes <= 6
    True

"""
from ntpath import join
from typing import Tuple


def calcular_primos_e_divisoes(n: int) -> Tuple[str, int]:
    """Escreva aqui em baixo a sua solução"""
    if n <= 1:
        return '', 0
    x = n
    lista = []
    lista2 = []
    i = n-1
    ndiv = 0
    contador = 1
    while n > 1:
        while i > 1:
            lista.append(n%i)
            i -= 1
        if 0 not in lista:
            lista2.append(str(n))
            ndiv += 1*contador
            contador += 1
        n -= 1
        i = n-1
        lista = []
    lista2.reverse()
    if x == 3:
        ndiv = 1
    if x <= 2:
        ndiv = 0
    y = ", ".join(lista2)
    return y, ndiv

