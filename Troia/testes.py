
from main import compilar_troia

def rodar_testes():
    print("=" * 60)
    print("EXECUÇÃO DA SUITE DE TESTES - LINGUAGEM TROIA")
    print("=" * 60)

    # 1. Caso Válido: Fatorial e Repetição
    print("\n[TESTE 1] Caso Válido: Fatorial (Laço eno e Aritmética)")
    codigo_valido = """
    § Cálculo de fatorial §
    kyrios C
        Zeus n =_ 5;
        Zeus fat =_ 1;
        eno n -> 1 C
            fat =_ fat * n;
            n =_ n - 1;
        F
        apotypoma("Fatorial de 5:");
        apotypoma(fat);
    F
    """
    res = compilar_troia(codigo_valido)
    if res:
        print(">> Sucesso na compilação!")
        print("Código Python traduzido:")
        for linha in res.strip().split('\n'):
            print("  ", linha)

    # 2. Caso Inválido: Erro Léxico
    print("\n" + "-" * 60)
    print("[TESTE 2] Caso Inválido: Erro Léxico (Caractere inválido '@')")
    codigo_erro_lex = """
    kyrios C
        Zeus valor =_ 10 @;
    F
    """
    compilar_troia(codigo_erro_lex)

    # 3. Caso Inválido: Erro Semântico (Variável não declarada)
    print("\n" + "-" * 60)
    print("[TESTE 3] Caso Inválido: Erro Semântico (Variável não declarada)")
    codigo_erro_sem_1 = """
    kyrios C
        total =_ 100;
    F
    """
    compilar_troia(codigo_erro_sem_1)

    # 4. Caso Inválido: Erro Semântico (Redeclaração de variável)
    print("\n" + "-" * 60)
    print("[TESTE 4] Caso Inválido: Erro Semântico (Redeclaração de identificador)")
    codigo_erro_sem_2 = """
    kyrios C
        Zeus idade =_ 20;
        Roma idade =_ 25.5;
    F
    """
    compilar_troia(codigo_erro_sem_2)

    # 5. Caso Inválido: Erro Sintático (Falta de ponto e vírgula)
    print("\n" + "-" * 60)
    print("[TESTE 5] Caso Inválido: Erro Sintático (Falta de terminador ';')")
    codigo_erro_sint = """
    kyrios C
        Zeus forca =_ 100
        apotypoma(forca);
    F
    """
    compilar_troia(codigo_erro_sint)

    # 6. Caso Válido: Condicional (an / allou) e Relacionais
    print("\n" + "-" * 60)
    print("[TESTE 6] Caso Válido: Condicional (an / allou) e Relacionais")
    codigo_valido_cond = """
    § Teste de recrutamento para Troia §
    kyrios C
        Zeus idade =_ 16;
        an idade ->= 18 C
            apotypoma("Apto para lutar!");
        F
        allou C
            apotypoma("Fique na cidade.");
        F
    F
    """
    res_cond = compilar_troia(codigo_valido_cond)
    if res_cond:
        print(">> Sucesso na compilação!")
        print("Código Python traduzido:")
        for linha in res_cond.strip().split('\n'):
            print("  ", linha)

if __name__ == '__main__':
    rodar_testes()

