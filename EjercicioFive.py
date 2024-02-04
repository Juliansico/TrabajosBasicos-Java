from MyLibrary import informacion, texto_es_numero, texto_color
from datetime import datetime

def calcular_fecha_ejr5(cadena: str, formato: str = '%Y%m%d') -> bool:
    try:
        numero = datetime.strptime(cadena, formato)
        return numero
    except ValueError as msg_error:
        return False

def extraer_fecha_ejr5(numero: int) -> (int, int, int) or bool:
    if 10000000 <= numero <= 99999999:
        num1 = numero % 100
        numero_sin_dia = numero // 100
        num2 = numero_sin_dia % 100
        num3 = numero_sin_dia // 100
        return num3, num2, num1
    return False

def menu_fecha_ejr5():
    print("")
    print(texto_color("Ingrese el valor de ocho dígitos en donde se le dará la fecha ordenada AÑO,MES Y DIA", color_texto="azul"))
    print(texto_color("Ingrese la fecha que desea validar",color_texto="azul"))
    numero = int(input())  # Cambiado a int() en lugar de texto_es_numero
    resultado = calcular_fecha_ejr5(str(numero))
    if resultado:
        fecha_extraida = extraer_fecha_ejr5(numero)
        if fecha_extraida:
            num3, num2, num1 = fecha_extraida
            print(texto_color(f"La fecha que digitaste fue: año {num3}, mes {num2:02d}, día {num1:02d}",color_texto="azul"))
            print(texto_color("Año:", color_texto="amarillo"), num3)
            print(texto_color("Mes:", color_texto="amarillo"), num2)
            print(texto_color("Día:", color_texto="amarillo"), num1)
        else:
            print(texto_color("La fecha ingresada no es válida.", color_texto="rojo"))
    else:
        print(texto_color("La fecha ingresada no es válida.", color_texto="rojo"))

if __name__ == "__main__":
    a = 20220128
    resultado = calcular_fecha_ejr5(str(a))
    print(resultado)
    menu_fecha_ejr5()
