from MyLibrary import informacion, texto_es_numero, texto_color

def es_capicua(numero: int) -> bool:
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

def menu_verificar_capicua():
    print("")
    print(texto_color("Verificar si un número es capicúa", color_texto="azul"))
    print(texto_color("Ingrese un número:",color_texto="azul"))
    numero = texto_es_numero(input())

    if len(str(numero)) % 2 == 0:
        if es_capicua(numero):
            print(texto_color("El número es capicúa.", color_texto="verde"))
        else:
            print(texto_color("El número no es capicúa.", color_texto="rojo"))
    else:
        print(texto_color("El número de cifras no es par.", color_texto="rojo"))

if __name__ == "__main__":
    menu_verificar_capicua()
