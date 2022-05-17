import pygame
pygame.init() # initialises all imported pygame modules

clock = pygame.time.Clock()

# Stored RGB values inside variables to save time instead of re writing each rgb value of a sprite
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

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
        pygame.draw.rect(surface,(WHITE),self.rect)
    

class Player(pygame.sprite.Sprite): 
    def __init__(self,pos):# pos = position
        super().__init__()# Calls parent class constructor
        
        # creates an image
        self.image = pygame.Surface([25,25]) 

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,surface):
        # draws the sprite in the display
        pygame.draw.rect(surface,RED,self.rect)



class Game:
    def __init__(self):
        # level layout 
        # X represents the block and P represents the player
        # 15 spaces in one row
        self.level =[
            "               ",
            "              X",
            "             X ",
            "P      XX  XX  ",
            "XX   XX  XX    ",
            "  X X     X    ",
            "               ",
            "               ",
            
        ] 

        self.block_height = 50
        self.block_width = 50

    def getBlockHeight(self):
        return self.block_height
    def getNumofRows(self):
        return len(self.level)
        

    def setUpLevel(self): # This function creates all the sprites that are going to be used in this game
        self.blocks = pygame.sprite.Group()# creates a group that will contain all the block sprites
        self.player = pygame.sprite.GroupSingle()# creates a sprite group class that can only contain one sprite which in this case would be player
        # enumerate() returns (index of the value,the actual value)
        for row_index,row in enumerate(self.level):
            for col_index,col in enumerate(row):
                # if an X is found then the programme creates a Block class and passes it a certain position in the screen
                if col == "X":
                    block_sprite = Block((col_index*self.block_width,row_index*self.block_height),self.block_width,self.block_height)
                    self.blocks.add(block_sprite) # Adds the block to the blocks group
                # if a P is found then a player class is created and it passes a certain position in the screen
                # then it adds the player into the player group
                elif col == "P":
                    player_sprite = Player((col_index*self.block_width,(row_index*self.block_height)+25))
                    self.player.add(player_sprite)

    def run(self,surface): # draws all the sprites to the screen
        self.blocks.update(surface)
        self.player.update(surface)

############################# Main Game ###################################################

game = Game() # initialises game class
game.setUpLevel() # Creates all the sprites

# creates a pygame window and names it 
DISPLAYSURF = pygame.display.set_mode((700,game.getBlockHeight()*game.getNumofRows())) #window height is adjusted by how many rows the level has and how tall the blocks are
pygame.display.set_caption("Test window")

run = True

while run:# main game loop
    
    for event in pygame.event.get():# Event handler
        # ends game loop if the top right cross button or the escape key is pressed
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    

    DISPLAYSURF.fill(BLACK)
    # draws the player on the screen
    game.run(DISPLAYSURF)

    # update the screen
    pygame.display.update()
    
    # Caps the framerate to 60 Frames per second
    clock.tick(60)
    
# Closes all pygame modules
pygame.quit()
