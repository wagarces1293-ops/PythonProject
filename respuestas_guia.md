# Respuestas y Desarrollo de Retos: Python Desde Cero (Niveles 1 al 7)

Este documento contiene la solucion a todas las preguntas teoricas, checkpoints, analisis y registro de experimentos de la guia, desarrollado paso a paso con mis propias palabras, de forma directa, organizada y sin complicaciones.

---

## Nivel 1: Los Cimientos

### Reto de Observador (Mision: Primer Contacto)

1. **Entorno y primer programa:**
   Cree el archivo `retos_nivel1.py` y ejecute el codigo del ejemplo 1.1:
   ```python
   nota = 4.2
   if nota >= 3.0:
       print("Aprobaste!")
   else:
       print("A recuperar")
   ```
   Al correrlo con `nota = 4.2`, la consola mostro: `Aprobaste!`.

2. **Cambio de valor y prueba de error de sangria:**
   - Cambie la nota a `2.5` y el resultado fue `A recuperar`.
   - Luego le borre los 4 espacios de sangria a la linea del `print` dentro del `if`. Python no dejo arrancar el programa y arrojo este error:
     ```text
     IndentationError: expected an indented block after 'if' statement on line 2
     ```
   - Esto pasa porque en Python los bloques no se cierran con llaves sino con espacios. Si no hay sangria, Python no sabe que esa instruccion depende del `if`.

3. **El Zen de Python (`import this`):**
   - Ejecute `import this` en la consola interactiva.
   - Principio elegido: *"Simple is better than complex"* (Lo simple es mejor que lo complejo).
   - Lo que significa para mi: Si puedo resolver un problema con tres lineas faciles de entender, no tiene sentido armar un codigo enredado de diez lineas solo para que parezca avanzado. El codigo claro ahorra dolores de cabeza.

4. **Investigacion de servicios famosos que usan Python (Nivel Jefe):**
   - **Instagram:** Usa Python y el framework Django en su backend para atender millones de solicitudes de fotos, comentarios y perfiles cada segundo.
   - **Spotify:** Lo usa para analisis de datos pesados y para alimentar los algoritmos que deciden que canciones recomendarte en tus listas diarias.
   - **Netflix:** Lo utiliza para gestionar y automatizar su infraestructura en la nube, optimizar la compresion de video y hacer pruebas de seguridad.
   - **Bonus (Dropbox):** Me sorprendio saber que casi todo el cliente de escritorio y los servidores originales de Dropbox se programaron en Python, al punto de que contrataron al mismo creador de Python (Guido van Rossum) durante anos para optimizar su sistema.

---

### Checkpoint - Nivel 1

1. **Que significa que Python sea "interpretado" y que ventaja tiene al aprender?**
   Significa que no hay que pasar el codigo por un proceso previo de compilacion para generar un archivo binario ejecutable; un programa llamado interprete va leyendo y ejecutando linea por linea en tiempo real. La ventaja al aprender es inmediata: escribes una linea, la pruebas al instante, ves el error de inmediato y puedes corregir sin perder tiempo esperando a compilar.

2. **Por que Python domina en inteligencia artificial si por dentro las librerias usan C++?**
   Porque combina lo mejor de dos mundos: la velocidad extrema de C++ por dentro (que hace los calculos pesados de matrices y tensores) con la sintaxis sencilla y legible de Python por fuera. Python funciona como el control remoto o el volante: los humanos le damos las ordenes comodamente y C++ hace el trabajo pesado en el motor.

3. **Que son la indentacion y las librerias, y por que son tan importantes?**
   - La **indentacion** es la sangria (espacios al inicio de la linea) que delimita que codigo pertenece a que bloque (como un `if` o una funcion). Es obligatoria y garantiza que todo codigo en Python sea ordenado y facil de leer.
   - Las **librerias** son paquetes de codigo ya hechos y probados por otras personas que podemos reutilizar gratis. Son clave porque nos evitan tener que inventar la rueda desde cero cada vez que queremos hacer una grafica, una pagina o un modelo de IA.

---

