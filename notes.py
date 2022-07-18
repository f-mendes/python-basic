#!/usr/bin/env python3
"""Bloco de notas

$  notes.py new "Minha nota"
tag: tech
text:
Python é lindo

$ notes.py read tech
...
...

"""
__version__ = "0.1.0"
__author__ = "Felipe Mendes"
__license__ = "Unlicense"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    sys.exit(1)

cmds = ("read", "new")
if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")
    sys.exit(1)

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()
    

if arguments[0] == "new":
    titulo = arguments[1]
    text = [
        f"{titulo}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
    with open(filepath, "a") as notes:
        notes.write("\t".join(text) + "\n") 
        
