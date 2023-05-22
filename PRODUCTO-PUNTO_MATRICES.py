print("PRODUCTO PUNTO DE MATRICES\n", "El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.") # Importante la condicion dicha en este apartado

def Crear_Matriz(filas,columnas): # Declaro mi primera funcion la cual se utilizara para crear las matrices.
    matriz=[] # Dejare esta lista de nombre matriz vacia.
    for i in range (0,filas): # Declaro que para i en el rango de 0 hasta las filas que halla puesto el lector realice lo siguiente.
        print("ingrese los valores de la fila" + str(i)) # Debe ingresar los valors que quiere por fila
        fila= [] # Ingreso otra variable vacia
        for j in range(0, columnas): # Ahora declaro que para j en el rango de 0, hasta columnas realice lo siguiente.
            valor=float(input()) # Pida un entero como valor
            fila. append(valor) # el anterior entero se adiciona a la lista vacia llamada fila que declaramos antes. 
        matriz.append(fila) # Ahora pido que la fila se adicione a la matriz vacia antes declarada.
    return(matriz) # Pido que retorne matriz

def Producto_Punto_Matrices (filas_A,filas_B,columnas_B,matrizA, matrizB): # Declaro la funcion, y en las valoriables que vamos a utilizar no le agregamos columnas A puesto que son iguales(relacion tamaño) que las filas B 
    Producto_Punto = [] # Agregamos una variable en forma de lista que estara vacia
    for i in range(0,filas_A): # Primer for que recorrera las filas A
        fila = [] # Agregamos variable en forma de lista que estara vacia
        for j in range(0,columnas_B): # Segundo for que recorrera las columnas B 
            lista1 = matrizA[i] # Declaro una lista que es igual a el reccorido de filas de la primera matriz
            lista2 = [] # Declaro segunda lista que estara vacia
            producto = 0 # Declaro variable producto la cual es 0 y la que utilizaremos mas adelante para operar
            for m in range(0,filas_B): # Ahora con este tercer for se recorrera las filas B
                lista2.append(matrizB[m][j]) # A la lista dos se le agregara o adiconara la matrizB[m][j] sabemos que m representa un valor desde 0 hasta la cantidad de filas de B y J tiene un valors desde 0 hasta la cantidad de columnas de B
            for n in range(len(lista1)): # Declaro un 4 for donde recorrera la lista 1 
                producto = producto + lista1[n]*lista2[n] # Hacemos la operacion donde 
            fila.append(producto) # La operacion anterior se agregara a la fila vacia 
        Producto_Punto.append(fila) # y la fila que ya no esta vacia se adiciona al producto punto que era una lista vacia
    return(Producto_Punto) # Retornamos producto punto


if __name__ == "__main__":
    print("Introduzca los valores por filas para la matriz")
    # Creo la primera matrizA     
    print("MATRIZ A")
    filas_A = int(input("Especifique el numero de filas de la primera matriz: ")) # Pido cantidad de filas
    columnas_A = int(input("Especifique el numero de columnas de la primera matriz: ")) # Pido cantidad de columnas
    matrizA = Crear_Matriz(filas_A,columnas_A) # Llamo a la funcion crear materiz
    for i in range (0,filas_A): 
        print(matrizA[i]) # imprimo la matriz
    
    # En matrizB se realiza casi lo mismo lo unico que lo diferencia es que la condicion que agregamos es que las filas son igual que las columnas de la anterior matriz por ende no le pedimos filas al lector
    print("MATRIZ B")
    filas_B = columnas_A
    columnas_B = int(input("Especifique el numero de columnas de la segunda matriz: "))
    matrizB = Crear_Matriz(filas_B,columnas_B)
    for i in range (0,filas_B):
        print(matrizB[i])
    
    matrizC = Producto_Punto_Matrices(filas_A,filas_B,columnas_B,matrizA, matrizB) # Llamo a la funcion de producto punto matrices
    print("El producto punto de las matrices es: ")
    for i in range (0,filas_A):
        print(matrizC[i]) # imprimo la matriz
    
