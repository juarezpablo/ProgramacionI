import pygame
import math
import random
import tarjeta
from constantes import *
import tarjeta2

class Tablero():
    def _init_(self):
        self.d_tablero={}
        self.lista_tarjetas=[]
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
                self.lista_tarjetas.append(tarjeta_test)
                i = i + 1
        self.d_tablero["l_tarjetas"] = self.lista_tarjetas
        self.d_tablero["tiempo_ultimo_destape"] = 0


    def colision(self,pos_xy):
            
        '''
        verifica si existe una colicion alguna tarjetas del tablero y la coordenada recivida como parametro
        Recibe como parametro el tablero y una tupla (X,Y)
        Retorna el indice de la tarjeta que colisiono con la coordenada
        '''
        #lista_tarjetas = d_tablero["l_tarjetas"]
        if(tarjeta2.Tarjeta.cantidad_tarjetas_visibles_no_descubiertas() < 2):
            for aux_tarjeta in self.lista_tarjetas:
                if(aux_tarjeta.rect.collidepoint(pos_xy)):
                    aux_tarjeta.visible=True
                    self.d_tablero["tiempo_ultimo_destape"] = pygame.time.get_ticks()    


    def cantidad_tarjetas_visibles_no_descubiertas2(self):
        cantidad = 0
        for tarjeta in self.lista_tarjetas:
            if(tarjeta.visible and not tarjeta.descubierto):
                cantidad += 1
        return cantidad 

    def update(self):
        '''
        verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
        Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
        '''
        tiempo_actual = pygame.time.get_ticks()
        if(tiempo_actual - self.d_tablero["tiempo_ultimo_destape"] > 3000 and self.d_tablero["tiempo_ultimo_destape"] > 0):
            self.d_tablero["tiempo_ultimo_destape"] = 0
            
            for aux_tarjeta in self.lista_tarjetas:
                if(aux_tarjeta.descubierto==False):
                    aux_tarjeta.visible=False
        
        if(self.d_tablero["tiempo_ultimo_destape"] > 0):
            for aux in self.lista_tarjetas:
                if(aux.match(self.d_tablero["l_tarjetas"])):
                    self.d_tablero["tiempo_ultimo_destape"] = 0


    def render(self,pantalla_juego):
        '''
        Dibuja todos los elementos del tablero en la superficie recibida como parametro
        Recibe como parametro el tablero
        '''
        #lista_tarjetas = d_tablero["l_tarjetas"]
        for tarjeta in self.lista_tarjetas:
            if(tarjeta.visible):
                pantalla_juego.blit(tarjeta.surface,tarjeta.rect)
            else:
                pantalla_juego.blit(tarjeta.surface_hide,tarjeta.rect)
            
