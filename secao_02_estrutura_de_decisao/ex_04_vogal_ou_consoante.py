"""
Exercício 04 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    >>> vogal_ou_consoante("F")
    'consoante'
    >>> vogal_ou_consoante("a")
    'vogal'
    >>> vogal_ou_consoante('c')
    'consoante'
    >>> vogal_ou_consoante('U')
    'vogal'
"""


def vogal_ou_consoante(letra):
    """Escreva aqui em baixo a sua solução"""
    # if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U" or letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    #     print("'vogal'")
    # else:
    #     print("'consoante'")

    lista = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if letra in lista:
        return 'vogal' 
    
    return 'consoante'