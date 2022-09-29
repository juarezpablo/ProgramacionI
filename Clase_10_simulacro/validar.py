import re

def validar_entero(dato:str,patron)->int:
    '''
    Valida un numero

    Recibe un strin o un numero

    devuelve el dato parseado a numero en caso de ser posible, 
    Ante errores devuelve -1
    '''
    if dato:
        if re.match(patron,dato) :
            return int(dato)
   
    return -1   