
import pygame
import colores
import dona
import personaje
import botones

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("PYGAME HOMERO COME DONAS")

# TIMER
timer = pygame.USEREVENT + 0
t=100
pygame.time.set_timer(timer,t)


player = personaje.crear(ANCHO_VENTANA/2,ALTO_VENTANA-200,200,200)
lista_donas = dona.crear_lista_donas(50)





flag_run = True
while flag_run:
    
    




    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.25)
    sonido_fondo=pygame.mixer.Sound("Clase_15_Pygame/CLASE_PYGAME_INTRO/conga.wav")
    
    sonido_fondo.play()


    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                dona.update(lista_donas)
        if evento.type == pygame.MOUSEBUTTONDOWN and boton_max.collidepoint(pygame.mouse.get_pos()):
            t=t+200
            print("click mas")
        if evento.type == pygame.MOUSEBUTTONDOWN and boton_min.collidepoint(pygame.mouse.get_pos()):
            t=t-200
            print("click menos")


    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_LEFT] :
        personaje.update(player,-10)
    if lista_teclas[pygame.K_RIGHT] :
        personaje.update(player,10)

    if lista_teclas[pygame.K_UP]  :
        sonido_fondo.stop(0)


    ventana_ppal.fill(colores.NEGRO)
    personaje.actualizar_pantalla(player,ventana_ppal)
    dona.actualizar_pantalla(lista_donas,player,ventana_ppal)
    boton_max = botones.crear_boton_max_speed(ventana_ppal)
    #botones.actualizar_pantalla(boton_max,ventana_ppal)
    boton_min = botones.crear_boton_min_speed(ventana_ppal)

    pygame.display.flip()
pygame.quit()