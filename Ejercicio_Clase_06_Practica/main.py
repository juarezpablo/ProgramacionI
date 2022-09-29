from xml.etree.ElementPath import xpath_tokenizer_re
from data_stark import lista_heroes




def extraer_iniciales(nombre_heroe:str) ->str:
    '''
    Obtiene las iniciales de un nombre

    Recibe un string con el nombre del personaje

    Retorna un string con las iniciales del nombre, Devuelve N/A en caso de vacio
    '''
    if(type(nombre_heroe) == str and nombre_heroe != ""):
        mensaje = ""
        
        nombre_heroe = nombre_heroe.replace("the","")
            
        inicial=nombre_heroe.replace("-"," ")
        lista_inicial=inicial.split(" ")
        #print(lista_inicial)
        for item in lista_inicial:
            inicial_item = item
            if(inicial_item != ""):
                inicial_item = inicial_item[:1]
                mensaje += inicial_item
        
        return mensaje
    else:
        retorno = "N/A"
        return retorno   


#nombre= "Drax the Destroyer"
#print(extraer_iniciales(nombre))

def definir_iniciales_nombre(heroe:dict) :
    if "nombre" in heroe.keys():
        nombre_heroe =heroe["nombre"]
        iniciales = extraer_iniciales(nombre_heroe)
        heroe["iniciales"] = iniciales

    else:
        return False    


dic_heroe= {
    "nombre": "Drax the Destroyer",
    "identidad": "Arthur Sampson Douglas",
    "empresa": "Marvel Comics",
    "altura": "193.00999999999999",
    "peso": "306.42000000000002",
    "genero": "M",
    "color_ojos": "Red",
    "color_pelo": "No Hair",
    "fuerza": "80",
    "inteligencia": "average"
  }
#print(dic_heroe)
#definir_iniciales_nombre(dic_heroe)
#print(dic_heroe)

            #1.3
def agregar_iniciales_nombre(lista:list) ->bool:
    if (type(lista) == list and lista != [""]):
        for heroe in lista:
            definir_iniciales_nombre(heroe)

        return True
    else:
        print("El origen de datos no contiene el formato correcto")  
        return False
         

#print(lista_heroes)
#agregar_iniciales_nombre(lista_heroes)
#print(lista_heroes)        

            #1.3 BIS

def stark_imprimir_nombres_con_iniciales(lista:list)  :
    if (type(lista) == list and lista != [""]):
        agregar_iniciales_nombre(lista)
        for heroe in lista:
            print("* {0}  ({1})".format(heroe["nombre"],heroe["iniciales"]))

#stark_imprimir_nombres_con_iniciales(lista_heroes)

            #2.1
def generar_codigo_heroe(id_heroe:int,genero_heroe:str) ->str:
    '''
    Genera un codigo con el sig formato GENERO-000…000ID
    Realiza las sig validaciones:
    El identificador del héroe sea numérico. 
    El género no se encuentre vacío y este dentro de los valores esperados (‘M’,  ‘F’ o ‘NB’)

    
    recibe el identificador del heroe en formato entero, recibe el genero que puede ser ‘M’,  ‘F’ o ‘NB’
    
    Retorna el codigo generado o N/A en caso de que la validacion de incorrecta
    '''

    if( type(id_heroe) == int and type(genero_heroe) == str and 
                        (genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB") ):

        maximo_caracteres = 10
        codigo = "{0}-".format(genero_heroe)
        largo_genero = len(codigo)
        codigo_numerico = str(id_heroe)
        largo_numero= len(codigo_numerico)
        largo_total_numero = maximo_caracteres - largo_genero
        for x in range(largo_numero,largo_total_numero):
            codigo_numerico= "0"+codigo_numerico
        #print(codigo_numerico)     
        codigo = codigo+codigo_numerico
        #print(codigo)
        return codigo
    else:
        retorno = "N/A"
        return retorno

#generar_codigo_heroe(12,"NB")

            #2.2
def agregar_codigo_heroe(heroe:dict,id_heroe:int):
    '''
    agregar una nueva clave llamada ‘codigo_heroe’ al diccionario ‘heroe’ recibido como parámetro 
    y asignarle como valor un código utilizando la función ‘generar_codigo_heroe’

    Recibe un diccionario de un heroe y un identificador de tipo entero para ese heroe

    '''
    if(type(heroe) == dict and heroe != {""} and type(id_heroe) == int):
        codigo_heroe = generar_codigo_heroe(id_heroe,heroe["genero"])
        heroe["codigo_heroe"] = codigo_heroe
        largo = len(codigo_heroe)
        if( largo == 10):
            return True
        else:
            return False    
    else:
        return False

#print(dic_heroe)
#agregar_codigo_heroe(dic_heroe,22)
#print(dic_heroe)

                #2.3
def stark_generar_codigos_heroes(lista:list):
    '''
    Itera cada personaja de la lista y le agrega un codigo unico
    recibe una lista de personajes

    '''

    if(type(lista) == list and lista != [""]):
        i=1
        for heroe in lista:

            if(type(heroe) == dict and ("genero" in heroe.keys()) ):
                agregar_codigo_heroe(heroe,i)
                
                
                i+=1
                
            else:
                print("El origen de datos no contiene el formato correcto")    
        #primer_heroe = lista[0]
        #primer_codigo=primer_heroe["codigo_heroe"]
        
        mensaje = "Se agregaron {0} codigos. \n El primer codigo es:  {1}\n El ultimo codigo es:  {2}".format(i,lista[0]["codigo_heroe"],lista[i-2]["codigo_heroe"])    
        print(mensaje)
#stark_generar_codigos_heroes(lista_heroes)

