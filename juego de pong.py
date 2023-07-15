import pygame
pygame.init()

#colores 
negro = (0, 0, 0)
blanco = (255, 255, 255)

#dimensiones de los jugadores
jugadorAncho = 15
jugadorAlto = 90
#cordenadas de los jugadores
#jugador 1
jugador1CordenadaX = 50
jugador1CordenadaY = 300 - (jugadorAlto / 2)
velocidadJugador1 = 0
#jugador 2
jugador2CordenadaX = 750 - jugadorAncho
jugador2CordenadaY = 300 - (jugadorAlto / 2)
velocidadJugador2 = 0

#cordenadas de la pelota
pelotaCordenadaX = 400
pelotaCordenadaY = 300
pelotaXVelocidad = 3
pelotaYVelocidad = 3

#tamaño de ventana
ventanaDimensiones = (800, 600)
ventana = pygame.display.set_mode(ventanaDimensiones)

reloj = pygame.time.Clock()

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        # controles de movimiento de los jugadores
        #al precionar
        if event.type == pygame.KEYDOWN:
            #jugador 1
            if event.key == pygame.K_w:
                velocidadJugador1 = -3
            if event.key == pygame.K_s:
                velocidadJugador1 = 3
            #jugador 2 
            if event.key == pygame.K_UP:
                velocidadJugador2 = -3
            if event.key == pygame.K_DOWN:
                velocidadJugador2 = 3    
        #al soltar
        if event.type == pygame.KEYUP:
            #jugador 1
            if event.key == pygame.K_w:
                velocidadJugador1 = 0
            if event.key == pygame.K_s:
                velocidadJugador1 = 0
            #jugador 2 
            if event.key == pygame.K_UP:
                velocidadJugador2 = 0
            if event.key == pygame.K_DOWN:
                velocidadJugador2 = 0   
    #mantiene la pelota en pantalla hasta que salga por algun lado de los jugadores
    if pelotaCordenadaY > 590 or pelotaCordenadaY < 10:
        pelotaYVelocidad *= -1
    #si la pelota sale del margen derecho la reinicia y invierte su direccion de salida
    if pelotaCordenadaX > 800  or pelotaCordenadaX < 0:
        pelotaCordenadaX = 400
        pelotaCordenadaY = 300
        pelotaXVelocidad *= -1
        pelotaYVelocidad *= -1
    #limita el recorrido de los jugadores para que no salgan de la pantalla
    #jugador 1
    if jugador1CordenadaY > 510 : 
        jugador1CordenadaY = 510
    if jugador1CordenadaY < 0:
        jugador1CordenadaY = 0
    #jugador 2
    if jugador2CordenadaY > 510 : 
        jugador2CordenadaY = 510
    if jugador2CordenadaY < 0:
        jugador2CordenadaY = 0
     
    #modifica las cordenadas de los jugadores y la pelota
    jugador1CordenadaY += velocidadJugador1
    jugador2CordenadaY += velocidadJugador2
    # movimiento pelota
    pelotaCordenadaX += pelotaXVelocidad
    pelotaCordenadaY += pelotaYVelocidad
            
    ventana.fill(negro)
    #dibuja los jugadores
    jugador1 = pygame.draw.rect(ventana, blanco, (jugador1CordenadaX, jugador1CordenadaY, jugadorAncho, jugadorAlto))
    jugador2 = pygame.draw.rect(ventana, blanco, (jugador2CordenadaX, jugador2CordenadaY, jugadorAncho, jugadorAlto))
    pelota = pygame.draw.circle(ventana, blanco, (pelotaCordenadaX, pelotaCordenadaY), 10)
    
    #coliciones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelotaXVelocidad *= -1
    
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()