lista=[34, 7, 23, 32, 5]
def buble(lista):
    n=len(lista)-1
    for i in range(0,n):
        for j in range(0,n):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    return lista
print(buble(lista=[1,4,8,7,84,54,53]))