import pygame
class Player(pygame.sprite.Sprite): 
    def __init__(self,pos):# pos = position
        super().__init__()# Calls parent class constructor
        
        # creates an image
        self.image = pygame.Surface([12,32]) 
        self.image.fill((255,0,0))

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(topleft = pos)
        
        self.speedX = 1
        self.speedY = 0

        self.jumping = False
        
        self.gravity = 1


p = Player((3,3))

print(p.rect)

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
        #Do y movement
        player.yMove()
        # Collision handler for y
        for block in blockGroup.sprites(): #loops every block in the game
            if block.rect.colliderect(player): # checks if the block rect and the player rect have collided returns true if so
                if player.speedY > 0: # going down
                    print("bottom")
                    player.rect.bottom = block.rect.top
                    player.jumpReset()
                elif player.speedY < 0: #going up
                    print("top")
                    player.rect.top = block.rect.bottom 
                
                player.speedY = 0 #reset player speed to prevent falling through block 

        # Do x movement
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