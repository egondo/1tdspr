class Pilha:

    def __init__(self, qtd: int):
        self.lista = [None] * qtd
        self.topo = -1

    def isEmpty(self):
        if self.topo == -1:
            return True
        return False

    def isFull(self):
        return False

    def pop(self):
        pos = self.topo
        self.topo = self.topo - 1
        return self.lista[pos]

    def peek(self):
        return self.lista[self.topo]

    def put(self, info):
        if self.topo + 1 == len(self.lista):
            self.topo = self.topo + 1
            self.lista.append(info)
        else:
            self.topo = self.topo + 1
            self.lista[self.topo] = info
