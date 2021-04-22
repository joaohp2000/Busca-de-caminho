
import interface

def busca_custo_uniforme(entrada,saida, matriz, tela):
    no=0
    solucao=[]

    borda=[[0,[0,0]]]
    borda[0]=[0, entrada]
    print(borda)
    explorado=[]
    while True:
        if len(borda) == 0: return -1
        #else: print(len(borda))
        no=borda.pop(0)
        if no[-1]==saida :
            return no
            #if len(solucao) == 0 : solucao=no
            #else no[0] < solucao[0] :
        if no[-1] not in explorado:
            explorado.append(no[-1])
            #print(no[-1])
            filhos = verifica_vizinhos(no[-1],len(matriz))
            interface.Pinta_borda(tela, matriz, no[-1],0)
            for filho in filhos:
                novo_no=no[:]
                if filho not in explorado:
                    novo_no[0]=novo_no[0]+matriz_valores(matriz,filho)
                    novo_no.append(filho)
                    interface.Pinta_borda(tela, matriz, filho,1)
                    borda.append(novo_no)
            borda.sort()
            #print(borda)

    
def verifica_vizinhos(estado, tamanho_matriz):
        tamanho_matriz=tamanho_matriz-1
        vizinho=[]
        if estado[0] != 0:
            vizinho.append([estado[0]-1, estado[1]]) #esquerda     
        if estado[0] != tamanho_matriz:
            vizinho.append([estado[0]+1, estado[1]]) #direita
        if estado[1] != tamanho_matriz:
            vizinho.append([estado[0], estado[1]+1]) #baixo
        if estado[1] != 0:
            vizinho.append([estado[0], estado[1]-1]) #cima
        return vizinho

def matriz_valores(matriz, pos):
    x=matriz[pos[1]][pos[0]]
    if x==1: return 1
    if x==2: return 5
    if x==3: return 10
    if x==4: return 15

      




