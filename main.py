import pygame
pygame.init() # initialises all imported pygame modules

clock = pygame.time.Clock()

# creates a pygame window and names it 
DISPLAYSURF = pygame.display.set_mode((640,704)) # window height and width will be 704x640 pixels
pygame.display.set_caption("Test window")

run = True

while run:# main game loop
    
    # Caps the framerate to 60 Frames per second
    clock.tick(60)
    
# Closes all pygame modules
pygame.quit()