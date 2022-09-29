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
def cantidad_tipos_ojos():
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
def cantidad_tipo_pelo():
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
def cantidad_tipo_inteligencia():
    dicc_inteligencia = {}
    for heroe in lista_heroes:
        inteligencia = heroe["inteligencia"]
        if( inteligencia == ""):
            inteligencia = "No tiene"
        if(inteligencia not in dicc_inteligencia.keys()):
            dicc_inteligencia[inteligencia] = 1
        else:
            dicc_inteligencia[inteligencia]+= 1
    
    
    for inteligencia in dicc_inteligencia:
        print("Tipo de inteligencia: {0}  Cantidad de heroes: {1}" .format(inteligencia,dicc_inteligencia[inteligencia]))

# M)Listar todos los superhéroes agrupados por color de ojos.
def lista_ojos_heroes():
    dicc_color_ojos_heroes ={}
    for heroe in lista_heroes:
        color_ojo2 = heroe["color_ojos"]
        if(color_ojo2 not in dicc_color_ojos_heroes.keys()):
            dicc_color_ojos_heroes[color_ojo2] = []


    for color_ojo2 in dicc_color_ojos_heroes:
        for heroe in lista_heroes:
            if (color_ojo2 == heroe["color_ojos"]):
                dicc_color_ojos_heroes[color_ojo2].append(heroe["nombre"])
            
        #ya tengo el dicc con sus respectivos key de colores y listas de heroes
        #imprimo el diccionario 
    for item in dicc_color_ojos_heroes:
        print("Color de ojo: {0} ----  Heroes: {1} \n".format(item,dicc_color_ojos_heroes[item]))

# N)Listar todos los superhéroes agrupados por color de pelo.
def lista_pelo_heroes():
    dicc_color_pelos_heroes = {}
    for heroe in lista_heroes:
        color_pelo2 = heroe["color_pelo"]
        if(color_pelo2 not in dicc_color_pelos_heroes.keys()):
            dicc_color_pelos_heroes[color_pelo2]=[]
        #ya obtuve el dicc con sus key de colores de pelos, ahora ingreso los heroes en cada lista que es un valor de key del dicc
        # de la sig forma
    for color_pelo2 in dicc_color_pelos_heroes:
        for heroe in lista_heroes:
            if(color_pelo2 == heroe["color_pelo"]):
                dicc_color_pelos_heroes[color_pelo2].append(heroe["nombre"])

        #imprimo cada key del dicc con su respectiva lista
        #para ello utilizo un for
        #de la manera usual for recorre solo las keys del dicc. por eso para obtener el valor de cada key,debo nombrar el dicc con su key en print
        #sino podria usar  for item in dicc.items(): (de esa forma recorro cada item del dicc)
    for color_pelo2 in dicc_color_pelos_heroes:
        print("Color de pelo: {0} ----- Heroes: {1}\n".format(color_pelo2,dicc_color_pelos_heroes[color_pelo2]))

# O) Listar todos los superhéroes agrupados por tipo de inteligencia
def lista_inteligencia_heroes():
    dicc_inteligencia2 = {}
    for heroe in lista_heroes:
        inteligencia = heroe["inteligencia"]
        if( inteligencia == ""):
            inteligencia = "No tiene"
        if(inteligencia not in dicc_inteligencia2.keys()):
            dicc_inteligencia2[inteligencia]=[heroe["nombre"]]
        else:
            dicc_inteligencia2[inteligencia].append(heroe["nombre"])
    for inteligencia in dicc_inteligencia2:
        print("Tipo de inteligencia: {0} ---- Heroes: {1}\n".format(inteligencia, dicc_inteligencia2[inteligencia]) )   

def menu():
    respuesta = -1
    while(True):
        mensaje_1= "    Menu Heroes \n A)Nombre de cada heroe masculino\n B)Nombre de cada heroe femenino\n"
        mensaje_2=" C)Heroe masculino mas alto\n D)Heroe femenino mas alto\n E)Heroe masculino mas bajo\n"
        mensaje_3=" F)Heroe femenino mas bajo\n G)Altura promedio de heroes masculinos\n H)Altura promedio heroes femeninos\n"
        mensaje_4=" I)Indicadores anteriores J)Cantidad de heroes con cada tipo de color de ojos\n"
        mensaje_5=" K)Cantidad de heroes con cada tipo de color de pelo \n L)Cantidad de heroes con cada tipo de inteligencia\n"
        mensaje_6=" M)Lista de heroes agrupados por color de ojos\n N)Lista de heroes agrupados por color de pelo\n O)Lista de heroes agrupados por tipo de inteligencia\n"
        mensaje_menu = mensaje_1+mensaje_2+mensaje_3+mensaje_4+mensaje_5+mensaje_6
        respuesta = input(mensaje_menu)
        if(respuesta == "A"):
            imprimir_heroes_masculinos()
        elif(respuesta == "B"):
            imprimir_heroes_femeninos()
        elif(respuesta == "C"): 
            imprimir_max_altura_masculino()       
        elif(respuesta == "D"):    
            imprimir_max_altura_femenino()
        elif(respuesta == "E"):
            imprimir_min_altura_masculino()
        elif(respuesta == "F"):
            imprimir_min_altura_femenino()
        elif(respuesta == "G"):
            imprimir_promedio_altura_masculinos()
        elif(respuesta == "H"):  
            imprimir_promedio_altura_femenino()
        elif(respuesta == "I"):
            imprimir_items_anteriores()
        elif(respuesta == "J"):
            cantidad_tipos_ojos()
        elif(respuesta == "K"):
            cantidad_tipo_pelo()
        elif(respuesta == "L"):
            cantidad_tipo_inteligencia()
        elif(respuesta == "M"):
            lista_ojos_heroes()
        elif(respuesta == "N"):
            lista_pelo_heroes()
        elif(respuesta == "O"):   
            lista_inteligencia_heroes()                                   
        elif(respuesta == 0):
            break
               
menu()               