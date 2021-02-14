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





#event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Check for quit command
            running = False #Set running as false if quit received
    screen.blit(background, (0,0)) #Load image
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() #upate display

pygame.quit()