heroes_para_reclutar = [
    "Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"
]
 
heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}

for heroe in heroes_para_reclutar :
    
    #iterar cada heroe y verificar que exista en el dic
    if heroe in heroes_info.keys():
        info_heroe = heroes_info[heroe]

        id = info_heroe["ID"]
        origen = info_heroe["Origen"]
        identidad = info_heroe['Identidad']
        #habilidad es una lista, 
        #habilidad_str = "agilidad fuerza etc"
        habilidades_lista = info_heroe["Habilidades"]
        
        #eliminar duplicados
        #paso la lista a set para borrar duplicados
        habilidades_unicas = set(habilidades_lista)
        #paso el set a lista
        habilidades_lista = list(habilidades_unicas)

        for habilidad in habilidades_lista:
            #mensaje += "{0}".format(habilidad)
            habilidades_mensaje = " | ".join(habilidades_lista)

        print( "ID:", id ,", Codename: ",heroe )
        print("Identidad: ",identidad,", Origen: ",origen)
        print("Habilidades: ",habilidades_mensaje)
        print("------------------------")