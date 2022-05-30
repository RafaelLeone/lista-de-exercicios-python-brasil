"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""
    if numero >= 1_000:
        print("'O número precisa ser menor que 1000'")
        return
    
    if numero < 0:
        print("'O número precisa ser positivo'")
        return

    list = str(numero)

    try:
        unidade = int(list[-1])
        dezena = int(list[-2])
        centena = int(list[-3])
    except:
        pass

    if numero == 1:
        print("'1 = 1 unidade'")
        return

    if 1 < numero < 10:
        print(f"'{numero} = {numero} unidades'")
        return

    if numero == 10:
        print("'10 = 1 dezena'")
        return

    if numero == 11:
        print("'11 = 1 dezena e 1 unidade'")
        return

    if 11 < numero < 20:
        print(f"'{numero} = 1 dezena e {unidade} unidades'")
        return

    if 20 <= numero < 100 and unidade != 0 and unidade != 1:
        print(f"'{numero} = {dezena} dezenas e {unidade} unidades'")
        return

    if 20 <= numero < 100 and unidade == 1:
        print(f"'{numero} = {dezena} dezenas e 1 unidade'")
        return
    
    if 20 <= numero < 100 and unidade == 0:
        print(f"'{numero} = {dezena} dezenas'")
        return

    if numero == 100:
        print("'100 = 1 centena'")
        return

    if numero == 101:
        print("'101 = 1 centena e 1 unidade'")
        return

    if numero == 110:
        print("'110 = 1 centena e 1 dezena'")
        return

    if numero == 111:
        print("'111 = 1 centena, 1 dezena e 1 unidade'")
        return

    if 101 < numero < 110:
        print(f"'{numero} = 1 centena e {unidade} unidades'")
        return

    if 111 < numero < 120:
        print(f"'{numero} = 1 centena, 1 dezena e {unidade} unidades'")
        return

    if 120 <= numero < 200 and unidade == 0:
        print(f"'{numero} = 1 centena e {dezena} dezenas'")
        return

    if 120 <= numero < 200 and dezena == 0 and unidade != 0:
        print(f"'{numero} = 1 centena e {unidade} unidades'")
        return

    if 120 <= numero < 200 and dezena != 0 and unidade != 0:
        print(f"'{numero} = 1 centena, {dezena} dezenas e {unidade} unidades'")
        return

    if 200 <= numero < 1_000 and unidade == 0 and dezena == 0:
        print(f"'{numero} = {centena} centenas'")
        return
    
    if 200 <= numero < 1_000 and unidade == 1 and dezena == 1:
        print(f"'{numero} = {centena} centenas, 1 dezena e 1 unidade'")
        return

    if 200 <= numero < 1_000 and unidade == 0 and dezena == 1:
        print(f"'{numero} = {centena} centenas e 1 dezena'")
        return

    if 200 <= numero < 1_000 and unidade == 1 and dezena == 0:
        print(f"'{numero} = {centena} centenas e 1 unidade'")
        return

    if 200 <= numero < 1_000 and unidade != 1 and unidade != 0 and dezena == 0:
        print(f"'{numero} = {centena} centenas e {unidade} unidades'")
        return

    if 200 <= numero < 1_000 and unidade != 1 and unidade != 0 and dezena == 1:
        print(f"'{numero} = {centena} centenas, 1 dezena e {unidade} unidades'")
        return

    if 200 <= numero < 1_000 and unidade == 0 and dezena != 1 and dezena != 0:
        print(f"'{numero} = {centena} centenas e {dezena} dezenas'")
        return

    if 200 <= numero < 1_000 and unidade == 1 and dezena != 1 and dezena != 0:
        print(f"'{numero} = {centena} centenas, {dezena} dezenas e 1 unidade'")
        return

    if 200 <= numero < 1_000 and unidade != 1 and unidade != 0 and dezena != 0 and dezena != 1:
        print(f"'{numero} = {centena} centenas, {dezena} dezenas e {unidade} unidades'")
        return
