
"""
Autor: Thiago Souza

"""

from time import sleep
from base import *

# Função que cria interfaces para o jogo
def interface_jokenpo():
    # Cria uma interface com o usuário
    print(f"\n{cores('azul')}{'='*25} JOGO JOKENPÔ {'='*25}{cores('padrao')}\n")
    sleep(1.5)
    print(f"{cores('amarelo')}Computador: \"Vou escolher entre\":")
    print("Pedra")
    print("Papel")
    print("Tesoura")
    print(f"...{cores('padrao')}")
    sleep(3)
    print("\nJá escolhi! Agora é sua vez.\n")
    sleep(2)

    # Exibe a opções para o usuário
    print(f"{cores('verde')}{'='*20}\nDigite uma opção:")
    print("(1) - PEDRA")
    print("(2) - PAPEL")
    print("(3) - TESOURA")
    print(f"{'='*20}{cores('padrao')}")