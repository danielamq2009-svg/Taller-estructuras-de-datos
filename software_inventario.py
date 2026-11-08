
inventario = []

def mostrar_menu():
    print("\n===== MENÚ DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Agregar lote de productos")
    print("3. Eliminar producto del inventario")
    print("4. Eliminar el producto más reciente")
    print("5. Ordenar productos alfabéticamente")
    print("6. Mostrar número total de productos")
    print("7. Salir")


def agregar_producto():
    producto = input("Ingrese el nombre del producto: ")
    inventario.append(producto)
    print("Producto agregado correctamente.")
    input("Presione enter para continuar")

def agregar_lote():
    cantidad = int(input("¿Cuántos productos desea agregar?: "))
    if cantidad <= 0:
        print("Ingrese una cantidad mayor que cero.")
        return
    for i in range(cantidad):
        producto = input(f"Ingrese el producto {i + 1}: ")
        inventario.append(producto)
        print(f"{producto} agregado correctamente.")
        
    print("Lote de productos agregado.")
    input("Presione enter para continuar")

def eliminar_producto():
    producto = input("Ingrese el producto que desea eliminar: ")

    if producto in inventario:
        inventario.remove(producto)
        print("Producto eliminado correctamente.")
        input("Preione enter para continuar")
    else:
        print("El producto no se encuentra en el inventario.")
        input("Presione enter para continuar")

def eliminar_reciente():
    producto = inventario.pop()
    print(f"Se eliminó el producto más reciente: {producto}")
    input("Presione enter para continuar")

def ordenar_productos():
    if inventario:
        inventario.sort(key=str.lower)
        print("Inventario ordenado alfabéticamente:")
        for producto in inventario:
            print("-", producto)
    else:
        print("No hay productos para ordenar.")
        input("Presione enter para continuar")
    input("Presione enter para continuar")

def mostrar_total():
    print(f"Total de productos: {len(inventario)}")
    input("Presione enter para continuar")

while True:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        agregar_lote()
    elif opcion == 3:
        eliminar_producto()
    elif opcion == 4:
        eliminar_reciente()
    elif opcion == 5:
        ordenar_productos()
    elif opcion == 6:
        mostrar_total()
    elif opcion == 7:
        print("Gracias por utilizar el sistema de inventario.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
