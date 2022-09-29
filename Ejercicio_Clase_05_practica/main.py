from xmlrpc.client import Boolean
from data_stark import lista_heroes

def stark_normalizar_datos(lista:list) -> list :
    '''
    Valida que la lista no este vacia/caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
    Valida primero que el tipo de dato no sea del tipo al cual será casteado.
    Si al menos un dato fue modificado Imprime como mensaje Datos normalizados, caso contrario no imprimirá nada

    Recibe una lista de heroes

    Retorna Error si la lista está vacia,Modif: ahora retorna una lista
    '''
    if lista:
        bandera_normalizado = 0
        retorno = []
        for item in lista:
            if( type(item["altura"])!= float ):
                item["altura"] = float(item["altura"])
                bandera_normalizado = 1
            if( type(item["peso"] != float)):
                item["peso"] = float(item["peso"])
                bandera_normalizado = 1
            if( type(item["fuerza"]) != int):
                item["fuerza"] = int(item["fuerza"]) 
                bandera_normalizado = 1 
            retorno.append(item)    
        return retorno
        if(bandera_normalizado == 1):
            print("Datos Normalizados")
        
    else:
        print("Error: Lista de heroes vacia")

def obtener_nombre(heroe:dict) -> str :
    '''
    Obtiene la key nombre de un diccionario y crea una variable con el mismo

    Recibe un diccionario correspondiente a un heroe

    Retorna un string con el nombre del heroe formateado 

    '''
    mensaje = "Nombre: {0}".format(heroe["nombre"])
    return mensaje

'''
dic_heroe ={
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": 79.349999999999994,
    "peso": 18.449999999999999,
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": 2,
    "inteligencia": ""
  }


'''

def imprimir_dato(mensaje:str) :
    '''
    Imprime un string

    Recibe por parametro un string

    '''
    if(type(mensaje) == str):
        print(mensaje)


#imprimir_dato(obtener_nombre(dic_heroe))

def stark_imprimir_nombres_heroes(lista:list) :
    '''
    Imprime una lista de heroes

    Recibe una lista de heroes
    
    Retorna -1 si la lista está vacia

    '''
    retorno = -1
    if lista:
        for item in lista:
            imprimir_dato(obtener_nombre(item))
    else:
        return retorno

#stark_imprimir_nombres_heroes(lista_heroes)

#---Fin punto 1----

#Punto 2)

def obtener_nombre_y_dato (heroe:dict,llave:str) -> str:
    '''
    crea un string formateado en forma de mensaje de acuerdo a la llave ingresada

    recibe el diccionario de un heroe y la key a incluir en el mensaje

    retorna un string en forma de mensaje con el nombre y la key ingresada
    '''
    if(type(heroe) == dict):
        mensaje = "Nombre: {0}  | {1}: {2}".format(heroe["nombre"],llave,heroe[llave])
        return mensaje


   
dic_heroes2 ={
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": 79.349999999999994,
    "peso": 18.449999999999999,
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": 2,
    "inteligencia": ""
  }   


#imprimir_dato(obtener_nombre_y_dato(dic_heroes2,"peso"))

# PUNTO 3)

def stark_imprimir_nombres_altura(lista:list):
    '''
    Imprime nombre y altura de cada heroe 

    Recibe una lista de heroes

    Retorna -1 en caso de que la lista este vacia
    '''
    retorno = -1
    if lista:
        for heroe in lista:
            imprimir_dato(obtener_nombre_y_dato(heroe,"altura"))

    else:
        return retorno    

#stark_imprimir_nombres_altura(lista_heroes)

# PUNTO 4)  #4.1

def calcular_max(lista:list,llave:str) ->dict:
    '''
    Calcula el dato con un valor maximo de una lista de heroes

    Recibe una lista de heroes y una llave la cual es el dato a buscar el max

    Devuelve un diccionario con la informacion del heroe
    '''
    if lista:
        heroe_max = lista[0]
        for heroe in lista:
            if(float(heroe[llave]) > float(heroe_max[llave])):
                heroe_max = heroe

        return heroe_max      


#print(calcular_max(lista_heroes,"fuerza"))

                #4.2

def calcular_min(lista:list,llave:str) ->dict:
    '''
    Calcula el dato  con un valor minimo de una lista de heroes

    Recibe una lista de heroes y una llave la cual es el dato a buscar el minimo

    Devuelve un diccionario con la informacion del heroe
    '''
    if lista:
        heroe_min = lista[0]
        for heroe in lista:
            if(float(heroe[llave]) < float(heroe_min[llave]) ):
                heroe_min = heroe
        return heroe_min        

