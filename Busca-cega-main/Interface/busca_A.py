import math
import interface
import busca_cega

#matriz=[[3,3,3,3,3,1,1,1,1,1],[3,3,3,3,3,3,1,1,2,2],[3,3,3,3,3,1,1,1,2,1],[1,3,3,3,1,1,1,1,1,1],[1,1,1,1,1,2,2,2,2,1],[1,1,1,2,1,1,1,2,1,1],[1,2,2,2,2,2,1,2,1,2],[1,1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2,1],[2,2,4,4,4,4,4,2,2,2]]


def func_busca_A(origem, destino, matriz, tela):
   cube = 0
   borda=[[0,0,[0,0]]]
   borda[0]=[0,0, origem]
   
   visitados = []
   
   run = True
   
   if(origem != destino):
       while run:
           cube = borda.pop(0)
           #print(cube[-1])
           #print(destino)
           
           if cube[-1] == destino:
               return cube
            
           if cube[-1] not in visitados:
                visitados.append(cube[-1])
                vizinhos = busca_cega.verifica_vizinhos(cube[-1],len(matriz))
                #interface.Pinta_borda(tela, matriz, cube[-1],0)
                for vizinho in vizinhos:
                    new_cube = cube[:]
                    if vizinho not in visitados:
                        new_cube[0] = new_cube[1] + busca_cega.matriz_valores(matriz,vizinho) + Heuristica(vizinho, destino)
                        new_cube[1] = new_cube[1] + busca_cega.matriz_valores(matriz,vizinho)
                        #print("checando posicao", new_cube[1])
                        new_cube.append(vizinho)
                        interface.Pinta_borda(tela, matriz, vizinho, 0)
                        borda.append(new_cube)
                borda.sort()
           


def Heuristica(no, destino):
    x1, y1 = no
    x2, y2 = destino
    return abs(x1 - x2) + abs(y1 - y2)
