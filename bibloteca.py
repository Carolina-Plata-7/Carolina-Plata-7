
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