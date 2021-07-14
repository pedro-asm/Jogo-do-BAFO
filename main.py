from jogo import jogo, colecao, novas_cartas, colecao_atual
from colecao_completa import colecao_completa

print('Bem vindo ao Jogo de Bafo')

while True:
    print('''
    Menu:
    [ 1 ] Iniciar Novo Jogo
    [ 2 ] Carregar Jogo
    [ 3 ] Ver a Coleção Completa
    [ 4 ] Ver a sua Coleção
    [ 5 ] Sair''')


    op = int(input('Digite sua opção: '))

    if op == 1:
        novas_cartas()
        colecao()
        jogo()

    elif op == 2:
        colecao_atual()
        jogo()

    elif op == 3:
        colecao_completa()

    elif op == 4:
        colecao_atual()

    elif op == 5:
        print('Obrigado por jogar conosco!')
        break

    else:
        print('Opção inválida')
