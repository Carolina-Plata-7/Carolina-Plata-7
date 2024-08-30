#Elabora una lista de números (7)
#Modifica 2 elementos de esta lista
numeros = ["1","2","3","15","4","5","6"]
numeros[0]="6"
print(numeros)


#Elabora una lista de frutas
#el usuario cambiará una de las frutas
#Que se guarde la nueva lista
frutas = ['Mango', 'Fresa', 'Uva', 'Piña', 'Manzana', 'Platano']
print("Esta es la lista de frutas: ")
for i, fruta in enumerate(frutas):
    print(f"{i+1}. {fruta}")

cambio_frut = int(input("¿Cuál te gustaría cambiar? (ingresa el número de la fruta) ")) - 1
nueva_frut = input("¿Cuál es la nueva? ")

frutas[cambio_frut] = nueva_frut
print(frutas)



#Realiza una lista que contenga elementos de diferentes tipos (números y un valor boleano)
#con un For mostrará lo que contiene
# Crear una lista con elementos de diferentes tipos
ListNue = [42, 3.14, True, 7, False, 12.5]
print("Lista:")
for elemento in ListNue:
    print(elemento)