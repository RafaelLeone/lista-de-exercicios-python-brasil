"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""

from math import ceil, floor


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    tamanho_parede = int(input('Digite: '))
    parede_com_folga = tamanho_parede *1.1
    tamanho_por_litro = 6
    litros_necessarios = ceil(parede_com_folga/tamanho_por_litro)
    print(f'Você deve comprar {litros_necessarios} litros de tinta.')

    preco_lata = 80
    litros_em_lata = 18
    latas_necessarias = ceil(litros_necessarios/litros_em_lata)
    custo_latas = latas_necessarias * preco_lata
    sobrar = (latas_necessarias*litros_em_lata) - litros_necessarios
    print(f'Você pode comprar {latas_necessarias} lata(s) de {litros_em_lata} litros a um custo de R$ {custo_latas}. Vão sobrar {sobrar:.1f} litro(s) de tinta.')

    preco_galao = 25
    litros_em_galao = 3.6
    galoes_necessarios = ceil(litros_necessarios/litros_em_galao)
    custo_galoes = galoes_necessarios * preco_galao
    sobrar = (galoes_necessarios*litros_em_galao) - litros_necessarios
    print(f'Você pode comprar {galoes_necessarios} lata(s) de {litros_em_galao} litros a um custo de R$ {custo_galoes}. Vão sobrar {sobrar:.1f} litro(s) de tinta.')

    latas_necessarias = floor(litros_necessarios/litros_em_lata)
    custo_latas = latas_necessarias * preco_lata
    resto = litros_necessarios % litros_em_lata
    galoes_necessarios = ceil(resto/litros_em_galao)
    custo_galoes = galoes_necessarios * preco_galao
    custo_total = custo_latas + custo_galoes
    sobrar = ((latas_necessarias*litros_em_lata) + (galoes_necessarios*litros_em_galao)) - litros_necessarios
    print(f'Para menor custo, você pode comprar {latas_necessarias} lata(s) de {litros_em_lata} litros e {galoes_necessarios} galão(ões) de {litros_em_galao} litros a um custo de R$ {custo_total}. Vão sobrar {sobrar:.1f} litro(s) de tinta.')