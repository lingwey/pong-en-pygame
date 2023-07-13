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
velocidad
#jugador 2
jugador2CordenadaX = 700
jugador2CordenadaY = 300 - (jugadorAlto / 2)


#tamaño de ventana
ventanaDimensiones = (800, 600)
ventana = pygame.display.set_mode(ventanaDimensiones)

reloj = pygame.time.Clock()

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        
    ventana.fill(negro)
    #dibuja los jugadores
    jugador1 = pygame.draw.rect(ventana, blanco, (50,300 - 45,jugadorAncho, jugadorAlto))
    jugador2 = pygame.draw.rect(ventana, blanco, (700,300 - 45,jugadorAncho, jugadorAlto))
    
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()