## Nivel 2: print() - Hacer Hablar a la Maquina

### Reto de Observador (Mision: La Consola Habla)

1. **Presentacion en 4 lineas con `\n`:**
   ```python
   print("Hola, mi nombre es Wilman.")
   print("Tengo 20 anos.\nMi comida favorita son las hamburguesas.")
   print("Mi meta es dominar la programacion en Python y crear mis propias aplicaciones.")
   ```
   Salida:
   ```text
   Hola, mi nombre es Wilman.
   Tengo 20 anos.
   Mi comida favorita son las hamburguesas.
   Mi meta es dominar la programacion en Python y crear mis propias aplicaciones.
   ```

2. **Dibujo con asteriscos (Inicial W):**
   ```python
   print("*       *       *")
   print(" *     * *     * ")
   print("  *   *   *   *  ")
   print("   * *     * *   ")
   print("    *       *    ")
   ```
   Aqui se nota que cada espacio en blanco dentro del texto cuenta para que el dibujo no quede chueco.

3. **Uso de `sep` y `end`:**
   ```python
   # Fecha con barras usando sep
   print("2026", "08", "07", sep="/")

   # Cuenta regresiva en un solo renglon usando end
   print("3...", end=" ")
   print("2...", end=" ")
   print("1...", end=" ")
   print("Ya!")
   ```
   Salida:
   ```text
   2026/08/07
   3... 2... 1... Ya!
   ```

4. **Diccionario de errores provocados a proposito (Nivel Jefe):**
   - **Error 1 (Olvidar cerrar comillas):**
     - Codigo: `print("Texto sin cerrar)`
     - Mensaje: `SyntaxError: unterminated string literal (detected at line 1)`
     - Causa: Python llego al final de la linea esperando la comilla de cierre y no la encontro.
   - **Error 2 (Escribir `Print` con mayuscula inicial):**
     - Codigo: `Print("Hola")`
     - Mensaje: `NameError: name 'Print' is not defined`
     - Causa: Python distingue entre mayusculas y minusculas; reconoce `print` pero `Print` no existe en su memoria.
   - **Error 3 (Mezclar comillas dobles y simples):**
     - Codigo: `print("Texto mezclado')`
     - Mensaje: `SyntaxError: unterminated string literal (detected at line 1)`
     - Causa: Si abres con comilla doble `"`, debes cerrar con comilla doble `"`. La comilla simple `'` adentro fue tomada como parte del texto.

---

### Checkpoint - Nivel 2

1. **Que diferencia hay entre la funcion `print`, sus parentesis y su argumento?**
   - `print`: Es el nombre de la funcion (la herramienta que sabe como mostrar cosas en la terminal).
   - Los parentesis `()`: Son los activadores que le indican a Python que ejecute la funcion en ese instante y delimitan lo que le estamos entregando.
   - El argumento: Es la informacion que metemos dentro de los parentesis (por ejemplo `"Hola"` o una variable) para que la funcion trabaje con ella.

2. **Para que sirven `sep` y `end`? Da un ejemplo de cada uno.**
   - `sep`: Define que caracter se colocara entre los multiples argumentos que le pasemos a `print()`. Por defecto es un espacio.
     Ejemplo: `print("A", "B", "C", sep="-")` produce `A-B-C`.
   - `end`: Define que se coloca al final de la impresion. Por defecto es un salto de linea `\n`.
     Ejemplo: `print("Cargando...", end="")` hace que el siguiente `print` continue en la misma linea.

3. **Por que los comentarios deben explicar el "por que" y no el "que"?**
   Porque lo que hace el codigo ya se puede leer directamente en la sintaxis. El comentario util es el que explica el motivo o la decision de negocio detras (por ejemplo: `# Se suma 1 porque el indice de la base de datos empieza en 1`). Eso es lo que uno olvida con los meses.

---

## Nivel 3: Variables y Tipos de Datos

### Reto de Observador (Mision: Tu Ficha de Personaje)

