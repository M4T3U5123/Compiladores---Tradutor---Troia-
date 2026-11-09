"""
Nós da Árvore Sintática Abstrata (AST) para a Linguagem Troia.
"""

class ASTNode:
    pass

class ProgramNode(ASTNode):
    def __init__(self, commands):
        self.commands = commands

class DeclNode(ASTNode):
    def __init__(self, var_type, name, expr=None):
        self.var_type = var_type
        self.name = name
        self.expr = expr

class AssignNode(ASTNode):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class InputNode(ASTNode):
    def __init__(self, name):
        self.name = name

class IfNode(ASTNode):
    def __init__(self, condition, then_body, else_body=None):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body

class WhileNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class BreakNode(ASTNode):
    pass

class ReturnNode(ASTNode):
    def __init__(self, expr=None):
        self.expr = expr

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class UnaryOpNode(ASTNode):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

class LiteralNode(ASTNode):
    def __init__(self, value, val_type):
        self.value = value
        self.val_type = val_type

class VarNode(ASTNode):
    def __init__(self, name):
        self.name = name