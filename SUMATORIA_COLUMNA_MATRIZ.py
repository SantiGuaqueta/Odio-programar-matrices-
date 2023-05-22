print("SUMATORIA DE COLUMNA DE UNA MATRIZ")

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

def Suma_Columna (filas,matrizA,k):
    Columna = [] # Dejo una variable llamada columna como una lista vacia
    Sumatoria = 0 # Agrego otra variable definida como 0 
    for x in range(0,filas): # Este for sirve para recorrer el numero de filas puesto por el lector
        Columna.append(matrizA[x][k-1]) # Despues de recorrer las filas voy a adicionar a la lista vacia (columna) x(que inicia en 0 y aumenta hasta la cantidad de filas que puso el lecto),k-1 a k se le resta 1 debido a que en python la matriz inicia en 0 
                                        # Este proceso obtendra la columna que quiere el lector ningun dato diferente a esa columna se adicionara a la lista vacia  
    for y in range(0,len(Columna)): # Ahora recorro la lista (Columna) la cual tiene los datos de la columna en una fila 
        Sumatoria = Sumatoria + Columna[y] # Opero 
    return(Sumatoria) # Retorno la anterior operacion osea sumatoria   


if __name__ == "__main__":
    print("Introduzca los valores por filas para la matriz")
        
    print("MATRIZ A")
    filas = int(input("Especifique el numero de filas de la primera matriz: ")) # Pido la cantidad de filas
    columnas = int(input("Especifique el numero de columnas de la primera matriz: ")) # Pido la cantidad de columnas
    matrizA = crear_matriz(filas,columnas) # Realizo la matriz en la cual llamo a la funcion crear matriz
    for i in range (0,filas): # recorro desde 0, hasta las filas que pidio el lector
        print(matrizA[i]) # Imprimo la matriz
    
    k = int(input("Cual es la columna de la que quiere obtener la sumatoria: ")) #  Pido cual la fila de la que quiere obtenenr la sumatoria
     
    Sumatoria_k = Suma_Columna (filas,matrizA,k) # Llamo a la funcion suma columna 
    print(Sumatoria_k) # imprimo la variable con la que llame la funcion