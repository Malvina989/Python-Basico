secret_number = 777
#impresion multilinea usando tiple comilla("""....""")
print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
number = int(input("Arriesgue número"))
while number != secret_number:
    print("Ja,ja Estás en mi bucle")
    number = int(input("Arriesgue número"))
if number == secret_number:
    print(secret_number)
    print("¡Bien hecho!")
    
