"""
Написать функцию copypaste(one, two), которая будет проверять, являются ли строки one и two синтаксически верными
программами на Python, которые отличаются только используемыми именами. Для простоты сравнение распространяется и на
заведомо различные объекты (например, подмена bin() на hex() также считается простой подменой имён).
Функция возвращает True, если условие выполнено, иначе — False.
"""


import ast

def are_syntax_trees_equal(node1, node2):
    if isinstance(node1, ast.Name) and isinstance(node2, ast.Name):
        return True
    elif isinstance(node1, ast.Attribute) and isinstance(node2, ast.Attribute):
        return are_syntax_trees_equal(node1.value, node2.value)
    elif type(node1) != type(node2):
        return False
    elif isinstance(node1, ast.AST):
        for field, value in ast.iter_fields(node1):
            if not are_syntax_trees_equal(value, getattr(node2, field, None)):
                return False
        return True
    elif isinstance(node1, list):
        return all(are_syntax_trees_equal(x, y) for x, y in zip(node1, node2))
    else:
        return node1 == node2

def copypaste(one, two):
    try:
        tree1 = ast.parse(one)
        tree2 = ast.parse(two)
        return are_syntax_trees_equal(tree1, tree2)
    except SyntaxError:
        return False

