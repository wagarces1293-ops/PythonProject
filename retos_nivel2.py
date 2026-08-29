# Retos Nivel 2 - print(): Hacer hablar a la maquina

# Reto 1: Presentacion en 4 lineas usando \n para unir dos renglones en un solo print
print("--- RETO 1 ---")
print("Hola, mi nombre es Wilman.")
print("Tengo 20 anos.\nMi comida favorita son las hamburguesas.")
print("Mi meta es dominar la programacion en Python y crear mis propias aplicaciones.")

# Reto 2: Dibujo con asteriscos (Inicial W)
print("\n--- RETO 2 ---")
print("*       *       *")
print(" *     * *     * ")
print("  *   *   *   *  ")
print("   * *     * *   ")
print("    *       *    ")

# Reto 3: Uso de sep y end
print("\n--- RETO 3 ---")
# Fecha con barras usando sep
print("2026", "08", "07", sep="/")

# Cuenta regresiva en un solo renglon usando end
print("3...", end=" ")
print("2...", end=" ")
print("1...", end=" ")
print("Ya!")

# Reto 4 (Nivel jefe): Provocar y registrar los 3 errores tipicos
print("\n--- RETO 4 ---")
print("Simulacion de los tres errores del recuadro rojo:")

# Error 1: SyntaxError por comilla no cerrada
try:
    eval('print("Texto sin cerrar)')
except SyntaxError as e:
    print(f"Error 1 provocado: {type(e).__name__}: {e.msg}")

# Error 2: NameError por escribir Print con mayuscula
try:
    eval('Print("Hola")')
except NameError as e:
    print(f"Error 2 provocado: {type(e).__name__}: {e}")

# Error 3: SyntaxError por mezclar comilla doble y simple
try:
    eval('print("Texto mezclado\')')
except SyntaxError as e:
    print(f"Error 3 provocado: {type(e).__name__}: {e.msg}")
