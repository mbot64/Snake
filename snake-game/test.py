import pygame
pygame.init()

width = 500
height = 500

WHITE = (255,255,255)
RED = (255,0,0)

screen = pygame.display.set_mode((width, height))

running = True
mousePressed = False

while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        #checks if exit button pressed
        if event.type== pygame.QUIT:
            running = False
        #when mouse is clicked down changes mousePressed to True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed = True
        #when mouse is unpressed changes mousePressed to False
        elif event.type == pygame.MOUSEBUTTONUP:
            mousePressed = False
    #if the mouse button is pressed then it draws a red circle at that point
    if mousePressed:
        mousePosition = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255,0,0), mousePosition,10)
    pygame.display.update()
pygame.quit()
