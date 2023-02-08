import pygame
import time
pygame.init() # initialises all imported pygame modules

######################################### Menu buttons #######################################################
class Button(pygame.sprite.Sprite):
    def __init__(self,command,pos,img=None):
        super().__init__()
        
        self.command = command
        # creates an image
        if self.command != "settings":
            self.image = pygame.Surface([125,40])
            self.image.fill((255,255,255))
        else:
            # Puts this image in a specific location in the screen
            loadedImage = pygame.image.load(img)
            self.image = pygame.transform.scale(loadedImage,(100,100)) # changes size of the image
            

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(center=pos)

        # Inserts text in buttons
        font = pygame.font.SysFont("Arial",40)
        self.text = font.render(command, True, (0,0,0))

    def getCommand(self):
        return self.command
        
    def update(self):
        mousePos = pygame.mouse.get_pos() # gets mouse position

        if self.command != "settings":
            if self.rect.collidepoint(mousePos): # checks if the position of the mouse is over the button
                self.image.fill((255,0,0)) #fills button with red
            else:
                self.image.fill((255,255,255)) #fills button with white

            # blits text into button
            self.image.blit(self.text,(27,-5))
        
        

############################################ Sprites #########################################################

class Player(pygame.sprite.Sprite): 
    def __init__(self,pos):# pos = position
        super().__init__()# Calls parent class constructor
        
        self.size = (32,52)
        # creates an image
        playerImage = pygame.image.load("images/player/standing.png")
        playerImage = pygame.transform.scale(playerImage,self.size)
        self.image = playerImage

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(topleft = pos)
        
        self.directionX = 0
        self.speedX = 1
        self.speedY = 0

        self.jumping = False
        
        self.gravity = 1

        self.loadPlayerImages() # will load all player images
        self.animaCounter = 0 # animation counter
        self.state = "idle" # current state of the player
        self.animaFrame = 0
        self.facing = "right"
        self.lives = 3 # number of lives the player will have.
        self.start_pos = pos
        
    def takelife(self):
        self.lives -= 1

    def jumpReset(self): # resets jump
        self.jumping = False


    def update(self): # moves player
        # checks for collison between the sides of the screen
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 628:
            self.rect.x = 628

        # performs animation
        self.animation()

        
        self.directionX = 0


    def xMove(self):
        key = pygame.key.get_pressed() #gets all boolean values of the keyboard keys

        if key[pygame.K_RIGHT]:
            self.directionX = 1
            self.state = "running"
        elif key[pygame.K_LEFT]:
            self.directionX = -1
            self.state = "running"
        elif self.jumping == False:
            self.state = "idle"
    
        self.rect.x += self.speedX * self.directionX * 4 # 2.5

    def yMove(self):
        key = pygame.key.get_pressed() #gets all boolean values of the keyboard keys
        if key[pygame.K_SPACE] and self.jumping == False:
            self.jumping = True
            self.speedY = -13
            self.animaCounter = 0
        
        
        

        # Adds gravity to the player
        self.speedY += self.gravity
        self.rect.y += self.speedY
    
    def getRect(self): # returns rect value of player sprite
        return self.rect

    def loadPlayerImages(self): # loads player images
        
        ## idle images #####
        idle1 = pygame.image.load("images/player/idle/1.png")
        idle2 = pygame.image.load("images/player/idle/2.png")
        idle3 = pygame.image.load("images/player/idle/3.png")
        idle4 = pygame.image.load("images/player/idle/4.png")
        self.idleAnima = [pygame.transform.scale(idle1,self.size),
                          pygame.transform.scale(idle2,self.size),
                          pygame.transform.scale(idle3,self.size),
                          pygame.transform.scale(idle4,self.size)]

        # running images ####

        run1 = pygame.image.load("images/player/running/1.png")
        run2 = pygame.image.load("images/player/running/2.png")
        run3 = pygame.image.load("images/player/running/3.png")
        run4 = pygame.image.load("images/player/running/4.png")
        run5 = pygame.image.load("images/player/running/5.png")
        run6 = pygame.image.load("images/player/running/6.png")
        self.runningAnima = [pygame.transform.scale(run1,self.size),
                             pygame.transform.scale(run2,self.size), 
                             pygame.transform.scale(run3,self.size),
                             pygame.transform.scale(run4,self.size),
                             pygame.transform.scale(run5,self.size),
                             pygame.transform.scale(run6,self.size)]
        
        jump1 = pygame.image.load("images/player/jumping/1.png")
        jump2 = pygame.image.load("images/player/jumping/2.png")
        jump3 = pygame.image.load("images/player/jumping/3.png")
        jump4 = pygame.image.load("images/player/jumping/4.png")
        jump5 = pygame.image.load("images/player/jumping/5.png")
        jump6 = pygame.image.load("images/player/jumping/6.png")
        jump7 = pygame.image.load("images/player/jumping/7.png")
        fall = pygame.image.load("images/player/fall.png")
        land = pygame.image.load("images/player/land.png")
        self.jumpingAnima = [pygame.transform.scale(jump1,self.size),
                             pygame.transform.scale(jump2,self.size),
                             pygame.transform.scale(jump3,self.size),
                             pygame.transform.scale(jump4,self.size),
                             pygame.transform.scale(jump5,self.size),
                             pygame.transform.scale(jump6,self.size),
                             pygame.transform.scale(jump7,self.size),
                             pygame.transform.scale(fall,self.size),
                             pygame.transform.scale(land,self.size)

        ]


    def animation(self):
        if self.jumping == True:
            self.state = "jumping"


        ## these if statements set the value of self.facing depending on what direction
        # the player is looking at
        if self.directionX == -1 and self.facing == "right":
            self.facing = "left"

        elif self.directionX == 1 and self.facing == "left":
            self.facing = "right"

        



        self.animaFrame = (self.animaFrame+1) % 6
        if self.animaFrame == 5:
            if self.state == "idle":

                self.animaCounter = (self.animaCounter+1) % len(self.idleAnima) # makes it so animacounter constantly counts up to length of list, resets then repeats
                self.image = self.idleAnima[self.animaCounter] # sets the new image
                if self.facing == "left":
                    self.image = pygame.transform.flip(self.image,True,False)
            
            elif self.state == "running":
                self.animaCounter = (self.animaCounter+1) % len(self.runningAnima) # makes it so animacounter constantly counts up to length of list, resets then repeats
                self.image = self.runningAnima[self.animaCounter] # sets the new image
                if self.facing == "left":
                    self.image = pygame.transform.flip(self.image,True,False)

        if self.state == "jumping":
            if self.animaCounter < len(self.jumpingAnima)-3: #  its minus 3 because last 2 images are the falling image and the landing image
                self.animaCounter += 1
                self.image = self.jumpingAnima[self.animaCounter]
                
                if self.facing == "left":
                    self.image = pygame.transform.flip(self.image,True,False)

            elif self.animaCounter == 6 and self.speedY > 1: # this passes this if statement player is falling 
                self.state = "falling"

            if self.state == "falling":
                self.image = self.jumpingAnima[7]

                if self.facing == "left":
                    self.image = pygame.transform.flip(self.image,True,False)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        
        self.name = "Enemy"
        # creates an image
        self.image = pygame.image.load("images/ufo_enemy.png")

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(topleft = pos)
        
        self.speedY = 2
        self.direction = 1 # positive interger meaning 1

        self.animaCounter = 0 # animation counter

    def xMove(self):
        self.rect.x += self.direction * self.speedY
        self.animaCounter += 1
        
        if self.animaCounter == 60*3: # three seconds in game time as 1 second has 60 frames
            self.flip()

    def flip(self):
        print(self.direction * -1)
        self.direction = self.direction * -1
        self.animaCounter = 0
        self.image = pygame.transform.flip(self.image,True,False)
        print("flipped")
    



