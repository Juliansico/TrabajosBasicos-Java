from MyLibrary import informacion, texto_es_numero, texto_color

def obtener_orden(valores):
    valores_ordenados = sorted(valores)
    mayor, medio, menor = valores_ordenados[2], valores_ordenados[1], valores_ordenados[0]
    return mayor, medio, menor

def menu_ordenar_numeros():
    print("")
    print(informacion(texto_color("Ordenar tres valores numéricos enteros", color_texto="amarillo")))
    valores = []
    for i in range(3):
        print(texto_color(f"Ingrese el valor {i + 1}:", color_texto="azul"))
        valor = texto_es_numero(input())
        valores.append(valor)

    mayor, medio, menor = obtener_orden(valores)

    print(texto_color("El valor mayor es:", color_texto="azul"), mayor)
    print(texto_color("El valor del medio es:", color_texto="azul"), medio)
    print(texto_color("El valor menor es:", color_texto="azul"), menor)

if __name__ == "__main__":
    menu_ordenar_numeros()