#print(calcular_min(lista_heroes,"peso"))

                #4.3

def calcular_max_min_dato(lista:list,tipo_calculo:str,llave:str) ->dict :
    '''
    Calcula maximo o minimo de un tipo de dato de una lista

    Recibe una lista de heroes, el tipo de calculo: "maximo" o "minimo"
    y el nombre de la key a calcular

    Devuelve un diccionario del heroe con el valor max o min buscado
    '''

    if lista:
        if(tipo_calculo == "maximo"):
            return calcular_max(lista,llave)
        elif(tipo_calculo == "minimo"):
            return calcular_min(lista,llave)


#print(calcular_max_min_dato(lista_heroes,"minimo","altura"))

                #4.4
def stark_calcular_imprimir_heroe(lista:list,tipo_calculo:str,llave:str) :
    '''
    Obtiene el heroe e imprime su nombre mas el resultado del calculo buscado

    Recibe una lista de heroes, el tipo de calculo: "maximo" o "minimo"
    y el nombre de la key a calcular

    Devuelve -1 en caso de lista vacia
    '''
    if lista:
        heroe = calcular_max_min_dato(lista,tipo_calculo,llave)
        if(tipo_calculo == "maximo"):
            
            print('Mayor {0} '.format(llave))
            imprimir_dato(obtener_nombre_y_dato(heroe,llave))
        if( tipo_calculo == "minimo"):
            print('Menor {0} '.format(llave))
            imprimir_dato(obtener_nombre_y_dato(heroe,llave))             
    else:
        return -1    

# stark_calcular_imprimir_heroe(lista_heroes,"maximo","fuerza")

                #5.1
def sumar_dato_heroe(lista:list,llave:str) ->int :
    '''
    Obtiene la suma total que correspondan a la llave ingresada

    Recibe una lista de heroes, la key de la cual se quiere obtener la suma

    Devuelve la suma total de la key de cada heroe
    '''
    if lista:
        suma_de_llaves = 0
        for heroe in lista:
            if (type(heroe) == dict  and heroe != {}):
                suma_de_llaves += int(heroe[llave])
    return suma_de_llaves

#x=sumar_dato_heroe(lista_heroes,"fuerza")
#print(x)
                    #5.2
def dividir(dividendo:float,divisor:float) ->float :
    '''
    Obtiene la division entre los parametros

    Recibe un numero que sera el dividendo, recibe otro numero que sera el divisor

    Devuelve la division entre dividendo y divisor, devuelve 0 si el divisor es 0
    '''
    if( (type(dividendo)== float or type(dividendo)== int) and (type(divisor)==float or type(divisor)==int) and divisor != 0):
        resultado = float(dividendo) / float(divisor)
        return resultado
    elif( divisor == 0):
        resultado = 0
        return resultado    
#x=dividir(20,2)
#print(x)    
     
                #5.3
def calcular_promedio(lista:list,llave:str) ->float :
    '''
    Calcula el promedio de una key de una lista pasada por parametro

    Recibe una lista y la key a calcular el promedio

    Devuelve el promedio del valor de la key pasada por parametro
    '''      
    if lista :
        acumulador_sumatoria_llave = sumar_dato_heroe(lista,llave)
        contador_cantidad_heroes = 0
        for heroe in lista :
            if(type(heroe)==dict and heroe != {}):
                
                contador_cantidad_heroes += 1

        promedio = dividir(acumulador_sumatoria_llave,contador_cantidad_heroes)
        return promedio
#x=calcular_promedio(lista_heroes,"fuerza")
#print(x)

                    #5.4
def stark_calcular_imprimir_promedio_altura(lista:list) :
    '''
    Calcula e imprime el promedio de la altura de una lista 

    Recibe una lista

    
    '''
    if lista:
        dato_a_imprimir = calcular_promedio(lista,"altura")
        print(dato_a_imprimir)
    else:
        return -1    

#stark_calcular_imprimir_promedio_altura(lista_heroes)
                        #6.1
def imprimir_menu():
    mensaje_1= "\n    Menu Heroes \n 1)Nombre de cada heroe masculino\n 2)Nombre de cada heroe femenino\n"
    mensaje_2=" 3)Heroe masculino mas alto\n 4)Heroe femenino mas alto\n 5)Heroe masculino mas bajo\n"
    mensaje_3=" 6)Heroe femenino mas bajo\n 7)Altura promedio de heroes masculinos\n 8)Altura promedio heroes femeninos\n"
    mensaje_4=" 9)Indicadores anteriores\n 10)Imprimir nombre y altura de cada heroe"
    mensaje_menu = mensaje_1+mensaje_2+mensaje_3+mensaje_4
    imprimir_dato(mensaje_menu)

                    #6.2
