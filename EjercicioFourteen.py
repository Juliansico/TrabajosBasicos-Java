from MyLibrary import informacion, texto_color

def es_palindroma(cadena: str) -> bool:
    return cadena == cadena[::-1]

def menu_verificar_palindroma():
    print("")
    print(texto_color("Verificar si una cadena es palíndroma", color_texto="azul"))
    print(texto_color("Ingrese una cadena:",color_texto="amarillo"))
    cadena = input()

    if es_palindroma(cadena):
        print(texto_color("La cadena es palíndroma.", color_texto="verde"))
    else:
        print(texto_color("La cadena no es palíndroma.", color_texto="rojo"))

if __name__ == "__main__":
    menu_verificar_palindroma()
