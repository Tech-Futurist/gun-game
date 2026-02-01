# import pygame
# import os
# # ???? Write it again in a proper format 
# pygame.init() # -> it is a good practice (but not necessary, your programs will work well even without this but you have to inititalize other modules that are needed.)
# # so by initializing the pygame module, or using pygame.init() you are initializing the other modules like graphic, mixer, (you can use them directly.)

# # print(pygame.__version__) # just checking the version

# # it is a good practice to make variables in capital which are going to be constant.
# WIDTH , HEIGHT = 600 , 400
# # creating a screen or surface, on which everything will get plot
# WIN = pygame.display.set_mode((WIDTH , HEIGHT))
# # how to make the name appearing not to be changed(like window form with this name)
# pygame.display.set_caption(" Martian Gun Game")
# WINCOLOR = (0,0,0)
# FPS = 60 # to make 60 times frame change in a loop, (to give same experience in every system in terms of speed, if we do not specify it then it will according to the system speed(let say 100 frames per second or 1000 frames per second based on systems.))

# def draw():
#     WIN.fill(WINCOLOR)
    
#     # yellowSpaceShip = pygame.image.load(os.join('Assets', 'spaceship_yellow'))
#     # WIN.blit(yellowSpaceShip,50,50)
    

# # creating main function for game loop, event handler and collision or all the operations
# def main():

#     # to keep window running or staying at its position until any event take place.
#     run = True
#     while run:
#         # part of making pygame workable according to this clock.
#         clock = pygame.time.Clock()
#         clock.tick(FPS)
#         draw()
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#         pygame.display.update()
#     # below code need to be out of the for loop because if close mark is clicked then it will get quit using pygame.quit(), otherwise it will give error that some module is not initialized(ex:- pygame.error: video system not initialized).
#     pygame.quit() # it is use for the cancel button


# # we are doing this so that if we will import this game file in another file then only this main function will run, not anything garbage that maybe we create here.
# if __name__ == "__main__":
#      main()

#################