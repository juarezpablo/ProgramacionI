'''
1 - Listar TOP N videos
2 - Ordenar videos por duracion (UP/DOWN)
3 - Ordenar videos por cantidad de views (UP/DOWN)
4 - Buscar videos por título 
5 - Exportar lista de videos a CSV

'''
from func import *





def app_paulina():
    lista_menu=["\n1 - Listar TOP N videos","2 - Ordenar videos por duracion (UP/DOWN)","3 - Ordenar videos por cantidad de views (UP/DOWN)","4 - Buscar videos por título ","5 - Exportar lista de videos a CSV\n"]
    lista_videos = cargar_json("C:/Users/Pablo/Desktop/ProgramacionI/repaso_paulina/data_paulina_reduce.json")
    mostrar_lista(lista_videos)
    while True:
        mostrar_lista(lista_menu)
        respuesta = int(input("Ingrese una opcion\n"))
        if(respuesta == 1):
            print(lista_menu[0])
            

        elif(respuesta == 2):
            print(lista_menu[1])
            
            mostrar_lista_mejorada(ordenar_videos(lista_videos,"length"))
        elif(respuesta == 3):
            print(lista_menu[2])
            mostrar_lista_mejorada(ordenar_videos(lista_videos,"views"))
        elif(respuesta == 4):
            print(lista_menu[3])
        elif(respuesta == 5):
           print(lista_menu[4])

app_paulina()


