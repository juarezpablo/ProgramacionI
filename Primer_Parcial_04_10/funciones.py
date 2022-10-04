import json
import re
def cargar_json(direccion:str)->list:
    '''
    Abre un archivo json y lo carga en una lista

    Recibe la direccion del archivo a cargar

    devuelve una lista
    '''
    with open(direccion,"r",encoding="utf8") as archivo:
        diccionario = json.load(archivo)
        return (diccionario["results"])


def parsear_peso_altura(lista:list)->list:
    '''
    Convierte las keys peso y altura en enteros

    REcibe una lista

    Devuelve una lista
    '''        
    for item in lista:
        item["height"]=int(item["height"])
        item["mass"]=int(item["mass"])
    return lista        

def buscar_maximo_key(lista:list,key:str)->int :
    '''
    Encuentra la posicion del elemento con valor maximo de la key

    REcibe una lista y la key a buscar el valor maximo

    Devuelve la posicion en la lista del valor maximo
    '''
    i_maximo=0
    largo=len(lista)
    for i in range (largo):
        if(lista[i][key] > lista[i_maximo][key]):
            i_maximo = i
    return i_maximo        



def ordenar_key(lista:list,key:str) ->list:
    '''
    Ordenar una lista de forma descendente de acuerdo a la key ingresada

    Recibe una lista y la key a ordenar

    Devuelve una lista ordenada de forma descendente
    '''    
    lista_a_ordenar=lista[:]
    lista_ordenada=[]
    while ( len(lista_a_ordenar)>0 ):
        i_maximo = buscar_maximo_key(lista_a_ordenar,key)
        lista_ordenada.append(lista_a_ordenar.pop(i_maximo))
    return lista_ordenada 

def imprimir_personajes(lista:list,key:str="height"):
    '''
    imprime una lista o un dicciconario de personajes

    REcibe una lista o un diccionario y la key a imprimir
    '''
    
    
    if type(lista)==dict:
        print( "Nombre :{0} | Altura:{1} | Genero: {2}".format(lista["name"],lista["height"],lista["gender"]))
    else:
        for item in lista:
            
            print(" Nombre: {0}  | {1} : {2}  ".format(item["name"],key.capitalize(),item[key]))

def listar_maximo_genero(lista:list,genero:str)->dict:
    '''
    Busca la altura maxima de un personaje de acuerdo al genero ingresado por parametro

    Recibe una lista y el genero a buscar la altura maxima

    Devuelve el personaje en formato diccionario con la altura maxima de acuerdo al genero ingresado
    '''

    personaje_mas_alto={}
    altura_maxima =0
    for item in lista:
        if( item["gender"]== genero and item["height"] > altura_maxima ):
            altura_maxima = item["height"]
            personaje_mas_alto = item
    return personaje_mas_alto


def exportar_csv(direccion:str,lista:list):
    '''
    Exporta una lista a un archivo csv

    REcibe una lista y la direccion a guardar 
    '''
    with open(direccion,"w",encoding="utf8") as archivo:
         for item in lista:
            archivo.write("{0},{1},{2},{3}\n".format(item["name"],item["height"],item["mass"],item["gender"]))
        
def buscador_personajes(lista:list,name:str) :
    '''
    Busca nombre de personajes de acuerdo a la palabra ingresada

    REcibe una lista y el nombre a buscar

    Devuelve el personaje encontrado 
    '''

    for item in lista:
    
        if re.search(name,item["name"],re.IGNORECASE) :
            imprimir_personajes(item)
        