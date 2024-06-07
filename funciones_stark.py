from os import system
from data_stark import lista_personajes


def limpiar_pantalla():
    """funcion que limpia la pantalla
    """
    system("clear")


def menu():
    limpiar_pantalla()
    print("      ***MENU DE OPCIONES***      ")
    print("A- Ver nombres de todos los superheroes")
    print("B- Ver nombres de todos los superheroes y su altura")
    print("C- Superheroe mas alto")
    print("D- Superheroe mas bajo")
    print("E- Altura promedio de todos los superheroes")
    print("F- Identidad del supeheroe mas alto")
    print("G- Identidad del supeheroe mas bajo")
    print("H- Superheroe mas pesado")
    print("I- Superheroe menos pesado")
    print("J- Superheroes de genero masculino")
    print("K- Superheroes de genero femenino")
    print("M- Superheroe mas alto de genero masculino")
    print("N- Superheroe mas alto de genero femenino")
    print("O- Superheroe mas bajo de genero masculino")
    print("P- Superheroe mas bajo de genero femenino")
    print("Q- Altura promedio de superheroes de genero masculino")
    print("R- Altura promedio de superheroes de genero femenino")
    print("S- Nombres de los superheroes mas altos y mas bajos de genero masculino y femenino")
    print("T- Cantidad de superheroes segun color de ojos")
    print("U- Cantidad de superheroes segun color de pelo")
    print("V- Cantidad de superheroes segun tipo de inteligencia")
    print("W- Superheroes agrupados por color de ojos")
    print("X- Superheroes agrupados por color de pelo")
    print("Y- Superheroes agrupados por inteligencia")
    print("Z- Salir")

    return input("Ingrese opcion: ").upper()


def pausar():
    input('Aprete una tecla para continuar...')


def listar_superheroes(funcion, lista:list):
    for sup in lista:
        print(funcion(sup))


def altura_promedio(lista:list):
    acumulador_alturas = 0
    contador_personajes = 0
    
    for sup in lista:
        acumulador_alturas += float(sup['altura'])
        contador_personajes += 1
    
    promedio = acumulador_alturas / contador_personajes
    
    return promedio


def definir_identidad (lista:list, campo:str, indicador:str)-> str:
    superh_max = obtener_mayor(lista, campo)
    superh_min = obtener_menor(lista, campo)
    
    for sup in lista:
        if sup['nombre'] == superh_max['nombre']:
            max = sup['identidad']
        elif sup['nombre'] == superh_min['nombre']:
            min = sup['identidad']
    
    if indicador == 'maximo':
        return max
    elif indicador == 'minimo':
        return min
    

def obtener_mayor(lista:list, campo:str):
    flag = True
    mayor = 0
    
    for el in lista:
        if flag:
            mayor = float(el[campo])
            sup_mayor = el
            flag = False
        else:
            if mayor < float(el[campo]):
                mayor = float(el[campo])
                sup_mayor = el
                
    return sup_mayor


def obtener_menor(lista:list, campo:str):
    flag = True
    menor = 0
    
    for el in lista:
        if flag:
            menor = float(el[campo])
            sup_menor = el
            flag = False
        else:
            if menor > float(el[campo]):
                menor = float(el[campo])
                sup_menor = el
                
    return sup_menor


def filtrar_lista(filtradora, lista:list)->list:
    lista_filtrada = []
    for elemento in lista:
        if filtradora(elemento):
            lista_filtrada.append(elemento)
    return lista_filtrada


def listado_superh():
    listar_superheroes(lambda sup: sup['nombre'], lista_personajes)
    
    
def listado_superh_altura():
    listar_superheroes(lambda sup: f"{sup['nombre']}: {sup['altura']}",lista_personajes) 


def superh_mas_alto():
    sup_mas_alto = obtener_mayor(lista_personajes, 'altura')
    print(f"El superheroe mas alto es:")
    for key, value in sup_mas_alto.items():
        print(f"{key} : {value}")
        
    
def superh_mas_bajo():
    sup_mas_bajo = obtener_menor(lista_personajes, 'altura')
    print(f"El personaje mas bajo es:")
    for key, value in sup_mas_bajo.items():
        print(f"{key} : {value}")


def promedio_altura_superh():
    print(f"La altura promedio de todos los superheroes es {altura_promedio(lista_personajes)}")


def ident_superh_mas_alto():
    print(f"La identidad del superheroe mas alto es: {definir_identidad(lista_personajes, 'altura', 'maximo')}")
    
    
def ident_superh_mas_bajo():
    print(f"La identidad del superheroe mas bajo es: {definir_identidad(lista_personajes, 'altura', 'minimo')}")
    
    
def superh_mas_pesado():
    sup_mas_peso = obtener_mayor(lista_personajes, 'peso')
    print(f"El personaje mas pesado es:")
    for key, value in sup_mas_peso.items():
        print(f"{key}: {value}")
    
    
def superh_menos_pesado():
    sup_menos_peso = obtener_menor(lista_personajes, 'peso')
    print(f"El personaje menos pesado es:")
    for key, value in sup_menos_peso.items():
        print(f"{key}: {value}")
    
    
def superh_masc():
    listar_superheroes(lambda sup: sup["nombre"], filtrar_lista(lambda s: s["genero"] == "M", lista_personajes))
    
    
