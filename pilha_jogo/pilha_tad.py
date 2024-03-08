# Nome: Lucas de Oliveira Fratus RA:134698
# Nome: Giovani Oliveira Santos RA:133166

from dataclasses import dataclass

@dataclass
class TpNo:
    info: int
    prox: None | TpNo

class Pilha:
    topo: None | TpNo

    def __init__(self) -> None:
        self.topo = None
    
    def empilha(self , info: int) -> None:
        self.topo = TpNo(info, self.topo)

    def desempilha(self) -> int | None:
        i: int | None = None

        if not self.vazio():
            i = self.topo.info
            self.topo = self.topo.prox
        
        return i

    def vazio(self) -> bool:
        return self.topo is None

    def __str__(self) -> str:
        s = '['
        n = self.topo

        while n is not None:
            s += str(n.info) + ', '
            n = n.prox
        
        if s[-1] == ' ':
            s = s[:-2] + ']'

        else:
            s += ']'

        return s

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Pilha):
            return False
        
        n1 = self.topo
        n2 = __value.topo

        while n1 is not None and n2 is not None:
            if n1.item != n2.item:
                return False
            n1 = n1.prox
            n2 = n2.prox
        
        return n1 is None and n2 is None
    
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)         