"""
Módulo de Análise Sintática para a Linguagem Troia
Constrói a Árvore Sintática Abstrata (AST) a partir dos tokens.
"""

import ply.yacc as yacc
from lexico import tokens
from ast_nos import (
    ProgramNode, DeclNode, AssignNode, PrintNode, InputNode,
    IfNode, WhileNode, BreakNode, ReturnNode,
    BinOpNode, UnaryOpNode, LiteralNode, VarNode
)

precedence = (
    ('left', 'I'),
    ('left', 'KAI'),
    ('right', 'DEN'),
    ('nonassoc', 'MAIOR', 'MENOR', 'MAIOR_IGUAL', 'MENOR_IGUAL', 'IGUAL'),
    ('left', 'SOMA', 'SUB'),
    ('left', 'MULT', 'DIV'),
)

def p_program(p):
    'program : KYRIOS BLOCO_C command_list BLOCO_F'
    p[0] = ProgramNode(p[3])

def p_command_list(p):
    """command_list : command_list command
                    | empty"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_command(p):
    """command : declaration SEMI
               | assignment SEMI
               | if_command
               | while_command
               | print_command SEMI
               | input_command SEMI
               | break_command SEMI
               | return_command SEMI"""
    p[0] = p[1]

def p_declaration(p):
    """declaration : type ID
                   | type ID ATRIB expression"""
    if len(p) == 3:
        p[0] = DeclNode(p[1], p[2], None)
    else:
        p[0] = DeclNode(p[1], p[2], p[4])

def p_type(p):
    """type : T_ZEUS
            | T_ROMA
            | T_TENDAO
            | T_HIEROGLIFO"""
    p[0] = p[1]

def p_assignment(p):
    'assignment : ID ATRIB expression'
    p[0] = AssignNode(p[1], p[3])

def p_if_command(p):
    """if_command : AN expression BLOCO_C command_list BLOCO_F
                  | AN expression BLOCO_C command_list BLOCO_F ALLOU BLOCO_C command_list BLOCO_F"""
    if len(p) == 6:
        p[0] = IfNode(p[2], p[4], None)
    else:
        p[0] = IfNode(p[2], p[4], p[8])

def p_while_command(p):
    'while_command : ENO expression BLOCO_C command_list BLOCO_F'
    p[0] = WhileNode(p[2], p[4])

def p_print_command(p):
    'print_command : APOTYPOMA LPAREN expression RPAREN'
    p[0] = PrintNode(p[3])

def p_input_command(p):
    'input_command : EISAGOGI LPAREN ID RPAREN'
    p[0] = InputNode(p[3])

def p_break_command(p):
    'break_command : DIAKOPI'
    p[0] = BreakNode()

def p_return_command(p):
    """return_command : APODOSI
                      | APODOSI expression"""
    expr = p[2] if len(p) == 3 else None
    p[0] = ReturnNode(expr)

def p_expression_binop(p):
    """expression : expression SOMA expression
                  | expression SUB expression
                  | expression MULT expression
                  | expression DIV expression
                  | expression MAIOR expression
                  | expression MENOR expression
                  | expression MAIOR_IGUAL expression
                  | expression MENOR_IGUAL expression
                  | expression IGUAL expression
                  | expression KAI expression
                  | expression I expression"""
    p[0] = BinOpNode(p[1], p[2], p[3])

def p_expression_unary(p):
    'expression : DEN expression'
    p[0] = UnaryOpNode(p[1], p[2])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_literal(p):
    """expression : NUM_INT
                  | NUM_REAL
                  | STRING_LITERAL"""
    if isinstance(p[1], int):
        p[0] = LiteralNode(p[1], 'Zeus')
    elif isinstance(p[1], float):
        p[0] = LiteralNode(p[1], 'Roma')
    else:
        p[0] = LiteralNode(p[1], 'Hieroglifo')

def p_expression_bool(p):
    """expression : TRUE
                  | FALSE"""
    val = True if p[1] == 'True' else False
    p[0] = LiteralNode(val, 'Tendao')

def p_expression_id(p):
    'expression : ID'
    p[0] = VarNode(p[1])

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"[ERRO SINTÁTICO] Token inesperado '{p.value}' (tipo: {p.type}) na linha {p.lineno}")
    else:
        print("[ERRO SINTÁTICO] Fim inesperado do arquivo (EOF). Verifique se todos os blocos 'C ... F' foram fechados.")

parser = yacc.yacc()