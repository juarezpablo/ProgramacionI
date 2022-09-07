from data_stark import lista_heroes

def imprimir_heroes_masculinos() :
    # A) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    for heroe in lista_heroes:
        if(heroe["genero"] == "M"):
            print(heroe["nombre"])

def imprimir_heroes_femeninos() :
    # B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
    for heroe in lista_heroes:
        if(heroe["genero"] == "F"):
            print(heroe["nombre"])

def imprimir_max_altura_masculino() :
    # C)Recorrer la lista y determinar cuál es el superhéroe más alto de género M 

    dicc_heroe_mayor_altura_masculino = []
    bandera_max_altura_masculino= 0
    for heroe in lista_heroes:
        if(bandera_max_altura_masculino == 0):
            if(heroe["genero"] == "M" ):
                dicc_heroe_mayor_altura_masculino = heroe
                bandera_max_altura_masculino = 1
        if(heroe["genero"] == "M"):
            if(float(heroe["altura"]) > float(dicc_heroe_mayor_altura_masculino["altura"])):
                dicc_heroe_mayor_altura_masculino = heroe
    print("Heroe masculino mas alto es: {0} y mide: {1}" .format(dicc_heroe_mayor_altura_masculino["nombre"],dicc_heroe_mayor_altura_masculino["altura"]))      

def imprimir_max_altura_femenino() :
    # D)Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
    dicc_heroe_mayor_altura_femenino = []
    bandera_max_altura_femenino = 0
    for heroe in lista_heroes:
        if(bandera_max_altura_femenino == 0):
            if(heroe["genero"] == "F"):
                dicc_heroe_mayor_altura_femenino = heroe
                bandera_max_altura_femenino = 1

        if(heroe["genero"] == "F"):
            if(float(heroe["altura"]) > float(dicc_heroe_mayor_altura_femenino["altura"])):
                dicc_heroe_mayor_altura_femenino = heroe
    print("Heroe femenino mas alta es: {0}" .format(dicc_heroe_mayor_altura_femenino["nombre"]))

def imprimir_min_altura_masculino() :
    # E) Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
    dicc_heroe_menor_altura_masculino = []
    bandera_min_altura_masculino = 0
    for heroe in lista_heroes:
        if(bandera_min_altura_masculino == 0):
            if(heroe["genero"] == "M"):
                dicc_heroe_menor_altura_masculino = heroe
                bandera_min_altura_masculino = 1
        if(heroe["genero"] == "M"):        
            if( float(heroe["altura"]) < float(dicc_heroe_menor_altura_masculino["altura"]) ):
                dicc_heroe_menor_altura_masculino = heroe
    print("Heroe masculino mas bajo es: {0}" .format(dicc_heroe_menor_altura_masculino["nombre"]))

def imprimir_min_altura_femenino() :
    # F) Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
    dicc_heroe_menor_altura_femenino = []
    bandera_min_altura_femenino = 0
    for heroe in lista_heroes:
        if(bandera_min_altura_femenino == 0):
            if( heroe["genero"] == "F"):
                dicc_heroe_menor_altura_femenino = heroe
                bandera_min_altura_femenino = 1
        if(heroe["genero"] == "F"):        
            if( (float(heroe["altura"])) < (float(dicc_heroe_menor_altura_femenino["altura"])) ):
                dicc_heroe_menor_altura_femenino = heroe
    print(" Heroe femenina mas baja es: {0}" .format(dicc_heroe_menor_altura_femenino["nombre"]))

def imprimir_promedio_altura_masculinos() :
    #G) Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
    acumulador_altura_masculino = 0
    contador_cantidad_masculino = 0
    for heroe in lista_heroes:
        if(heroe["genero"] == "M"):
            contador_cantidad_masculino += 1
            acumulador_altura_masculino += (float(heroe["altura"]))
    promedio_altura_masculino = acumulador_altura_masculino / contador_cantidad_masculino
    print(" Altura promedio de heroes masculinos es: {0} centimetros" .format(promedio_altura_masculino))

def imprimir_promedio_altura_femenino() :
    # H)Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
    acumulador_altura_femenino = 0
    contador_cantidad_femenino = 0
    for heroe in lista_heroes:
        if(heroe["genero"] == "F"):
            contador_cantidad_femenino += 1
            acumulador_altura_femenino += (float(heroe["altura"]))
    promedio_altura_femenino = acumulador_altura_femenino / contador_cantidad_femenino
    print(" Altura promedio de heroes femeninas es: {0} centimetros" .format(promedio_altura_femenino))

# I)Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
def imprimir_items_anteriores() :
    imprimir_max_altura_masculino()
    imprimir_max_altura_femenino()
    imprimir_min_altura_masculino()
    imprimir_min_altura_femenino()
    imprimir_promedio_altura_masculinos()
    imprimir_promedio_altura_femenino()
    
# J)Determinar cuántos superhéroes tienen cada tipo de color de ojos.
dicc_ojos ={}
for heroe in lista_heroes:
    color_ojos = heroe["color_ojos"]
    if( color_ojos not in dicc_ojos.keys()): #si el color no esta todavia  como una key en el diccionario
        dicc_ojos[color_ojos] = 1              #asigno el color como una key e inicializo su valor en 1
    else:
        dicc_ojos[color_ojos] += 1         #si ya tiene la key asignada  incremento su valor

for color in dicc_ojos:
    print (" Color de ojos: {0}  Cantidad  de heroes: {1}" .format(color,dicc_ojos[color]))

# K)Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    #tip:selecciono la variable y apreto f2, puedo hacer un cambio global en la variable.
lista_color_pelo = []
for heroe in lista_heroes:
    lista_color_pelo.append(heroe["color_pelo"])
  
lista_color_pelo = set(lista_color_pelo)
lista_color_pelo = list(lista_color_pelo)    


for color_pelo in lista_color_pelo:
    contador_color_pelo = 0
    for heroe in lista_heroes:
        if(heroe["color_pelo"] == color_pelo):
            contador_color_pelo += 1
    print("color de pelo: {0}  cantidad de heroes: {1}" .format(color_pelo,contador_color_pelo))


# L)Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 

dicc_inteligencia = {}
for heroe in lista_heroes:
    inteligencia = heroe["inteligencia"]
    if( inteligencia == ""):
        inteligencia = "No tiene"
    if(inteligencia not in dicc_inteligencia.keys()):
        dicc_inteligencia[inteligencia] = 1
    else:
        dicc_inteligencia[inteligencia]+= 1
 
print(dicc_inteligencia)
for inteligencia in dicc_inteligencia:
    print("Tipo de inteligencia: {0}  Cantidad de heroes: {1}" .format(inteligencia,dicc_inteligencia[inteligencia]))

# M)Listar todos los superhéroes agrupados por color de ojos.

dicc_color_ojos_heroes ={}
for heroe in lista_heroes:
    color_ojo2 = heroe["color_ojos"]
    if(color_ojo2 not in dicc_color_ojos_heroes.keys()):
        dicc_color_ojos_heroes[color_ojo2] = []
print(dicc_color_ojos_heroes) 

for color_ojo2 in dicc_color_ojos_heroes:
    for heroe in lista_heroes:
        if (color_ojo2 == heroe["color_ojos"]):
            dicc_color_ojos_heroes[color_ojo2].append(heroe["nombre"])
           
print(dicc_color_ojos_heroes)

# N)Listar todos los superhéroes agrupados por color de pelo.

dicc_color_pelos_heroes = {}

