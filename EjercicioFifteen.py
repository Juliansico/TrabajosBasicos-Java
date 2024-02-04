from MyLibrary import informacion, texto_color

UNIDADES = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
DECENAS = ['', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']

def numero_a_palabras(numero: int) -> str:
    if 0 <= numero <= 99:
        if numero < 10:
            return UNIDADES[numero]
        elif numero == 10:
            return 'diez'
        elif 11 <= numero <= 19:
            return 'dieci' + UNIDADES[numero % 10]
        else:
            unidad = UNIDADES[numero % 10]
            decena = DECENAS[numero // 10]
            return decena + (' y ' + unidad if unidad != '' else '')
    else:
        return 'Número fuera del rango válido (0-99)'

def menu_numero_a_palabras():
    print("")
    print(texto_color("Convertir número a palabras", color_texto="azul"))
    print(texto_color("Ingrese un número entre 0 y 99:",color_texto="amarillo"))
    numero = input()

    try:
        numero = int(numero)
        resultado = numero_a_palabras(numero)
        print(texto_color(f"Representación en palabras: {resultado}", color_texto="verde"))
    except ValueError:
        print(texto_color("Por favor, ingrese un número válido.", color_texto="rojo"))

if __name__ == "__main__":
    menu_numero_a_palabras()
