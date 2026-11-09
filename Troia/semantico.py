"""
Módulo de Tabela de Símbolos e Validação Semântica para a Linguagem Troia.
"""

class SemanticError(Exception):
    pass

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def declare(self, name, var_type):
        if name in self.symbols:
            raise SemanticError(f"Variável '{name}' já foi declarada anteriormente neste escopo.")
        self.symbols[name] = var_type

    def lookup(self, name):
        if name not in self.symbols:
            raise SemanticError(f"Variável '{name}' utilizada sem ter sido declarada.")
        return self.symbols[name]

    def exists(self, name):
        return name in self.symbols