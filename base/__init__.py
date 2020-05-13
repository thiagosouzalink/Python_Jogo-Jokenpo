
# PACOTE BASE
# PACOTE COM FUNÇÕES BÁSICAS
"""
Autor: Thiago Souza

"""
from time import sleep

# Função linha
def linha(tam=40):

    print(f"{'='*tam}") # Exibe uma sequência de caracter


# Função cores
def cores(tom='padrao'):

    # Seleciona a cor
    cor = { # Dicionário com as cores
        'padrao': '\33[m',          # Sem cor, fim
        'branco': '\31[m',          # Cor branca
        'vermelho': '\33[1;31m',    # Cor vermelha
        'verde': '\33[1;32m',       # Cor verde
        'amarelo': '\33[1;33m',     # Cor amarela
        'azul': '\33[1;34m',        # Cor azul
        'roxo': '\33[1;35m',        # Cor roxa
        'magenta': '\33[1;36m',     # Cor magenta
        'cinza': '\33[1;37m',       # Cor cinza
        }

    return cor[tom] # Retorna a cor desejada pelo usuário


def leiaInt(txt=""): # Caso nenhum argumento seja passado, inicia com string vazia

    if txt == "": # Verifica se iniciou com string vazia
        txt = ("Digite o valor de um número inteiro: ") # Mostra uma mensagem default

    while True:

        try: # Tenta ler um número inteiro
            texto = int(input(txt))

        except (KeyboardInterrupt):
            print(f"{cores('vermelho')}ERRO! Entrada de dados interrompida pelo usuário!{cores('padrao')}")
            sleep(1)
            texto = 0
            break

        except: # Exceção, mostra mensagem de erro
            print(f"{cores('vermelho')}ERRO! Você digitou um valor inteiro inválido, tente novamente...{cores('padrao')}")
            sleep(1)

        else: # Caso sucesso, sai do laço
            break

    return texto # Retorna valor inteiro
