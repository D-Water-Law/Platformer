import pygame
pygame.init() # initialises all imported pygame modules

######################################### Menu buttons #######################################################
class Button(pygame.sprite.Sprite):
    def __init__(self,command,img=None): # pos = position, width,height = width and height of the blocks
        super().__init__()

        # creates an image
        if img == None:
            self.image = pygame.Surface([175,40])
            self.image.fill((255,255,255))
        else:
            self.image = pygame.image.load(img)

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(center=(320,200))
        
    
    def start(self):
        gameLoop()

    def quit(self):
        return 1

    def settings(self):
        pass
        # settingsLoop()
        

############################################ Sprites #########################################################

class Player(pygame.sprite.Sprite): 
    def __init__(self,pos):# pos = position
        super().__init__()# Calls parent class constructor
        
        # creates an image
        self.image = pygame.Surface([12,32]) 
        self.image.fill((255,0,0))

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(topleft = pos)
        
        self.directionX = 0
        self.speedX = 1
        self.speedY = 0

        self.jumping = False
        
        self.gravity = 1

        

    def jumpReset(self): # resets jump
        self.jumping = False


    def update(self): # moves player
        # checks for collison between the sides of the screen
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 628:
            self.rect.x = 628

        self.directionX = 0
        


    def xMove(self):
        key = pygame.key.get_pressed() #gets all boolean values of the keyboard keys

        if key[pygame.K_RIGHT]:
            self.directionX = 1
        elif key[pygame.K_LEFT]:
            self.directionX = -1
    
        self.rect.x += self.speedX * self.directionX * 2.5

    def yMove(self):
        key = pygame.key.get_pressed() #gets all boolean values of the keyboard keys
        if key[pygame.K_SPACE] and self.jumping == False:
            self.jumping = True
            self.speedY = -13
        
        

        # Adds gravity to the player
        self.speedY += self.gravity
        self.rect.y += self.speedY




    
    def getRect(self): # returns rect value of player sprite
        return self.rect

        


class Block(pygame.sprite.Sprite):
    def __init__(self,pos,width,height): # pos = position, width,height = width and height of the blocks
        super().__init__()
        self.block_height = width
        self.block_width = height

        # creates an image
        self.image = pygame.Surface([self.block_width,self.block_height])
        self.image.fill((255,255,255))

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(topleft=pos)


####################################################################################################
class Game: # This class will store functions and variables necessary for the gameplay and that manipulate the sprites.
    def __init__(self):
        # level layout 
        # the game screen is going to be split into a grid. The grid is going to be represented by this 2D array
        # Each cell will contain a number that will indicate what should be in each cell 
        # 2 represents a block and 1 represent the player
        # 20 spaces in one row
        self.levelmap = [
            [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0],
            [0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0],
            [0,0,0,2,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
        self.player = pygame.sprite.GroupSingle()# creates a sprite group class that can only contain one sprite which in this case would be player
        # enumerate() returns (index of the value,the actual value)
        for row_index,row in enumerate(self.levelmap):
            for col_index,col in enumerate(row):
                # if an 2 is found then the programme creates a Block class and passes it a certain position in the screen
                if col == 2:
                    block_sprite = Block((col_index*self.unit_width,row_index*self.unit_height),self.unit_width,self.unit_height)
                    self.blocks.add(block_sprite) # Adds the block to the blocks group
                # if a 1 is found then a player class is created and it passes a certain position in the screen
                # then it adds the player into the player group
                elif col == 1:
                    player_sprite = Player((col_index*self.unit_width,(row_index*self.unit_height)))
                    self.player.add(player_sprite)
        
        return self.player, self.blocks
        

    def draw(self,surface): # draws all the sprites within a group to the screen
        self.blocks.draw(surface)
        self.player.draw(surface)




############################# Functions ###################################################
def menu():
    DISPLAYSURF = pygame.display.set_mode((640,704)) # window height and width will be 704x640 pixels
    pygame.display.set_caption("Menu") # sets name of window
    background_img = pygame.image.load("images/background.jpg") # loads the background image
    background = pygame.transform.scale(background_img,(640,704)) # changes size of the image
    
    run = True
    buttonGroup = pygame.sprite.Group()

    startGame = Button("Start")
    #quitGame = Button("Quit")

    buttonGroup.add(startGame)
    

    while run:# main menu loop

        for event in pygame.event.get():# Event handler
            # ends game loop if the top right cross button or the escape key is pressed
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False


        DISPLAYSURF.blit(background,(0,0)) # displays image in screen
        buttonGroup.draw(DISPLAYSURF)
        pygame.display.update() # displays changes made in screen
        

def gameLoop():
    clock = pygame.time.Clock()

    game = Game() # creating an instance of the game class
    playerGroup, blockGroup = game.setUpLevel()

    # creates a pygame window and names it 
    DISPLAYSURF = pygame.display.set_mode((640,704)) # window height and width will be 704x640 pixels
    pygame.display.set_caption("Test window")

    run = True

    while run:# main game loop

        for event in pygame.event.get():# Event handler
            # ends game loop if the top right cross button or the escape key is pressed
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        # updates player position
        playerGroup.update()

        player = playerGroup.sprites()[0] # puts the player sprite within the group inside the variable
        # player y movement
        player.yMove()
            
        # Collision handler for y
        for block in blockGroup.sprites(): #loops every block in the game
            if block.rect.colliderect(player): # checks if the block rect and the player rect have collided returns true if so           #if pygame.sprite.spritecollideany(player,blockGroup):
                                                                                                                                         # use this function if the program gets too slow
                if player.speedY > 0: # going down
                    player.rect.bottom = block.rect.top
                    player.jumpReset()
                elif player.speedY < 0: #going up
                    player.rect.top = block.rect.bottom 
                
                player.speedY = 0 #reset player speed to prevent falling through block 

        # player x movement
        player.xMove()

        # do collision handler for x  
        for block in blockGroup.sprites():
            if block.rect.colliderect(player):
                if player.directionX > 0: # moving right
                    player.rect.right = block.rect.left
                elif player.directionX < 0: # moving left
                    player.rect.left = block.rect.right
                

        # resets the whole screen    
        DISPLAYSURF.fill((0,0,0))

        # draws the player on the screen
        game.draw(DISPLAYSURF)

        # update the screen
        pygame.display.update()
        
        # Caps the framerate to 60 Frames per second
        clock.tick(60)
        
    # Closes all pygame modules
    pygame.quit()

menu()
