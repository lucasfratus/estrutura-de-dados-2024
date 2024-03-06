class Pilha:
    elem: list[int]
    topo: int

    def __init__(self, size):
        self.elem = [0] * size
        self.topo = -1

    def vazio(self):
        return self.topo == -1
    
    def cheia(self):
        return self.topo == len(self.elem) - 1

    def tamanho_pilha(self):
        return self.top + 1

    def empilha(self, valor):
        if self.cheia():
            raise ValueError('Pilha Cheia!')
        else:
            self.topo += 1
            self.elem[self.topo] = valor

    def desempilha(self):
        if self.vazio():
            raise ValueError('Pilha Vazia!')
        else:
            desempilhado = self.elem[self.topo]
            self.elem[self.topo] = 0
            self.topo += -1
            return desempilhado

    #def __str__(self) -> str:
        return str(self.elem)