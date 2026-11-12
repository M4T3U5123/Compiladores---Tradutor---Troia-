PYTHON = python
PIP = pip
ARQUIVO ?= exemplo.troia

.PHONY: help install test lexico compilar rodar clean

help:
	@echo "Comandos disponíveis para o projeto Troia:"
	@echo "  make install                    - Instala as dependências (ply)"
	@echo "  make test                       - Executa a suíte de testes (testes.py)"
	@echo "  make lexico                     - Testa o analisador léxico isoladamente"
	@echo "  make compilar ARQUIVO=arq.troia - Compila um arquivo .troia para .py"
	@echo "  make rodar ARQUIVO=arq.troia    - Compila e executa o arquivo Python gerado"
	@echo "  make clean                      - Remove arquivos temporários e caches"

install:
	$(PIP) install ply

test:
	$(PYTHON) testes.py

lexico:
	$(PYTHON) lexico.py

compilar:
	$(PYTHON) main.py $(ARQUIVO)

rodar: compilar
	$(PYTHON) $(ARQUIVO:.troia=.py)

clean:
	rm -rf __pycache__
	rm -f parser.out parsetab.py
	@echo "Arquivos temporários removidos."
