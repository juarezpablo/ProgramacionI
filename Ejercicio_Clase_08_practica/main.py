import re
import json

def imprimir_dato(mensaje:str) :
    '''
    Imprime un string

    Recibe por parametro un string

    '''
    if(type(mensaje) == str):
        print(mensaje)

def menu():
        mensaje_1= "    Menu Heroes \n A)Nombre de cada heroe masculino\n B)Nombre de cada heroe femenino\n"
        mensaje_2=" C)Heroe masculino mas alto\n D)Heroe femenino mas alto\n E)Heroe masculino mas bajo\n"
        mensaje_3=" F)Heroe femenino mas bajo\n G)Altura promedio de heroes masculinos\n H)Altura promedio heroes femeninos\n"
        mensaje_4=" I)Indicadores anteriores \n J)Cantidad de heroes con cada tipo de color de ojos\n"
        mensaje_5=" K)Cantidad de heroes con cada tipo de color de pelo \n L)Cantidad de heroes con cada tipo de inteligencia\n"
        mensaje_6=" M)Lista de heroes agrupados por color de ojos\n N)Lista de heroes agrupados por color de pelo\n O)Lista de heroes agrupados por tipo de inteligencia\n Z)Salir \n"
        mensaje_menu = mensaje_1+mensaje_2+mensaje_3+mensaje_4+mensaje_5+mensaje_6
        imprimir_dato(mensaje_menu)
        
def imprimir_menu_desafio_5():
    menu()

def stark_menu_principal_desafio_5() :
    
    imprimir_menu_desafio_5()
    respuesta = input("Ingresa la letra de una de las opciones del menu\n")
        
    if( type(respuesta) == str and len(respuesta) == 1):
        respuesta =respuesta.lower()
        lista=[]
        lista = re.findall('[a-oz]',respuesta)
        print(lista)
        if(lista == ""):
            print("error retorno -1")
            return -1

        
        print(lista[0])
        return lista[0]
    else: 
        print("-1")
        return -1    
               
        


#imprimir_menu_desafio_5()
#   stark_menu_principal_desafio_5()
'''
def stark_marvel_app_5(lista_de_heroes:list) :
    while True:
        respuesta = stark_menu_principal_desafio_5()
        if(respuesta == "a"):
            imprimir_heroes_masculinos()
        elif(respuesta == "B"):
            imprimir_heroes_femeninos()
        elif(respuesta == "C"): 
            imprimir_max_altura_masculino()       
        elif(respuesta == "D"):    
            imprimir_max_altura_femenino()
        elif(respuesta == "E"):
            imprimir_min_altura_masculino()
        elif(respuesta == "F"):
            imprimir_min_altura_femenino()
        elif(respuesta == "G"):
            imprimir_promedio_altura_masculinos()
        elif(respuesta == "H"):  
            imprimir_promedio_altura_femenino()
        elif(respuesta == "I"):
            imprimir_items_anteriores()
        elif(respuesta == "J"):
            cantidad_tipos_ojos()
        elif(respuesta == "K"):
            cantidad_tipo_pelo()
        elif(respuesta == "L"):
            cantidad_tipo_inteligencia()
        elif(respuesta == "M"):
            lista_ojos_heroes()
        elif(respuesta == "N"):
            lista_pelo_heroes()
        elif(respuesta == "O"):   
            lista_inteligencia_heroes()                                   
        elif(respuesta == 0):
            break

        '''

with open("C:/Users/Pablo/Desktop/ProgramacionI/Ejercicio_Clase_08_practica/data_stark.json","r") as archivo:
    dicc=json.load(archivo)
    print(dicc)
