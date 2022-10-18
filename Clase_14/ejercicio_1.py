lista_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100  
    }

}

# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el 
# producto mostrar el mensaje 'el articulo no se encuentra en la lista'


# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)


# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios


# Punto 4: imprimir el listado de frutas (solo su nombre)


# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'

 
def app_frutas():
    while True:
        
        respuesta = int(input("1-Ingresar un producto nuevo \n 2-Imprimir listado de frutas \n 3-Eliminar fruta \n 4-Buscar un producto \n"))
        if respuesta == 4:
            fruta = input("Buscar un producto\n")
            #print(lista_precios.get(fruta,"El articulo no se encuentra en la lista"))
            if fruta in lista_precios.keys():
                print(" Precio: {0} Stock: {1}".format(lista_precios[fruta]["precio"],lista_precios[fruta]["stock"]))
                cantidad = int(input("Ingrese la cantidad\n"))
                print("Precio total: {0}".format((lista_precios[fruta]["precio"]*cantidad)))
            else:
                print("El articulo no se encuentra en la lista")



        if respuesta == 1 :
            nueva_fruta=input("Ingrese el nombre de la nueva fruta: ")
            nueva_fruta_precio=int(input("Ingrese el precio: "))
            nueva_fruta_unidad_medida=input("Unidad de Medida: ")
            nueva_fruta_stock = int(input("Stock: "))
            nuevo_dict={}
            nuevo_dict[nueva_fruta]={}
            nuevo_dict[nueva_fruta]["precio"]=nueva_fruta_precio
            nuevo_dict[nueva_fruta]["unidad_medida"]=nueva_fruta_unidad_medida
            nuevo_dict[nueva_fruta]["stock"]=nueva_fruta_stock
            
            lista_precios.update(nuevo_dict)
            print(lista_precios)
        if respuesta ==2 :
            lista_nombres_frutas = list(lista_precios.keys())
            
            x=list(map(lambda i: print(i) ,lista_nombres_frutas))
        if respuesta==3 :
            fruta_a_eliminar = input("Ingrese la fruta a eliminar: \n")
            dict_fruta_eliminada =lista_precios.pop(fruta_a_eliminar,"error")
            if type(dict_fruta_eliminada) == str :
                print("el articulo no se encuentra en la lista")       

            
app_frutas()