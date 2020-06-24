#Ejercicio 4 con su libreria
import numpy as np
def crea_arreglo():
    n = np.random.randint(5,21,size=(20,20)) #Creo mi matriz con valores aleatorios
    print("============================Original============================")
    print(n) #Imprimo la matriz original
    print("================================================================")
    
    for i in range(20):
        print((i+1),"ITERACIÓN") #Voy enumerando las iteraciones
        x = n[:,0] #Guardo la primera columna que se va a pasear por el arreglo
        x = np.reshape(x,(20,1)) #Reformo la variable x para que sea solo una columna

        h=n[:,1:20] #Elimino las primera columna para que las demas avanzen 
        n = np.append(h,x,axis=1) #Añado la columna que guarde en un principio como columna final del arreglo

        print(n) #Va imprimir 20 veces y nuestra columna 0 se va a pasear por todo el arreglo hasta ser como el arreglo original
        print("================================================================")
    return "Finalizado"
