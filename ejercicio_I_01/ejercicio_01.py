#Alumno: Juarez Juan Pablo
#Comision 00
#Division: 1H
# EJERCICIO 01

#La división de higiene está trabajando en un control de stock para productos sanitarios. 
# Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, 
# de cada una debe obtener los siguientes datos:
#-El tipo (validar "barbijo", "jabón" o "alcohol")
#-El precio: (validar entre 100 y 300)
#-La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#-La marca y el Fabricante.
  
 #Se debe informar lo siguiente:
#1-Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#2-Del ítem con más unidades, el fabricante.
#3-Cuántas unidades de jabones hay en total.

cantidad_productos = 5
precio_barbijo_mas_caro = 0 
cantidad_barbijo_mas_caro = 0
mayor_cantidad_unidades = 0
cantidad_jabones_total = 0
for contador in range(cantidad_productos):
    #Ingreso de datos
    tipo_producto = input("Ingrese tipo de producto 'barbijo', 'jabon' o 'alcohol': ")
    while(tipo_producto!="barbijo" and tipo_producto!="jabon" and tipo_producto!="alcohol"):
        tipo_producto = input("ERROR -Ingrese tipo de producto 'barbijo', 'jabon' o 'alcohol': ")
    
    while(True):
        precio_producto = int(input("Ingrese precio 'Entre 100 y 300': "))
        if(precio_producto>=100 and precio_producto<=300):
            break
    
    cantidad_unidades = int(input("Ingrese cantidad de unidades 'No debe superar 1000': ")) 
    while(cantidad_unidades<=0 or cantidad_unidades>1000):
        cantidad_unidades = int(input("Ingrese cantidad de unidades 'No debe superar 1000': ")) 

    marca_producto = input("Ingrese la marca del producto: ")
    fabricante_producto = input("Ingrese fabricante del producto: ")
    #1-Del más caro de los barbijos, la cantidad de unidades y el fabricante.
    if(tipo_producto == "barbijo"):
        if(precio_producto>precio_barbijo_mas_caro):
            precio_barbijo_mas_caro = precio_producto
            fabricante_barbijo_mas_caro = fabricante_producto
            cantidad_barbijo_mas_caro = cantidad_unidades
    #2-Del ítem con más unidades, el fabricante.
    if(cantidad_unidades>mayor_cantidad_unidades):
        mayor_cantidad_unidades = cantidad_unidades
        fabricante_mayor_cantidad_unidades = fabricante_producto
        tipo_producto_mayor_cantidad_unidades = tipo_producto
    #3-Cuántas unidades de jabones hay en total.   
    if(tipo_producto == "jabon"):
        cantidad_jabones_total += cantidad_unidades 

print("El mas caro de los barbijo tiene una cantidad de: ",cantidad_barbijo_mas_caro," y su fabricante es: ",fabricante_barbijo_mas_caro)
print("El fabricante del item con mas unidades es: ",fabricante_mayor_cantidad_unidades," y tiene ",mayor_cantidad_unidades," unidades")
print("Cantidad de jabones en total: ",cantidad_jabones_total)