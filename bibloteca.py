#1
#Escribe un programa que reciba una contraseña del usuario y valide si es segura o no.
#Tiene al menos 10 caracteres.
#Contiene al menos una letra mayúscula, una minúscula, un número y un carácter especial.
#Si la contraseña no es segura, el programa debe indicar cuál o cuáles criterios no cumple.
import re
def validar_contrasena(contrasena):
    criterios_no_cumplidos = []
    if len(contrasena) < 10:
        criterios_no_cumplidos.append("La contraseña debe tener al menos 10 caracteres.")
    if not re.search(r'[A-Z]', contrasena):
        criterios_no_cumplidos.append("La contraseña debe contener al menos una letra mayúscula.")
    if not re.search(r'[a-z]', contrasena):
        criterios_no_cumplidos.append("La contraseña debe contener al menos una letra minúscula.")
    if not re.search(r'[0-9]', contrasena):
        criterios_no_cumplidos.append("La contraseña debe contener al menos un número.")
    if not re.search(r'[!\"#$%&\'()*+,\-./:;<=>?@[\\\]^_`{|}~]', contrasena):
        criterios_no_cumplidos.append("La contraseña debe contener al menos un carácter especial.")
    if criterios_no_cumplidos:
        print("La contraseña no es segura por las siguientes razones:")
        for criterio in criterios_no_cumplidos:
            print(f"- {criterio}")
    else:
        print("La contraseña es segura.")
contrasena_usuario = input("Introduce una contraseña: ")
validar_contrasena(contrasena_usuario)


#2
#Crea un programa que reciba una cantidad en una moneda específica y convierta esa cantidad a otras dos monedas diferentes.
#Los tipos de cambio deben estar almacenados en un diccionario. El usuario ingresará la moneda de origen, la cantidad y las monedas de destino.
#El programa debe mostrar el resultado de las conversiones y validar si las monedas ingresadas son válidas.
# Diccionario con los tipos de cambio
# Diccionario con los tipos de cambio
# Diccionario con los tipos de cambio
tipos_cambio = {
    'MXN': {'USD': 0.052, 'EUR': 0.047, 'ARS': 49.95, 'RUB': 4.86},
    'USD': {'MXN': 19.27, 'EUR': 0.90, 'ARS': 962.27, 'RUB': 93.62},
    'EUR': {'MXN': 21.40, 'USD': 1.11, 'ARS': 1069.23, 'RUB': 104.04},
    'ARS': {'MXN': 0.020, 'USD': 0.0010, 'EUR': 0.00094, 'RUB': 0.097},
    'RUB': {'MXN': 0.21, 'USD': 0.011, 'EUR': 0.096, 'ARS': 10.28}
}
def convertir_moneda(cantidad, moneda_origen, moneda_destino):
    if moneda_origen in tipos_cambio and moneda_destino in tipos_cambio[moneda_origen]:
        tasa_cambio = tipos_cambio[moneda_origen][moneda_destino]
        return cantidad * tasa_cambio
    else:
        return None
def main():
    moneda_origen = input("Introduce la moneda de origen (MXN, USD, EUR, ARS, RUB): ").upper()
    cantidad = float(input("Introduce la cantidad a convertir: "))
    moneda_destino_1 = input("Introduce la primera moneda de destino (MXN, USD, EUR, ARS, RUB): ").upper()
    moneda_destino_2 = input("Introduce la segunda moneda de destino (MXN, USD, EUR, ARS, RUB): ").upper()
    if moneda_origen not in tipos_cambio:
        print(f"La moneda de origen '{moneda_origen}' no es válida.")
        return
    if moneda_destino_1 not in tipos_cambio[moneda_origen]:
        print(f"La primera moneda de destino '{moneda_destino_1}' no es válida.")
        return
    if moneda_destino_2 not in tipos_cambio[moneda_origen]:
        print(f"La segunda moneda de destino '{moneda_destino_2}' no es válida.")
        return
    result_1 = convertir_moneda(cantidad, moneda_origen, moneda_destino_1)
    result_2 = convertir_moneda(cantidad, moneda_origen, moneda_destino_2)
    print(f"{cantidad} {moneda_origen} son {result_1:.2f} {moneda_destino_1}.")
    print(f"{cantidad} {moneda_origen} son {result_2:.2f} {moneda_destino_2}.")
if __name__ == "__main__":
    main()


#3
#Sistema de votación en el cual un usuario puede votar por un candidato (utilizando su nombre) en una elección.
#El programa debe aceptar múltiples votos y al final mostrar el total de votos para cada candidato.
#Si el candidato no existe, debe preguntar al usuario si desea agregarlo.
#Utiliza un diccionario para almacenar los nombres de los candidatos y sus votos.
def main():
    candidatos = {
        'Fulanito': 0,
        'Sultanito': 0,
        'Menganito': 0
    }
    print('Los candidatos son los siguientes: \n-Fulanito.\n-Sultanito.\n-Menganito.')
    while True:
        voto = input("Introduce el nombre del candidato por el que deseas votar (o 'salir' para terminar): ").strip()
        if voto.lower() == 'salir':
            break
        if voto in candidatos:
            candidatos[voto] += 1
            print(f"Voto registrado para {voto}. Total de votos: {candidatos[voto]}")
        else:
            agregar = input(f"El candidato '{voto}' no existe. ¿Deseas agregarlo? (sí/no): ").strip().lower()
            if agregar == 'sí':
                candidatos[voto] = 1
                print(f"Candidato '{voto}' agregado. Total de votos: 1")
            else:
                print("Voto no registrado.")
    print("\nResultados finales de la votación:")
    for candidato, votos in candidatos.items():
        print(f"{candidato}: {votos} votos")
