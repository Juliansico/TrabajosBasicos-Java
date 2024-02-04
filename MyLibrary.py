from copy import error


def texto_color(texto: str, color_texto: str, color_numero: str = "blanco"):
    colores = {
        "negro": "\033[30m",
        "rojo_oscuro": "\033[31m",
        "verde_oscuro": "\033[32m",
        "amarillo_oscuro": "\033[33m",
        "azul_oscuro": "\033[34m",
        "magenta_oscuro": "\033[35m",
        "cyan_oscuro": "\033[36m",
        "gris": "\033[37m",
        "gris_oscuro": "\033[90m",
        "rojo": "\033[91m",
        "verde": "\033[92m",
        "amarillo": "\033[93m",
        "azul": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "blanco": "\033[97m",
    }

    fin_color = "\033[00m"

    return colores.get(color_numero, "") + colores.get(color_texto, "") + texto + fin_color

def informacion(texto: str):
    return texto_color(texto, color_texto="verde")

def texto_es_numero(valor: str):
    while True:
        try:
            numero = int(valor)
            return numero
        except ValueError:
            print(texto_color("Ingrese un número válido", color_texto="rojo"))
            valor = input()
