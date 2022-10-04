'''
1)Listar los últimos N pokemones. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)


2)Ordenar y Listar pokemones por poder. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)


3)Ordenar y Listar pokemones por ID. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)


4)Calcular la cantidad promedio de las key tipo lista (evoluciones, fortaleza, debilidad, tipo), filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con tener mayores o menores cantidades en la lista de dicha key según corresponda.


 5)Buscar pokemones por tipo (dar e elegir los diversos tipos que un pokémon puede poseer, muchos de ellos poseen más de un tipo, con lo cual habrá que darle a elegir al usuario entre todos los tipos que existen en el json) una vez seleccionado listar en consola los que posean dicho tipo. (Usando RegEx para la búsqueda).
Ejemplo: Si el usuario elige: volador y hay un pokemon con muchos tipos, pero uno de ellos es volador, deberá listarlo. (charizard, zapdos, moltres, articuno poseen más de un tipo, pero uno de ellos es volador).


 6)Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente [1-4]



Aclaraciones:
Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por consola con RegEx
El set de datos proviene de un json
Realizar las validaciones que crea pertinentes
En todos los casos se deberá trabajar con una copia de la lista original

'''

from func import *
from validar import *

INPUT ="C:/Users/Pablo/Desktop/ProgramacionI/practica_preparcial_pokemon/pokedex.json"

def app_pokedex():
    lista_pokemon_original=cargar_json(INPUT)    
    lista_pokemon = lista_pokemon_original[:]
    lista_menu=["1)Listar los últimos N pokemones.",
                "2)Ordenar y Listar pokemones por poder. ",
                "3)Ordenar y Listar pokemones por ID.",
                "4)Calcular la cantidad promedio de las key tipo lista (evoluciones, fortaleza, debilidad, tipo) ",
                "5)Buscar pokemones por tipo ",
                "6)Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente (1-4)"
                ]
    while True :
        imprimir_lista_menu(lista_menu)
        patron =  "^[0-6]{1}$"
        respuesta = input("Elija una opcion\n>>")
        respuesta = validar_entero(respuesta,patron)

        if (respuesta == 1):
            print(lista_menu[0])
            cantidad = input(">>>Elija la cantidad de ultimos pokemones de la lista a ver\n")
           
            cantidad = int(cantidad)
            comienzo_de_listeo = len(lista_pokemon) - cantidad
            if (comienzo_de_listeo <0):
                comienzo_de_listeo = 0
            lista_pokemon=lista_pokemon[comienzo_de_listeo:]    
            imprimir_pokemones(lista_pokemon)
        if(respuesta == 2):
            print(lista_menu[1])
            orden = input(" >>>Lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’) ?\n")
            lista_pokemon=ordenar_lista(lista_pokemon,orden,"poder")
            imprimir_pokemones(lista_pokemon,"poder")

        if(respuesta == 3):
            print(lista_menu[2])
            orden = input(" >>>Lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’) ?\n")      
            lista_pokemon = ordenar_lista(lista_pokemon,orden,"id") 
            imprimir_pokemones(lista_pokemon,"id")
        if(respuesta == 4):
            pass
        if(respuesta ==5):
            print(lista_menu[4])

            imprimir_lista_menu(listar_por_tipo(lista_pokemon))
            clave=input("Elija el tipo de pokemon a buscar:  ")
            lista_pokemon=buscar_por_tipo(lista_pokemon,clave)
            imprimir_pokemones(lista_pokemon,"tipo")


app_pokedex()