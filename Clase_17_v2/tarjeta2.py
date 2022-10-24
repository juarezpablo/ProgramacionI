from constantes import *
import pygame
import tablero2

class Tarjeta:
    
        
    def __init__(self,nombre_imagen,nombre_imagen_hide,x,y) -> None:
        self.path_imagen= PATH_RECURSOS+nombre_imagen
        self.visible=False
        self.descubierto=False
        self.surface=pygame.transform.scale(pygame.image.load(self.path_imagen), (ANCHO_TARJETA,ALTO_TARJETA))
        self.surface_hide=pygame.transform.scale(pygame.image.load(PATH_RECURSOS+nombre_imagen_hide), (ANCHO_TARJETA,ALTO_TARJETA))
        self.rect= self.surface.get_rect()
        self.rect.x=x
        self.rect.y=y
    ''' 
    def nombre_imagen(self, nombre_imagen):
       self.path_imagen = PATH_RECURSOS+nombre_imagen
    def nombre_imagen_hide(self, nombre_imagen_hide):
       self.surface_hide=pygame.transform.scale(pygame.image.load(PATH_RECURSOS+nombre_imagen_hide), (ANCHO_TARJETA,ALTO_TARJETA))

    def x(self,x):
        self.rect.x=x
    def y(self,y):
        self.rect.y=y    
    '''       

    def cantidad_tarjetas_descubiertas(self,lista_tarjetas:list):
        cantidad = 0
        for tarjeta in lista_tarjetas:
            if(tarjeta.descubierto):
                cantidad += 1
        return cantidad

    def cantidad_tarjetas_visibles_no_descubiertas(self):
        cantidad = 0
        for tarjeta in self:
            if(tarjeta.visible and not tarjeta.descubierto):
                cantidad += 1
        return cantidad
     
    def match(self):
        for index_p in range(len(self)):
            if(self[index_p].visible and not self[index_p].descubierto):
                aux_primer_tarjeta = self[index_p]
                for index_s in range(index_p+1,len(self)):
                    if(self[index_s].visible and not self[index_s].descubierto ):
                        aux_segunda_tarjeta = self[index_s]
                        if(aux_primer_tarjeta.path_imagen == aux_segunda_tarjeta.path_imagen):
                            aux_primer_tarjeta.descubierto=True
                            aux_segunda_tarjeta.descubierto=True
                            return True
        return False





