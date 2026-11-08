fila = []
grupo1 = []
grupo2 = []
N = int(input("Numero de personas: "))
for n in range(N):
    peso = int(input(f"Peso de la persona {n+1}: "))
    fila.append(peso)
for i in range(N):
    if i % 2 == 0:
        grupo1.append(fila[i])
    else:
        grupo2.append(fila[i])

total1 = sum(grupo1)
total2 = sum(grupo2)

resultado = [total1, total2]
print(resultado)

dias = ["Lunes", "Martes", "Miercoles", "Jueves",
        "Viernes", "Sabado", "Domingo"]

lstTotalesDias = []

for c in range(7):
    suma = 0
    for f in range(5):
        suma += matVentas[f][c] * lstPrecios[f]

    lstTotalesDias.append(suma)

maxDia = max(lstTotalesDias)
diaMayor = lstTotalesDias.index(maxDia)

print(f"El dia {dias[diaMayor]} es el que genera mayores ingresos "f"con ventas de ${maxDia:,}")