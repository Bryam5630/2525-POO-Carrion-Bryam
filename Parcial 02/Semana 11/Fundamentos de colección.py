import os

# Aqui es  donde se almacenará el inventario
ARCHIVO = "inventario.txt"

# Cargar inventario desde el archivo
def cargar_inventario():
    inventario = {}
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 4:
                    id_prod, nombre, cantidad, precio = datos
                    inventario[id_prod] = {
                        "nombre": nombre,
                        "cantidad": int(cantidad),
                        "precio": float(precio)
                    }
    return inventario

# Guardar inventario en archivo
def guardar_inventario(inventario):
    with open(ARCHIVO, "w") as f:
        for id_prod, datos in inventario.items():
            f.write(f"{id_prod},{datos['nombre']},{datos['cantidad']},{datos['precio']}\n")

# Este es el menú principal
def menu():
    inventario = cargar_inventario()

    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_prod = input("ID: ")
            if id_prod in inventario:
                print("Error: ya existe un producto con ese ID.")
                continue
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: $"))
            except ValueError:
                print("Error: cantidad y precio deben ser números.")
                continue
            inventario[id_prod] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
            guardar_inventario(inventario)
            print("Producto agregado.")

        elif opcion == "2":
            id_prod = input("ID del producto a eliminar: ")
            if id_prod in inventario:
                del inventario[id_prod]
                guardar_inventario(inventario)
                print("Producto eliminado.")
            else:
                print("Error: producto no encontrado.")

        elif opcion == "3":
            id_prod = input("ID del producto a actualizar: ")
            if id_prod in inventario:
                try:
                    cantidad = int(input("Nueva cantidad: "))
                    precio = float(input("Nuevo precio: $"))
                except ValueError:
                    print("Error: cantidad y precio deben ser números.")
                    continue
                inventario[id_prod]["cantidad"] = cantidad
                inventario[id_prod]["precio"] = precio
                guardar_inventario(inventario)
                print("Producto actualizado.")
            else:
                print("Error: producto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ").lower()
            encontrados = [datos for datos in inventario.values() if datos["nombre"].lower() == nombre]
            if encontrados:
                for p in encontrados:
                    print(f"Nombre: {p['nombre']}, Cantidad: {p['cantidad']}, Precio: ${p['precio']:.2f}")
            else:
                print("No se encontró el producto.")

        elif opcion == "5":
            if inventario:
                for id_prod, datos in inventario.items():
                    print(f"ID: {id_prod}, Nombre: {datos['nombre']}, Cantidad: {datos['cantidad']}, Precio: ${datos['precio']:.2f}")
            else:
                print("El inventario está vacío.")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()



#DOCUMENTACIÓN:

# Este programa sirve para llevar el inventario de una tienda.
#   Usa un diccionario para guardar los productos con su ID, nombre, cantidad y precio.
#  Permite agregar, eliminar, actualizar, buscar y mostrar productos.
#   Guarda los datos en un archivo llamado "inventario.txt" para que no se pierdan.
#  Tiene un menú sencillo en la consola para usar todas las funciones.