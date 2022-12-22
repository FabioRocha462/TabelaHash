from lista_encadeada import ListaEncadeada
def restodiv(valor,fator):
    return valor % fator
def insert(valor,fator,lista,dict):
    resto = restodiv(valor,fator)
    if lista[resto] == 0:
        lista[resto] = valor
    else:
        if resto in dict.keys():
            LE = dict[resto]
            LE.insert(valor)
        else:
            LE = ListaEncadeada()
            LE.insert(valor)
            dict[resto] = LE
def print_lista(listaDeLista,listaDedict):
    index_dict = 0
    for lista in listaDeLista:
        dict = listaDedict[index_dict]
        index = 0
        for i in lista:
            if i != 0:
                print(i, sep="")
                if index in dict.keys():
                    LE = dict[index]
                    print(LE.printList())
                else:
                    print("->",sep="")
            print("/")
            index = index + 1
        index_dict = index_dict + 1
        print("-------------------------")
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
    for a in range(len(lista)+fator):
        listaenv.append(0)
    dict = {}
    for b in lista:
        insert(b,fator,listaenv,dict)
    listaDelista.append(lista)
    listaDedict.append(dict)

    
print("SAÍDA")
print_lista(listaDelista,listaDedict)
     

    

