import random
def gerar_cartela(sigla):
    coluna_b = []
    coluna_i = []
    coluna_n = []
    coluna_g = []
    coluna_o = []
    while len(coluna_b) < 5:
        num = random.randint(1, 15)
        if num not in coluna_b:
            coluna_b.append(num)
    while len(coluna_i) < 5:
        num = random.randint(16, 30)
        if num not in coluna_i:
            coluna_i.append(num)
    while len(coluna_n) < 4:
        num =random.randint(31, 45)
        if num not in coluna_n:
            coluna_n.append(num)
    coluna_n.insert(2, sigla)
    while len(coluna_g) < 5:
        num = random.randint(46, 60)
        if num not in coluna_g:
            coluna_g.append(num)
    while len(coluna_o) < 5:
        num = random.randint(61,75)
        if num not in coluna_o:
            coluna_o.append(num)
    cartela = []
    for i in range(5):
        linha = [coluna_b[i], coluna_i[i], coluna_n[i], coluna_g[i], coluna_o[i]]
        cartela.append(linha.copy())
    return cartela
def imprimir_cartela(cartela):
    print('-' * 27)
    print('  B  I  N  G  O  ')
    print('-' * 27)
    for linha in cartela:
        texto_linha = ''
        for numero  in linha:
            if type(numero) == str:
                texto_linha += f' {numero}'
            else:
                texto_linha += f' {numero:02d}'
        print(texto_linha)
    print('-' * 27)

def sorteia_valor(sorteados):
    while True:
        num = random.randint(1, 75)
        if num not in sorteados:
            sorteados.append(num)
            return num
def verifica_ganhador_cheia(cartela, sorteados):
    for linha in cartela:
        for numero in linha:
            if type(numero) == str:
                continue
            if numero not in sorteados:
                return False
    return True
def verifica_ganhador_linha_coluna_diagonal(cartela, sorteados):
    for linha in cartela:
        linha_completa = True
        for numero in linha:
            if type(numero) != str and numero not in sorteados:
                linha_completa = False
        if linha_completa:
            return True
    for c in range(5):
        coluna_completa = True
        for l in range(5):
            numero = cartela[l][c]
            if type(numero) != str and numero not in sorteados:
                coluna_completa = False
        if coluna_completa:
            return True
    diag1 = [cartela[0][0], cartela[1][1], cartela[2][2], cartela[3][3], cartela[4][4]]
    diag2 = [cartela[0][4], cartela[1][3], cartela[2][2], cartela[3][1], cartela[4][0]]
    for diagonal in [diag1, diag2]:
        diag_completa = True
        for numero in diagonal:
            if type(numero) != str and numero not in sorteados:
                diag_completa = False
        if diag_completa:
            return True
    return False
#codigo principal
cartela_jogador = []
numero_sorteados = []
regra_jogo = ''
while True:
    print('\n' + '='*30)
    print('    MENU PRINCIPAL - BINGO   ')
    print('='*30)
    print('1- GERAR CARTELA')
    print('2- DEFINIR REGRAS DO JOGO')
    print('3- SORTEIA VALOR / INICIAR JOGO')
    print('4- ENECERRAR PROGRAMA')
    opcao = input('Escolha  a opção desejada:  ')
    if opcao == '1':
        cartela_jogador = gerar_cartela('KM')
        print('\nSua cartela foi gerada com sucesso!')
        imprimir_cartela(cartela_jogador)
    elif opcao == '2':
        print('\n--- ESCOLHA A REGRA DE VITÓRIA ---')
        print('1- Cartela Cheia')
        print('2- Linha, Coluna ou diagonal')
        escolha_regra = input('Escolha a opção que deseja: ')
        if escolha_regra == '1':
            regra_jogo = 'CHEIA'
            print('Regra do jogo definida: CARTELA CHEIA')
        elif escolha_regra == '2':
            regra_jogo = 'LINHA_COLUNA_DIAGONAL'
            print('Regra definida: LINHA, COLUNA ou DIAGONAL')
        else:
            print('Opção invalida!')
    elif opcao =='3':
        if not cartela_jogador:
            print('ERRO! Gere uma cartela na opção 1 primeiro.')
            continue
        if not regra_jogo:
            print('ERRO! Defina a regra do jogo na opção 2 primeiro.')
            continue
        print('--- COMEÇANDO O SORTEIO DE PEDRAS--- ')
        input('---Pressione ENTER para sortear a primeira pedra --- ')
        while True:
            pedra = sorteia_valor(numero_sorteados)
            print(f"\nPedra Sorteada: {pedra:02d}!")
            print(f'Pedras que já saíram: {sorted(numero_sorteados)}')
            ganhou = False
            if regra_jogo == 'CHEIA':
                ganhou = verifica_ganhador_cheia(cartela_jogador, numero_sorteados)
            else:
                ganhou = verifica_ganhador_linha_coluna_diagonal(cartela_jogador, numero_sorteados)
            if ganhou:
                print("\n" + "*" * 30)
                print('       B I N G O O O O O !    ')
                print('     VOCÊ É O GANHADOR!     ')
                print("*" * 30)
                imprimir_cartela(cartela_jogador)
                cartela_jogador = []
                numero_sorteados = []
                break
            proxima = input('Aperte ENTER para a próxima pedra ou digite S para SAIR:  ').upper()
            if proxima == 'S':
                break
    elif opcao == '4':
        print('Encerrando o programa. Obrigado por jogar!')
        break
    else:
        print('Opção inválida! Tente novamente!')





