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
    
