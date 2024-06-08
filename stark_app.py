# APELLIDO Y NOMBRE: GONZALEZ, PAULA
# DNI: 36807959
# COMISION: 312


from funciones_stark import *

""""Desafío #00:
A. Analizar detenidamente el set de datos
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
G. Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
H. Calcular e informar cual es el superhéroe más y menos pesado.
I. Ordenar el código implementando una función para cada uno de los valores informados.
J. Construir un menú que permita elegir qué dato obtener"""

"""Desafío #01:
Agregar al código elaborado para cumplir el desafío #01 los siguientes puntos,
utilizando un menú que permita acceder a cada uno de los puntos por separado.
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia"""


while True:
    match menu():
        case 'A':
            listado_superh()
        case 'B':
            listado_superh_altura()      
        case 'C':
            superh_mas_alto()
        case 'D':
            superh_mas_bajo()
        case 'E':
            promedio_altura_superh()
        case 'F':
            ident_superh_mas_alto()
        case 'G':
            ident_superh_mas_bajo()
        case 'H':
            superh_mas_pesado()
        case 'I':
            superh_menos_pesado()
        case 'J':
            superh_masc()
        case 'K':
            superh_fem()
        case 'M':
            superh_alto_masc()
        case 'N':
            superh_alta_fem()
        case 'O':
            superh_bajo_masc()
        case 'P':
            superh_baja_fem()
        case 'Q':
            alt_promedio_masc()
        case 'R':
            alt_promedio_fem()
        case 'S':
            alto_bajo_masc_fem()
        case 'T':
            cant_color_ojos()
        case 'U':
            cant_color_pelo()
        case 'V':
            cant_inteligencia()
        case 'W':
            grupos_ojos()
        case 'X':
            grupos_pelo()
        case 'Y':
            grupos_inteligencia()
        case 'Z':
            break
        case _:
            print("La opcion no es valida")
  
    pausar()
    
print("Fin del programa")



    