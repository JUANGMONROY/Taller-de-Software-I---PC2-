#1 funcion con libreria
from random import randint

def lista2D(m,n):
    lista=[]

    for i in range(m):
            lista.append([0]*n) #HAGO LA LISTA DE LISTAS
    for i in range(m):
        for j in range(n):
            lista[i][j]= randint(0,100) #LLENO LA LISTA CON VALORES RANDOM
    return lista #retorno la lista
