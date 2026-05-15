from pilha import Pilha

stack = Pilha(10)

stack.put("FIAP")
stack.put("FGV")
stack.put("USP")
stack.put("UNIP")
stack.put("PUC")
stack.put("UFRJ")

while not stack.isEmpty():
    info = stack.pop()
    print(info)