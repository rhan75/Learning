import pygame

pygame.init() #initialize

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#Title
pygame.display.set_caption("My Game")
#event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Check for quit command
            running = False #Set running as false if quit received

pygame.quit()