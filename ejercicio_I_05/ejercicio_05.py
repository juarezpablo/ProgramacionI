habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]

lista_2 = []
for item in habilidades:
    habilidad = item["Nombre"]
    numero = item["Poder"]
    
   
    tupla=tuple([habilidad , numero])
    lista_2.append (tupla)

    print(item)  
    #prueba
print("-----------")    
print(lista_2)