def superh_fem():
    listar_superheroes(lambda sup: sup["nombre"], filtrar_lista(lambda s: s["genero"] == "F", lista_personajes))
    
    
def superh_alto_masc():
    print("El superheroe mas alto de genero masculino es:")
    sup_alto = obtener_mayor(filtrar_lista(lambda sup: sup['genero'] == 'M', lista_personajes), 'altura')
    for key, value in sup_alto.items():
        print(f"{key}: {value}")
    
    
def superh_alta_fem():
    print("El superheroe mas alto de genero femenino es:")
    sup_alta = obtener_mayor(filtrar_lista(lambda sup: sup['genero'] == 'F', lista_personajes), 'altura')
    for key, value in sup_alta.items():
        print(f"{key}: {value}")
 
    
def superh_bajo_masc():
    print("El superheroe mas bajo de genero masculino es:")
    sup_bajo = obtener_menor(filtrar_lista(lambda sup: sup['genero'] == 'M', lista_personajes), 'altura')
    for key, value in sup_bajo.items():
        print(f"{key}: {value}")  
    
    
def superh_baja_fem():
    print("El superheroe mas bajo de genero femenino es:")
    sup_baja = obtener_menor(filtrar_lista(lambda sup: sup['genero'] == 'F', lista_personajes), 'altura')
    for key, value in sup_baja.items():
        print(f"{key}: {value}")    
   
    
def alt_promedio_masc():
    print(f"La altura promedio de los superheroes de genero masculino es {altura_promedio(filtrar_lista(lambda sup: sup['genero'] == 'M', lista_personajes))}")
    
    
def alt_promedio_fem():
    print(f"La altura promedio de los superheroes de genero femenino es {altura_promedio(filtrar_lista(lambda sup: sup['genero'] == 'F', lista_personajes))}")


def alto_bajo_masc_fem():
    sup_alto_m = obtener_mayor(filtrar_lista(lambda sup: sup['genero'] == 'M', lista_personajes), 'altura')
    for key, value in sup_alto_m.items():
        if key == 'nombre':
            print(f"Superheroe mas alto de genero masculino: {value}")
            
    sup_bajo_m = obtener_menor(filtrar_lista(lambda sup: sup['genero'] == 'M', lista_personajes), 'altura')
    for key, value in sup_bajo_m.items():
        if key == 'nombre':
            print(f"Superheroe mas bajo de genero masculino: {value}")
    
    sup_alta_f = obtener_mayor(filtrar_lista(lambda sup: sup['genero'] == 'F', lista_personajes), 'altura')
    for key, value in sup_alta_f.items():
        if key == 'nombre':
            print(f"Superheroe mas alto de genero femenino: {value}")
            
    sup_baja_f = obtener_menor(filtrar_lista(lambda sup: sup['genero'] == 'F', lista_personajes), 'altura')
    for key, value in sup_baja_f.items():
        if key == 'nombre':
            print(f"Superheroe mas bajo de genero femenino: {value}")
              
            
def calcular_cantidad_caract(lista:list, campo:str)->dict:
    dict_cantidades = {}
    for sup in lista:
        if sup[campo] not in dict_cantidades:
            if sup[campo] == "":
                dict_cantidades["No tiene"] = 1
            else:
                dict_cantidades[sup[campo]] = 1
        else:
            dict_cantidades[sup[campo]] += 1
    return dict_cantidades


def cant_color_ojos():
    dict_color_ojos = calcular_cantidad_caract(lista_personajes, 'color_ojos')
    for color, cantidad in dict_color_ojos.items():
        print(f"{color}: {cantidad}")
        
        
def cant_color_pelo():
    dict_color_pelo = calcular_cantidad_caract(lista_personajes, 'color_pelo')
    for color, cantidad in dict_color_pelo.items():
        print(f"{color}: {cantidad}")
        
        
def cant_inteligencia():
    dict_inteligencia = calcular_cantidad_caract(lista_personajes, 'inteligencia')
    for tipo_inteligencia, cantidad in dict_inteligencia.items():
        print(f"{tipo_inteligencia}: {cantidad}")
        

def grupos_superheroes(lista:list, campo:str)->dict:
    diccionario_grupos = {}
    
    for sup in lista:
        if sup[campo] not in diccionario_grupos:
            if sup[campo] == "":
                diccionario_grupos["No tiene"] = [sup['nombre']]
            else:
                diccionario_grupos[sup[campo]] = [sup['nombre']]
        else:
            diccionario_grupos[sup[campo]].append(sup['nombre'])
            
    return diccionario_grupos


def grupos_ojos():
    dict_ojos = grupos_superheroes(lista_personajes, 'color_ojos')
    for color, superheroes in dict_ojos.items():
        print(f"- {color} -".upper())
        for sup in superheroes:
            print(sup)
        print("------------------")
        
        
def grupos_pelo():
    dict_pelo = grupos_superheroes(lista_personajes, 'color_pelo')
    for color, superheroes in dict_pelo.items():
        print(f"- {color} -".upper())
        for sup in superheroes:
            print(sup)
        print("------------------")
        
        
def grupos_inteligencia():
    dict_inteligencia = grupos_superheroes(lista_personajes, 'inteligencia')
    for inteligencia, superheroes in dict_inteligencia.items():
        print(f"- {inteligencia} -".upper())
        for sup in superheroes:
            print(sup)
        print("------------------")

        
            

    
    