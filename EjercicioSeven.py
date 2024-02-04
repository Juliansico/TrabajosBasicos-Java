from MyLibrary import informacion, texto_es_numero, texto_color

def calcular_hipotenusa(cateto1: float, cateto2: float) -> float:
    hipotenusa = (cateto1**2 + cateto2**2)**0.5
    return hipotenusa

def menu_calculo_hipotenusa():
    print("")
    print(informacion(texto_color("Calcular la hipotenusa de un triángulo", color_texto="amarillo")))
    print(texto_color("Ingrese el valor del cateto 1:", color_texto="azul"))
    cateto1 = texto_es_numero(input())
    print(texto_color("Ingrese el valor del cateto 2:", color_texto="azul"))
    cateto2 = texto_es_numero(input())

    hipotenusa = calcular_hipotenusa(cateto1, cateto2)

    print(texto_color(f"La hipotenusa del triángulo es:  {hipotenusa}", color_texto="azul"))

if __name__ == "__main__":
    menu_calculo_hipotenusa()
