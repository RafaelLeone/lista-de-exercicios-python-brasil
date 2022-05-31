"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
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
    # tipos_de_notas = [1, 5, 10, 50, 100]
    # pedacos=[]
    # resto = valor
    # while resto > 0:
    #     tipo_de_nota = tipos_de_notas.pop()
    # if len(pedacos)==1:
    #     return pedacos.pop()

    list = str(valor)

    try:
        unidade = int(list[-1])
        dezena = int(list[-2])
        centena = int(list[-3])
    except:
        pass

    # contador_de_1 = 0
    # contador_de_5 = 0
    # contador_de_10 = 0
    # contador_de_50 = 0
    # contador_de_100 = 0
    
    if unidade < 5:
        contador_de_1 = unidade

    if unidade > 5:
        contador_de_1 = unidade - 5

    if dezena < 5:
        contador_de_10 = dezena

    if dezena > 5:
        contador_de_10 = dezena - 5

    if valor == 1:
        print(f"'1 nota de R$ 1'")
        return

    if  1 < valor < 5:
        print(f"'{contador_de_1} notas de R$ 1'")
        return

    if valor == 5:
        print(f"'1 nota de R$ 5'")
        return

    if valor == 6:
        print(f"'1 nota de R$ 5 e 1 nota de R$ 1'")
        return

    if 6 < valor < 10:
        print(f"'1 nota de R$ 5 e {contador_de_1} notas de R$ 1'")
        return

    if valor == 10:
        print("'1 nota de R$ 10'")
        return

    if 10 < valor < 50 and unidade == 0:
        print(f"'{contador_de_10} notas de R$ 10'")
        return

    if 10 < valor < 50 and unidade == 1:
        print(f"'{contador_de_10} notas de R$ 10 e 1 nota de R$ 1'")
        return

    if 10 < valor < 50 and 1 < unidade < 5:
        print(f"'{contador_de_10} notas de R$ 10 e {contador_de_1} notas de R$ 1'")
        return

    if 10 < valor < 50 and unidade == 5:
        print(f"'{contador_de_10} notas de R$ 10 e 1 nota de R$ 5'")
        return

    if 10 < valor < 50 and unidade == 6:
        print(f"'{contador_de_10} notas de R$ 10, 1 nota de R$ 5 e 1 nota de R$ 1'")
        return

    if 10 < valor < 50 and unidade > 6:
        print(f"'{contador_de_10} notas de R$ 10, 1 nota de R$ 5 e {contador_de_1} notas de R$ 1'")
        return

    if valor == 50:
        print("'1 nota de R$ 50'")
        return
    
    if valor == 51:
        print("'1 nota de R$ 50 e 1 nota de R$ 5'")
        return

    if 50 < valor < 60 and 1 < unidade < 5:
        print(f"'1 nota de R$ 50 e {contador_de_1} notas de R$ 1'")
        return

    if 50 < valor < 60 and unidade > 6:
        print(f"'1 nota de R$ 50, 1 nota de R$ 5  e {contador_de_1} notas de R$ 1'")
        return

    if valor == 55:
        print("'1 nota de R$ 50 e 1 nota de R$ 5'")
        return

    if valor == 56:
        print(f"'1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'")
        return
    
    if valor == 60:
        print("'1 nota de R$ 50 e 1 nota de R$ 10'")
        return

    if valor == 61:
        print("'1 nota de R$ 50, 1 nota de R$ 10 e uma nota de R$ 1'")
        return

    if 50 < valor < 100 and unidade == 0 and valor != 60:
        print(f"'1 nota de R$ 50 e {contador_de_10} notas de R$ 10'")
        return
    
    if 50 < valor < 100 and dezena == 6 and 1 < unidade < 5:
        print(f"'1 nota de R$ 50, 1 nota de R$ 10 e {contador_de_1} notas de R$ 1'")
        return

    if valor == 65:
        print(f"'1 nota de R$ 50, 1 nota de R$ 10 e 1 nota de R$ 5'")
        return

    if valor == 66:
        print(f"'1 nota de R$ 50, 1 nota de R$ 10, 1 nota de R$ 5 e 1 nota de R$ 1'")
        return

    if 50 < valor < 100 and dezena == 6 and unidade > 6:
        print(f"'1 nota de R$ 50, 1 nota de R$ 10, 1 nota de R$ 5 e {contador_de_1} notas de R$ 1'")
        return

    if 50 < valor < 100 and dezena > 6 and unidade == 1:
        print(f"'1 nota de R$ 50, {contador_de_10} notas de R$ 10 e 1 nota de R$ 1'")
        return

    if 50 < valor < 100 and dezena > 6 and 1 < unidade < 5:
        print(f"'1 nota de R$ 50, {contador_de_10} notas de R$ 10 e {contador_de_1} notas de R$ 1'")
        return

    if 50 < valor < 100 and dezena > 6 and unidade == 5:
        print(f"'1 nota de R$ 50, {contador_de_10} notas de R$ 10 e 1 nota de R$ 5'")
        return

    if 50 < valor < 100 and dezena > 6 and unidade == 6:
        print(f"'1 nota de R$ 50, {contador_de_10} notas de R$ 10, 1 nota de R$ 5 e 1 nota de R$ 1'")
        return

    if 50 < valor < 100 and dezena > 6 and unidade > 6:
        print(f"'1 nota de R$ 50, {contador_de_10} notas de R$ 10, 1 nota de R$ 5 e {contador_de_1} notas de R$ 1'")
        return

calcular_troco(79)