def validar_entero(dato:str) ->Boolean:
    if type(dato)==str and dato.isnumeric() == True :
        return True
    else:
        return False 

#x=validar_entero("2a3242")
#print(x)  
                    #6.3
def stark_menu_principal() ->int :
    
    imprimir_menu()
    opcion =input("Elija una opcion del menu\n >")
    if(type(opcion)== int and opcion>0 and opcion <=15):
        return opcion
    elif(validar_entero(opcion)):
        opcion =int(opcion)
        return opcion
    else:
        return -1

         #------funciones auxiliares--------
def obtener_lista_dato(lista:list,llave:str,valor) ->list:
    '''
    Crea una lista con los diccionarios que cumplan la condicion clave/valor ingresada

    Recibe una lista ,la key y su valor a filtrar

    Devuelve una lista filtrada de acuerdo a los parametros ingresados
    '''
    #ista = stark_normalizar_datos(lista)
    retorno = []
    for heroe in lista:
        if (heroe[llave] == valor) :
            retorno.append(heroe)
    return retorno

def obtener_lista_masculinos(lista:list) ->list:
    lista_heroes_masculinos=obtener_lista_dato(lista,"genero","M")
    return lista_heroes_masculinos 

def imprimir_heroe_masculino_mas_alto(lista:list):
    maximo_heroe_altura = calcular_max((obtener_lista_masculinos(lista)),"altura")
    imprimir_dato(obtener_nombre_y_dato(maximo_heroe_altura,"altura"))

def obtener_lista_femeninos(lista:list) ->list:
    lista_heroes_femeninos = obtener_lista_dato(lista,"genero","F")
    return lista_heroes_femeninos  

def imprimir_heroe_femenino_mas_alto(lista:list):
    maximo_heroe_altura = calcular_max((obtener_lista_femeninos(lista)),"altura")
    imprimir_dato(obtener_nombre_y_dato(maximo_heroe_altura,"altura"))

def imprimir_heroe_masculino_mas_bajo(lista:list):
    minimo_heroe_altura =calcular_min((obtener_lista_masculinos(lista)),"altura")
    imprimir_dato(obtener_nombre_y_dato(minimo_heroe_altura,"altura"))

def imprimir_heroe_femenino_mas_bajo(lista:list):
    minimo_heroe_altura = calcular_min((obtener_lista_femeninos(lista)),"altura")
    imprimir_dato(obtener_nombre_y_dato(minimo_heroe_altura,"altura"))







        #-------fin de funciones auxiliares---
                #7.0
def stark_marvel_app(lista:list):
    lista = stark_normalizar_datos(lista)
    while True:
        respuesta = stark_menu_principal()
        if(respuesta == 1):
            stark_imprimir_nombres_heroes(obtener_lista_masculinos(lista))
        elif(respuesta == 2):
            stark_imprimir_nombres_heroes(obtener_lista_femeninos(lista))
        elif(respuesta == 3):
            imprimir_heroe_masculino_mas_alto(lista)
        elif(respuesta == 4):
            imprimir_heroe_femenino_mas_alto(lista)
        elif(respuesta == 5):
            imprimir_heroe_masculino_mas_bajo(lista)
        elif(respuesta == 6):
            imprimir_heroe_femenino_mas_bajo(lista)
        elif(respuesta ==7):
            print("Promedio altura masculino:\n ")
            stark_calcular_imprimir_promedio_altura(obtener_lista_masculinos(lista))
        elif(respuesta == 8):    
            print("Promedio altura femenino:\n ")
            stark_calcular_imprimir_promedio_altura(obtener_lista_femeninos(lista))
        elif(respuesta ==9):
            imprimir_heroe_masculino_mas_alto(lista)
            imprimir_heroe_femenino_mas_alto(lista)
            imprimir_heroe_masculino_mas_bajo(lista)
            imprimir_heroe_femenino_mas_bajo(lista)
            print("\nPromedio altura masculino:\n ")
            stark_calcular_imprimir_promedio_altura(obtener_lista_masculinos(lista))
            print("\nPromedio altura femenino:\n ")
            stark_calcular_imprimir_promedio_altura(obtener_lista_femeninos(lista))
        elif(respuesta==10):
            stark_imprimir_nombres_altura(lista)

stark_marvel_app(lista_heroes)
#x= stark_normalizar_datos(lista_heroes)
#print (x)
