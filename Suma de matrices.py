print("SUMA MATRICES: Para sumar matrices deben tener el mismo tamaño de filas y columnas") # Aclaro que este programa cuple esta condicion

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

def suma_matrices(columnas,filas,MatrizA, MatrizB): # Declaro la funcion de la suma de matrices, la cual utilizara valores como filas, columnas, Matriz A y Matriz B.
    suma=[] # Igual que la anterior funcion declararemos una lista vacia pero este caso con el nombre de suma
    for i in range (0,filas): 
        fila=[] # Declaro igual que antes una lista con nombre fila que vaya vacia 
        for j in range (0,columnas):
            sumador= MatrizA[i][j]+ MatrizB [i][j] # Aqui hago la suma de matrices donde digo que sume i que recorrio filas y j que reccorrio columnas de ambas matrices ya antes creadas
            fila.append(sumador) # Aqui adiciono a la lista vacia de fila el resultado anterior
        suma.append(fila) # En este adiciono fila a la lista vacia suma ya antes declarada
    return(suma) # Al final retorno suma


if __name__ =="__main__":
    filas=int(input( "Diga la cantidad de filas: ")) # Pido la cantidad de filas
    columnas=int(input( "Diga la cantidad de columnas: ")) # Pido la cantidad de columnas
    print( "Introduzca los valores por fila para la matriz")

    print("MatrizA")
    MatrizA=crear_matriz(columnas,filas) # Realizo la primera matriz en la cual llamo a la funcion crear matriz
    for i in range(0,filas): # recorro desde 0, hasta las filas que pidio el lector
        print(MatrizA[i]) # Imprimo la primera matriz

    print(" MatrizB")
    MatrizB=crear_matriz(columnas,filas) # Realizo la segunda matriz  en la cual llamo a la funcion crear matriz
    for i in range (0,filas): # recorro desde 0, hasta las filas que pidio el lector
        print(MatrizB[i]) # Imprimo la Segunda matriz
    
    print("MatrizC")
    MatrizC=suma_matrices(columnas,filas,MatrizA, MatrizB) # aqui llamo a la funcion suma de matrices
    print("La suma de las matrices es: ")
    for i in range(0,filas): # Realizo lo mismo que con las dos matrices anteriores
        print (MatrizC[i])