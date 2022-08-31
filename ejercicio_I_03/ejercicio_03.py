#Alumno: Juan Pablo Juarez
#Comision: 00
#EJERCICIO 3
#La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar datos de heroínas y héroes, 
# para para tener un control de las condiciones de heroes existentes, nos solicitan:
#1-Nombre de Heroína/Héroe
#2-EDAD (mayores a 18 años)
#3-Sexo ("m", "f" o "nb")
#4-Habilidad ("fuerza", "magia", "inteligencia").
#A su vez, el programa deberá mostrar por consola lo siguiente:
#A)Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
#B)El sexo y nombre de Heroe | Heroína de mayor edad.
#C)La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
#D)El promedio de edad entre Heroinas.
#E)El promedio de edad entre Heroes de fuerza.

menor_edad_heroe_fuerza = 1000
mayor_edad_heroes = 0
contador_heroinas_fuerza_magia = 0
acumulador_edad_heroes_sexo_f = 0
contador_heroes_sexo_f = 0
contador_heroes_fuerza_sexo_m = 0
acumulador_edad_heroes_fuerza_sexo_m = 0

while(True):
    nombre = input("Ingrese nombre de Heroina/Heroe:  ")
    while(nombre == ""):
        nombre = input("Ingrese nombre de Heroina/Heroe:  ")
    while(True):   
        edad = input("Ingrese edad (mayor de 18)  ")
        if(edad.isnumeric() == True ):
            edad = int(edad)
            if(edad>=18):
                break
    sexo = input("Ingrese sexo 'f' , 'm' o 'nb' ")
    while(sexo != "f" and sexo != "m" and sexo != "nb" ):
         sexo = input("Ingrese sexo 'f' , 'm' o 'nb' ")
    habilidad = input("Ingrese habilidad 'fuerza', 'magia' o 'inteligencia'  ")
    while(habilidad != "fuerza" and habilidad != "inteligencia" and habilidad != "magia"):
        habilidad = input("Ingrese habilidad 'fuerza', 'magia' o 'inteligencia'  ")

    #A)Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
    if(habilidad == "fuerza"):
        if(edad<menor_edad_heroe_fuerza):
            menor_edad_heroe_fuerza = edad
            nombre_menor_edad_heroe_fuerza = nombre
        #E)El promedio de edad entre Heroes de fuerza.  
        if(sexo == "m"):
            contador_heroes_fuerza_sexo_m += 1
            acumulador_edad_heroes_fuerza_sexo_m += edad
    #B)El sexo y nombre de Heroe | Heroína de mayor edad.
    if(edad>mayor_edad_heroes):
        mayor_edad_heroes = edad
        sexo_mayor_edad_heroes = sexo
        nombre_mayor_edad_heroes = nombre
    #C)La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
    if(sexo == "f"):
        if(habilidad == "fuerza" or habilidad == "magia"):
            contador_heroinas_fuerza_magia += 1
        #D)El promedio de edad entre Heroinas.
        acumulador_edad_heroes_sexo_f += edad
        contador_heroes_sexo_f += 1
    
    respuesta = input("Desea salir? S/N ")
    if(respuesta == "S" or respuesta == "s"):
        break

promedio_edad_heroes_sexo_f = acumulador_edad_heroes_sexo_f / contador_heroes_sexo_f
promedio_edad_masculinos_fuerza = acumulador_edad_heroes_fuerza_sexo_m / contador_heroes_fuerza_sexo_m
if(sexo_mayor_edad_heroes == "m"):
    sexo_mayor_edad_heroes = "Masculino"
elif(sexo_mayor_edad_heroes == "f"):
    sexo_mayor_edad_heroes == "Femenino"
else:
    sexo_mayor_edad_heroes == "No binario"   

print("A) Elnombre de Héroe | Heroína de 'fuerza' más joven es:  ",nombre_menor_edad_heroe_fuerza, 
                                " con ",menor_edad_heroe_fuerza," años")
print("B) El sexo y nombre de Heroe | Heroína de mayor edad. es: ",sexo_mayor_edad_heroes," ",nombre_mayor_edad_heroes, 
                                " con ",mayor_edad_heroes, " años.")
print("La cantidad de Heroinas que tienen habilidades de fuerza o magia es: ",contador_heroinas_fuerza_magia)
print("El promedio de edad entre Heroinas es: ",promedio_edad_heroes_sexo_f," años")
print("El promedio de edad entre Heroes de fuerza es: ",promedio_edad_masculinos_fuerza," años")