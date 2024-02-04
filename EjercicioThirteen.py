from MyLibrary import informacion, texto_color

def contar_ocurrencias_caracter(cadena: str, caracter: str) -> int:
    return cadena.count(caracter)

def menu_contar_ocurrencias_caracter():
    print("")
    print(texto_color("Contar ocurrencias de un carácter en una cadena", color_texto="azul"))
    print(texto_color("Ingrese una cadena de caracteres:",color_texto="amarillo"))
    cadena = input()

    print(texto_color("Ingrese el carácter a contar:",color_texto="amarillo"))
    caracter = input()

    if len(caracter) == 1:
        ocurrencias = contar_ocurrencias_caracter(cadena, caracter)
        print(texto_color(f"El carácter '{caracter}' aparece {ocurrencias} veces en la cadena.", color_texto="verde"))
    else:
        print(texto_color("Por favor, ingrese solo un carácter.", color_texto="rojo"))

if __name__ == "__main__":
    menu_contar_ocurrencias_caracter()
