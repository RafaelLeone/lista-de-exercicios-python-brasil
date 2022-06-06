"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos

"""


from time import altzone


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    inputs = []
    while True:
        inp = input("Type Anything/ Press Enter: ")
        if inp == "0":
            break
        inputs.append(inp)
    nome_alto = ''
    nome_baixo = ''
    nome_magro = ''
    nome_gordo = ''
    alto = 0
    baixo = 1_000
    magro = 1_000
    gordo = 0
    while len(inputs) > 0:
        if int(inputs[1]) > int(alto):
            alto = inputs[1]
            nome_alto = inputs[0]
        if int(inputs[1]) < int(baixo):
            baixo = inputs[1]
            nome_baixo = inputs[0]
        if int(inputs[2]) > int(gordo):
            gordo = inputs[2]
            nome_gordo = inputs[0]
        if int(inputs[2]) < int(magro):
            magro = inputs[2]
            nome_magro = inputs[0]
        inputs.pop(0)
        inputs.pop(0)
        inputs.pop(0)
    print(f'''Cliente mais alto: {nome_alto}, com {alto} centímetros
Cliente mais baixo: {nome_baixo}, com {baixo} centímetros
Cliente mais magro: {nome_magro}, com {magro} kilos
Cliente mais gordo: {nome_gordo}, com {gordo} kilos''')