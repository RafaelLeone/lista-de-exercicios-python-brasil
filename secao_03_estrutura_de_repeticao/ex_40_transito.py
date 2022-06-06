"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil habitantes.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil habitantes.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil habitantes é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    lista_cidades = []
    lista_veiculos = []
    lista_acidentes = []
    media = []

    maior_acidentes = 0
    maior_cidade = ''
    menor_acidentes = 1_000_000
    menor_cidade = ''

    soma = 0
    media_veiculos = 0

    lista_aux_media_acidentes_menos_150 = []
    media_acidentes_menos_150 = 0

    for i in range(len(cidades)):
        lista_cidades.append(cidades[i][0])
        lista_veiculos.append(cidades[i][1])
        lista_acidentes.append(cidades[i][2])
        media.append((lista_acidentes[i]/lista_veiculos[i])*1_000)

    for i in range(len(lista_veiculos)):
        soma += int(lista_veiculos[i])

    media_veiculos = int(soma/len(lista_acidentes))

    for i in range(len(cidades)):
        if float(media[i]) > float(maior_acidentes):
            maior_cidade = lista_cidades[i]
            maior_acidentes = media[i]
        if float(media[i]) < float(menor_acidentes):
            menor_cidade = lista_cidades[i]
            menor_acidentes = media[i]

    for i in range(len(lista_veiculos)):
        if lista_veiculos[i] <= 150_000:
            aux = lista_acidentes[i]
            lista_aux_media_acidentes_menos_150.append(aux)
    
    media_acidentes_menos_150 = (sum(lista_aux_media_acidentes_menos_150))/len(lista_aux_media_acidentes_menos_150)
    
    print(f'''O maior índice de acidentes é de {maior_cidade}, com {"%.1f" %maior_acidentes} acidentes por mil habitantes.
O menor índice de acidentes é de {menor_cidade}, com {"%.1f" %menor_acidentes} acidentes por mil habitantes.
O média de veículos por cidade é de {media_veiculos}.
A média de acidentes total nas cidades com menos de 150 mil habitantes é de {media_acidentes_menos_150} acidentes.''')