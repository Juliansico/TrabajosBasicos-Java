from MyLibrary import informacion, texto_es_numero

from MyLibrary import texto_color, informacion, texto_es_numero

def calcular_cociente(numero1: int, numero2: int) -> float:
    if numero2 == 0:
        print(texto_color("Error: La división es una indeterminación", color_texto="rojo"))
        return 0
    else:
        return numero1 / numero2

def menu_cociente():
    print("")
    print(informacion(texto_color("Validación de cociente de dos números", color_texto="amarillo")))
    print("")
    print(texto_color("Ingresar primer número:", color_texto="azul"))
    numero1 = texto_es_numero(input())
    print(texto_color("Ingresar segundo número:", color_texto="azul"))
    numero2 = texto_es_numero(input())
    resultado = calcular_cociente(numero1, numero2)
    print(texto_color("El resultado es: ", color_texto="azul") + texto_color(f"{resultado}", color_texto="amarillo"))
if __name__ == "__main__":
    a = 5
    print(calcular_cociente(a, 0))
    b = 6
    print(calcular_cociente(b, 2))
    menu_cociente(a, b)



