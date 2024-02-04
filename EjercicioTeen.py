from MyLibrary import informacion, texto_es_numero, texto_color

def calcular_tiempo_invertido(segundos: int) -> tuple:
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_residuales = segundos % 60

    return horas, minutos, segundos_residuales

def menu_calcular_tiempo_invertido():
    print("")
    print(texto_color("Calcular tiempo invertido en un examen", color_texto="azul"))
    print(texto_color("Ingrese el número de segundos invertidos:",color_texto="azul"))
    segundos = texto_es_numero(input())

    horas, minutos, segundos_residuales = calcular_tiempo_invertido(segundos)

    print(texto_color(f"Tiempo invertido: {horas} horas, {minutos} minutos y {segundos_residuales} segundos", color_texto="azul"))

if __name__ == "__main__":
    menu_calcular_tiempo_invertido()
