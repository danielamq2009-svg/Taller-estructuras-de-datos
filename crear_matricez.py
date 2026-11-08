def crearMatCuadrada(tam, valor=0):
    mat = []
    for f in range(tam):
        mat.append([valor] * tam)
    return mat

def printMatriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end="\t")
        print("")

tamaño=int(input("Indique el tamaño de la matriz cuadrada: "))

while tamaño <= 0:
    tam = int(input("Ingrese un tamaño mayor que cero: "))
    
matriz = crearMatCuadrada(tamaño)

# Matriz uno
cont = 1
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        matriz[f][c] = cont
        cont +=1
print("Matriz 1 ")        
printMatriz(matriz)
print(" ")

# Matriz dos
matriz = crearMatCuadrada(tamaño)
cont = 1
signo=1
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        matriz[f][c] = cont
        cont =cont + signo * 1
    signo *= -1
    cont =cont + signo * 1

print("Matriz 2 ")  
asc = list(range(1,tamaño+1))
des = asc[::-1]
matriz = []
for i in range(tamaño):
    matriz.append(asc if i%2 == 0 else des)
printMatriz(matriz)

# Matriz tres
matriz = crearMatCuadrada(tamaño)

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if [f]==[c]:
            matriz[f][c] = 1
            
print("Matriz 3 ")  
printMatriz(matriz)
            
# Matriz cuatro
matriz = crearMatCuadrada(tamaño)

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if f + c == tamaño - 1:
            matriz[f][c] = 1

print("Matriz 4 ")  
printMatriz(matriz)

# Matriz cinco
matriz = crearMatCuadrada(tamaño)

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if f >= c:
            matriz[f][c] = 1

print("Matriz 5 ")  
printMatriz(matriz)

# Matriz seis
matriz = crearMatCuadrada(tamaño)

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if f <= c:
            matriz[f][c] = 1

print("Matriz 6")  
printMatriz(matriz)

# Matriz siete
matriz = crearMatCuadrada(tamaño)

cont = 1
for c in range(tamaño):
    for f in range(tamaño):
        matriz[f][c] = cont
        cont +=1
print("Matriz 7 ")        
printMatriz(matriz)
print(" ")

# Matriz ocho
matriz = crearMatCuadrada(tamaño," ")

cont = " "
for f in range(tamaño):
    for c in range(tamaño):
        if f >= c:
            if c %2==0:
                matriz[f][c] = "A"
            else:
                matriz[f][c] = "B"
                
        
print("Matriz 8")        
printMatriz(matriz)
print(" ")