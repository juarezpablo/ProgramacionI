from pickletools import pyfloat
import pygame
import math
import random
import tarjeta
from constantes import *
'''
ANCHO_PANTALLA = 500
ALTO_PANTALLA = 550
ALTO_TEXTO = 50
CANTIDAD_TARJETAS_H = 2
CANTIDAD_TARJETAS_V = 2
'''
def init():
    '''
    Crea una lista de tarjetas
    Recibe como parametro la cantidad de tarjetas
    Retorna un dict tablero
    '''
    d_tablero = {}
    lista_tarjetas = []
    i = 1
    for x in range(0,ANCHO_PANTALLA,ANCHO_TARJETA):
        for y in range(0,ALTO_PANTALLA-ALTO_TEXTO,ALTO_TARJETA):
            if(i > CANTIDAD_TARJETAS_UNICAS):
                tarjeta_test = tarjeta.init("0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS),r"00.png",x,y)
            else:
                tarjeta_test = tarjeta.init("0{0}.png".format(i),r"00.png",x,y)
            tarjeta_test["visible"] = False
            tarjeta_test["descubierto"]= False
            lista_tarjetas.append(tarjeta_test)
            i = i + 1
            

    d_tablero["l_tarjetas"] = lista_tarjetas

    return d_tablero

def colicion(d_tablero,pos_xy):
    '''
    verifica si existe una colicion alguna tarjetas del tablero y la coordenada recivida como parametro
    Recibe como parametro el tablero y una tupla (X,Y)
    Retorna el indice de la tarjeta que colisiono con la coordenada
    '''
    print(pos_xy)
    
    #print(d_tablero)
    #bandera_segundo_click = 0
    lista_tarjetas = d_tablero["l_tarjetas"]
    #print(tarjeta.cantidad_tarjetas_visibles_nodescubiertas(lista_tarjetas))
    if ((tarjeta.cantidad_tarjetas_visibles_nodescubiertas(lista_tarjetas)) < 2):
        for tarjeta_1 in lista_tarjetas:
       # print(tarjeta)
            if tarjeta_1["rect"].collidepoint(pos_xy):
                if tarjeta_1["visible"]==False:
                    tarjeta_1["visible"]=True
                else:    
                    tarjeta_1["visible"] = False
      
           
            

def update(d_tablero,tiempo):
    '''
    verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
    Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
    
    #if tarjeta.cantidad_tarjetas_visibles(d_tablero["l_tarjetas"]) == 2 :
    temp=pygame.time.get_ticks()
    lista_tarjetas = d_tablero["l_tarjetas"]
    if temp >3000 :
        for tarjeta_aux in lista_tarjetas:
            tarjeta_aux["descubierto"]=False
            tarjeta_aux["visible"]=False
    '''
    


    pass
    

def render(d_tablero,pantalla_juego):
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero
    '''
    lista_tarjetas = d_tablero["l_tarjetas"]
    for tarjeta in lista_tarjetas:
        if(tarjeta["visible"]):
            pantalla_juego.blit(tarjeta["surface"],tarjeta["rect"])
        else:
            pantalla_juego.blit(tarjeta["surface_hide"],tarjeta["rect"])
     
def primer_muestreo(d_tablero):
   pass
        
