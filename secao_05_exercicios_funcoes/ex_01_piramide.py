"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes

Faça um programa para imprimir:

  1
  2   2
  3   3   3
  .....
  n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

"""


def imprimir_piramide(n: int):
  for i in range(1, n + 1):
    for _ in range(i):
      print(i, end='   ')
    print('')

#resolução ex2:
# def imprimir_piramide_crescente(n: int):
#   for linha in range(1, n + 1):
#     for coluna in range(1, linha + 1):
#       print(coluna, end='   ')
#     print('')