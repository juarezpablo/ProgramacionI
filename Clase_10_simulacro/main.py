'''
1)Listar los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)

2)Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (asc) o descendente (desc)

3)Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (asc) o descendente (desc)

4)Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: menor o mayor) se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.

5)Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda.
 6)Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]

Aclaraciones:
Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por consola con RegEx
El set de datos proviene de un json
Realizar las validaciones que crea pertinentes
En todos los casos se deberá trabajar con una copia de la lista original


'''


from func import *
from validar import *


def app_heroes():
    lista_heroes = cargar_json("C:/Users/Pablo/Desktop/ProgramacionI/Clase_10_simulacro/data_stark.json")
    lista_menu=["1)Listar los primeros N héroes.","2)Ordenar y Listar héroes por altura.","3)Ordenar y Listar héroes por fuerza.","4)Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio","5)Buscar héroes por inteligencia [good, average, high]","6)Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]"]
    nueva_lista = lista_heroes[:] 
    while True:
        imprimir_lista(lista_menu)
        respuesta = (input("\nElige una opcion\n"))
        patron = "^[0-6]{1}$"
        respuesta=validar_entero(respuesta,patron)
        print(respuesta)
        if(respuesta == 1):
            print(lista_menu[0])
            n=int(input("Elige la cantidad de heroes a listar\n"))
            
            while(n > len(lista_heroes)):
                n=int(input("Elige la cantidad de heroes a listar\n"))
            nueva_lista = lista_heroes[:n] 
            imprimir_lista_mejorada(nueva_lista)
        
        if(respuesta == 2):
            print(lista_menu[1])
            orden = input("Asc o Desc ?")
            nueva_lista = ordenar_lista_key_max_min(nueva_lista,"altura",orden)
            imprimir_lista_mejorada(nueva_lista,"altura")
        
        if(respuesta == 3):
            print(lista_menu[2])
            orden = input("Asc o Desc ?")
            nueva_lista =ordenar_lista_key_max_min(nueva_lista,"fuerza",orden)
            imprimir_lista_mejorada(nueva_lista,"fuerza")
        if(respuesta == 4):
            print(lista_menu[3])
            key=input("Elige la key numerica a promediar\n")
            promedio = calcular_promedio_key(nueva_lista,key)
            print("Promedio {0}".format(promedio))
            comparador = input("Elegir listar valores que sean 'mayor' o 'menor' al promedio\n")
            nueva_lista = listar_mayor_menor_key(nueva_lista,key,promedio,comparador)
            imprimir_lista_mejorada(nueva_lista,key)
        if(respuesta == 5):
            print(lista_menu[4])
            tipo_inteligencia = input(" Elija que tipo de inteligencia abuscar 'good' 'average''high' ")
            #Sin reg ex nueva_lista = obtener_lista_dato(nueva_lista,"inteligencia",tipo_inteligencia)
            #imprimir_lista_mejorada(nueva_lista,"inteligencia")
            key = "inteligencia"
            nueva_lista = buscar_dato(nueva_lista,tipo_inteligencia,key)
            imprimir_lista_mejorada(nueva_lista,key)
        if (respuesta == 6):
            print(lista_menu[5])
            nombre =   "C:/Users/Pablo/Desktop/ProgramacionI/Clase_10_simulacro/heroes.csv"  
            exportar_csv(nueva_lista,nombre)

app_heroes()    