from MyLibrary import informacion, texto_color

def capitalizar_frase(frase: str) -> str:
    palabras = frase.split()

    if len(palabras) >= 5:
        palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
        return texto_color(' '.join(palabras_capitalizadas), color_texto="blanco")
    else:
        return texto_color('La frase debe contener al menos 5 palabras.', color_texto="rojo")


def menu_capitalizar_frase():
    print("")
    print(texto_color("Capitalizar frase", color_texto="azul"))
    print(texto_color("Ingrese una frase de al menos 5 palabras:",color_texto="amarillo"))
    frase = input()

    resultado = capitalizar_frase(frase)
    print(texto_color(f"Frase capitalizada: {resultado}",color_texto="azul"))


if __name__ == "__main__":
    menu_capitalizar_frase()
