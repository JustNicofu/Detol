from command import *
from option import *
from core import *

print(f"""Detols v1.0""")

while True:
    line: str = input("$ ")

    if line == "exit":
        break

    mainLexer: lexer = lexer(line)
    mainParse: parse = parse(mainLexer.tokenize())
    mainNode: Union[node, message] = mainParse.parse()

    if isinstance(mainNode,message):
        print(mainNode)
    else:
        mainDispatcher = dispatcher(mainNode,commands)
        mainDispatcher.execute()
