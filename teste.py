from lista_encadeada import ListaEncadeada
#import random as r
#list1 = [44,45,49,70,27,73,92,97,95]
#listaenv = []
#for i in range(12):
    #listaenv.append(0)

# dict = {}

def insert(valor,fator,lista,dict):
    restante = valor % fator
    if lista[restante] == 0:
        lista[restante] = valor
    else:
        if restante in dict.keys():
            LE = dict[restante]
            LE.insert(valor)
            dict[restante] = LE
        else:
            LE = ListaEncadeada()
            LE.insert(valor)
            dict[restante] = LE

def printListaHash(listas,listadedict):
    index_dict = 0
    for lista in listas:
        index = 0
        dict = listadedict[index_dict]
        for i in lista:
            if i != 0:
                numero = str(i)
                if index in dict.keys():
                    LE = dict[index]
                    print(str(index) + "->" + numero + "-> " + LE.printList() + "\ ")
                else:
                    print(str(index) + "->" + numero + "-> \ ")
            else:
                print(str(index) + "-> \ ")
            index = index + 1
        print("------------------")
        index_dict = index_dict + 1

print("ENTRADA")

numeroVezes = int(input())

listaDelista = []
listaDedict = []
for i in range(numeroVezes):
    args = input()
    lista_args = args.split(" ")
    fator = int(lista_args[0])
    qtdNumero  = int(lista_args[1])
    numeros = input()
    lista = numeros.split(" ")
    j = 0
    for h in lista:
        lista[j] = int(h)
        j= j+1
    listaenv=[]
    for a in range(fator):
        listaenv.append(0)
    dict = {}
    for b in lista:
        insert(b,fator,listaenv,dict)
    listaDelista.append(listaenv)
    listaDedict.append(dict)

    
print("SAÍDA")
printListaHash(listaDelista,listaDedict)
