#!/usr/bin/env python3

import logging
import sys

words = []

while True:
    
    new_word = input("Digite uma palavra (ou enter para sair):")

    try:
        if new_word.isdigit():
            raise
    except:
        logging.error('Digite somente palavras')
        sys.exit(1)
    
    if not new_word:
        break
                  
    words.append(new_word)

    
vogais = ('a','e','i','o','u')

for word in words:
    nword = ''
    for char in word:
        if char.lower() in vogais:
            nword += char * 2
        else:
            nword += char

    print(nword)
        
