# Retos Nivel 1 - Los Cimientos

# Reto 1: Primer programa del ejemplo 1.1
print("--- RETO 1 ---")
nota = 4.2
if nota >= 3.0:
    print("Aprobaste!")
else:
    print("A recuperar")

# Reto 2: Cambiar nota a 2.5 y probar la logica
print("\n--- RETO 2 ---")
nota = 2.5
if nota >= 3.0:
    print("Aprobaste!")
else:
    print("A recuperar")

# Nota sobre el error provocado al borrar la sangria:
# Si dejamos 'print("Aprobaste!")' sin los 4 espacios de sangria:
# Python lanza: IndentationError: expected an indented block after 'if' statement on line 2

# Reto 3: El Zen de Python
print("\n--- RETO 3 ---")
import this

# Reto 4 (Nivel jefe): Investigacion de 3 servicios y el bonus
print("\n--- RETO 4 ---")
servicios = {
    "Instagram": "Usa Python (Django) en su backend para procesar millones de peticiones por segundo.",
    "Spotify": "Usa Python para analisis de datos y los algoritmos del motor de recomendaciones.",
    "Netflix": "Usa Python para automatizacion de infraestructura, seguridad y algoritmos de optimizacion de video.",
    "Bonus (Dropbox)": "Gran parte de su aplicacion de escritorio y servidor fue escrita en Python por su facilidad de mantenimiento."
}

for servicio, uso in servicios.items():
    print(f"{servicio}: {uso}")
