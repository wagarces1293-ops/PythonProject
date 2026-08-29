# Retos Nivel 5 - Operadores: Las herramientas de calculo

# Reto 1: 7 operaciones aritmeticas con f-strings alineadas
def reto1_operaciones_aritmeticas(a=17, b=5):
    print("--- RETO 1: OPERACIONES ARITMETICAS ---")
    print(f"Operando A = {a}, Operando B = {b}\n")
    print(f"{'Operacion':<20} | {'Resultado':>12}")
    print("-" * 35)
    print(f"{'Suma (+)':<20} | {a + b:>12}")
    print(f"{'Resta (-)':<20} | {a - b:>12}")
    print(f"{'Multiplicacion (*)':<20} | {a * b:>12}")
    print(f"{'Division (/)':<20} | {a / b:>12.2f}")
    print(f"{'Division entera (//)':<20} | {a // b:>12}")
    print(f"{'Modulo/Residuo (%)':<20} | {a % b:>12}")
    print(f"{'Potencia (**)':<20} | {a ** 2:>12}")

# Reto 2: Detector de numeros
def reto2_detector_numeros(numero=18):
    print("\n--- RETO 2: DETECTOR DE NUMEROS ---")
    print(f"Analizando el numero: {numero}")
    es_par = (numero % 2 == 0)
    es_multiplo_3 = (numero % 3 == 0)
    esta_en_rango = (1 <= numero <= 100)
    
    print(f"- Es par: {es_par}")
    print(f"- Es multiplo de 3: {es_multiplo_3}")
    print(f"- Esta entre 1 y 100: {esta_en_rango}")

# Reto 3: Filtro de tienda en una sola expresion
def reto3_filtro_tienda():
    print("\n--- RETO 3: FILTRO DE TIENDA ---")
    # Criterio: precio <= 150000, talla 'M' o 'L', color 'negro' o 'azul', y que haya stock disponible
    precio = 120000
    talla = "M"
    color = "negro"
    hay_stock = True
    
    cumple_criterio = (precio <= 150000) and (talla in ["M", "L"]) and (color in ["negro", "azul"]) and hay_stock
    print(f"Producto: Precio={precio}, Talla={talla}, Color={color}, Stock={hay_stock}")
    print(f"Cumple lo que busco: {cumple_criterio}")

    # Probando con un producto que no cumple
    precio_invalido = 200000
    cumple_criterio_2 = (precio_invalido <= 150000) and (talla in ["M", "L"]) and (color in ["negro", "azul"]) and hay_stock
    print(f"Producto con sobreprecio (200000): {cumple_criterio_2}")

# Reto 4 (Nivel jefe): Precedencia y asociatividad
def reto4_precedencia():
    print("\n--- RETO 4: PREDICCION Y ASOCIATIVIDAD ---")
    r1 = 10 / 2
    r2 = 10 // 3
    r3 = 2 ** 3 ** 2
    
    print(f"10 / 2 = {r1} (Division normal siempre produce float)")
    print(f"10 // 3 = {r2} (Division entera trunca los decimales)")
    print(f"2 ** 3 ** 2 = {r3}")
    print("Explicacion del 2 ** 3 ** 2: El operador de potencia en Python es asociativo de derecha a izquierda. Se evalua primero 3 ** 2 = 9, y luego 2 ** 9 = 512, en lugar de (2 ** 3) ** 2 = 64.")

if __name__ == "__main__":
    reto1_operaciones_aritmeticas(17, 5)
    reto2_detector_numeros(18)
    reto3_filtro_tienda()
    reto4_precedencia()