1. **6 variables con los 4 tipos de datos y su `type()`:**
   ```python
   nombre = "Wilman"                  # str
   edad = 20                          # int
   estatura = 1.75                    # float
   tiene_mascota = True               # bool
   videojuego_favorito = "Minecraft"  # str
   horas_de_sueno = 7.5               # float

   print(nombre, edad, estatura, tiene_mascota, videojuego_favorito, horas_de_sueno)
   print(type(nombre), type(edad), type(estatura), type(tiene_mascota), type(videojuego_favorito), type(horas_de_sueno))
   ```
   Salida de tipos:
   ```text
   <class 'str'> <class 'int'> <class 'float'> <class 'bool'> <class 'str'> <class 'float'>
   ```

2. **Nombres de variables malos vs buenos:**
   - Malo: `x = 20` | Bueno: `edad_usuario = 20`
     *Explicacion:* `x` no le dice nada a quien lea el codigo; `edad_usuario` explica exactamente que dato guarda la memoria.
   - Malo: `nom = "Wilman"` | Bueno: `nombre_completo = "Wilman"`
     *Explicacion:* Las abreviaturas generan confusiones y dudas; el nombre completo en `snake_case` es 100% claro.
   - Malo: `tot = 15000.5` | Bueno: `total_factura = 15000.5`
     *Explicacion:* `tot` podria ser total de alumnos, total de puntos o total de dinero; `total_factura` da el contexto correcto.

3. **Provocar el `TypeError` de 3.4 y solucionarlo:**
   - Codigo que falla:
     ```python
     edad = 20
     texto = "anos"
     print(edad + texto)
     ```
   - Error obtenido: `TypeError: unsupported operand type(s) for +: 'int' and 'str'`
   - Por que se queja Python: Porque el signo `+` sirve para sumar numeros o para concatenar textos, pero Python tiene tipado fuerte y no asume si queremos sumar o pegar texto; prefiere detenerse a avisarnos antes de adivinar mal.
   - **Solucion 1 (con comas):** `print("Tengo", edad, "anos")`
   - **Solucion 2 (con `str()`):** `print("Tengo " + str(edad) + " anos")`

4. **Precision con flotantes y funcion `round()` (Nivel Jefe):**
   - Al ejecutar `print(0.1 + 0.2)` el resultado es `0.30000000000000004`.
   - Al ejecutar `print(round(0.1 + 0.2, 2))` el resultado es `0.3`.
   - **Explicacion:** Las computadoras representan los numeros internamente en binario (base 2). Fracciones como `0.1` o `0.2` son numeros periodicos infinitos en binario, similar a lo que pasa con `1/3` en base decimal (`0.3333...`). Al sumar, queda un residuo microscopico. La funcion `round(valor, 2)` redondea la presentacion visual a 2 decimales, ocultando el residuo ante el usuario, aunque internamente la naturaleza binaria de los flotantes siga siendo la misma.

---

### Checkpoint - Nivel 3

1. **Que hace exactamente el signo `=` y por que es incorrecto leerlo como "igual"?**
   El signo `=` es el operador de asignacion. No evalua igualdad matematica; lo que hace es tomar el valor o expresion de la derecha y guardarlo en la variable ubicada a la izquierda. Si se lee como "igual", uno se confunde al ver cosas como `x = x + 1`. Debe leerse como "asigna a" o "guarda en".

2. **Nombra los 4 tipos basicos con un ejemplo de cada uno y una trampa asociada:**
   - **`int`:** Ejemplo `25`. *Trampa:* Ponerle puntos o comas de miles (ej. `1.000` lo convierte en float `1.0` y `1,000` crea una tupla).
   - **`float`:** Ejemplo `3.14`. *Trampa:* Usar coma decimal en lugar de punto (ej. `3,14`), lo cual no es un numero valido.
   - **`str`:** Ejemplo `"Hola"`. *Trampa:* Poner un numero entre comillas como `"100"`; no se podra sumar aritmeticamente sino que se concatenara.
   - **`bool`:** Ejemplo `True` o `False`. *Trampa:* Escribirlos en minuscula (`true` o `false`), lo cual genera un `NameError`.

