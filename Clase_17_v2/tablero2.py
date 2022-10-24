import pygame
import math
import random
#import tarjeta
from constantes import *
import tarjeta2

class Tablero():
    def __init__(self)->None:
        
        self.d_tablero={}
        self.lista_tarjetas= self.crear_lista_tarjetas()
        
        self.d_tablero["l_tarjetas"] = self.lista_tarjetas
        self.tiempoultimodestape = 0 

    def crear_lista_tarjetas(self):
        lista_tarjetas=[]
        i = 1
        for x in range(0,CANTIDAD_TARJETAS_H*ANCHO_TARJETA,ANCHO_TARJETA):
            for y in range(0,CANTIDAD_TARJETAS_V*ALTO_TARJETA,ALTO_TARJETA):
                if(i > CANTIDAD_TARJETAS_UNICAS):
                # tarjeta_test = tarjeta.init("/0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS),"/00.png",x,y)
                    tarjeta_test=tarjeta2.Tarjeta("/0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS),"/00.png",x,y)
                else:
                    #tarjeta_test = tarjeta.init("/0{0}.png".format(i),"/00.png",x,y)
                    nombre_imagen="/0{0}.png".format(i)
                    tarjeta_test=tarjeta2.Tarjeta(nombre_imagen,"/00.png",x,y)
                lista_tarjetas.append(tarjeta_test)
                i = i + 1

        return lista_tarjetas


    def colision(self,pos_xy):
            
        '''
        verifica si existe una colicion alguna tarjetas del tablero y la coordenada recivida como parametro
        Recibe como parametro el tablero y una tupla (X,Y)
        Retorna el indice de la tarjeta que colisiono con la coordenada
        '''
        #lista_tarjetas = d_tablero["l_tarjetas"]
        
        if(self.cantidad_tarjetas_visibles_no_descubiertas() < 2):
            for aux_tarjeta in self.lista_tarjetas:
                if(aux_tarjeta.rect.collidepoint(pos_xy)):
                    aux_tarjeta.visible=True
                    self.tiempoultimodestape = pygame.time.get_ticks() 

    def cantidad_tarjetas_visibles_no_descubiertas(self):
        cantidad = 0
        for tarjeta in self.lista_tarjetas:
            if(tarjeta.visible and not tarjeta.descubierto):
                cantidad += 1
        return cantidad                      

    def cantidad_tarjetas_descubiertas(self):
        cantidad = 0
        for tarjeta in self.lista_tarjetas:
            if(tarjeta.descubierto):
                cantidad += 1
        return cantidad

    def match(self):
        for index_p in range(len(self.lista_tarjetas)):
            indice=self.__getitem__(index_p)
            if(indice.visible and not indice.descubierto):
                aux_primer_tarjeta = indice
                for index_s in range(index_p+1,len(self.lista_tarjetas)):
                    indice_2=self.__getitem__(index_s)
                    if(indice_2.visible and not indice_2.descubierto ):
                        aux_segunda_tarjeta = indice_2
                        if(aux_primer_tarjeta.path_imagen == aux_segunda_tarjeta.path_imagen):
                            aux_primer_tarjeta.descubierto=True
                            aux_segunda_tarjeta.descubierto=True
                            return True
        return False


   
    def __getitem__(self,index) -> str:
        return self.lista_tarjetas[index]






    

    def update(self):
        '''
        verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
        Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
        '''
        tiempo_actual = pygame.time.get_ticks()
        var_temp = tiempo_actual - (self.tiempoultimodestape)
        if( var_temp > 3000 and self.tiempoultimodestape > 0):
            self.tiempoultimodestape = 0
            
            for aux_tarjeta in self.lista_tarjetas:
                if(aux_tarjeta.descubierto==False):
                    aux_tarjeta.visible=False
        
        if(self.tiempoultimodestape > 0):
            
            if self.match():
                self.tiempoultimodestape = 0


    def render(self,pantalla_juego):
        '''
        Dibuja todos los elementos del tablero en la superficie recibida como parametro
        Recibe como parametro el tablero
        '''
        #lista_tarjetas = d_tablero["l_tarjetas"]
        for tarjet in self.lista_tarjetas:
            if(tarjet.visible):
                pantalla_juego.blit(tarjet.surface,tarjet.rect)
            else:
                pantalla_juego.blit(tarjet.surface_hide,tarjet.rect)
            
