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
