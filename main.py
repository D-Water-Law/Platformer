import pygame
pygame.init() # initialises all imported pygame modules

clock = pygame.time.Clock()

# creates a pygame window and names it 
DISPLAYSURF = pygame.display.set_mode((640,704)) # window height and width will be 704x640 pixels
pygame.display.set_caption("Test window")

run = True

while run:# main game loop

    for event in pygame.event.get():# Event handler
        # ends game loop if the top right cross button or the escape key is pressed
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    
    # Caps the framerate to 60 Frames per second
    clock.tick(60)
    
# Closes all pygame modules
pygame.quit()