3. **Que significa que Python sea de tipado dinamico pero fuerte?**
   - **Dinamico:** No tenemos que declarar el tipo de dato al crear la variable; Python lo deduce solo y una misma variable puede cambiar de tipo mas adelante si le asignamos otro valor.
   - **Fuerte:** Python no convierte tipos de datos automaticamente a lo loco en operaciones no permitidas (por ejemplo, no te deja sumar un texto con un numero directamente), obligandote a ser explicito.

---

## Nivel 4: input(), Conversion y f-strings

### Reto de Observador (Mision: Programa Conversador)

1. **Calculadora de promedio con tres notas:**
   ```python
   n1 = float(input("Ingresa la primera nota: "))
   n2 = float(input("Ingresa la segunda nota: "))
   n3 = float(input("Ingresa la tercera nota: "))

   promedio = (n1 + n2 + n3) / 3
   print(f"El promedio final es: {promedio:.2f}")
   ```

2. **Ficha de perfil con calculo dentro de llaves:**
   ```python
   nombre = input("Nombre: ")
   edad = int(input("Edad: "))
   ciudad = input("Ciudad: ")

   print(f"Hola {nombre} de {ciudad}, actualmente tienes {edad} anos y en el 2036 tendras {edad + 10} anos.")
   ```

3. **Prueba de errores al convertir con `float()`:**
   - **Caso "hola":**
     - Error: `ValueError: could not convert string to float: 'hola'`
     - Explicacion: `float()` requiere un texto con caracteres numericos. "hola" no tiene representacion numerica.
   - **Caso "4,5":**
     - Error: `ValueError: could not convert string to float: '4,5'`
     - Explicacion: Python solo reconoce el punto `.` como separador decimal en su sintaxis base. La coma es un caracter invalido para convertir a float.

4. **Tabla de 3 estudiantes alineada con `<` y `>` (Nivel Jefe):**
   ```python
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
   ```
   Salida en consola:
   ```text
   +--------------------+----------+
   |Estudiante          |  Promedio|
   +--------------------+----------+
   |Ana Perez           |      4.75|
   |Sebastian Gomez     |      3.20|
   |Wilman Diaz         |      4.50|
   +--------------------+----------+
   ```

---

### Checkpoint - Nivel 4

1. **Por que `int(input())` es tan comun? Que hace cada funcion y en que orden se ejecutan?**
   Es comun porque `input()` siempre captura la entrada como texto (`str`), asi que si queremos operar matematicamente con un numero entero debemos transformarlo.
   - Se ejecuta de adentro hacia afuera:
     1. Primero `input()` le pide el dato al usuario y devuelve un string (por ejemplo `"18"`).
     2. Luego `int()` toma ese string y lo convierte en el numero entero `18`.

2. **Explica por que `"5" + "3"` da `"53"` y como se arregla:**
   Da `"53"` porque ambos valores son cadenas de texto (`str`). Con cadenas, el operador `+` realiza una concatenacion (las une o pega una tras otra).
   Se arregla convirtiendo los textos a enteros o flotantes antes de operar: `int("5") + int("3")`, lo que da `8`.

3. **Escribe de memoria una f-string que muestre un promedio con dos decimales:**
   ```python
   print(f"Tu promedio final es {promedio:.2f}")
   ```

---

## Nivel 5: Operadores - Las Herramientas de Calculo

### Reto de Observador (Mision: La Calculadora Total)

1. **Las 7 operaciones aritmeticas con 17 y 5:**
   ```python
   a = 17
   b = 5
   print(f"{'Suma (+)':<20} | {a + b:>10}")        # 22
   print(f"{'Resta (-)':<20} | {a - b:>10}")       # 12
   print(f"{'Multiplicacion (*)':<20} | {a * b:>10}") # 85
   print(f"{'Division (/)':<20} | {a / b:>10.2f}") # 3.40
   print(f"{'Division entera (//)':<20} | {a // b:>10}") # 3
   print(f"{'Residuo (%)':<20} | {a % b:>10}")     # 2
   print(f"{'Potencia (**)':<20} | {a ** 2:>10}")   # 289
   ```

