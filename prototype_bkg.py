import pygame
pygame.init() # initialises all imported pygame modules

clock = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

class Block(pygame.sprite.Sprite):
    def __init__(self,pos,width,height):
        super().__init__()
        self.block_height = width
        self.block_width = height

        self.image = pygame.Surface([self.block_width,self.block_height])

        self.rect = self.image.get_rect(topleft=pos)


    def update(self,surface):
        pygame.draw.rect(surface,(WHITE),self.rect)
    

class Player(pygame.sprite.Sprite): 
    def __init__(self,pos):# pos = position
        super().__init__()# Calls parent class constructor
        
        # creates an image and fills the image in with a colour
        self.image = pygame.Surface([25,25]) 

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,surface):
        pygame.draw.rect(surface,RED,self.rect)



class Game:
    def __init__(self):
        # level layout 
        # X represents the block and P represents the player
        # 
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
        

    def setUpLevel(self):
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()# creates a sprite group class that can only contain one sprite which in this case would be player
        # enumerate() returns (index of the value,the actual value)
        for row_index,row in enumerate(self.level):
            for col_index,col in enumerate(row):
                # if an X is found then the programme creates a Block class and passes it a certain position in the screen
                if col == "X":
                    block_sprite = Block((col_index*self.block_width,row_index*self.block_height),self.block_width,self.block_height)
                    self.blocks.add(block_sprite)
                # if a P is found then a player class is created with and it passes a certain position in the screen
                # then it adds the player into the player group
                elif col == "P":
                    player_sprite = Player((col_index*self.block_width,(row_index*self.block_height)+25))
                    self.player.add(player_sprite)

    def run(self,surface):
        self.blocks.update(surface)
        self.player.update(surface)



game = Game() # initialises game class
game.setUpLevel()

# creates a pygame window and names it
DISPLAYSURF = pygame.display.set_mode((700,game.getBlockHeight()*game.getNumofRows()))
pygame.display.set_caption("TEst window")

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
    

pygame.quit()
