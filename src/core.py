from typing import Union, Literal, Callable
from command import *
from node import node
from option import *

commands: str = commandList
options: str = optionList

class message:
    def __init__(self, type: str, details: str) -> None:
        self.type: str = type
        self.details: str = details
    def __repr__(self) -> None:
        return f"[{self.type}] {self.details}"

class token:
    def __init__(self, content: str, type: str) -> None:
        self.content: str = content
        self.type: str = type

    def __repr__(self) -> str:
        return f"Token({self.content}, {self.type})"

class lexer:
    def __init__(self, text: str) -> None:
        self.text: str = text.split(" ")
        self.position: int = 0
        self.current: str = self.text[self.position]

    def advance(self) -> None:
        if self.position + 1 < len(self.text) and self.current != None:
            self.position += 1
            self.current = self.text[self.position]
        else:
            self.current = None

    def tokenize(self) -> list[token]:
        tokens: list[token] = []

        while self.position + 1 <= len(self.text) and self.current != None:
            if self.current in commands:
                tokens.append(token(self.current,"command"))
            elif self.current in options:
                tokens.append(token(self.current,"option"))
            else:
                tokens.append(token(self.current,"value"))

            
            self.advance()

        return tokens

class parse:
    def __init__(self, tokens: list[token]) -> None:
        self.tokens: list[token] = tokens
        self.position: int = 0
        self.current: token = self.tokens[0] if tokens else None

    def advance(self) -> None:
        if self.position + 1 < len(self.tokens):
            self.position += 1
            self.current = self.tokens[self.position]
        else:
            self.current = None

    def parse(self) -> Union[node,message]:
        result: node = node()

        while self.current:

            if self.current.type == "command":
                result.command = self.current.content

            elif self.current.type == "option":
                option_name = options[self.current.content]

                self.advance()

                if self.current is None:
                    return message("Error",f"Not value has been input to option {option_name}.")
                else:
                    result.arguments[option_name] = self.current.content

            self.advance()

        if not result.command in commands:
            return message("Info",f"Valid command don't enfound.")


        return result

class dispatcher:
    def __init__(self, argNode : node, commands: dict[str,Callable]) -> None:
        self.node: node = argNode
        self.commands: dict[str,] = commands
    
    def execute(self) -> None:
        if self.node.command in self.commands:
            command = self.commands[self.node.command]
            commandFunc = command["func"] if "func" in command else None

            if isinstance(commandFunc,Callable):
                print("[Success] Valid command enfound.")
                commandFunc(self.node)
            else:
                print("[Success] Valid command don't enfound.")
                commandFunc(self.node)