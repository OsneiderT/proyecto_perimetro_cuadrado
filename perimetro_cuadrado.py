# hacer un programa que calcule el perimetro de un cuadrado

# funcion para hallar el perimetro
def perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro

# solicitar la longitud del lado del cuadrado
lado_cuadrado = float(input("Digite la longitud de un lado del cuadrado en cm: "))

# mostrar la informacion al usuario
print(f'El perimetro del cuadrado con lado {lado_cuadrado}, es: {perimetro_cuadrado(lado_cuadrado)}')
