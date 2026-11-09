"""
Módulo Gerador de Código: Traduz a AST de Troia para Python 3 executável.
"""

from semantico import SymbolTable, SemanticError
from ast_nos import (
    ProgramNode, DeclNode, AssignNode, PrintNode, InputNode,
    IfNode, WhileNode, BreakNode, ReturnNode,
    BinOpNode, UnaryOpNode, LiteralNode, VarNode
)

class TroiaToPythonCompiler:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.indent_level = 0
        self.code_lines = []

    def indent(self):
        return "    " * self.indent_level

    def compile(self, ast):
        self.code_lines = [
            "# ========================================================",
            "# Código gerado automaticamente pelo Compilador Troia",
            "# Linguagem Alvo: Python 3",
            "# ========================================================",
            ""
        ]
        self.visit(ast)
        return "\n".join(self.code_lines)

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise NotImplementedError(f"Método de visita visit_{type(node).__name__} não implementado.")

    def visit_ProgramNode(self, node):
        for cmd in node.commands:
            self.visit(cmd)

    def visit_DeclNode(self, node):
        self.symbol_table.declare(node.name, node.var_type)
        if node.expr:
            expr_code = self.visit(node.expr)
            self.code_lines.append(f"{self.indent()}{node.name} = {expr_code}")
        else:
            default_val = {
                'Zeus': '0',
                'Roma': '0.0',
                'Tendao': 'False',
                'Hieroglifo': '""'
            }.get(node.var_type, 'None')
            self.code_lines.append(f"{self.indent()}{node.name} = {default_val}")

    def visit_AssignNode(self, node):
        self.symbol_table.lookup(node.name)
        expr_code = self.visit(node.expr)
        self.code_lines.append(f"{self.indent()}{node.name} = {expr_code}")

    def visit_PrintNode(self, node):
        expr_code = self.visit(node.expr)
        self.code_lines.append(f"{self.indent()}print({expr_code})")

    def visit_InputNode(self, node):
        var_type = self.symbol_table.lookup(node.name)
        if var_type == 'Zeus':
            self.code_lines.append(f"{self.indent()}{node.name} = int(input())")
        elif var_type == 'Roma':
            self.code_lines.append(f"{self.indent()}{node.name} = float(input())")
        else:
            self.code_lines.append(f"{self.indent()}{node.name} = input()")

    def visit_IfNode(self, node):
        cond_code = self.visit(node.condition)
        self.code_lines.append(f"{self.indent()}if {cond_code}:")
        self.indent_level += 1
        if not node.then_body:
            self.code_lines.append(f"{self.indent()}pass")
        else:
            for cmd in node.then_body:
                self.visit(cmd)
        self.indent_level -= 1

        if node.else_body:
            self.code_lines.append(f"{self.indent()}else:")
            self.indent_level += 1
            for cmd in node.else_body:
                self.visit(cmd)
            self.indent_level -= 1

    def visit_WhileNode(self, node):
        cond_code = self.visit(node.condition)
        self.code_lines.append(f"{self.indent()}while {cond_code}:")
        self.indent_level += 1
        if not node.body:
            self.code_lines.append(f"{self.indent()}pass")
        else:
            for cmd in node.body:
                self.visit(cmd)
        self.indent_level -= 1

    def visit_BreakNode(self, node):
        self.code_lines.append(f"{self.indent()}break")

    def visit_ReturnNode(self, node):
        if node.expr:
            expr_code = self.visit(node.expr)
            self.code_lines.append(f"{self.indent()}return {expr_code}")
        else:
            self.code_lines.append(f"{self.indent()}return")

    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op_map = {
            '+': '+', '-': '-', '*': '*', '/': '/',
            '->': '>', '<-': '<', '->=': '>=', '<-=': '<=', '=_=': '==',
            'kai': 'and', 'i': 'or'
        }
        return f"({left} {op_map[node.op]} {right})"

    def visit_UnaryOpNode(self, node):
        operand = self.visit(node.operand)
        return f"(not {operand})"

    def visit_LiteralNode(self, node):
        if node.val_type == 'Hieroglifo':
            return f'"{node.value}"'
        return str(node.value)

    def visit_VarNode(self, node):
        self.symbol_table.lookup(node.name)
        return node.name