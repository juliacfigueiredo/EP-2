def extrai_naipe(carta):
    resposta = carta[1]
    if carta[0] == '1':
        resposta = carta[2]
    return resposta