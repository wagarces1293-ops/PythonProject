# Retos Nivel 3 - Variables y Tipos de Datos

# Reto 1: Ficha de personaje con 6 variables y sus tipos
print("--- RETO 1 ---")
nombre = "Wilman"                  # str
edad = 20                          # int
estatura = 1.75                    # float
tiene_mascota = True               # bool
videojuego_favorito = "Minecraft"  # str
horas_de_sueno = 7.5               # float

print("Valores:")
print(nombre, edad, estatura, tiene_mascota, videojuego_favorito, horas_de_sueno)

print("\nTipos de datos:")
print("nombre:", type(nombre))
print("edad:", type(edad))
print("estatura:", type(estatura))
print("tiene_mascota:", type(tiene_mascota))
print("videojuego_favorito:", type(videojuego_favorito))
print("horas_de_sueno:", type(horas_de_sueno))

# Reto 2: Tres nombres de variable malos vs buenos
print("\n--- RETO 2 ---")
ejemplos_variables = [
    ("x = 20", "edad_usuario = 20", "La variable 'x' no describe que guarda; 'edad_usuario' deja claro el dato."),
    ("nom = 'Wilman'", "nombre_completo = 'Wilman'", "'nom' es una abreviatura ambigua; 'nombre_completo' es explicita."),
    ("tot = 15000.5", "total_factura = 15000.5", "'tot' no dice total de que; 'total_factura' le da contexto exacto.")
]

for malo, bueno, explicacion in ejemplos_variables:
    print(f"Malo: {malo} | Bueno: {bueno}")
    print(f"Explicacion: {explicacion}\n")

# Reto 3: Provocar TypeError y solucionarlo de dos formas
print("--- RETO 3 ---")
edad = 20
texto = "anos"

# Provocamos el TypeError
try:
    resultado = edad + texto
except TypeError as e:
    print(f"TypeError provocado con exito: {e}")

# Solucion 1: Pasando argumentos separados por comas a print()
print("Solucion 1 (con comas): Tengo", edad, "anos")

# Solucion 2: Convirtiendo el int a str con str() y concatenando
print("Solucion 2 (con str()): Tengo " + str(edad) + " anos")

# Reto 4 (Nivel jefe): Precision de flotantes y round()
print("\n--- RETO 4 ---")
suma_flotantes = 0.1 + 0.2
print(f"print(0.1 + 0.2) = {suma_flotantes}")

suma_redondeada = round(0.1 + 0.2, 2)
print(f"print(round(0.1 + 0.2, 2)) = {suma_redondeada}")
print("Explicacion: round() limita la cantidad de decimales en la salida visible al redondear al numero de posiciones indicado, ocultando el residuo binario sin cambiar la forma en que la maquina almacena internamente los numeros flotantes.")
