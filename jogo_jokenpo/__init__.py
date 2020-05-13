
# Módulo jogo_jokenpo

"""
Autor: Thiago Souza

"""

from time import sleep
from base import cores

# Função que executa o jogo
def jogo_jokenpo(tipo, comp, user):
    
    # Mensagem de efeito
    print(f"\n{cores('roxo')}JO...")
    sleep(1)
    print("KEN...")
    sleep(1)
    print(f"PÔ...{cores('padrao')}")
    sleep(1)

    # Interface mostando a opção escolhida pelo usuário e pelo PC
    print(f"{cores('azul')}{'--' * 20}{cores('padrao')}")
    print(f"Usuário escolheu: {cores('azul')}{user}{cores('padrao')}")
    print(f"O computador escolheu: {cores('azul')}{comp}{cores('padrao')}")
    print(f"{cores('azul')}{'--' * 20}{cores('padrao')}")
    sleep(1.5)

    # Opção pedra
    if comp == tipo[0]:
        if user == tipo[0]:
            print("\nO Jogo Empatou!")
        elif user == tipo[1]:
            print("\nUsuário Venceu!")
        elif user == tipo[2]:
            print("\nComputador Venceu!")

    # Opção papel
    elif comp == tipo[1]:
        if user == tipo[0]:
            print("\nComputador Venceu!")
        elif user == tipo[1]:
            print("\nO Jogo Empatou!")
        elif user == tipo[2]:
            print("\nUsuário Venceu!")

    # Opção tesoura
    elif comp == tipo[2]:
        if user == tipo[0]:
            print("\nUsuário Venceu!")
        elif user == tipo[1]:
            print("\nComputador Venceu!")
        elif user == tipo[2]:
            print("\nO Jogo Empatou!")

    sleep(2)