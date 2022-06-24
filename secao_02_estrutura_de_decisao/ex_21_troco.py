"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""

def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    notas100 = notas50 = notas10 = notas5 = notas1 = 0
    notas100str = notas50str = notas10str = notas5str = notas1str = ''
    saque = valor
    lista = []

    notas100, saque = divmod(saque, 100)
    notas50, saque = divmod(saque, 50)
    notas10, saque = divmod(saque, 10)
    notas5, notas1 = divmod(saque, 5)

    if notas100 > 0:
        if notas100 == 1:
            notas100str = f'{notas100} nota de R$ 100'
            lista.append(notas100str)
        if notas100 > 1:
            notas100str = f'{notas100} notas de R$ 100'
            lista.append(notas100str)

    if notas50 > 0:
        if notas50 == 1:
            notas50str = f'{notas50} nota de R$ 50'
            lista.append(notas50str)
        if notas50 > 1:
            notas50str = f'{notas50} notas de R$ 50'
            lista.append(notas50str)

    if notas10 > 0:
        if notas10 == 1:
            notas10str = f'{notas10} nota de R$ 10'
            lista.append(notas10str)
        if notas10 > 1:
            notas10str = f'{notas10} notas de R$ 10'
            lista.append(notas10str)

    if notas5 > 0:
        if notas5 == 1:
            notas5str = f'{notas5} nota de R$ 5'
            lista.append(notas5str)
        if notas5 > 1:
            notas5str = f'{notas5} notas de R$ 5'
            lista.append(notas5str)

    if notas1 > 0:
        if notas1 == 1:
            notas1str = f'{notas1} nota de R$ 1'
            lista.append(notas1str)
        if notas1 > 1:
            notas1str = f'{notas1} notas de R$ 1'
            lista.append(notas1str)

    if len(lista) > 2:
        ultimo_valor = lista[-1]
        lista.pop()
        texto = ", ".join(lista)
        texto_final = f'{texto} e {ultimo_valor}'
        return texto_final

    if len(lista) <= 2:
        texto = " e ".join(lista)
        return texto