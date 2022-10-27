import random

tablero = []
tamaño = int(input("introduzca el tamaño del tablero: "))
#rellenar tablero
for i in range(int(tamaño)):
    fila = []
    for j in range(int(tamaño)):
        fila+=["0"]
    tablero.append(fila)
print(tablero)
#colocar minas
contador = 5
while contador!=0:
    posicion1 = random.randint(0,int(tamaño)-1)
    posicion2 = random.randint(0,int(tamaño)-1)
    if tablero[posicion1][posicion2]!="B":
        tablero[posicion1][posicion2]="B"
        contador-=1
    else:
        pass
#rellenar numeros tablero
num_aux = int
for i in range(len(tablero)):
    for j in range(len(tablero)):
        
        if i < tamaño-1:
            if tablero[j][i + 1]=="B" and tablero[j][i]!="B":
                num_aux =int(tablero[j][i])+ 1
                tablero[j][i]=num_aux
            if j > 0:
                if tablero[j - 1][i + 1]=="B" and tablero[j][i]!="B":
                    num_aux = int(tablero[j][i])+1
                    tablero[j][i]=num_aux
        if i > 0:
            if tablero[j][i - 1]=="B" and tablero[j][i]!="B":
                num_aux =int(tablero[j][i])+ 1
                tablero[j][i]=num_aux
            if j < tamaño - 1:
                if tablero[j + 1][i - 1]=="B" and tablero[j][i]!="B":
                    num_aux =int(tablero[j][i])+ 1
                    tablero[j][i]=num_aux
        if j > 0:
            if tablero[j - 1][i]=="B" and tablero[j][i]!="B":
                num_aux = int(tablero[j][i]) + 1
                tablero[j][i]=num_aux
            if i > 0:
                if tablero[j - 1][i - 1]=="B" and tablero[j][i]!="B":
                    num_aux =int(tablero[j][i])+ 1
                    tablero[j][i]=num_aux
        if j < tamaño - 1:
            if tablero[j + 1][i]=="B" and tablero[j][i]!="B":
                num_aux = int(tablero[j][i])+1
                tablero[j][i]=num_aux
            if i < tamaño - 1:
                if tablero[j + 1][i + 1]=="B" and tablero[j][i]!="B":
                    num_aux = int(tablero[j][i]) + 1
                    tablero[j][i]=num_aux
#imprimir tablero
for i in range(len(tablero)):
    for j in range(len(tablero[i])):
        print(tablero[i][j], end=" ")
    print()
