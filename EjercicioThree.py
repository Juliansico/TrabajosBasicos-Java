from MyLibrary import informacion, texto_es_numero, texto_color
import math

def calcular_hipotenusa(numero1: int | float | str) -> bool | float:
    if numero1 == 0:
        print(texto_color("La división es una indeterminación", color_texto="rojo"))
        return numero1
    else:
        return math.hypot(numero1, 2)

def menu_hipotenusa():
    print("")
    print(informacion(texto_color("Validación del cociente de ambos números", color_texto="amarillo")))
    print("")
    print(texto_color("Ingresa el número al cual deseas calcular la hipotenusa:", color_texto="azul"))
    numero1 = texto_es_numero(input())
    resultado = calcular_hipotenusa(numero1)
    print(texto_color(f"El resultado de la hipotenusa es: {resultado}", color_texto="verde"))

if __name__ == "__main__":
    a = 4
    print(calcular_hipotenusa(a))
    menu_hipotenusa()
