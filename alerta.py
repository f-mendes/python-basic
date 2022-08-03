#!/usr/bin/env python3

import sys
import logging

info = {
    'temperatura': None,
    'umidade': None
}
keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key}? "))
    except ValueError as e:
        logging.error(f"{key.title()} inválida")
        sys.exit(1)

temp = info['temperatura']
umid = info['umidade']
    

if temp >= 45:
    print("Perigo calor extremo!")
elif (temp * 3) >= umid:
    print("Perigo de calor umido")
elif temp >= 10 and temp <= 30:
    print("Temperatura normal")
elif temp >= 0 and temp <= 10:
    print("Frio")
else:
    print("Frio extremo")
