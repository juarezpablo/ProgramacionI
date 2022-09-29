import json


def mostrar_lista(lista:list):
    '''
    Imprime una lista por pantalla

    Recibe una lista

    No devuelve nada
    '''
    for elemento in lista:
        print(elemento)

def mostrar_lista_mejorada(lista:list)->list:
    for elemento in lista:
        print("{0}\nviews: {1}\nlength {2}\n-----".format(elemento["title"],elemento["views"], elemento["length"]))

def cargar_json(direccion:str)->list:

    '''
    Obtiene una lista de un archivo json

    Recibe el path del archivo json deseado

    devuelve una lista
    '''

    with open(direccion,"r",encoding="utf8") as archivo:
        diccionario = json.load(archivo)
        
        return diccionario["paulina"]
def buscar_minimo(lista:list,key:str)->int:
    '''
    busca el valor minimo de una key de una lista 

    recibe una lista y una key 

    devuelve la posicion donde se encuentra el valor minimo en la lista
    '''
    i_minimo = 0
    for i in range (len(lista)):
        if (lista[i][key] < lista[i_minimo][key]):
            i_minimo = i

    return i_minimo        

def ordenar_videos(lista:list,key:str) ->list:
    '''
    Ordena una lista de acuerdo al parametro key ingresado

    recibe una lista y una key

    devuelve una lista ordenada
    '''
    
    lista_a_ordenar = lista[:]
    
    lista_ordenada=[]
    
    
    while(len(lista_a_ordenar)>0):
        x=buscar_minimo(lista_a_ordenar,key)
        lista_ordenada.append(lista_a_ordenar.pop(x))
    return lista_ordenada


#lista_videos = cargar_json("C:/Users/Pablo/Desktop/ProgramacionI/repaso_paulina/data_paulina_reduce.json")
#mostrar_lista_mejorada(lista_videos)
#ordenar_videos(lista_videos,"views")