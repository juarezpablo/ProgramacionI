import json
import re

def cargar_json(direccion:str)->list:
    '''
    Obtiene una lista a partir de un archivo json

    Recibe el path donde se encuentra el archivo json

    Devuelve una lista basada en el archivo json
    '''
    with open(direccion,"r",encoding="utf8") as archivo:
        lista = json.load(archivo)
        return lista["pokemones"]

def imprimir_lista_menu(lista:list):
    '''
    Imprime una lista en formato menu

    Recibe el menu en forma de lista

    '''
    for item in lista:
        print("{0}\n".format(item))

def imprimir_pokemones(lista:list,key:str="poder") :
    '''
    Imprime una lista de pokemones y su key ingresada,por defecto"poder"

    Recibe una lista de pokemones y la key a imprimir


    '''
    
    for pokemon in lista:
        mensaje = " ID: {0} || Nombre: {1} || {2} : {3}\n".format(pokemon["id"],pokemon["nombre"],key.capitalize(),pokemon[key])
        print(mensaje)


def buscar_minimo_maximo(lista:list,orden:str,key:str) ->int:
    '''
    Busca el valor minimo de una key y su posicion en una lista

    Recibe una lista, el tipo de orden"asc o desc" y su key

    Devuelve el valor de la posicion del numero minimo en la lista
    '''
    i_minimo_maximo=0
    for i in range (len(lista)):
        if( (lista[i][key] > lista[i_minimo_maximo][key] and orden == "desc") or (lista[i][key] < lista[i_minimo_maximo][key] and orden == "asc") ):
            i_minimo_maximo = i
    return i_minimo_maximo           

def ordenar_lista(lista:list,orden:str="desc",key:str="poder") ->list:
    '''
    Ordena una lista de forma asc o desc

    Recibe una lista y su estilo de orden deseado

    Devuelve una lista ordenada de manera asc o desc
    '''
    lista_a_ordenar=lista[:]
    lista_ordenada=[]
    largo=len(lista_a_ordenar)
    while ( len(lista_a_ordenar) >0 ):
        i_minimo_maximo = buscar_minimo_maximo(lista_a_ordenar,orden,key)
        lista_ordenada.append(lista_a_ordenar.pop(i_minimo_maximo))
    return lista_ordenada
    
def listar_por_tipo(lista:list)->list:
    '''
    Crea una lista de tipos de pokemones

    Recibe una lista

    Devuelve una lista con todos los tipos de pokemones
    '''        
    lista_de_tipos=[]
    lista_nueva=[]
    for pokemon in lista:
        lista_de_tipos.append(pokemon["tipo"])
        for item in pokemon["tipo"]:
            lista_nueva.append(item)
    
    lista_nueva=set(lista_nueva)
    lista_nueva=list(lista_nueva)
    return(lista_nueva)

def buscar_por_tipo(lista:list,clave:str) ->list:
    '''
    Busca pokemones por tipo de acuerdo a la clave ingresada

    REcibe una lista y el tipo de pokemon a buscar  

    Devuelve todos los pokemones que coinicidan con la busqueda
    '''
    lista_a_devolver=[]
    for pokemon in lista:
        for tipo in pokemon["tipo"]:
            if(re.search(clave,tipo,re.IGNORECASE)):
                lista_a_devolver.append(pokemon)
    return lista_a_devolver