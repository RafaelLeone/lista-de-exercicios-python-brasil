"""
Exercício 26 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

uma eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar
 e ao final mostrar o número de votos de cada candidato.

    >>> calcular_votos()
    Votantes: 0
    Votos no candidato corrupto: 0
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto')
    Votantes: 1
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso')
    Votantes: 2
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 3
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 1
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz', 'corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 6
    Votos no candidato corrupto: 2
    Votos no candidato mentiroso: 2
    Votos no candidato rouba, mas faz: 2

"""


def calcular_votos(*votos):
    """Escreva aqui em baixo a sua solução"""
    lista = []
    voto_c = 0
    voto_m = 0
    voto_r = 0
    votantes = 0
    for voto in votos:
        lista.append(voto)
        votantes += 1
    lista.sort()
    for index in range(0,len(lista)):
        if lista[index] == 'corrupto':
            voto_c += 1
        if lista[index] == 'mentiroso':
            voto_m += 1
        if lista[index] == 'rouba, mas faz':
            voto_r += 1
        
    print(f'''Votantes: {votantes}
Votos no candidato corrupto: {voto_c}
Votos no candidato mentiroso: {voto_m}
Votos no candidato rouba, mas faz: {voto_r}''')

    