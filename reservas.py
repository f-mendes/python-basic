#!/usr/bin/env python3

import sys

print(f"Quartos disponiveis")
print('-' * 10)

reserved = []
rooms = {}

for reserve in open('reservados.txt'):
	client, room, days = reserve.split(',')
	reserved.append(room)

for room in open('quartos.txt'):
	cod,name,value = room.split(',')
	if not cod in reserved:
		rooms[cod] = value
		print(room)	


if input("Deseja reservar um quarto? digite enter ou N para sair: "):
	print("Volte Sempre")
	sys.exit()
	
name_reserve = input("Digite o seu nome: ")
cod_reserve = input("Digite o código do quarto: ")
days_reserve = input("Digite a quantidade de dias desejado: ")

if not cod_reserve in rooms:
	print()
	print("Desculpe! Esse quarto não está disponivel ou não existe.")
	sys.exit()
	
text = [
    name_reserve,
    cod_reserve,
    days_reserve,
]


with open('reservados.txt', "a") as file_:
    file_.write(",".join(text) + "\n")

total = int(days_reserve) * int(rooms[cod_reserve])
print(f"Total: {total}")
