from data_stark import lista_heroes

#B)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
for heroe in lista_heroes:
    print(heroe["nombre"])

# C)Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
for heroe in lista_heroes:
    print( "{0}  Altura: {1}" .format(heroe["nombre"], heroe["altura"]) )
# D) Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)

diccionario_heroe_mayor_altura = lista_heroes[0]
for heroe in lista_heroes:
    if( float(heroe["altura"]) > float(diccionario_heroe_mayor_altura["altura"])):
        diccionario_heroe_mayor_altura = heroe   
print( " Heroe mas alto es: {0} con una altura de: {1}" .format(diccionario_heroe_mayor_altura["nombre"], diccionario_heroe_mayor_altura["altura"]))

# E)Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

diccionario_heroe_menor_altura = lista_heroes[0]
for heroe in lista_heroes:
    if(float(heroe["altura"]) < float(diccionario_heroe_menor_altura["altura"])):
        diccionario_heroe_menor_altura = heroe
print( " Heroe mas bajo es: {0} con una altura de: {1}" .format(diccionario_heroe_menor_altura["nombre"], diccionario_heroe_menor_altura["altura"]))  

# F)Recorrer la lista y determinar la altura promedio de los  superhéroes 
acumulador_altura = 0
contador_cantidad_heroes = 0
for heroe in lista_heroes:
    acumulador_altura += float(heroe["altura"])
    contador_cantidad_heroes+=1
print("Altura promedio de heroes es {0} centimetros" .format(acumulador_altura/contador_cantidad_heroes))

# H) Calcular e informar cual es el superhéroe más y menos pesado.

diccionario_heroe_mayor_peso = lista_heroes[0]
diccionario_heroe_menor_peso = lista_heroes[0]
for heroe in lista_heroes:
    #print(type(heroe["peso"]))#Es string, debo pasarlo a float
    if(float(heroe["peso"]) > float(diccionario_heroe_mayor_peso["peso"])):
        diccionario_heroe_mayor_peso = heroe
    if(float(heroe["peso"]) < float(diccionario_heroe_menor_peso["peso"])):
        diccionario_heroe_menor_peso = heroe    
print("Heroe mas pesado es: {0} y pesa: {1} kilos \n Heroe menos pesado es:{2} y pesa: {3} kilos" .format(
                                    diccionario_heroe_mayor_peso["nombre"], diccionario_heroe_mayor_peso["peso"],
                                    diccionario_heroe_menor_peso["nombre"], diccionario_heroe_menor_peso["peso"]))

# I)Ordenar el código implementando una función para cada uno de los valores informados. 





