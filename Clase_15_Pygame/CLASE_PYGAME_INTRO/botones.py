from cmath import rect
import pygame
import colores

def crear_boton_max_speed(ventana_ppal):
    dict_boton_max={}
    font = pygame.font.SysFont("Arial Narrow", 50)
    text = font.render("+", True, (200, 100, 0))
    #rect_boton = text.get_rect()
    ventana_ppal.blit(text,(500,0))
    #dict_boton_max["surface"]=text
    #dict_boton_max["rect"]=rect_boton
    #return dict_boton_max
    #boton = pygame.rect(250,20,20,20)
    rect_boton_max= text.get_rect()
    rect_boton_max.centerx=500
    ventana_ppal.blit(text,rect_boton_max)
    return rect_boton_max

#def actualizar_pantalla(dict_boton,ventana_ppal):
#    ventana_ppal.blit(dict_boton["surface"],dict_boton["rect"])    

def crear_boton_min_speed(ventana_ppal):
    font = pygame.font.SysFont("Arial Narrow", 50)
    text = font.render("-", True, (200, 100, 0))
    #rect_boton = text.get_rect()
    ventana_ppal.blit(text,(600,0))
    #dict_boton_max["surface"]=text
    #dict_boton_max["rect"]=rect_boton
    #return dict_boton_max
    #boton = pygame.rect(250,20,20,20)
    rect_boton_min= text.get_rect()
    rect_boton_min.centerx=600
    ventana_ppal.blit(text,rect_boton_min)
    return rect_boton_min