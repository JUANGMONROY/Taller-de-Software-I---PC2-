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

#2 función con libreria
import numpy as np
def mueve_col(n,columna):
    x1 = n.shape[0] #filas que tiene mi arreglo
    x2 = n.shape[1] #columnas que tiene mi arreglo
    cero = np.zeros((x1,1))
    #=======================
    x = n[:,columna] #Guardo la columna que quiero cambiar en una variable
    x = np.reshape(x,(x1,1)) #Reformo la columna para que sea solo una columna con el numero de filas que tenga el arreglo
    suma = cero + x #Sumo la columna de ceros con la columna que queria mover para no perder los valores
    #=======================
    n[:,columna]=n[:,x2-1] #Cambio la ultima columna por la columna que quiero mover
    n1 = n
    n1=np.delete(n1,x2-1,axis=1) #Elimino la ultima columna porque esta repetida dos veces
    #=======================
    new = np.append(n1,suma,axis=1) #Añado la columna que queria mover en un principio al final del arreglo
    return new
