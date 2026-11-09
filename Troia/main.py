"""
Ponto de Entrada Principal do Compilador Troia.
"""

import sys
from lexico import lexer
from sintatico import parser
from gerador import TroiaToPythonCompiler
from semantico import SemanticError

def compilar_troia(codigo_fonte):
    lexer.lineno = 1
    ast = parser.parse(codigo_fonte, lexer=lexer)
    if not ast:
        print("[FALHA] Não foi possível construir a AST devido a erros sintáticos.")
        return None

    compiler = TroiaToPythonCompiler()
    try:
        codigo_python = compiler.compile(ast)
        return codigo_python
    except SemanticError as e:
        print(f"[ERRO SEMÂNTICO] {e}")
        return None

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arquivo_entrada = sys.argv[1]
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            fonte = f.read()
        print(f"Compilando '{arquivo_entrada}'...")
        resultado = compilar_troia(fonte)
        if resultado:
            arquivo_saida = arquivo_entrada.replace('.troia', '.py')
            if arquivo_saida == arquivo_entrada:
                arquivo_saida += '.py'
            with open(arquivo_saida, 'w', encoding='utf-8') as f:
                f.write(resultado)
            print(f"[SUCESSO] Código Python gerado em: {arquivo_saida}")
    else:
        print("Uso: python main.py <programa.troia>")