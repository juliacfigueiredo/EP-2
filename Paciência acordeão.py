
def cria_baralho():
    baralho = ['A♠', 'A♥', 'A♦', 'A♣','2♠', '2♥', '2♦', '2♣', '3♠', '3♥', '3♦', '3♣', '4♠', '4♥', '4♦', '4♣', '5♠', '5♥', '5♦', '5♣', '6♠', '6♥', '6♦', '6♣', '7♠', '7♥', '7♦', '7♣', '8♠', '8♥', '8♦', '8♣', '9♠', '9♥', '9♦', '9♣', '10♠', '10♥', '10♦', '10♣', 'J♠', 'J♥', 'J♦', 'J♣', 'Q♠', 'Q♥', 'Q♦', 'Q♣', 'K♠', 'K♥', 'K♦', 'K♣']
    return baralho

def extrai_naipe(carta):
    resposta = carta[1]
    if carta[0] == '1':
        resposta = carta[2]
    return resposta

def extrai_valor(carta):
    resposta = carta[0]
    if carta[0] == '1':
        resposta = '10'
    return resposta

def lista_movimentos_possiveis(baralho, posicao):
    carta = baralho[posicao]
    naipe = extrai_naipe(carta)
    valor = extrai_valor(carta)
    movimentos = []
    if posicao > 2:
        movimento3 = baralho[posicao - 3]
        naipe3 = extrai_naipe(movimento3)
        valor3 = extrai_valor(movimento3)
        if naipe == naipe3 or valor == valor3:
            movimentos.append(3)
        
        movimento1 =  baralho[posicao - 1]
        naipe1 = extrai_naipe(movimento1)
        valor1 = extrai_valor(movimento1)
        if naipe == naipe1 or valor == valor1:
            movimentos.append(1)

    elif posicao > 0:
        movimento1 =  baralho[posicao - 1]
        naipe1 = extrai_naipe(movimento1)
        valor1 = extrai_valor(movimento1)
        if naipe == naipe1 or valor == valor1:
            movimentos.append(1)
    else:
        movimentos = []
    return movimentos

def empilha(lista_baralho, posicao_origem, destino):
    posicao_origem1 = lista_baralho[posicao_origem]
    lista_baralho[destino] = posicao_origem1
    del lista_baralho[posicao_origem]
    return lista_baralho

def possui_movimentos_possiveis(baralho):
    for i in range (len(baralho)):
        carta = baralho[i]
        valor = extrai_valor(carta)
        naipe = extrai_naipe(carta)
        if i > 2:
            carta3 = baralho[i-3]
            valor3 = extrai_valor(carta3)
            naipe3 = extrai_naipe(carta3)
            if valor == valor3 or naipe == naipe3:
                resposta = True
            
            carta1 = baralho[i-1]
            valor1 = extrai_valor(carta1)
            naipe1 = extrai_naipe(carta1)
            if valor == valor1 or naipe == naipe1:
                resposta = True
        elif i > 0:
            carta1 = baralho[i-1]
            valor1 = extrai_valor(carta1)
            naipe1 = extrai_naipe(carta1)
            if valor == valor1 or naipe == naipe1:
                resposta = True 
        else:
            resposta = False      
    
    return resposta

print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.')

print('Existem apenas dois movimentos possíveis:')

print('1. Empilhar uma carta sobre a carta imediatamente anterior;')
print('2. Empilhar uma carta sobre a terceira carta anterior.')

print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:')

print('1. As duas cartas possuem o mesmo valor ou')
print('2. As duas cartas possuem o mesmo naipe.')

print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.')

inicio = input("\nAPERTE: \n[ENTER] PARA JOGAR ")

print('Escolha uma carta (digite um número entre 1 e 49):')

baralho = cria_baralho()

import random
random.shuffle(baralho)
while possui_movimentos_possiveis(baralho):
    print('O estado atual do baralho é:')
    for e in baralho:
        print (e)
    escolha = input('Escolha um número entre os disponívei:')
    if escolha < 0 or escolha > len(baralho):
        print('Essa carta não é valida')
        escolha = input('Escolha um número entre os disponívei:')





