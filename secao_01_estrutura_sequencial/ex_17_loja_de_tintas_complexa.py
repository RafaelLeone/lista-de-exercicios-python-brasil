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

from math import ceil


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    tamanho_parede = float(input('Informar valor do tamanho da área a ser pintada em metros quadrados: '))
    litros_necessarios = ceil((tamanho_parede/6)*1.1)
    latas_necessarias = ceil(litros_necessarios/18) #80
    galoes_necessarios = ceil(litros_necessarios/3.6) #25

    galoes_menor = 0
    latas_menor = 0
    galao = 3.6
    lata = 18
    sobrar = 0
    
    if litros_necessarios <= galao:
        galoes_menor = 1
        sobrar = (galoes_menor*galao)%litros_necessarios
    if galao < litros_necessarios <= (2*galao):
        galoes_menor = 2
        sobrar = (galoes_menor*galao)%litros_necessarios
    if (2*galao) < litros_necessarios <= lata:
        latas_menor = 1
        sobrar = (latas_menor*lata)%litros_necessarios
    if lata < litros_necessarios <= (lata + galao):
        latas_menor = 1
        galoes_menor = 1
        sobrar = ((latas_menor*lata)+(galoes_menor*galao))%litros_necessarios
    if (lata + galao) < litros_necessarios <= (lata + (2*galao)):
        latas_menor = 1
        galoes_menor = 2
        sobrar = ((latas_menor*lata)+(galoes_menor*galao))%litros_necessarios
    if (lata + (2*galao)) < litros_necessarios < (2*lata):
        latas_menor = 2
        sobrar = (latas_menor*lata)%litros_necessarios
    if (2*lata) < litros_necessarios < ((2*lata)+galao):
        latas_menor = 2
        galoes_menor = 1
        sobrar = ((latas_menor*lata)+(galoes_menor*galao))%litros_necessarios
    if ((2*lata)+galao) < litros_necessarios < ((2*lata)+(2*galao)):
        latas_menor = 2
        galoes_menor = 2
        sobrar = ((latas_menor*lata)+(galoes_menor*galao))%litros_necessarios

    print(f'''Você deve comprar {int(litros_necessarios + 0.5)} litros de tinta.
Você pode comprar {latas_necessarias} lata(s) de 18 litros a um custo de R$ {80*latas_necessarias}. Vão sobrar {"%.1f" %(((latas_necessarias*18) - litros_necessarios))} litro(s) de tinta.
Você pode comprar {galoes_necessarios} lata(s) de 3.6 litros a um custo de R$ {25*galoes_necessarios}. Vão sobrar {"%.1f" %(((galoes_necessarios*3.6) - litros_necessarios))} litro(s) de tinta.
Para menor custo, você pode comprar {latas_menor} lata(s) de 18 litros e {galoes_menor} galão(ões) de 3.6 litros a um custo de R$ {((latas_menor)*80) + (galoes_menor*25)}. Vão sobrar {"%.1f" %sobrar} litro(s) de tinta.''')
