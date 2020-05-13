
# Programa que simula o jogo Jokenpô
"""
Autor: Thiago Souza
Data: 18/04/2020
"""
from random import choice # Importa o método choice do módulo random
from interface_jokenpo import*
from jogo_jokenpo import*

# Criar uma lista com as opções de escolha do jogo
tipo = ['pedra', 'papel', 'tesoura']

while True: # Laço para executar o programa
    
    comp = choice(tipo) # Escolhe aleatoriarmente um elemento na lista5

    interface_jokenpo() # Chama a função que exibe a interface com o usuário

    opcao = leiaInt("Opção: ") # Recebe a opção do usuário

    # Testa se a opção escolhida é válida
    while opcao!=1 and opcao!=2 and opcao!=3:
        print(f"\n{cores('vermelho')}Opção inválida do usuário!")
        print(f"Tente novamente{cores('padrao')}")
        opcao = leiaInt("Opção: ")

    else:
        user = tipo[opcao - 1]
        jogo_jokenpo(tipo, comp, user)

    # Pergunta se o usuário deseja jogar novamente
    cont = input(f"\n{cores('magenta')}Deseja jogar novamente? [s/n]: {cores('padrao')}").strip().lower()[0]
    while cont not in 'sn': # Verifica se o usuário digitou uma opção inválida
        print(f"{cores('vermelho')}Opção inválida, tente novamente...{cores('padrao')}")
        cont = input(f"\n{cores('magenta')}Deseja jogar novamente? [s/n]: {cores('padrao')}").strip().lower()[0]

    # Finaliza o jogo
    if cont == 'n': 
        print("\nMuito obrigado!\n")
        sleep(1.5)
        break
