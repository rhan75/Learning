import pygame
##########################################################################################
# Initialization For All Games

pygame.init() #initialize

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#Title
pygame.display.set_caption("My Game")

# FPS
clock = pygame.time.Clock()
##########################################################################################

##########################################################################################
# 1. Background / Game images / Coordinate / Speed / Font
#event loop
running = True
while running:
    dt = clock.tick(60)
    # 2. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Check for quit command
            running = False #Set running as false if quit received

    # 3. Character Position
    
    
    
    # 4. Collision Handling
    
    
    
    
    # 5. Draw on screen
    
    pygame.display.update() #upate display




pygame.quit()