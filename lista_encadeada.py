class No:
    def __init__(self,valor=0,proximo=None):
        self.valor = valor
        self.proximo = proximo

    def getValor(self):
        return self.valor

    def getProximo(self):
        return self.proximo
    
    def setValor(self, valor):
        self.valor = valor

    def setProximo(self,proximo):
        self.proximo = proximo

class ListaEncadeada:
    def __init__(self):
        self.cabeca = No()
    
    def insert(self,valor):
        novo_no = No(valor)
        if self.cabeca.getProximo() is None:
            self.cabeca.setProximo(novo_no)
        else:
            aux = self.cabeca.getProximo()
            self.cabeca.setProximo(novo_no)
            novo_no.setProximo(aux)

    def printList(self):
        no = self.cabeca.getProximo()
        string = ""
        while(no):
            string = string + str(no.getValor()) + "->"
            no = no.getProximo()
        return string
        



        
