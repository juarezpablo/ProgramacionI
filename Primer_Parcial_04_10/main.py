'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''







import funciones

SALIDA = "C:/Users/Pablo/Desktop/ProgramacionI/Primer_Parcial_04_10/personajes.csv"

def starwars_app():
    lista_personajes = funciones.cargar_json("C:/Users/Pablo/Desktop/ProgramacionI/Primer_Parcial_04_10/data.json")
    lista_personajes=funciones.parsear_peso_altura(lista_personajes)
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            print("1 - Listar los personajes ordenados por altura\n")
            lista_nueva=funciones.ordenar_key(lista_personajes,"height")
            funciones.imprimir_personajes(lista_nueva)
        elif(respuesta=="2"):
            print("2 - Mostrar el personaje mas alto de cada genero\n")
            personaje_masc_alto=funciones.listar_maximo_genero(lista_personajes,"male")
            personaje_fem_alto=funciones.listar_maximo_genero(lista_personajes,"female")
            personaje_robot_alto=funciones.listar_maximo_genero(lista_personajes,"n/a")
            funciones.imprimir_personajes(personaje_masc_alto)
            funciones.imprimir_personajes(personaje_fem_alto)
            funciones.imprimir_personajes(personaje_robot_alto)
        elif(respuesta=="3"):
            print("3 - Ordenar los personajes por peso\n")
            lista_nueva=funciones.ordenar_key(lista_personajes,"mass")
            funciones.imprimir_personajes(lista_nueva,"mass")
        elif(respuesta=="4"):
            print("4 - Armar un buscador de personajes\n")
            clave=input("\n Ingrese el nombre a buscar:  ")
            funciones.buscador_personajes(lista_personajes,clave)
        elif(respuesta=="5"):
            print("5 - Exportar lista personajes a CSV\n")
            funciones.exportar_csv(SALIDA,lista_personajes)
        elif(respuesta=="6"):
            break


starwars_app()

