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

class Game:
    def __init__(self):
        # level layout 
        # the game screen is going to be split into a grid. The grid is going to be represented by this 2D array
        # Each cell will contain a number that will indicate what should be in each cell 
        # 2 represents a block
        # 20 spaces in one row
        self.levelmap = [
            [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0],
            [0,0,0,2,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0],
            [0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
            [0,0,0,0,0,0,2,2,2,2,0,0,2,0,0,0,2,2,0,0],
            [0,0,0,0,0,2,2,0,0,2,0,0,2,2,2,2,2,2,0,0],
            [2,2,0,2,2,2,2,0,0,2,0,0,2,2,2,2,2,2,0,0],        
        ] 

        # the game screen is going to be split into a grid. The grid is going to be represent
        self.unit_height = 32
        self.unit_width = 32
        

    def setUpLevel(self): # This function creates all the sprites that are going to be used in this game
        self.blocks = pygame.sprite.Group()# creates a group that will contain all the block sprites
        # enumerate() returns (index of the value,the actual value)
        for row_index,row in enumerate(self.levelmap):
            for col_index,col in enumerate(row):
                # if an 2 is found then the programme creates a Block class and passes it a certain position in the screen
                if col == 2:
                    block_sprite = Block((col_index*self.unit_width,row_index*self.unit_height),self.unit_width,self.unit_height)
                    self.blocks.add(block_sprite) # Adds the block to the blocks group

    def draw(self,surface): # draws all the sprites within a group to the screen
        self.blocks.update(surface)



############################# Main Game ###################################################

clock = pygame.time.Clock()

game = Game() # creating an instance of the game class
game.setUpLevel()

# creates a pygame window and names it 
DISPLAYSURF = pygame.display.set_mode((640,704)) # window height and width will be 704x640 pixels
pygame.display.set_caption("Test window")

run = True

while run:# main game loop

    for event in pygame.event.get():# Event handler
        # ends game loop if the top right cross button or the escape key is pressed
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    game.draw(DISPLAYSURF)

    pygame.display.update()
    
    # Caps the framerate to 60 Frames per second
    clock.tick(60)
    
# Closes all pygame modules
pygame.quit()