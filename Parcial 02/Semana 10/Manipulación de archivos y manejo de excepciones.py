import os
import shutil
from datetime import datetime

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def to_line(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_line(linea):
        try:
            id_producto, nombre, cantidad, precio = linea.strip().split(",")
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except ValueError:
            return None


# Clase Inventario
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        base_dir = os.path.dirname(os.path.abspath(__file__))  # carpeta donde está el .py
        self.archivo = os.path.join(base_dir, archivo)         # archivo fijo en esa carpeta
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        validos = 0
        invalidos = 0
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    producto = Producto.from_line(linea)
                    if producto:
                        self.productos.append(producto)
                        validos += 1
                    else:
                        invalidos += 1
        except FileNotFoundError:
            print("[INFO] Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
            try:
                open(self.archivo, "w", encoding="utf-8").close()
            except PermissionError:
                print("[ERROR] No tienes permisos para crear el archivo de inventario en esta ubicación.")
        except PermissionError:
            print("[ERROR] Sin permisos para leer el archivo de inventario. Cambia permisos o la ubicación.")
        except Exception as e:
            print(f"[ERROR] Error inesperado al leer el archivo: {e}")

        if validos == 0 and invalidos > 0:
            try:
                ts = datetime.now().strftime("%Y%m%d-%H%M%S")
                backup = f"{self.archivo}.bak-{ts}"
                shutil.copy2(self.archivo, backup)
                print(f"[ALERTA] El archivo parecía corrupto. Se hizo respaldo en: {backup}")
                open(self.archivo, "w", encoding="utf-8").close()
                self.productos = []
                print("[INFO] Inventario reconstruido vacío.")
            except PermissionError:
                print("[ERROR] No se pudo hacer respaldo: sin permisos para copiar el archivo.")
            except Exception as e:
                print(f"[ERROR] No se pudo respaldar el archivo corrupto: {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(p.to_line())
            return True
        except PermissionError:
            print("[ERROR] Sin permisos para escribir en el archivo de inventario.")
            return False
        except Exception as e:
            print(f"[ERROR] Error al guardar en el archivo: {e}")
            return False

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        ok = self.guardar_en_archivo()
        if ok:
            print("Producto agregado con éxito y guardado en archivo.")
        else:
            print("Producto agregado en memoria, pero NO se pudo guardar en archivo.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                ok = self.guardar_en_archivo()
                if ok:
                    print("Producto eliminado y archivo actualizado.")
                else:
                    print("Producto eliminado en memoria, pero NO se pudo actualizar el archivo.")
                return
        print("No se encontró el producto.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                ok = self.guardar_en_archivo()
                if ok:
                    print("Producto actualizado y guardado en archivo.")
                else:
                    print("Producto actualizado en memoria, pero NO se pudo guardar en archivo.")
                return
        print("No se encontró el producto.")

    def buscar_por_nombre(self, nombre):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
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
            try:
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: cantidad y precio deben ser números.")

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (deja vacío si no cambias): ")
            nuevo_precio = input("Nuevo precio (deja vacío si no cambias): ")

            try:
                cantidad_valor = int(nueva_cantidad) if nueva_cantidad else None
                precio_valor = float(nuevo_precio) if nuevo_precio else None
                inventario.actualizar_producto(id_producto, cantidad_valor, precio_valor)
            except ValueError:
                print("Error: cantidad y precio deben ser números válidos.")

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


if __name__ == "__main__":
    menu()