class Block(pygame.sprite.Sprite):
    def __init__(self,pos,width,height): # pos = position, width,height = width and height of the blocks
        super().__init__()
        self.block_height = width
        self.block_width = height


        # loads and resizes an image
        loadedImage = pygame.image.load("images/brick.jpg")
        self.image = pygame.transform.scale(loadedImage,(self.block_width,self.block_height))

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(topleft=pos)

class Goal(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        
        # loads images
        closed = pygame.image.load("images/door/1.png")
        opened = pygame.image.load("images/door/2.png")
        self.doorAnima = [pygame.transform.scale(closed,(32,60)), 
                     pygame.transform.scale(opened,(32,52))]

        self.state = "close"
        self.enter = False

        # creates an image
        self.image = self.doorAnima[0]

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(topleft = pos)

    def switch(self):
        self.state = "open"
    
    def animation(self):
        if self.state == "close":
            self.image = self.doorAnima[0]
        if self.state == "open":
            self.image = self.doorAnima[1]
        

    def update(self):
        self.animation()
        self.state = "close"

class Spike(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()

        self.name = "spike"

        loadedImage = pygame.image.load("images/spikes.png")
        self.image = pygame.transform.scale(loadedImage,size)
        self.rect = self.image.get_rect(topleft=pos)
    


####################################################################################################
class Game: # This class will store functions and variables necessary for the gameplay and that manipulate the sprites.
    def __init__(self):
        # level layout 
        # the game screen is going to be split into a grid. The grid is going to be represented by this 2D array
        # Each cell will contain a number that will indicate what should be in each cell 
        # 2 represents a block and 1 represent the player 3 for goal 4 for enemy 5 for spikes
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
            [0,0,2,0,0,0,0,0,0,0,0,0,0,2,3,2,0,0,0,0],
            [0,0,0,2,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,2,2,0,0,5,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
            [0,0,0,0,0,0,2,2,2,2,0,0,2,0,0,0,0,2,0,0],
            [0,0,0,0,0,2,2,0,0,2,0,0,2,2,2,2,2,2,0,0],
            [2,2,0,2,2,2,2,0,0,2,0,0,2,2,2,2,2,2,0,0],        
        ] 

        # the game screen is going to be split into a grid. The grid is going to be represent
        self.unit_height = 32
        self.unit_width = 32
        

    def setUpLevel(self): # This function creates all the sprites that are going to be used in this game
        self.blocks = pygame.sprite.Group()# creates a group that will contain all the block sprites
        self.player = pygame.sprite.GroupSingle()# creates a sprite group class that can only contain one sprite which in this case would be player
        self.goal = pygame.sprite.Group() # will contain all the end goal sprites
        self.danger = pygame.sprite.Group() # will store dangerous objects sprites like spikes and enemies
        # enumerate() returns (index of the value,the actual value)
        for row_index,row in enumerate(self.levelmap):
            for col_index,col in enumerate(row):
                # if an 2 is found then the programme creates a Block class and passes it a certain position in the screen
                if col == 2: # Block
                    block_sprite = Block((col_index*self.unit_width,row_index*self.unit_height),self.unit_width,self.unit_height)
                    self.blocks.add(block_sprite) # Adds the block to the blocks group
                # if a 1 is found then a player class is created and it passes a certain position in the screen
                # then it adds the player into the player group
                elif col == 1: #player
                    print(2)
                    player_sprite = Player((col_index*self.unit_width,(row_index*self.unit_height)))
                    self.player.add(player_sprite)
                elif col == 3: # Goal
                    print(2)
                    endGoal_sprite = Goal(((col_index*self.unit_width)-1,(row_index*self.unit_height)-25))
                    self.goal.add(endGoal_sprite)
                elif col == 4: # Enemy
                    enemy_sprite = Enemy((col_index*self.unit_width,(row_index*self.unit_height)))
                    self.danger.add(enemy_sprite)
                elif col == 5: # Spike
                    spike_sprite = Spike(((col_index*self.unit_width)-1,(row_index*self.unit_height)),(self.unit_width,self.unit_height))
                    self.danger.add(spike_sprite)
        print(3)
        return self.player, self.blocks, self.goal, self.danger
        

    def draw(self,surface): # draws all the sprites within a group to the screen
        self.blocks.draw(surface)
        self.player.draw(surface)
        self.goal.draw(surface)
        self.danger.draw(surface)




############################# Functions ###################################################
def menu():
    DISPLAYSURF = pygame.display.set_mode((640,704)) # window height and width will be 704x640 pixels
    pygame.display.set_caption("Menu") # sets name of window
    background_img = pygame.image.load("images/background.jpg") # loads the background image
    background = pygame.transform.scale(background_img,(640,704)) # changes size of the image
    
    run = True
    buttonGroup = pygame.sprite.Group()

    startGame = Button("start",(320,230))
    selectGame = Button("select",(320,330))
    quitGame = Button("quit",(320,430))
    options = Button("settings",(585,650),"images/gear_Icon.png")

    buttonGroup.add(startGame)
    buttonGroup.add(selectGame)
    buttonGroup.add(quitGame)
    buttonGroup.add(options)

    

    while run:# main menu loop
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():# Event handler
            # ends game loop if the top right cross button or the escape key is pressed
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in buttonGroup.sprites():
                    if button.rect.collidepoint(mousePos):
                        return button.getCommand()
                
        buttonGroup.update()

        DISPLAYSURF.blit(background,(0,0)) # displays image in screen
        buttonGroup.draw(DISPLAYSURF)
        pygame.display.update() # displays changes made in screen
        
print(1)
def gameLoop():
    clock = pygame.time.Clock()

    game = Game() # creating an instance of the game class
    playerGroup, blockGroup, goalGroup, dangerGroup = game.setUpLevel()

    for sprite in dangerGroup.sprites(): # searches for enemy sprite and stores it in the variable enemy
        if sprite.name == "Enemy":
            print("found")
            enemy = sprite


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
        
        ####################################### Collisions ##############################################################

        ################################ player/enemy collisions with blocks #######################################
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
        # enemy x movement
        enemy.xMove()

        # do collision handler for x  
        for block in blockGroup.sprites():
            if block.rect.colliderect(player):
                if player.directionX > 0: # moving right
                    player.rect.right = block.rect.left
                elif player.directionX < 0: # moving left
                    player.rect.left = block.rect.right
            
            if block.rect.colliderect(enemy):
                if enemy.direction == -1: # moving left
                    enemy.rect.left = block.rect.right
                elif enemy.direction == 1: # moving right
                    enemy.rect.right = block.rect.left 
                enemy.flip()


        ###################### endGoal collisions ###########################
        endGoal_sprite = goalGroup.sprites()[0]

        if endGoal_sprite.rect.colliderect(player):
            endGoal_sprite.switch()

            if pygame.key.get_pressed()[pygame.K_RETURN]:# checks if the key e has been pressed on the keyboard
                run = False # exits game loop
            
        endGoal_sprite.update()

        
        ###################################### end of collisions ##################################################### 

        #################### Dangerous Objects  ##########################
        # collision function returns an empty dictionary, the bool function returns False if a dictionary is empty
        if bool(pygame.sprite.groupcollide(playerGroup,dangerGroup,False,False)) == True: 
            player.takelife() # takes one life
            player.rect.topleft = player.start_pos
            

        ### pit fall ##
        if player.rect.y > DISPLAYSURF.get_height(): # checks if player has fallen out the screen by comparing
            run = False                              # the players y value and screen height.

        ### enemy object ####
        

               

        # resets the whole screen    
        DISPLAYSURF.fill((0,0,0))

        # draws the player on the screen
        game.draw(DISPLAYSURF)
        pygame.draw.rect(DISPLAYSURF,(255,0,0),player.rect,1)

        # update the screen
        pygame.display.update()
        
        # Caps the framerate to 60 Frames per second
        clock.tick(60)

        if player.lives == 0: #ends the game is if the player has no lives left
            run = False
        
    # Closes all pygame modules
    pygame.quit()


# action = menu()

# if action == "start":
#     gameLoop()
# elif action == "select":
#     pass
# elif action == "quit":
#     pass
# elif action == "settings":
#     pass

gameLoop()