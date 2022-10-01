
import json
import re




def  imprimir_lista(lista:list):
    '''
    Imprime una lista

    Recibe una lista

    No devuelve nada
    '''
    for elemento in lista:
        print("\n{0}\n".format(elemento))

def imprimir_lista_mejorada(lista:list,key:str = "peso"):
    '''
    Imprime una lista y su key ingresada

    Recibe una lista de personajes y una key a mostrar


    '''
    for heroe in lista:
        print("Nombre: {0} -- Identidad: {1} -- {2}: {3}\n".format(heroe["nombre"],heroe["identidad"],key,heroe[key]))


def cargar_json(direccion:str)->list:
    '''
    Abre un archivo json y vuelca su contenido en una lista

    Recibe la ubicacion del archivo

    Devuelve una lista
    '''        
    with open(direccion,"r",encoding="utf8") as archivo:
        diccionario = json.load(archivo)
        return diccionario["heroes"]


def buscar_minimo_maximo_key(lista:list,key:str,orden:str)->int:
    '''
    busca una sola posicion del valor minimo de la key ingresada

    Recibe una lista y la key del valor a buscar minimo

    devuelve un numero entero correspondiente a la posicion del valor minimo
    '''    
    i_minimo_maximo = 0
    for i in range (len(lista)):
        if ( (orden == "asc" and lista[i][key]< lista[i_minimo_maximo][key]) or (orden == "desc" and lista[i][key]> lista[i_minimo_maximo][key]) ):
            i_minimo_maximo = i

    return i_minimo_maximo        

def ordenar_lista_key_max_min(lista:list,key:str,orden:str)->list:
    '''
    ordenar una lista de acuerdo a la key ingresada

    recibe una lista y su respectiva key a ordenar

    devuelve la lista ordenada
    '''    
    lista_a_ordenar=lista[:]
    lista_ordenada =[]
    
    
    while (len(lista_a_ordenar) > 0 ):
        i_min_max = buscar_minimo_maximo_key(lista_a_ordenar,key,orden)
        lista_ordenada.append(lista_a_ordenar.pop(i_min_max))
       
    return lista_ordenada

def calcular_promedio_key(lista:list,key:str) ->int:
    '''
    Calcula el promedio de la key ingresada

    Recibe una lista y la key a calcular el promedio

    Devuelve el valor del promedio de la key ingresada
    '''
    contador = 0
    acumulador_key = 0
    for item in lista:
        if ( key in item.keys() ):
            acumulador_key = acumulador_key + item[key]
            contador+=1

    promedio = acumulador_key/contador
    return promedio

def listar_mayor_menor_key(lista:list,key:str,valor:int,comparador:str)->list:
    '''
    Crea una lista con los valores que sean mayores o menores de las keys con respecto a el valor ingresado

    REcibe una lista, el valor y la key a comparar

    Devuevlve una lista con los valores mayores o menores respecto del valor ingresado
    '''
    lista_a_devolver =[]
    for item in lista:
        if((item[key] > valor and comparador == "mayor")or( item[key]<valor and comparador == "menor") ):
            lista_a_devolver.append(item)
    return lista_a_devolver

def obtener_lista_dato(lista:list, key:str,valor:str)->list:
    '''
    Crea una lista con los diccionarios que concuerden con la key y su valor ingresados

    Recibe una lista, la key y su valor a filtrar

    Devuelve una lista filltrada de acuerdo a los parametros ingresados
    '''   
    lista_a_devolver =[]
    for item in lista:
        if(item[key] == valor):
            lista_a_devolver.append(item)
    return lista_a_devolver

def buscar_dato(lista:list, dato:str,key) ->list:
    '''
    Buscar el dato ingresado en una lista

    Recibe la lista a iterar y el dato a buscar

    Devuelve una lista de los heroes que coincidan con el dato
    '''  
    lista_a_devolver = []      
    for item in lista:
      
        if( re.search(dato,item[key],re.IGNORECASE)  ):
            lista_a_devolver.append(item)
    if(lista_a_devolver ):
        return lista_a_devolver 
    else:
        return -1       

def exportar_csv(lista:list,nombre:str):
    '''
    Crea un archivo csv de la lista recibida

    Recibe una lista y la direccion donde se guarda el csv
    '''
    '''
    

    mensaje =""
    for item in lista:
        for key in item:
            mensaje = mensaje + "{0},".format(item[key])
            
        mensaje=mensaje+"\n"
    print(mensaje)
    x = re.findall("^[a-z]",mensaje)
    '''
    
    with open(nombre,"w") as archivo:
        mensaje =""
        for item in lista:
            for key in item:
                mensaje = mensaje + "{0},".format(item[key])
            
            mensaje=mensaje+"\n"

        archivo.write(mensaje)
           
