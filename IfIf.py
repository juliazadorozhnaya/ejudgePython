"""
Написать программу, которая получает на вход некоторый текст и определяет, является ли он синтаксически верным кодом на
Python, в котором присутствует оператор if. Программа выводит True или False соответственно.
"""


import ast
import sys


def has_if_statement(text):
    try:
        tree = ast.parse(text)
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                return True
        return False
    except SyntaxError:
        return False


try:
    input_text = sys.stdin.read()
except KeyboardInterrupt:
    sys.exit(0)

result = has_if_statement(input_text)
print(result)
