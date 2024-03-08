from pilha_vetor_tad import Pilha
import random

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
        print('Pilha', x,' -> ', lista[x].elem)
        x += 1

def verifica_iguais(lista: list[Pilha], n):
    igualdade = True
    x = 0
    while x < n + 2 and igualdade:
        y = 0
        while y < 3 and igualdade:
            if lista[x].elem[y] == lista[x].elem[y+1]:
                igualdade = True
            else:
                igualdade = False
            y += 1
        x += 1
    return igualdade

def inicia_jogo(n: int):
    pilhas_criadas = criar_pilhas(n)
    numeros_aleatorizados = aleatoriza_elementos(n)
    pilhas_com_elementos_inseridos = inserir_elementos(numeros_aleatorizados, pilhas_criadas)
    imprimir_pilhas(pilhas_com_elementos_inseridos)
    return pilhas_com_elementos_inseridos

def jogada(lista: list[Pilha], pilha_origem: int, pilha_destino: int):
    if not lista[pilha_origem].vazio():
        if not lista[pilha_destino].cheia():
            desempilhado = lista[pilha_origem].desempilha()
            empilhado = lista[pilha_destino].empilha(desempilhado)
        else:
            print('Erro! Pilha de destino está cheia! Tente novamente...') 
    else:
        print('Erro! Pilha de origem está vazia! Tente novamente...')
            
    
    imprimir_pilhas(lista)
    return lista

def jogo_pilha(n):
    z = inicia_jogo(n)
    while verifica_iguais(z, n) == False:
        desempilhar_pilha = int(input('De qual pilha você deseja desempilhar os elementos? '))
        empilhar_pilha = int(input('Em qual pilha você deseja empilhar o elemento desempilhado? '))
        jogada(z, desempilhar_pilha, empilhar_pilha)
    print('Parabéns, você ganhou o jogo!')

print('Bem vindo(a) ao jogo! \nNesse jogo, você escolhe uma quantidade de números(entre 1 e 7) que vão ser distribuidos entre a mesma quantidade de pilhas \
que o número escolhido.\nSeu objetivo é fazer com que as pilhas fiquem, cada uma, com os 4 elementos iguais.')

n = int(input('Quantos números, entre 1 e 7, você deseja deseja distribuir entre as pilhas? ')) # entrada da quantidade de números

if n < 1 or n > 7: # garante que o número inserido seja entre 1 e 7
    raise ValueError('Erro! Número menor que 1 ou maior que 7! Tente novamente')
else:
    jogo_pilha(n)





    





