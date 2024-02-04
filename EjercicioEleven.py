from MyLibrary import informacion, texto_es_numero, texto_color

def mostrar_digitos_en_orden_inverso(numero: int):
    digitos = [int(digito) for digito in str(numero)]
    digitos.reverse()

    print(texto_color("Dígitos en orden inverso:", color_texto="azul"))
    for digito in digitos:
        print(digito)

def menu_mostrar_digitos_en_orden_inverso():
    print("")
    print(texto_color("Mostrar dígitos en orden inverso", color_texto="azul"))
    print(texto_color("Ingrese un número entero:",color_texto="azul"))
    numero = texto_es_numero(input())

    mostrar_digitos_en_orden_inverso(numero)

if __name__ == "__main__":
    menu_mostrar_digitos_en_orden_inverso()
