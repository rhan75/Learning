import pygame

pygame.init() #initialize

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#Title
pygame.display.set_caption("My Game")
background = pygame.image.load(r"F:\My Drive\Code\python\Learning\Games\Pang\background.png")

#Load Character
character = pygame.image.load(r"F:\My Drive\Code\python\Learning\Games\Pang\character.png")
character_size = character.get_rect().size # Get dimension of character.png
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height

#New Position
to_x = 0 #Relative X position
to_y = 0 #Relative Y position




#event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Check for quit command
            running = False #Set running as false if quit received
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x
    character_y_pos += to_y
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    screen.blit(background, (0,0)) #Load image
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() #upate display


pygame.quit()