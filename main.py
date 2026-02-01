'''
keys are different only in case of up and down, here 'up' means 'down' and 'down' means 'up'
similarly 'w' means 'down' and 's' means 'up'.

here we can't draw surface over surface, but in case of our spaceship we are drawing image over the rectangle, basically surface over the surface(to make it movable)

here we are saying that rectangle have x and y coordinate(therefore we are drawing image over the rectangle) to make it movable(because we can increase or decrease its coordinate.)
??? but image may also have x and y coordinate, then why we can't use it for moving it further directly ??? -> ( maybe because if we use it directly for moving then we have to add or subtract coordinates to it and it will decrease or change its size(possibly))

# ??? use of blit and draw method
'''

''' 
# # *** Whatever we made in pygame is a surface. ***
# # *** Here coordinate start from the left top corner *** so +1 in x means moving in right and +1 in y means moving downward.

### common lines of code for every pygame project ###

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False // by this it will get out of the while loop
    pygame.quit() # it is use for the cancel button (and this quit function will actually quit the game.)

'''


import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# changing the window name -> it seems to be changing instanteneously over come with the changed name
pygame.display.set_caption("First Game")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0 , 0)
YELLOW = (255,255, 0)
FPS = 60 # FRAMES PER SECOND IN ORDER TO MAKE GAME SMOOTH IN EVERY SYSTEM
VEL = 4 # velocity of spaceship which is constant

SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55, 40

yellow_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
# resizing the image and transformed the image
yellow = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)

red_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
red = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)

yellow_x_coordinate, yellow_y_coordinate = 100, 200
red_x_coordinate, red_y_coordinate = 800, 200

border_x_coordinate , border_y_coordinate = 440 , 0 
border_width , border_height = 5, 900
# creating a border for spaceships
border = pygame.Rect(border_x_coordinate,border_y_coordinate,border_width,border_height)

# bullets stuff
bullet_width , bullet_height = 4, 3
# bullets = [] # don't know what we will do with this.
bulletVel = 7
redBullets = []
yellowBullets = []
maxBullets = 3


def draw_window(yellow_spaceship, red_spaceship):
    WIN.fill(WHITE)
    WIN.blit(yellow, (yellow_spaceship.x, yellow_spaceship.y))
    WIN.blit(red,(red_spaceship.x, red_spaceship.y))
    pygame.draw.rect(WIN,BLACK,border)
    # WIN.blit(border,400,0) # it's wrong here

    # pygame.draw.rect(WIN,YELLOW,red_bullet)


    # here we have to update manually after making every small change
    pygame.display.update()

def yellow_handle_spaceship(key,yellow_spaceship):
        # for yellow spaceship movements

        # here we will use if condition over elif, so that we can move diagonally in any direction by pressing keys like up and left at the same time.
        # left 
        if (key[pygame.K_a]) and (yellow_spaceship.x > 0 ):
        # if (key[pygame.K_a]) and (yellow_spaceship.x > 0 + SPACESHIP_WIDTH):
            yellow_spaceship.x-=VEL
        
        # right
        # if (key[pygame.K_d]) and (yellow_spaceship.x < 440):
        if (key[pygame.K_d]) and (yellow_spaceship.x < border_x_coordinate-SPACESHIP_HEIGHT):
        # if (key[pygame.K_d]) and (yellow_spaceship.x < 445-SPACESHIP_WIDTH):
            yellow_spaceship.x+=VEL
        
        # up
        if (key[pygame.K_w]) and (yellow_spaceship.y > border_y_coordinate ):
        # if (key[pygame.K_w]) and (yellow_spaceship.y > 0 + SPACESHIP_HEIGHT):
            yellow_spaceship.y-=VEL
        
        # down
        # if (key[pygame.K_s]) and (yellow_spaceship.y < 500 ):
        if (key[pygame.K_s]) and (yellow_spaceship.y < (HEIGHT - SPACESHIP_WIDTH-1)): # don't know why 445 was not working before and now working and don't know how.
        # if (key[pygame.K_s]) and (yellow_spaceship.y < 445): # don't know why 445 was not working before and now working and don't know how.
        # if (key[pygame.K_s]) and (yellow_spaceship.y < 500 - SPACESHIP_HEIGHT): # and don't know why this code is not working despite of using the right subtracting factor.
            yellow_spaceship.y+=VEL

def red_handle_spaceship(key,red_spaceship):
        
        # for red spaceship movements

        # left
        # if key[pygame.K_LEFT] and (red_spaceship.x in [0,440]):
        if (key[pygame.K_LEFT]) and (red_spaceship.x > (border_x_coordinate + border_width )) :
        # if (key[pygame.K_LEFT]) and (red_spaceship.x > (445 + SPACESHIP_WIDTH)) :
            red_spaceship.x-=VEL

        # right
        if (key[pygame.K_RIGHT]) and ( red_spaceship.x < (WIDTH - SPACESHIP_HEIGHT)):
            red_spaceship.x+=VEL

        # up
        if (key[pygame.K_UP]) and ( red_spaceship.y > ( border_y_coordinate )):
        # if (key[pygame.K_UP]) and ( red_spaceship.y > ( 0 + SPACESHIP_WIDTH)):
            red_spaceship.y-=VEL

        # down
        if (key[pygame.K_DOWN]) and (red_spaceship.y < (HEIGHT - SPACESHIP_WIDTH-1)):
        # if (key[pygame.K_DOWN]) and (red_spaceship.y < 445):
            red_spaceship.y+=VEL

def bulletMOvements(yellow_spaceship, red_spaceship,yellowBullets, redBullets):
     for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
                 if pygame.event.Event == pygame.K_LCTRL and len(yellowBullets) < maxBullets:
                      yellow_bullet = pygame.Rect(yellow_spaceship.x + yellow_spaceship.width , yellow_spaceship.height//2,bullet_width,bullet_height )
                      yellowBullets.append(yellow_bullet)


                 if pygame.event.Event == pygame.K_RCTRL and len(redBullets) < maxBullets:
                      red_bullet = pygame.Rect(red_spaceship.x , red_spaceship.height//2, bullet_width, bullet_height)
                      redBullets.append(red_bullet)
               

def main():
    yellow_spaceship = pygame.Rect(yellow_x_coordinate,yellow_y_coordinate,SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red_spaceship = pygame.Rect(red_x_coordinate,red_y_coordinate, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
        
            
        draw_window(yellow_spaceship, red_spaceship)
        # draw_window(yellow_spaceship, red_spaceship, yellow_bullet, red_bullet)

        key = pygame.key.get_pressed()
        yellow_handle_spaceship(key,yellow_spaceship)
        red_handle_spaceship(key,red_spaceship)

        # just testing yellow and red spaceship horizontal movement.

        # yellow_spaceship.x+=1
        # red_spaceship.x-=1

        
    pygame.quit()

# why if we are not writing main function inside the -> name == main, then it is getting close by itself.
if __name__ == "__main__":
    main()
