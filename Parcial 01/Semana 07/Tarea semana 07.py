class Persona:
    # esto se ejecuta cuando se crea el objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"[Constructor] Se crea la persona {self.nombre} con {self.edad} años.")

    # método para mostrar los datos de la persona
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    # Esto se ejecuta cuando se elimina el objeto
    def __del__(self):
        print(f"[Destructor] El objeto de {self.nombre} fue eliminado .")


# esta es la parte princiipal del programa
if __name__ == "__main__":
    # Aquí se crea una persona
    persona1 = Persona("Bryam", 19)

    # Mostramos los datos de la persona
    persona1.mostrar_datos()

    # Eliminamos el objeto
    del persona1
    print("Fin del programa..")