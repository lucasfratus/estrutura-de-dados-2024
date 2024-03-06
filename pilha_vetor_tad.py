class Pilha:
    memoria: list[int]
    topo: int

    def __init__(self, size):
        self.memoria = [0] * size
        self.topo = -1

    def vazio(self):
        return self.topo == -1
    
    def cheia(self):
        return self.topo == len(self.memoria) - 1

    def tamanho_pilha(self):
        return self.top + 1

    def empilha(self, valor):
        if self.cheia():
            raise ValueError('Pilha Cheia!')
        else:
            self.topo += 1
            self.memoria[self.topo] = valor

    def desempilha(self):
        if self.vazio():
            raise ValueError('Pilha Vazia!')
        else:
            desempilhado = self.memoria[self.topo]
            self.memoria[self.topo] = 0
            self.topo += -1
            return desempilhado

    def __str__(self) -> str:
        return str(self.memoria)