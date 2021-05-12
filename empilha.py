def empilha(lista_baralho, posicao_origem, destino):
    posicao_origem1 = lista_baralho[posicao_origem]
    lista_baralho[destino] = posicao_origem1
    del lista_baralho[posicao_origem]
    return lista_baralho