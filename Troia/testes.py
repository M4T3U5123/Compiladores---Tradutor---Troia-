
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

    # 7. Caso Válido: Soma de 1 a N (Laço eno e Aritmética)
    print("\n" + "-" * 60)
    print("[TESTE 7] Caso Válido: Soma de 1 a N (Laço eno e Aritmética)")
    codigo_valido_soma = """
    kyrios C
        Zeus n =_ 10;
        Zeus soma =_ 0;
        Zeus k =_ 1;
        eno k <-= n C
            soma =_ soma + k;
            k =_ k + 1;
        F
        apotypoma("Soma de 1 a 10:");
        apotypoma(soma);
    F
    """
    res_soma = compilar_troia(codigo_valido_soma)
    if res_soma:
        print(">> Sucesso na compilação!")
        print("Código Python traduzido:")
        for linha in res_soma.strip().split('\n'):
            print("  ", linha)

    # 8. Caso Inválido: Erro Semântico (variável usada antes de ser declarada)
    print("\n" + "-" * 60)
    print("[TESTE 8] Caso Inválido: Erro Semântico (variável usada antes da declaração)")
    codigo_erro_sem_3 = """
    kyrios C
        an contador -> 0 C
            apotypoma("positivo");
        F
        Zeus contador =_ 0;
    F
    """
    compilar_troia(codigo_erro_sem_3)

    # 9. Caso Inválido: Erro no Gerador (código Python inválido gerado)
    print("\n" + "-" * 60)
    print("[TESTE 9] Caso Inválido: Erro no Gerador (Python inválido gerado)")
    codigo_erro_gerador = """
    kyrios C
        Zeus x =_ 5;
        apodosi x;
    F
    """
    res_gerador = compilar_troia(codigo_erro_gerador)
    if res_gerador:
        print(">> Compilação concluída. Código Python gerado:")
        for linha in res_gerador.strip().split('\n'):
            print("  ", linha)
        print()
        try:
            compile(res_gerador, '<gerado>', 'exec')
            print(">> Código Python gerado é válido.")
        except SyntaxError as e:
            print(f">> [ERRO NO GERADOR] Código Python gerado é inválido: {e}")
            print(">> Causa: 'apodosi' gera 'return' no nível do módulo,")
            print("   o que é inválido em Python 3 (return fora de função).")

if __name__ == '__main__':
    rodar_testes()

