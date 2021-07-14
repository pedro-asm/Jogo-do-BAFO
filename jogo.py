from random import randint, shuffle
from time import sleep
from prettytable import PrettyTable
from cartas_embaralhadas import embaralhar


sleep(0.5)
pilha_jog_colecao = []
pilha_BAFO= []
cont = []
cartas_novas = []
cartas_perdidas = []

def novas_cartas():
    for i in range(10):
        pilha_jog_colecao.append(embaralhar())
        cont.append('->')
    return pilha_jog_colecao

def colecao():
    global pilha_jog_colecao
    tabela_colecao_jog = PrettyTable()
    tabela_colecao_jog.padding_width = 1
    tabela_colecao_jog.add_column('Nº', list(enumerate(cont, start=1)))
    tabela_colecao_jog.add_column('Cartas', pilha_jog_colecao, align="l")
    print(f'Essa é a sua coleção das Figurinhas Sapos de Chocolate:\n{tabela_colecao_jog}')
    return tabela_colecao_jog

def jogo():
    pilha_jog_inicial = []
    pilha_com = []
    pilha_com2 = []
    global pilha_jog_colecao, \
        pilha_jog_final, \
        cont, \
        cartas_novas, \
        cartas_perdidas, \
        pilha_BAFO

    if len(pilha_jog_colecao) == 0:
        print('Por favor reinicie!')
    else:
        while True:
            r = str(input('Deseja apostar todas as cartas da sua coleção? [S/N] ')).upper()
            if r != 'S' and r != 'N':
                print('Por favor digite "S" ou  "N"!')
            elif r == 'S':
                pilha_jog_inicial = pilha_jog_colecao
                break
            else:
                aposta = int(input('Quais cartas desseja apostar(min. 1)? [Digite 0 para sair]: '))
                if aposta > len(pilha_jog_colecao):
                    print('Não existe esta posição! Digite novamente.')
                elif aposta == 0 and len(pilha_jog_inicial) >= 1:
                    break
                elif pilha_jog_colecao[aposta - 1] in pilha_jog_inicial:
                    print('Você já apostou essa carta!')
                elif aposta == 0 and len(pilha_jog_inicial) == 0:
                    print('Você tem que apostar ao menos uma!')
                else:
                    pilha_jog_inicial.append(pilha_jog_colecao[aposta - 1])
                if len(pilha_jog_colecao) == len(pilha_jog_inicial):
                    break

        for i in range(5):
            pilha_com.append(embaralhar())
            cont.append('->')

        for i in range(5):
            pilha_com2.append(embaralhar())
            cont.append('->')

        pilha_BAFO = pilha_jog_inicial + pilha_com + pilha_com2
        sleep(0.5)

        tabela_pilha_jog_inicial = PrettyTable()
        tabela_pilha_jog_inicial.padding_width = 1
        tabela_pilha_jog_inicial.add_column('Suas Cartas', pilha_jog_inicial, align="l")
        print(f'Suas cartas apostadas são:\n{tabela_pilha_jog_inicial}')
        sleep(0.5)

        tabela_pilha_com = PrettyTable()
        tabela_pilha_com.padding_width = 1
        tabela_pilha_com.add_column('Cartas do Computador', pilha_com, align="l")
        print(f'As cartas apostadas do computador são:\n{tabela_pilha_com}')
        sleep(0.5)

        tabela_pilha_com2 = PrettyTable()
        tabela_pilha_com2.padding_width = 1
        tabela_pilha_com2.add_column('Cartas do Computador 2', pilha_com2, align="l")
        print(f'As cartas apostadas do computador 2 são:\n{tabela_pilha_com2}')
        sleep(0.5)

        shuffle(pilha_BAFO)

        tabela_pilha_BAFO = PrettyTable()
        tabela_pilha_BAFO.padding_width = 1
        tabela_pilha_BAFO.add_column('Cartas do BAFO', pilha_BAFO, align="l")
        print(f'A pilha do Bafo ficou desse jeito:\n{tabela_pilha_BAFO}')
        sleep(0.5)

        pilha_com = pilha_com2 = []

        while True: #INICO DO JOGO!

            print('Sua vez!')
            sleep(0.5)
            print('Tente virar a carta')
            jogada_jog = randint(0, 1)
            if jogada_jog == 0:
                print('Você conseguiu!')
                sleep(0.5)
                print(f'A carta \033[0;31m{pilha_BAFO[len(pilha_BAFO) - 1]}\033[m é sua!')
                sleep(0.5)
                if pilha_BAFO[len(pilha_BAFO) - 1] not in pilha_jog_colecao:
                    cartas_novas.append(pilha_BAFO[len(pilha_BAFO) - 1])
                    pilha_jog_colecao.append(pilha_BAFO[len(pilha_BAFO) - 1])
                pilha_BAFO.pop()

                if len(pilha_BAFO) > 0:
                    tabela_pilha_BAFO = PrettyTable()
                    tabela_pilha_BAFO.padding_width = 1
                    tabela_pilha_BAFO.add_column('Cartas do BAFO', pilha_BAFO, align="l")
                    print(f'A pilha do Bafo ficou desse jeito:\n{tabela_pilha_BAFO}')
                    sleep(0.5)
            else:
                print('Você não conseguiu virar a carta!')
                sleep(0.5)
            if len(pilha_BAFO) == 0:
                print('Jogo Finalizado!')
                tabela_cartas_novas = PrettyTable()
                tabela_cartas_novas.padding_width = 1
                tabela_cartas_novas.add_column('Cartas', cartas_novas, align="l")
                print(f'Você conseguiu essas novas cartas:\n{tabela_cartas_novas}')

                tabela_cartas_perdidas = PrettyTable()
                tabela_cartas_perdidas.padding_width = 1
                tabela_cartas_perdidas.add_column('Cartas', cartas_perdidas, align="l")
                print(f'Você perdeu essas cartas:\n{tabela_cartas_perdidas}')

                sleep(0.5)

                cont2 = []
                for seta in range(len(pilha_jog_colecao)):
                    cont2.append('->')

                tabela_colecao_jog = PrettyTable()
                tabela_colecao_jog.padding_width = 1
                tabela_colecao_jog.add_column('Nº', list(enumerate(cont2, start=1)))
                tabela_colecao_jog.add_column('Cartas', pilha_jog_colecao, align="l")
                print(f'Sua coleção das Figurinhas Sapos de Chocolate ficou assim:\n{tabela_colecao_jog}')
                break

            print('É a vez do computador')
            sleep(0.5)
            print('Ele tentará virar a carta')
            jogada_com = randint(0, 1)
            if jogada_com == 0:
                print(f'O computador conseguiu! ')
                sleep(0.5)
                print(f'A carta \033[0;31m{pilha_BAFO[len(pilha_BAFO) - 1]}\033[m é dele!')
                sleep(0.5)
                if pilha_BAFO[len(pilha_BAFO) - 1] in pilha_jog_colecao:
                    cartas_perdidas.append(pilha_BAFO[len(pilha_BAFO) - 1])
                    pilha_jog_colecao.remove(pilha_BAFO[len(pilha_BAFO) - 1])
                pilha_com.append(pilha_BAFO[len(pilha_BAFO) - 1])
                pilha_BAFO.pop()
                if len(pilha_BAFO) > 0:
                    tabela_pilha_BAFO = PrettyTable()
                    tabela_pilha_BAFO.padding_width = 1
                    tabela_pilha_BAFO.add_column('Cartas do BAFO', pilha_BAFO, align="l")
                    print(f'A pilha do Bafo ficou desse jeito:\n{tabela_pilha_BAFO}')
                    sleep(0.5)
            else:
                print('O computador não conseguiu a carta!')
                sleep(0.5)
            if len(pilha_BAFO) == 0:
                print('Jogo Finalizado!')
                tabela_cartas_novas = PrettyTable()
                tabela_cartas_novas.padding_width = 1
                tabela_cartas_novas.add_column('Cartas', cartas_novas, align="l")
                print(f'Você conseguiu essas novas cartas:\n{tabela_cartas_novas}')

                tabela_cartas_perdidas = PrettyTable()
                tabela_cartas_perdidas.padding_width = 1
                tabela_cartas_perdidas.add_column('Cartas', cartas_perdidas, align="l")
                print(f'Você perdeu essas cartas:\n{tabela_cartas_perdidas}')

                sleep(0.5)

                cont2 = []
                for seta in range(len(pilha_jog_colecao)):
                    cont2.append('->')

                tabela_colecao_jog = PrettyTable()
                tabela_colecao_jog.padding_width = 1
                tabela_colecao_jog.add_column('Nº', list(enumerate(cont2, start=1)))
                tabela_colecao_jog.add_column('Cartas', pilha_jog_colecao, align="l")
                print(f'Sua coleção das Figurinhas Sapos de Chocolate ficou assim:\n{tabela_colecao_jog}')
                break

            print('É a vez do computador 2')
            sleep(0.5)
            print('Ele tentará virar a carta')
            jogada_com2 = randint(0, 1)
            if jogada_com2 == 0:
                print(f'O computador 2 conseguiu!')
                sleep(0.5)
                print(f'A carta \033[0;31m{pilha_BAFO[len(pilha_BAFO) - 1]}\033[m é dele!')
                sleep(0.5)
                if pilha_BAFO[len(pilha_BAFO) - 1] in pilha_jog_colecao:
                    cartas_perdidas.append(pilha_BAFO[len(pilha_BAFO) - 1])
                    pilha_jog_colecao.remove(pilha_BAFO[len(pilha_BAFO) - 1])
                pilha_com2.append(pilha_BAFO[len(pilha_BAFO) - 1])
                pilha_BAFO.pop()
                if len(pilha_BAFO) > 0:
                    tabela_pilha_BAFO = PrettyTable()
                    tabela_pilha_BAFO.padding_width = 1
                    tabela_pilha_BAFO.add_column('Cartas do BAFO', pilha_BAFO, align="l")
                    print(f'A pilha do Bafo ficou desse jeito:\n{tabela_pilha_BAFO}')
                    sleep(0.5)
            else:
                print('O computador 2 não conseguiu a carta!')
                sleep(0.5)
            if len(pilha_BAFO) == 0:
                print('Jogo Finalizado!')
                tabela_cartas_novas = PrettyTable()
                tabela_cartas_novas.padding_width = 1
                tabela_cartas_novas.add_column('Cartas', cartas_novas, align="l")
                print(f'Você conseguiu essas novas cartas:\n{tabela_cartas_novas}')

                tabela_cartas_perdidas = PrettyTable()
                tabela_cartas_perdidas.padding_width = 1
                tabela_cartas_perdidas.add_column('Cartas', cartas_perdidas, align="l")
                print(f'Você perdeu essas cartas:\n{tabela_cartas_perdidas}')

                sleep(0.5)

                cont2 = []
                for seta in range(len(pilha_jog_colecao)):
                    cont2.append('->')

                tabela_colecao_jog = PrettyTable()
                tabela_colecao_jog.padding_width = 1
                tabela_colecao_jog.add_column('Nº', list(enumerate(cont2, start=1)))
                tabela_colecao_jog.add_column('Cartas', pilha_jog_colecao, align="l")
                print(f'Sua coleção das Figurinhas Sapos de Chocolate ficou assim:\n{tabela_colecao_jog}')
                break

    return pilha_jog_colecao, pilha_BAFO

def colecao_atual():
    global pilha_jog_colecao
    cont = []
    if len(pilha_jog_colecao) == 0:
        print('Você ainda não iniciou um novo jogo!')
    else:
        for i in range(len(pilha_jog_colecao)):
            cont.append('->')

        tabela_colecao_jog = PrettyTable()
        tabela_colecao_jog.padding_width = 1
        tabela_colecao_jog.add_column('Nº', list(enumerate(cont, start=1)))
        tabela_colecao_jog.add_column('Cartas', pilha_jog_colecao, align="l")
        print(f'Essa é a sua coleção das Figurinhas Sapos de Chocolate:\n{tabela_colecao_jog}')
        return tabela_colecao_jog
