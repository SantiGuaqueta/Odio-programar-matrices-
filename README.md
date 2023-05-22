# Odio-programar-matrices-
El dia de hoy resolveremos el reto 11 que nos dejo el profesor, el cual trata unicamente de matrices. Como sabemos antes de empezar a resolver los ejercicios mostraremos un dato innecesario pero interesante asi que a continuacion:
#### Dato Inncesesario del día


[![Dato-innecesario-1.jpg](https://i.postimg.cc/Jn3rx1gt/Dato-innecesario-1.jpg)](https://postimg.cc/0MQ12q9q)


Ahora si empecemos a relizar el reto para esto se pondra el enunciado y abajo su codigo sin embargo cada punto se suvira en un archivo aparte y alfinal en un archivo unido.

#### Reto 11
1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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
```
2.Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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

```

3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
``` python
print("MATRIZ TRANSPUESTA")

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

def Matriz_Transpuesta (filas,columnas,matrizA):
    transpuesta = [] # Adiciono variable de nombre transpuesta como una lista vacia
    for x in range(0,columnas): # Recorro la cantidad de columnas que haya puesto el lector osea de 0 hasta n columnas. Es muy importante que este for recorra columnas si recorre filas el programa no funcionara
        lista = [] # Agrego una lista vacia
        for m in range (0,filas): # Ahora recorro el numero de filas que se hayan puesto al correr el codigo
            lista.append(matrizA[m][x]) # Agrego a la lista vacia la matriz[x][m] esto es muy importante pues en este paso es donde las columnas se vuelven filas.
                                        # Porque cuando x sea 0 y m sea 0 se tomara el rpimer valor de la primera fila osea 0,0 cuando m sea 1 se tomara el primer valor de la segunda fila y asi sucesivamente. y despues de acabar con los m se volvera a repetir el cilo pero esta vez con x 1 y asi hasta que se complete el primer for
        transpuesta.append(lista) # Adicionamos los valores de la lista ahora a la variable vacia de nombre transpuesta con ayuda del append
    return(transpuesta)  # Retornamos la transpuesta 


if __name__ == "__main__":
    print("Introduzca los valores por filas para la matriz")
        
    print("MATRIZ A")
    filas = int(input("Especifique el numero de filas de la primera matriz: ")) # Pido la cantidad de filas
    columnas = int(input("Especifique el numero de columnas de la primera matriz: ")) # Pido la cantidad de columnas
    matrizA = Crear_Matriz(filas,columnas) # Realizo la matriz en la cual llamo a la funcion crear matriz
    for i in range (0,filas): # recorro desde 0, hasta las filas que pidio el lector
        print(matrizA[i]) # Imprimo la matriz
    
    
    matrizT = Matriz_Transpuesta(filas,columnas,matrizA) # Llamo a la funcion de Matriz tranpuesta
    print("La transpuesta de la matriz es: ")
    for i in range (0,columnas): # Estos dos ultimos paso son igual que la matriz A y sirve para que la matriz se observe como una matriz osea como un cuadrado o rectangulo y no como una linea recta
        print(matrizT[i])
```     

4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.
``` python
print("SUMATORIA DE COLUMNA DE UNA MATRIZ")

def crear_matriz(filas,columnas): # Declaro mi primera funcion la cual se utilizara para crear las matrices.
    matriz=[] # Dejare esta lista de nombre matriz vacia.
    for i in range (0,filas): # Declaro que para i en el rango de 0 hasta las filas que halla puesto el lector realice lo siguiente.
        print("ingrese los valores de la fila" + str(i)) # Debe ingresar los valors que quiere por fila
        fila= [] # Ingreso otra variable vacia
        for j in range(0, columnas): # Ahora declaro que para j en el rango de 0, hasta columnas realice lo siguiente.
            valor=floatt(input()) # Pida un entero como valor
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
```
5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.
``` python
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
```
