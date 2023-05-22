print("SUMATORIA DE FILA DE UNA MATRIZ")

def crear_matriz(filas,columnas): # Declaro mi primera funcion la cual se utilizara para crear las matrices.
    matriz=[] # Dejare esta lista de nombre matriz vacia.
    for i in range (0,filas): # Declaro que para i en el rango de 0 hasta las filas que halla puesto el lector realice lo siguiente.
        print("ingrese los valores de la fila" + str(i)) # Debe ingresar los valors que quiere por fila
        fila= [] # Ingreso otra variable vacia
        for j in range(0, columnas): # Ahora declaro que para j en el rango de 0, hasta columnas realice lo siguiente.
            valor=float(input()) # Pida un entero como valor
            fila. append(valor) # el anterior entero se adiciona a la lista vacia llamada fila que declaramos antes. 
        matriz.append(fila) # Ahora pido que la fila se adicione a la matriz vacia antes declarada.
    return(matriz) # Pido que retorne matriz

def Suma_Filas (filas,matrizA,k): 
    lista = [] # Dejo una lista vacia
    Sumatoria = 0 # le agrego una vatiable con nombre sumatoria la cual vale 0
    lista = matrizA[k-1] # explico que lista es igual a la fila que quiere el lector de la matriz que el lector escribio antes
    for x in range(len(lista)): # Recorro la lista la cual contiene la fila deseada
        Sumatoria = lista[x] + Sumatoria # Opero 
    return(Sumatoria) # Retorno la sumatoria


if __name__ == "__main__":
    print("Introduzca los valores por filas para la matriz")
        
    print("MATRIZ A")
    filas = int(input("Especifique el numero de filas de la primera matriz: ")) # Pido la cantidad de filas
    columnas = int(input("Especifique el numero de columnas de la primera matriz: ")) # Pido la cantidad de columnas
    matrizA = crear_matriz(filas,columnas) # Realizo la matriz en la cual llamo a la funcion crear matriz
    for i in range (0,filas): # recorro desde 0, hasta las filas que pidio el lector
        print(matrizA[i]) # Imprimo la matriz
    
    k = int(input("Cual es la fila de la que quiere obtener la sumatoria: ")) # Pido cual la fila de la que quiere obtenenr la sumatoria
    
    Sumatoria_k = Suma_Filas (filas,matrizA,k) # Llamo a la funcion de suma de filas
    print(Sumatoria_k) # Imprimo la Sumatoria_K la cual llamo a la funcion