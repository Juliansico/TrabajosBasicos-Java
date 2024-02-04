from MyLibrary import informacion, texto_es_numero, texto_color

def verificar_fecha(fecha: int) -> bool:
    # Extraer año, mes y día de la fecha
    ano = fecha // 10000
    mes = (fecha // 100) % 100
    dia = fecha % 100

    # Verificar si el año, mes y día son válidos
    if 1000 <= ano <= 9999 and 1 <= mes <= 12 and 1 <= dia <= 31:
        # Verificar si el día es válido para el mes dado
        dias_en_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if 1 <= dia <= dias_en_mes[mes]:
            return True

    return False

def menu_verificar_fecha():
    print("")
    print(texto_color("Verificar si una fecha es correcta", color_texto="azul"))
    print(texto_color("Ingrese la fecha en formato aaaammdd:",color_texto="azul"))
    fecha = texto_es_numero(input())

    if verificar_fecha(fecha):
        print(texto_color("La fecha es válida.", color_texto="azul"))
    else:
        print(texto_color("La fecha ingresada no es válida.", color_texto="rojo"))

if __name__ == "__main__":
    menu_verificar_fecha()
