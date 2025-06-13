class SemanaTemperaturas:
    def __init__(self):
        # Diccionario para guardar temperaturas
        self.temperaturas = {
            "lunes": 0,
            "martes": 0,
            "miércoles": 0,
            "jueves": 0,
            "viernes": 0,
            "sábado": 0,
            "domingo": 0
        }

    def pedir_temperaturas(self):
        for dia in self.temperaturas:
            while True:
                # Le pedimos  la temperatura y la guardamos en el diccionario
                temp = float(input(f"Ingresa la temperatura del {dia} (°C): "))
                self.temperaturas[dia] = temp
                break

    def calcular_promedio(self):
        # Aqui se calcula el promedio de la semana
        total = sum(self.temperaturas.values())
        return total / 7


# Aqui empieza el programa principal
if __name__ == "__main__":
    # Creamos el objeto
    semana = SemanaTemperaturas()

    # Pedimos temperaturas
    semana.pedir_temperaturas()

    # Calculamos y muestra el promedio
    promedio = semana.calcular_promedio()
    print(f"\nEl promedio de la semana es: {round(promedio, 2)} °C")