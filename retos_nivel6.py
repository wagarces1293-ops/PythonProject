# Retos Nivel 6 - Decisiones: if, elif, ternario y match

# Reto 1: Clasificador de edades
def clasificar_edad(edad):
    if edad < 0:
        return "Edad no valida"
    elif edad <= 11:
        return "Nino"
    elif edad <= 17:
        return "Adolescente"
    elif edad <= 64:
        return "Adulto"
    else:
        return "Adulto mayor"

def reto1_clasificador():
    print("--- RETO 1: CLASIFICADOR DE EDADES ---")
    pruebas = [5, 11, 12, 15, 17, 18, 40, 64, 65, 80]
    for e in pruebas:
        print(f"Edad {e:>2} anos -> {clasificar_edad(e)}")

# Reto 2: Operador ternario con temperatura
def reto2_ternario():
    print("\n--- RETO 2: OPERADOR TERNARIO ---")
    temperatura = 28
    # Asignacion con ternario
    mensaje = "Hace calor" if temperatura > 25 else "Esta fresco"
    print(f"Mensaje asignado: {mensaje}")
    
    # Directamente dentro de una f-string
    temp2 = 19
    print(f"Temperatura actual: {temp2}C -> {'Hace calor' if temp2 > 25 else 'Esta fresco'}")

# Reto 3: Menu con match-case
def ejecutar_opcion_menu(opcion):
    match opcion:
        case "1":
            return "Opcion 1: Consultando tu ultima nota registrada..."
        case "2":
            return "Opcion 2: Tu promedio acumulado actual es 4.40"
        case "3":
            return "Opcion 3: Centro de ayuda. Contacta a soporte estudiantil."
        case "4":
            return "Opcion 4: Sesion finalizada. Hasta luego."
        case _:
            return "Opcion no valida. Selecciona un numero del 1 al 4."

def reto3_menu():
    print("\n--- RETO 3: MENU CON MATCH-CASE ---")
    opciones_prueba = ["1", "2", "3", "4", "9"]
    for op in opciones_prueba:
        print(f"Entrada '{op}': {ejecutar_opcion_menu(op)}")

# Reto 4 (Nivel jefe): Demostracion del bug de orden en elif y su correccion
def calificador_con_bug(nota):
    # BUG: El orden esta invertido, evaluando primero >= 3.0
    if nota >= 3.0:
        return "Aprobaste"
    elif nota >= 4.0:
        return "Muy bien"
    elif nota >= 4.5:
        return "Excelente"
    else:
        return "A recuperar"

def calificador_corregido(nota):
    # CORREGIDO: De la condicion mas restrictiva a la mas general
    if nota >= 4.5:
        return "Excelente"
    elif nota >= 4.0:
        return "Muy bien"
    elif nota >= 3.0:
        return "Aprobaste"
    else:
        return "A recuperar"

def reto4_demostracion_bug():
    print("\n--- RETO 4: BUG DE ORDEN EN ELIF ---")
    nota_test = 5.0
    print(f"Evaluando nota {nota_test}:")
    print(f"- Resultado con bug: {calificador_con_bug(nota_test)}")
    print(f"- Resultado corregido: {calificador_corregido(nota_test)}")
    print("Explicacion: En una cadena if/elif, Python evalua de arriba abajo y se detiene en la primera condicion que sea True. Por eso las condiciones mas exigentes o especificas deben evaluarse primero.")

if __name__ == "__main__":
    reto1_clasificador()
    reto2_ternario()
    reto3_menu()
    reto4_demostracion_bug()