2. **Detector de numeros:**
   ```python
   numero = 18
   print(f"Es par: {numero % 2 == 0}")
   print(f"Es multiplo de 3: {numero % 3 == 0}")
   print(f"Esta entre 1 y 100: {1 <= numero <= 100}")
   ```
   Salida para 18:
   - Es par: `True`
   - Es multiplo de 3: `True`
   - Esta entre 1 y 100: `True`

3. **Filtro de tienda en una sola expresion logica:**
   ```python
   precio = 120000
   talla = "M"
   color = "negro"
   hay_stock = True

   cumple = (precio <= 150000) and (talla == "M" or talla == "L") and (color in ["negro", "blanco"]) and hay_stock
   print(f"El producto cumple las condiciones: {cumple}") # Da True
   ```

4. **Prediccion y asociatividad (Nivel Jefe):**
   - Prediccion de las lineas:
     - `10 / 2` -> `5.0` (la division normal siempre entrega un float).
     - `10 // 3` -> `3` (la division entera descarta la parte decimal).
     - `2 ** 3 ** 2` -> `512`.
   - **Explicacion:** A diferencia de la suma o resta que se evaluan de izquierda a derecha, el operador de potencia `**` en Python tiene **asociatividad por la derecha**. Esto significa que primero calcula `3 ** 2 = 9`, y luego calcula `2 ** 9 = 512`. Si fuera de izquierda a derecha daria `(2 ** 3) ** 2 = 8 ** 2 = 64`.

---

### Checkpoint - Nivel 5

1. **Explica la diferencia entre `/`, `//` y `%`, con un ejemplo de cada uno:**
   - `/` (Division real): Realiza la division exacta y siempre devuelve un `float`. Ejemplo: `7 / 2 = 3.5`.
   - `//` (Division entera): Divide y se queda solo con el cociente entero, descartando los decimales. Ejemplo: `7 // 2 = 3`.
   - `%` (Modulo o residuo): Devuelve lo que sobra de la division entera. Ejemplo: `7 % 2 = 1` (porque 2 cabe 3 veces en 7 y sobra 1).

2. **Cual es la diferencia entre `=` y `==`? Por que es el error mas comun?**
   - `=` es de asignacion: mete un dato dentro de una variable (`x = 10`).
   - `==` es de comparacion: pregunta si dos valores son equivalentes y devuelve `True` o `False` (`x == 10`).
   - Es el error mas comun porque en el colegio nos ensenan a usar un solo `=` para decir que dos cosas son iguales, asi que la mente tiende a escribirlo por reflejo dentro de los `if`.

3. **Traduce a espanol: `edad >= 18 and (tiene_entrada or es_socio)`:**
   "La persona tiene 18 anos o mas, y ademas cuenta con una entrada o es socia del lugar". Debe ser mayor de edad obligatoriamente y cumplir al menos una de las dos condiciones de acceso.

---

## Nivel 6: Decisiones - if, elif, ternario y match

### Reto de Observador (Mision: El Programa que Elige)

1. **Clasificador de edades con bordes:**
   ```python
   def clasificar_edad(edad):
       if edad < 0:
           return "Invalido"
       elif edad <= 11:
           return "Nino"
       elif edad <= 17:
           return "Adolescente"
       elif edad <= 64:
           return "Adulto"
       else:
           return "Adulto mayor"
   ```
   Probado con:
   - 11 -> `Nino`
   - 12 -> `Adolescente`
   - 17 -> `Adolescente`
   - 18 -> `Adulto`
   - 65 -> `Adulto mayor`

2. **Operador ternario con temperatura:**
   ```python
   temperatura = 28
   mensaje = "Hace calor" if temperatura > 25 else "Esta fresco"
   print(mensaje)

   # Dentro de una f-string
   print(f"El clima marca que {'Hace calor' if temperatura > 25 else 'Esta fresco'}")
   ```

