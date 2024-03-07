from pilha_vetor_tad import Pilha
import random

n = int(input('Quantos números, entre 1 e 7, você deseja deseja distribuir entre as pilhas? ')) # entrada da quantidade de números

assert n >= 1 and n <= 7 # garante que o número inserido seja entre 1 e 7

def criar_pilhas(n: int):
    qntde_pilhas = n + 2
    lista_pilhas = []
    for i in range(1, qntde_pilhas + 1):
        x = Pilha(4)
        lista_pilhas.append(x)
    return lista_pilhas

def aleatoriza_elementos(n: int):
    elementos = [0] * (n * 4)
    i = len(elementos) - 1
    j = n
    while i >= 0:
        contador = 4 # Limita a 4 a quantidade que cada número até n é inserido na lista
        while contador > 0:
            elementos[i] = j
            i += -1
            contador += -1
        j += -1    
    random.shuffle(elementos)
    return elementos

def inserir_elementos(aleatorizados: list[int], lista: list[Pilha]):
    x = 0 
    z = 0
    while x < n:
        if not lista[x].cheia():
            lista[x].empilha(aleatorizados[z])
            z += 1
        else:
            x += 1
    return lista

def imprimir_pilhas(lista: list[Pilha]):
    x = 0
    while x < len(lista):
        print(lista[x].elem)
        x += 1

def verifica_iguais(lista: list[Pilha], n):
    x = 0
    n = 3
    lista = [[2,2,2,2],[1,1,1,1],[3,3,3,3],[0,0,0,0],[0,0,0,0]]
    igualdade = True
    while x < n + 2 and igualdade:
        y = 0
        while y < 3 and igualdade:
            if lista[x].elem[y] == lista[x].elem[y+1]:
                igualdade = True
            else:
                igualdade = False
            y += 1
        x += 1
    return igualdade ######


y = criar_pilhas(n)
#l = verifica_iguais(y,n)
#print(l)
w = aleatoriza_elementos(n)
h = inserir_elementos(w,y)
#imprimir_pilhas(h)
#print(verifica_iguais(h,n))




    