if __name__ == "__main__":
    main()


#4
#Escribe un programa que reciba una lista de palabras introducida por el usuario (una sola línea separada por espacios).
#El programa debe ordenar la lista de palabras según su longitud y en caso de palabras con la misma longitud, debe ordenarlas alfabéticamente.
def main():
    entrada = input("Introduce una lista de palabras separadas por espacios: ")
    palabras = entrada.split()
    palabras_ordenadas = sorted(palabras, key=lambda palabra: (len(palabra), palabra))
    print("\nPalabras ordenadas:")
    for palabra in palabras_ordenadas:
        print(palabra)
if __name__ == "__main__":
    main()


#5
#Crea un programa que gestione un inventario de productos utilizando un diccionario donde:
#La clave es el nombre del producto. El valor es una tupla con el precio y la cantidad disponible.
#El programa debe permitir al usuario: Consultar la cantidad y el precio de un producto específico. Agregar un nuevo producto o modificar uno existente. Mostrar todos los productos en stock.
def main():
    inventario = {}
    while True:
        print("\n Menú de Inventario \n1. Agregar o modificar producto existente.\n2. Consultar cantidad y precio del producto.\n3. Mostrar todos los productos en stock.\n4. Salir")
        opcion = input("Selecciona una opción (1-4): ")
        if opcion == '1':
            nombre_producto = input("Introduce el nombre del producto: ").strip()
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad disponible: "))
            inventario[nombre_producto] = (precio, cantidad)
            print(f"Producto '{nombre_producto}' agregado/modificado con éxito.")
        elif opcion == '2':
            nombre_producto = input("Introduce el nombre del producto a consultar: ").strip()
            if nombre_producto in inventario:
                precio, cantidad = inventario[nombre_producto]
                print(f"Producto: {nombre_producto}, Precio: ${precio:.2f}, Cantidad disponible: {cantidad}")
            else:
                print(f"El producto '{nombre_producto}' no se encuentra en el inventario.")
        elif opcion == '3':
            if not inventario:
                print("No hay productos en el inventario.")
            else:
                print("\n--- Productos en Inventario ---")
                for producto, (precio, cantidad) in inventario.items():
                    print(f"Producto: {producto}, Precio: ${precio:.2f}, Cantidad disponible: {cantidad}")
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor selecciona una opción del 1 al 4.")
if __name__ == "__main__":
    main()


#6
#Escribe un programa que analice la frecuencia de cada palabra en un texto ingresado por el usuario.
#El programa debe ignorar mayúsculas y minúsculas, y contar las palabras repetidas.
# Muestra el resultado en un formato de diccionario, donde las claves son las palabras y los valores son las frecuencias.
def contar_frecuencia(texto):
    texto = texto.lower()
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1   
    return frecuencia
def main():
    texto_usuario = input("Introduce un texto: ")
    resultado = contar_frecuencia(texto_usuario)
    print("\nFrecuencia de palabras:")
    for palabra, cantidad in resultado.items():
        print(f"{palabra}: {cantidad}")
if __name__ == "__main__":
    main()

#7
#Crea un programa que reciba un conjunto de puntos en un plano 2D representados como tuplas (x, y).
#El programa debe calcular la distancia entre todos los puntos y devolver cuáles dos puntos están más cercanos entre sí.
#Usa la fórmula de distancia Euclidiana [d = √((x2 - x1)² + (y2 - y1)²)]
import math
def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])*2 + (point2[1] - point1[1])*2)
def closest_points(points):
    min_distance = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    return closest_pair, min_distance
# uso
points = [(1, 2), (3, 4), (0, 0), (5, 1)]
result, distance = closest_points(points)
print(f"Los puntos más cercanos son {result} con una distancia de {distance:.2f}")


#8
#Escribe un programa que genere una contraseña compleja de longitud variable según lo indicado por el usuario. La contraseña debe incluir:
#Letras mayúsculas y minúsculas. Números. Caracteres especiales.
import random
import string
def generar_contrasena(longitud):
    if longitud < 8:
        print("La longitud mínima recomendada para una contraseña es de 8 caracteres.")
        return None
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    nums = string.digits
    caract_esp = string.punctuation
    todos_los_caracteres = letras_mayusculas + letras_minusculas + nums + caract_esp
    contra = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(nums),
        random.choice(caract_esp)
    ]
    contra += random.choices(todos_los_caracteres, k=longitud - 4)
    random.shuffle(contra)
    return ''.join(contra)
def main():
    longitud = int(input("Introduce la longitud deseada para la contraseña (mínimo 8): "))
    contra = generar_contrasena(longitud)
    if contra:
        print(f"Tu nueva contraseña generada es: {contra}")
if __name__ == "__main__":
    main()