3. **Menu con `match-case`:**
   ```python
   opcion = input("Elige (1: Consultar nota, 2: Ver promedio, 3: Ayuda, 4: Salir): ")
   match opcion:
       case "1":
           print("Tu ultima nota registrada es 4.5")
       case "2":
           print("Tu promedio general es 4.2")
       case "3":
           print("Manual de usuario y contacto de soporte")
       case "4":
           print("Sesion cerrada correctamente")
       case _:
           print("Opcion invalida")
   ```

4. **Prueba de escritorio del bug de orden y correccion (Nivel Jefe):**
   - **Codigo con bug:**
     ```python
     if nota >= 3.0:
         print("Aprobaste")
     elif nota >= 4.0:
         print("Muy bien")
     elif nota >= 4.5:
         print("Excelente")
     ```
   - **Prueba de escritorio con `nota = 5.0`:**
     1. Python revisa `5.0 >= 3.0`.
     2. Como es `True`, entra e imprime `"Aprobaste"`.
     3. Como ya encontro una condicion verdadera, se salta todos los demas `elif`.
     4. Resultado: Un estudiante con 5.0 recibe "Aprobaste" en lugar de "Excelente".
   - **Codigo corregido:**
     ```python
     if nota >= 4.5:
         print("Excelente")
     elif nota >= 4.0:
         print("Muy bien")
     elif nota >= 3.0:
         print("Aprobaste")
     else:
         print("A recuperar")
     ```
   - **Regla violada:** Las estructuras `if/elif` evaluan de arriba a abajo y se detienen en la primera coincidencia; por eso las condiciones mas restrictivas o exigentes siempre deben ir primero.

---

### Checkpoint - Nivel 6

1. **Por que la indentacion en Python no es estetica? Da un ejemplo de como cambia el significado:**
   La indentacion le indica a Python que lineas de codigo estan subordinadas a un bloque condicional o bucle.
   Ejemplo:
   ```python
   # Caso A: El print de despedida solo sale si eres mayor
   if edad >= 18:
       print("Bienvenido")
       print("Adios")

   # Caso B: El print de despedida sale SIEMPRE
   if edad >= 18:
       print("Bienvenido")
   print("Adios")
   ```

2. **Por que el orden de los `elif` es tan importante? Explica con la cadena de notas:**
   Porque Python evalua en cascada y se detiene en el primer `True`. Si pones una condicion muy general al inicio (como `nota >= 3.0`), se tragara todas las notas altas (`4.5`, `5.0`) y nunca dejara que se evaluen los rangos superiores.

3. **Cuando conviene `match` en vez de una cadena de `elif`, y cuando no?**
   - **Conviene `match`:** Cuando comparamos una sola variable contra valores exactos y discretos conocidos (como opciones de menu `"1"`, `"2"`, `"3"`, o comandos fijos).
   - **No conviene `match` (usar `if/elif`):** Cuando necesitamos evaluar rangos continuos con operadores relacionales (como `nota >= 4.0`) o condiciones logicas combinadas con `and`/`or`.

---

## Nivel 7: Errores, Depuracion y Proyecto Final

### Reto de Observador (Mision: Haz Tuyo el Proyecto)

1. **Ejecucion del Boletin Inteligente con tres juegos de datos:**
   - **Caso 1 (Notas altas: 4.5, 4.8, 4.9):**
     - Promedio: `4.73`
     - Estado: `APROBADO`
     - Desempeno: `SUPERIOR`
   - **Caso 2 (Notas bajas: 2.0, 1.8, 2.5):**
     - Promedio: `2.10`
     - Estado: `REPROBADO`
     - Desempeno: `BAJO`
   - **Caso 3 (Caso borde exacto: 3.0, 3.0, 3.0):**
     - Promedio: `3.00`
     - Estado: `APROBADO`
     - Desempeno: `BASICO`

2. **Arreglo del bug comunicativo (puntos negativos para el 4.0):**
   - En el codigo original, al pedir la opcion "mejorar" con notas altas arrojaba: `Para llegar a 4.0 te faltan -1.2 puntos`.
   - Se soluciono condicionando el mensaje:
     ```python
     falta = round((4.0 * 3) - (n1 + n2 + n3), 2)
     if falta <= 0:
         print(f"Felicitaciones! Ya superaste la meta de 4.0 (promedio actual: {promedio:.2f}).")
     else:
         print(f"Para alcanzar un promedio de 4.0 te faltan {falta:.2f} puntos en total.")
     ```

