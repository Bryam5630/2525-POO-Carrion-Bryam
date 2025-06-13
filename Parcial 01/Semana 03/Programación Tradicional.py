lunes= float(input("Ingrese la temperatura en grados °C de lunes: "))
Martes= float(input("Ingrese la temperatura en grados °C de martes: "))
Miercoles= float(input("Ingrese la temperatura en grados °C de miercoles: "))
Jueves= float(input("Ingrese la temperatura en grados °C de jueves : "))
Viernes= float(input("Ingrese la temperatura en grados °C de viernes: "))
Sabado= float(input("Ingrese la temperatura en grados °C de sabado: "))
Domingo= float(input("Ingrese la temperatura en grados °C de domingo: "))

def promedio_semana_temperatura():
    promedio=lunes+Martes+Miercoles+Jueves+Viernes+Sabado+Domingo

    promedio_semanal= promedio/7

    return promedio_semanal


temperaturasemana= promedio_semana_temperatura()

print("El promedio de la temperatura de la semana es",round (temperaturasemana,2)," °C")