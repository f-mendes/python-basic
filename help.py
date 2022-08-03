#!/usr/bin/env python3
"""Atalho para o comando --help
"""

import sys
import os


cmd = sys.argv[1:]

directories = os.system(cmd[0] + " --help")
print(directories)

