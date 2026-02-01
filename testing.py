import pygame
pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))

player = pygame.Rect((50,50,50,50))
run = True
while run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,255,250),player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
         player.move_ip(-1,0)
    
    elif key[pygame.K_d]:
         player.move_ip(1,0)
    
    elif key[pygame.K_w]:
         player.move_ip(0,-1)
    
    elif key[pygame.K_s]:
         player.move_ip(0,1)
        
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.display.update()
pygame.quit()