import pygame

pygame.init() #initialize

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#Title
pygame.display.set_caption("My Game")

# FPS
clock = pygame.time.Clock()

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

#Speed
character_speed = 0.3
#Enemy
enemy = pygame.image.load(r"F:\My Drive\Code\python\Learning\Games\Pang\enemy.png")
enemy_size = enemy.get_rect().size # Get dimension of character.png
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) 
enemy_y_pos = (screen_height /2)- enemy_height

gameover = pygame.image.load(r"F:\My Drive\Code\python\Learning\Games\Pang\gameover.png")

#event loop
running = True
while running:
    dt = clock.tick(60)
    #26
    #print("fps :  " + str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Check for quit command
            running = False #Set running as false if quit received
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #Collision position
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #Check collision
    if character_rect.colliderect(enemy_rect):
        #screen.blit(gameover, (screen_width/2, screen_height/2))
        running = False 
    screen.blit(background, (0,0)) #Load image
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))
    pygame.display.update() #upate display


pygame.quit()