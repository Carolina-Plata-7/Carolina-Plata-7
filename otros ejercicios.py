#1
#Cuenta cuántas veces aparece la palabra "Python" en la lista.
palabras = ["Python", "Java", "C++", "Python", "JavaScript", "Python", "C#"]
print("¿Cuántos 'python hay en la lista?' tiene", palabras.count("Python"))

#2
#Convierte todas las cadenas a mayúsculas sin usar métodos como upper().
frases = ["hola", "mundo", "python", "es", "genial"]
print("frase a mayuscula")
for i in range(len(frases)):
    frases[i] = "".join([chr(ord(c) - 32) for c in frases[i]])
print(frases)

#3
#Elimina todas aquellas palabras que tengan menos de 4 caracteres.
palabras = ["sol", "luna", "cielo", "mar", "estrella", "pez"]
NuePal = [palabra for palabra in palabras if len(palabra) >= 4]
print(NuePal)

#4
#Encuentra el número máximo sin usar la función max().
numeros = [15, 22, 8, 34, 9, 6, 17]
maximo = numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero
print("El número máximo es:", maximo)

#5
#Cuenta cuántos números son positivos.
Numeros = [-3, 5, -7, 2, -8, 10, -4, 6]
positivos = 0
for Numero in Numeros:
    if Numero > 0:
        positivos += 1
print("La cantidad de números positivos es:", positivos)

#6
#Invierte el orden de los elementos sin usar métodos como reverse().
Nums = [1, 2, 3, 4, 5]
invert = len(Nums) // 2
for i in range(invert):
    opuesto = len(Nums) - 1 - i
    Nums[i], Nums[opuesto] = Nums[opuesto], Nums[i]
print("Lista invertida:", Nums)

#7
#Encuentra y muestra la media (promedio) de los elementos de la lista.
Nombers = [4, 7, 2, 9, 3, 8, 5]
suma = sum(Nombers)
cant = len(Nombers)
prom = suma / cant
print("El promedio es:", prom)