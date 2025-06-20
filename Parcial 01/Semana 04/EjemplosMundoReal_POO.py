#PRIMEOR CREAMOS LA CLASE
class Pantalon:
    def __init__(self, marca, talla, precio):
        #Aqui van los atributos que teine el pantalon
        self.marca = marca
        self.talla = talla
        self.precio = precio

    def mostrarInformacion(self):
        print(f"Pantalón {self.marca}, Talla: {self.talla}, Precio: ${self.precio}")

# Ahora la hacemos la teinda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def agregarPantalon(self, pantalon):
        self.inventario.append(pantalon)

    def mostrarInventario(self):
        print(f"Inventario de {self.nombre}:")
        for pant in self.inventario:
            pant.mostrarInformacion()


# Creamso los pantalones
p1 = Pantalon("Fila", "L", 18.49)
p2 = Pantalon("Adibas", "M", 19.99)
p3 = Pantalon("Kike", "S", 23.05)

# Creamos la tienda
miTienda = Tienda("TIENDA DE LA VECI")

# Agregamos pantalones
miTienda.agregarPantalon(p1)
miTienda.agregarPantalon(p2)
miTienda.agregarPantalon(p3)

# Mostramos inventario
miTienda.mostrarInventario()
