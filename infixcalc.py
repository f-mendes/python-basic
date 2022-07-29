#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operaçao: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "Felipe Mendes"
__license__ = "Unlicense"

import sys

while True:
    args = sys.argv
    count_args = len(args)

    if count_args == 4:
        operation, n1, n2 = args[1:4]
    elif count_args == 1:
        operation = input('operação: ')
        n1 = input('n1: ')
        n2 = input('n2: ')
    else:
        print('Number of args invalid! The calculator expected 3 args')
        sys.exit()


    operations = ['sum', 'sub', 'mul', 'div']

    if operation not in operations:
        print(f"Operation Invalid `{operation}`")
        sys.exit()

    try:
        if n1.find('.') == 1:
            n1 = float(n1)
        else:
            n1= int(n1)
        
        if n2.find('.') == 1:
            n2 = float(n2)
        else:
            n2= int(n2)
            
    except:
        print('Number is required in args n1 and n2')
        sys.exit()

    total = ''
    if operation == 'sum':
        total = n1 + n2
    elif operation == 'sub':
        total = n1 - n2
    elif operation == 'mul':
        total = n1 * n2
    elif operation == 'div':
        total = n1 / n2

    print(total)
    
    cont = input("Pressione enter para continuar ou qualquer tecla para sair ")
    if cont:
        break
    