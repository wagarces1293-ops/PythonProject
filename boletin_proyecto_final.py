# ===== BOLETIN INTELIGENTE - PROYECTO FINAL =====
# Sistema de gestion y reporte de calificaciones

NOTA_MINIMA = 3.0

def pedir_nota(mensaje):
    """Pide una nota al usuario con proteccion contra ValueError."""
    while True:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            nota = float(entrada)
            if 0.0 <= nota <= 5.0:
                return nota
            else:
                print("Error: La nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("Error: Ingresa un numero valido (ejemplo: 4.5).")

def generar_boletin(nombre, n1, n2, n3, accion="repasar"):
    promedio = (n1 + n2 + n3) / 3
    mejor = max(n1, n2, n3)
    peor = min(n1, n2, n3)
    aprobo = promedio >= NOTA_MINIMA

    # Operador ternario para el estado
    estado = "APROBADO" if aprobo else "REPROBADO"

    # Evaluacion de desempeno con cadena if/elif/else ordenada
    if promedio >= 4.5:
        desempeno = "SUPERIOR"
    elif promedio >= 4.0:
        desempeno = "ALTO"
    elif promedio >= NOTA_MINIMA:
        desempeno = "BASICO"
    else:
        desempeno = "BAJO"

    print("\n" + "=" * 40)
    print("       BOLETIN DE CALIFICACIONES")
    print("=" * 40)
    print(f"Estudiante:  {nombre.title()}")
    print(f"Notas:       {n1:.1f}, {n2:.1f}, {n3:.1f}")
    print(f"Promedio:    {promedio:.2f}")
    print(f"Mejor nota:  {mejor:.1f}")
    print(f"Nota minima: {peor:.1f}")
    print(f"Estado:      {estado}")
    print(f"Desempeno:   {desempeno}")
    print("=" * 40)

    # Evaluacion con match-case y correccion del bug comunicativo
    match accion:
        case "repasar":
            print(f"Recomendacion: Enfocate en reforzar la materia donde sacaste {peor:.1f}.")
        case "mejorar":
            puntos_necesarios = 4.0 * 3
            suma_actual = n1 + n2 + n3
            falta = round(puntos_necesarios - suma_actual, 2)
            
            # Correccion del bug comunicativo (Reto 2)
            if falta <= 0:
                print(f"Felicitaciones! Ya superaste la meta de 4.0 (promedio actual: {promedio:.2f}).")
            else:
                print(f"Para alcanzar un promedio de 4.0 te faltan {falta:.2f} puntos en total.")
        case "detalle":
            print(f"Detalle academico: Suma total de puntos = {n1 + n2 + n3:.2f} / 15.00")
        case "salir":
            print("Reporte finalizado. Hasta la proxima.")
        case _:
            print("Opcion no reconocida.")

def ejecutar_interactivo():
    print("==================================")
    print("    BOLETIN DE CALIFICACIONES     ")
    print("==================================")
    nombre = input("Nombre del estudiante: ")
    n1 = pedir_nota("Nota 1 (0.0 a 5.0): ")
    n2 = pedir_nota("Nota 2 (0.0 a 5.0): ")
    n3 = pedir_nota("Nota 3 (0.0 a 5.0): ")

    print("\nQue quieres hacer? (repasar / mejorar / detalle / salir)")
    accion = input("> ").lower().strip()
    generar_boletin(nombre, n1, n2, n3, accion)

if __name__ == "__main__":
    # Demostracion automatica de los 3 casos requeridos en el Reto 1
    print("--- CASO 1: NOTAS ALTAS ---")
    generar_boletin("Sofia Ramirez", 4.5, 4.8, 4.9, "mejorar")

    print("\n--- CASO 2: NOTAS BAJAS ---")
    generar_boletin("Carlos Mendoza", 2.0, 1.8, 2.5, "mejorar")

    print("\n--- CASO 3: CASO BORDE EXACTO (3.0) ---")
    generar_boletin("Laura Gomez", 3.0, 3.0, 3.0, "repasar")