3. **Mejoras propias implementadas en `boletin_proyecto_final.py`:**
   - **Mejora 1 (Proteccion contra ValueError):** Cree la funcion `pedir_nota()` con un bloque `try/except` y un bucle de validacion. Si el usuario escribe letras, comas o notas fuera del rango `0.0 a 5.0`, el programa no explota; le muestra un mensaje claro y le vuelve a pedir el dato.
   - **Mejora 2 (Calculo de nota minima y nueva opcion en el menu):** Agregue el calculo de la nota mas baja (`min(n1, n2, n3)`) y un nuevo caso `"detalle"` en el `match-case` que muestra el total acumulado de puntos sobre 15.00.

4. **Manual de Depuracion - Los 3 tipos de error provocados a proposito (Nivel Jefe):**

   - **Error 1: Error de Sintaxis (SyntaxError)**
     - *Que hice:* Borre los dos puntos al final de la linea del `if` (`if promedio >= 4.5`).
     - *Mensaje en consola:* `SyntaxError: expected ':'`
     - *Como lo detecte:* Python se nego a iniciar y marco con una flecha el final de la linea del `if`.
     - *Solucion:* Agregue los dos puntos `:` al final de la sentencia.

   - **Error 2: Error en Tiempo de Ejecucion (TypeError / ValueError)**
     - *Que hice:* Intente calcular `falta = (4.0 * 3) - input("Nota: ")` sin convertir el input a float.
     - *Mensaje en consola:* `TypeError: unsupported operand type(s) for -: 'float' and 'str'`
     - *Como lo detecte:* El programa arranco, pero en cuanto intente hacer la operacion matematica se detuvo y lanzo el traceback en la linea especifica.
     - *Solucion:* Envolvi la lectura con la conversion `float(input(...))`.

   - **Error 3: Error Logico (Sin mensaje de error)**
     - *Que hice:* Escribi la formula del promedio sin parentesis: `promedio = n1 + n2 + n3 / 3`.
     - *Que paso:* Con notas `4.0, 4.0, 4.0` el promedio dio `9.33` en lugar de `4.0`. No hubo pantalla roja ni advertencias.
     - *Como lo detecte:* Haciendo una prueba de escritorio y poniendo un `print` espia para comparar el resultado esperado con el real.
     - *Solucion:* Agregue parentesis para forzar a sumar primero: `promedio = (n1 + n2 + n3) / 3`.

---

### Checkpoint - Nivel Final

1. **Cual de los 3 tipos de error es mas peligroso y por que Python no puede ayudarte con el?**
   El **error logico** es el mas peligroso. En los errores de sintaxis y de ejecucion Python nos frena y nos dice en que linea esta la falla. En cambio, en un error logico la sintaxis es valida y el programa corre sin quejarse, pero produce informacion falsa o danina. Python no puede saber que queriamos calcular nosotros; la unica defensa es el razonamiento humano y las pruebas de escritorio.

2. **Explica como se lee un traceback y que linea contiene la informacion mas util?**
   Se lee **de abajo hacia arriba**:
   - La **ultima linea** es la mas util e importante: te da el nombre exacto de la excepcion (como `ValueError`, `IndexError` o `TypeError`) y una breve explicacion del motivo.
   - Las lineas intermedias te muestran el archivo y el numero de linea exacto donde ocurrio el problema para que vayas directo a inspeccionar el codigo.

3. **En el bug del promedio, que regla del Nivel 5 se habia violado y como se arregla?**
   Se habia violado la regla de **precedencia de operadores**. La division `/` tiene mayor jerarquia que la suma `+`, por lo que Python divide primero la ultima nota entre 3 y luego le suma las dos primeras.
   Se arregla usando parentesis obligatorios para darle maxima prioridad a la suma: `(n1 + n2 + n3) / 3`.
