#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.0"

# Dados
salas = {
    "Sala1":["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "Sala2":["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

aulas = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música":["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"]
}


# Listar alunos em cada atividade por sala
for nome_atividade, turma in aulas.items():

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    for nome_sala, sala in salas.items():
        intersection = set(sala) & set(turma)
        print(nome_sala, '->', intersection)

    print()
    print("#" * 40)