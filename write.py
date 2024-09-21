#1
#Uso de la instrucción open()
archivo = open("ArchivoPrueba.txt", "a") #para crear era w
#archivo.write('Saludos a todoslos presente. Aqui es donde se escribe para que se ponga en el archivo \n')
#archivo.write('que gusto de volverte a encontrar\n')
#archivo.write('Ultima linea')
nuevoTexto = ['\n otra linea nueva', '\npenultima linea', '\nlinea final']
#Se agrega con ayuda de writelines
archivo.writelines(nuevoTexto)
#instruccion que cierra el archivo
archivo.close()



#2
# Escribir una Lista de Cadenas
# Dada una lista de nombres, escribir cada nombre en 'nombres.txt'.
nombres = ["Hugo", "Paco", "Luis", "McPato"]
with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")


#3
# Escribir Datos en Formato CSV
# Crear un archivo CSV 'productos.csv' con nombre, precio y cantidad.
import csv
productos = [
    ["Nombre", "Precio", "Cantidad"],
    ["Manzana", 20, 5],
    ["Banana", 15, 10],
    ["Naranja", 10, 15]
]
with open("productos.csv", "w", newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerows(productos)


#4
# Manejo de Errores al Escribir en Archivos
# Intentar escribir en un archivo y manejar errores.
try:
    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Escribiendo en un archivo que no existe.")
except Exception as e:
    print(f"Ocurrió un error: {e}")