# esta es la clase baes que tiene el nombre y el correo
class Usuario:
    def __init__(self, nombre, correo):
        self.__nombre = nombre           # Aqui el nombre es privado no se puede usar directo
        self.__correo = correo           # lo mismo con el correo

    # esto es para obtener el nombre
    def get_nombre(self):
        return self.__nombre

    # y este de aca para el correo
    def get_correo(self):
        return self.__correo

    # este metodo se puede cambiar en otras clases
    def mostrar_informacion(self):
        print(f"Usuario: {self.__nombre}, Correo: {self.__correo}")

# aqui se crea una clase quee hereda de Usuario
class Estudiante(Usuario):
    def __init__(self, nombre, correo, carrera):
        super().__init__(nombre, correo)    # esto llama a la clase de arriba
        self.carrera = carrera              # aqui se le agrega la carrera

    # esto muestra la informacion del estudiante
    def mostrar_informacion(self):
        print(f"Estudiante: {self.get_nombre()}, Correo: {self.get_correo()}, Carrera: {self.carrera}")

# esta otra clase tambien hereda pero es para profesor
class Profesor(Usuario):
    def __init__(self, nombre, correo, materia):
        super().__init__(nombre, correo)
        self.materia = materia

    # lo mismo aqui muestra la informacion pero del profesorr
    def mostrar_informacion(self):
        print(f"Profesor: {self.get_nombre()}, Correo: {self.get_correo()}, Materia: {self.materia}")

# Aqui ya empieza a funcionar el código

# creamos un usuario normal
usuario1 = Usuario("Bryam", "bryam@email.com")
# un estudiante
estudiante1 = Estudiante("Carlos", "carlos@email.com", "TICS")
# y un profesor
profesor1 = Profesor("Diana", "diana@email.com", "Programacion")

# ahora se muestra la informacion de cada uno
usuario1.mostrar_informacion()
estudiante1.mostrar_informacion()
profesor1.mostrar_informacion()