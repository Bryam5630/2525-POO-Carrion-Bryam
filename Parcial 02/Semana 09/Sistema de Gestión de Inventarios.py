# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos básicos
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters para poder obtener lso valores
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters aqui se cambia los valores
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []  # Lista para guardar productos

    def agregar_producto(self, producto):
        # Verificar que no haya otro producto con el mismo ID
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("No se encontró el producto.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("No se encontró el producto.")

    def buscar_por_nombre(self, nombre):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():  # Coincidencia parcial
                resultados.append(p)
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for p in self.productos:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, "
                      f"Cantidad: {p.get_cantidad()}, Precio: ${p.get_precio():.2f}")


# Interfaz de usuario
def menu():
    inventario = Inventario()

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
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (deja vacío si no cambias): ")
            nuevo_precio = input("Nuevo precio (deja vacío si no cambias): ")

            # si se deja vacio , no se actualiza
            cantidad_valor = int(nueva_cantidad) if nueva_cantidad else None
            precio_valor = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id_producto, cantidad_valor, precio_valor)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, "
                          f"Cantidad: {p.get_cantidad()}, Precio: ${p.get_precio():.2f}")
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")


# Ejecutar el programa
menu()
