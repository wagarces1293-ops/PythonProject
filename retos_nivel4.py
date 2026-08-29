# Retos Nivel 4 - input(), Conversion y f-strings

# Reto 1: Calculadora de promedio de 3 notas
def reto1_calculadora():
    print("--- RETO 1: CALCULADORA DE PROMEDIO ---")
    n1 = float(input("Ingresa la primera nota: "))
    n2 = float(input("Ingresa la segunda nota: "))
    n3 = float(input("Ingresa la tercera nota: "))
    
    promedio = (n1 + n2 + n3) / 3
    print(f"El promedio de las tres notas es: {promedio:.2f}")

# Reto 2: Ficha de perfil interactiva con calculo en llaves
def reto2_ficha_perfil():
    print("\n--- RETO 2: FICHA DE PERFIL ---")
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    ciudad = input("Ingresa tu ciudad: ")
    
    anio_actual = 2026
    print(f"Hola, soy {nombre}, vivo en {ciudad}, tengo {edad} anos y cumplire 30 en el anio {anio_actual + (30 - edad)}.")

# Reto 3: Demostracion de errores con float()
def reto3_explicacion_errores():
    print("\n--- RETO 3: DEMOSTRACION DE ERRORES AL CONVERTIR ---")
    # Caso 1: entrada con texto 'hola'
    try:
        float("hola")
    except ValueError as e:
        print(f"Caso 'hola': ValueError: {e}")
        print("Explicacion: 'hola' contiene caracteres alfabeticos que no representan ninguna cifra numerica.")
    
    # Caso 2: entrada con coma '4,5'
    try:
        float("4,5")
    except ValueError as e:
        print(f"\nCaso '4,5': ValueError: {e}")
        print("Explicacion: Python utiliza exclusivamente el punto '.' como separador decimal. La coma ',' genera error de formato.")

# Reto 4 (Nivel jefe): Tabla de 3 estudiantes con alineacion (< y >)
def reto4_tabla_estudiantes():
    print("\n--- RETO 4: TABLA DE ESTUDIANTES ALINEADA ---")
    estudiantes = [
        ("Ana Perez", 4.75),
        ("Sebastian Gomez", 3.20),
        ("Wilman Diaz", 4.50)
    ]
    
    print(f"+{'-'*20}+{'-'*10}+")
    print(f"|{'Estudiante':<20}|{'Promedio':>10}|")
    print(f"+{'-'*20}+{'-'*10}+")
    for nombre, prom in estudiantes:
        print(f"|{nombre:<20}|{prom:>10.2f}|")
    print(f"+{'-'*20}+{'-'*10}+")

if __name__ == "__main__":
    reto3_explicacion_errores()
    reto4_tabla_estudiantes()
    print("\nEjecucion de retos interactivos (1 y 2):")
    # Para pruebas directas
    # reto1_calculadora()
    # reto2_ficha_perfil()
