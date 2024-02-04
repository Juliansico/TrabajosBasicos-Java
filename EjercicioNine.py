from MyLibrary import informacion, texto_es_numero, texto_color

def obtener_nombre_mes(numero_mes: int) -> str:
    nombres_meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    if 1 <= numero_mes <= 12:
        return nombres_meses[numero_mes - 1]
    else:
        return "Número de mes no válido"

def menu_obtener_nombre_mes():
    print("")
    print(texto_color("Obtener el nombre del mes", color_texto="azul"))
    print(texto_color("Ingrese un número de mes (entre 1 y 12):",color_texto="azul"))
    numero_mes = texto_es_numero(input())

    nombre_mes = obtener_nombre_mes(numero_mes)

    print(texto_color(f"El nombre del mes es: {nombre_mes}", color_texto="azul"))

if __name__ == "__main__":
    menu_obtener_nombre_mes()
