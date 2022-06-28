"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Tamanho de strings. Faça um programa que compare 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings

String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.

    >>> comparar('Brasil Hexa 2006', 'Brasil! Hexa 2006!')

"""


def comparar(s1: str, s2: str):
    """Escreva aqui em baixo a sua solução"""

    str1 = "ola"
    str2 = "Mundo!"

    tamanho1 = len(str1)
    tamanho2 = len(str2)

    print(f'"{str1}": {tamanho1} caracteres')
    print(f'"{str2}": {tamanho2} caracteres')

    comparacao_de_tamanhos = 'diferentes'
    comparacao_de_conteudo = 'diferente'

    if str1 == str2:
        comparacao_de_tamanhos = 'iguais'
        comparacao_de_conteudo = 'igual'

    if tamanho1 == tamanho2:
        comparacao_de_tamanhos = 'iguais'

    print(f'As duas strings são de tamanhos {comparacao_de_tamanhos}')
    print(f'As duas strings possuem conteúdo {comparacao_de_conteudo}')