from command import *
from option import *
from core import *

import os
import platform

commands = commandList
options = optionList

print(f"""Detols v1.0""")

while True:
    line = input("$ ")

    if line == "exit":
        break

    mainLexer = lexer(line)
    mainParse = parse(mainLexer.tokenize())
    mainNode = mainParse.parse()

    if isinstance(mainNode,message):
        print(mainNode)
    else:
        mainDispatcher = dispatcher(mainNode,commands)
        mainDispatcher.execute()
