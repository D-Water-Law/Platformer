import pygame
pygame.init() # initialises all imported pygame modules

class Block(pygame.sprite.Sprite):
    def __init__(self,pos,width,height): # pos = position, width,height = width and height of the blocks
        super().__init__()
        self.block_height = width
        self.block_width = height

        # creates an image
        self.image = pygame.Surface([self.block_width,self.block_height])

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(topleft=pos)


    def update(self,surface):
        # draws the sprite in the display
        pygame.draw.rect(surface,(255,255,255),self.rect)




############################# Main Game ###################################################

clock = pygame.time.Clock()

block = Block((50,50),100,100)

# creates a pygame window and names it 
DISPLAYSURF = pygame.display.set_mode((640,704)) # window height and width will be 704x640 pixels
pygame.display.set_caption("Test window")

run = True

while run:# main game loop

    for event in pygame.event.get():# Event handler
        # ends game loop if the top right cross button or the escape key is pressed
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    block.update()

    pygame.display.update()
    
    # Caps the framerate to 60 Frames per second
    clock.tick(60)
    
# Closes all pygame modules
pygame.quit()