"""
Módulo de Análise Léxica para a Linguagem Troia
Utiliza PLY (Python Lex-Yacc) para tokenização.
"""

import ply.lex as lex

# Palavras reservadas da Linguagem Troia
reserved = {
    'kyrios': 'KYRIOS',
    'Zeus': 'T_ZEUS',
    'Roma': 'T_ROMA',
    'Tendao': 'T_TENDAO',
    'Hieroglifo': 'T_HIEROGLIFO',
    'an': 'AN',
    'allou': 'ALLOU',
    'eno': 'ENO',
    'diakopi': 'DIAKOPI',
    'apodosi': 'APODOSI',
    'apotypoma': 'APOTYPOMA',
    'eisagogi': 'EISAGOGI',
    'kai': 'KAI',
    'i': 'I',
    'den': 'DEN',
    'True': 'TRUE',
    'False': 'FALSE',
    'C': 'BLOCO_C',
    'F': 'BLOCO_F'
}

# Lista completa de Tokens
tokens = [
    'ID', 'NUM_REAL', 'NUM_INT', 'STRING_LITERAL',
    'ATRIB', 'SOMA', 'SUB', 'MULT', 'DIV',
    'MAIOR_IGUAL', 'MENOR_IGUAL', 'MAIOR', 'MENOR', 'IGUAL',
    'SEMI', 'LPAREN', 'RPAREN'
] + list(reserved.values())

# Operadores relacionais e de atribuição
t_ATRIB       = r'=_\s*'
t_MAIOR_IGUAL = r'->='
t_MENOR_IGUAL = r'<-='
t_MAIOR       = r'->'
t_MENOR       = r'<-'
t_IGUAL       = r'=_='

# Operadores aritméticos
t_SOMA        = r'\+'
t_SUB         = r'-'
t_MULT        = r'\*'
t_DIV         = r'/'

# Delimitadores e Pontuação
t_SEMI        = r';'
t_LPAREN      = r'\('
t_RPAREN      = r'\)'

# Comentários no padrão § ... § (ignorados pelo lexer)
def t_COMMENT(t):
    r'§[^§]*§'
    t.lexer.lineno += t.value.count('\n')
    pass

# Literais de texto (Hieroglifo)
def t_STRING_LITERAL(t):
    r'\"([^\\\"]|\\.)*\"'
    t.value = t.value[1:-1]  # remove as aspas
    return t

# Números Reais (Roma)
def t_NUM_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Números Inteiros (Zeus)
def t_NUM_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identificadores e palavras-chave
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t\r'

def t_error(t):
    print(f"[ERRO LÉXICO] Linha {t.lineno}: Caractere inesperado '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()