from MyLibrary import informacion, texto_es_numero, texto_color

def calcular_el_multiplo(numero1: int | float | str) -> bool | float:
    if numero1 <= 0:
        print(texto_color("El número debe ser mayor a 0", color_texto="rojo"))
        return numero1
    else:
        return numero1 % 2 == 0 and numero1 % 3 == 0

def menu_el_multiplo():
    print("")
    print(informacion(texto_color("Validación de múltiplo de 3 o 4", color_texto="amarillo")))
    print("")
    print(texto_color("Ingresar número para saber si es múltiplo de 3 o 4:", color_texto="azul"))
    numero1 = texto_es_numero(input())
    resultado = calcular_el_multiplo(numero1)
    mensaje = "El número es múltiplo de 2 y de 3" if resultado else "El número no es múltiplo de 2 ni de 3"
    print(texto_color(mensaje, color_texto="verde"))

if __name__ == "__main__":
    a = 4
    print(calcular_el_multiplo(a))
    b = 6
    print(calcular_el_multiplo(b))
    menu_el_multiplo()
