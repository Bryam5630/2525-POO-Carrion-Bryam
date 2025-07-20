import os
import subprocess

def mostrar_codigo(ruta_script):
    # Abre el archivo y muestra el código en pantalla
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("No se encontró el archivo.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    # Ejecuta el script python en la consola, para que puedas interactuar con él
    # Se usa subprocess.call para que espere a que termines antes de volver al menú
    try:
        carpeta_script = os.path.dirname(ruta_script)
        if os.name == 'nt':  # Si estás en Windows
            subprocess.call(['py', ruta_script], cwd=carpeta_script)
        else:  # En otros sistemas (Linux, Mac)
            subprocess.call(['python3', ruta_script], cwd=carpeta_script)
    except Exception as e:
        print(f"Error al ejecutar el código: {e}")

def mostrar_menu():
    # Esta función muestra el menú principal con la unidad "Parcial 01"
    ruta_base = os.path.dirname(__file__)
    unidad = "Parcial 01"
    ruta_unidad = os.path.join(ruta_base, unidad)

    if not os.path.isdir(ruta_unidad):
        print(f"No se encontró la carpeta '{unidad}' en la raíz del proyecto.")
        return

    while True:
        print("\nMenu Principal - Dashboard")
        print(f"1 - {unidad}")
        print("0 - Salir")

        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            print("Saliendo del programa.")
            break
        elif eleccion == '1':
            mostrar_sub_menu(ruta_unidad)
        else:
            print("Opción no válida. Intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    # Lista las carpetas que son semanas (ejemplo: Semana 02, Semana 03)
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir() and f.name.startswith('Semana ')]
    # Ordena las semanas para que aparezcan en orden numérico
    sub_carpetas.sort(key=lambda x: int(x.split(' ')[1]))

    if not sub_carpetas:
        print("No se encontraron semanas en esta unidad.")
        return

    while True:
        print(f"\nSubmenú - {os.path.basename(ruta_unidad)} - Selecciona una semana")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion = input("Elige una semana o '0' para regresar: ")
        if eleccion == '0':
            break
        try:
            index = int(eleccion) - 1
            if 0 <= index < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[index]))
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Opción no válida. Intenta de nuevo.")

def mostrar_scripts(ruta_semana):
    # Muestra los scripts Python que hay dentro de la carpeta de la semana elegida
    scripts = [f.name for f in os.scandir(ruta_semana) if f.is_file() and f.name.endswith('.py')]
    if not scripts:
        print("No se encontraron scripts Python en esta semana.")
        return

    while True:
        print(f"\nScripts - {os.path.basename(ruta_semana)} - Selecciona un script para ver y ejecutar")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion = input("Elige un script, '0' para regresar o '9' para menú principal: ")
        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        try:
            index = int(eleccion) - 1
            if 0 <= index < len(scripts):
                ruta_script = os.path.join(ruta_semana, scripts[index])
                codigo = mostrar_codigo(ruta_script)
                if codigo:
                    ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                    elif ejecutar == '0':
                        print("No se ejecutó el script.")
                    else:
                        print("Opción no válida. Regresando al menú de scripts.")
                input("\nPresiona Enter para volver al menú de scripts.")
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    # Aquí empieza el programa mostrando el menú principal
    mostrar_menu()
