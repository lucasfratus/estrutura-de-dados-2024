from pilha_vetor_tad import Pilha
import random

n = int(input('Quantos números, entre 1 e 7, você deseja deseja distribuir entre as pilhas?')) # entrada da quantidade de números

assert n >= 1 and n <= 7 # garante que o número inserido seja entre 1 e 7

def criar_pilhas(n: int):
    qntde_pilhas = n + 2
    lista_pilhas = []
    for i in range(1, qntde_pilhas + 1):
        x = Pilha(4)
        lista_pilhas.append(x)
    return lista_pilhas

def insere_elementos(lista: list[Pilha], n):
    for x in range(len(lista) - 2):
        contador = 4
        while contador > 0:
            if not Pilha.cheia(lista[x]):
                Pilha.empilha(lista[x],x+1)
                contador += -1

def aleatoriza_pilha(lista: list[Pilha]):
    num_pilhas_validas = len(lista)
    for i in range(4):
        for j in range(num_pilhas_validas - 2):
            destino = random.randint(0, num_pilhas_validas - 3)
            # Troca os elementos entre as pilhas
            lista[j][i], lista[destino][i] = lista[destino][i], lista[j][i]

def imprimir_pilhas(lista: list[Pilha]):
    for x in lista:
        print(x)

i = criar_pilhas(n)
x = insere_elementos(i,n)
z = aleatoriza_pilha(i)
imprimir_pilhas(i)



    





