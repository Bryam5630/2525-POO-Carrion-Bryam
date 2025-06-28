# Porgama para convertir centímetros a metros y metros a kilómetros
# Utiliza tipos string, float y boolean, con validación de entrada y resultados formateados

def centimetros_a_metros(centimetros: float) -> float:
    "Convierte centímetros a metros."
    return centimetros / 100

def metros_a_kilometros(metros: float) -> float:
    "Convierte metros a kilómetros."
    return metros / 1000

print("Un gusto caballero usted sen encuentra en un convertidor de unidades xd.")

# Se le pide al usuario la cantidad en centímetros
entrada_centimetros = input("Ingresa la cantidad en centímetros que quieres convertir a metros por favor: ").strip()

#Aqui se ve si la enrtada ingresada es correcta
es_valido = False

try:
    valor_centimetros = float(entrada_centimetros)
    if valor_centimetros >= 0:
        es_valido = True
    else:
        print("El valor debe ser un número positivo.")
except ValueError:
    print("Entrada inválida. Por favor ingresa un número válido.")

if es_valido:
    metros = centimetros_a_metros(valor_centimetros)
    kilometros = metros_a_kilometros(metros)

    print(f"{valor_centimetros} centímetros equivalen a {metros:.2f} metros.")
    print(f"{metros:.2f} metros equivalen a {kilometros:.5f} kilómetros.")
else:
    print("Debe ser un numero para que funcione el programa.")
