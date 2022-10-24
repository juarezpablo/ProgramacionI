from constantes import *
import pygame


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





