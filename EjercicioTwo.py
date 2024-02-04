from MyLibrary import informacion, texto_es_numero, texto_color

def calcular_Par(numero1: int) -> float:
    if numero1 == 0:
        print(texto_color("La división es una indeterminación", color_texto="rojo"))
        return 0
    else:
        return numero1 % 2 == 0

def Menu_Par():
    print("")
    print(informacion(texto_color("Validar si es par o impar", color_texto="amarillo")))
    print("")
    print(texto_color("Ingresa un número para saber si es par o impar:", color_texto="azul"))
    numero1 = texto_es_numero(input())
    resultado = calcular_Par(numero1)
    print(texto_color("El número es par." if resultado else "El número es impar.", color_texto="verde"))

if __name__ == "__main__":
    a = 5
    print(calcular_Par(a))
    Menu_Par()
