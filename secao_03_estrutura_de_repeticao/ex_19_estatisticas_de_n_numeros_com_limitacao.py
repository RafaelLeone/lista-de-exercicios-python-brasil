"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, -10)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1001)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1198)
    'Somente números de 0 a 1000 são permitidos'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""
    lista =[]
    i = 0
    sum = 0
    if numeros == ():
        return 'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    for numero in numeros:
        lista.append(numero)
        i += 1
    for index in range(0, len(lista)):
        sum += lista[index]
    lista.sort()
    maior = lista[-1]
    menor = lista[0]
    if menor < 0 or maior > 1_000:
        return 'Somente números de 0 a 1000 são permitidos'
    else:
        return f'Maior valor: {maior}. Menor valor: {menor}. Soma: {sum}'