"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    dict_month = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    mylist = data.split('/')
    try:
        for i in range(0, len(mylist)):
            mylist[i] = int(mylist[i])
    except:
        pass
    if len(mylist) == 3:
        if mylist[1] in dict_month.keys():
            value = dict_month[mylist[1]]
            if mylist[0] < value:
                print("'Data válida'")
            else:
                print("'Data inválida'")
        else:
            print("'Data inválida'")
    else:
        print("'Data inválida'")
