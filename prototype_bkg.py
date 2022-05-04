import pygame
pygame.init() # initialises all imported pygame modules

clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite): 
    def __init__(self,pos):# pos = position
        super().__init__()# Calls parent class constructor
        
        # creates an image and fills the image in with a colour
        self.image = pygame.Surface([50,75]) 
        self.image.fill((255,0,0))

        # Puts this image in a specific location in the screen
        self.rect = self.image.get_rect(topleft = pos)

        # self.direction = pygame.math.Vector2(0,0)

    # def get_input(self):
    #     keys = pygame.key.get_pressed()

    #     if keys[pygame.K_RIGHT]:
    #         self.direction.x = 1
    #     else:
    #         self.direction.x = 0

# level layout 
# X represents the block and P represents the player
level = [
    "X    ",
    " X   ",
    "     ",
    "PXXX ",
    "X   X",
    "X    ",
    "     ",
    "     ",
    "     ",
]

# This is a function that puts each object in a certain position in the screen depending on where the letters are in the string
def draw_background(backg,surface,size):

    player = pygame.sprite.GroupSingle()# creates a sprite group class that can only contain one sprite which in this case would be player
    # enumerate() returns (index of the value,the actual value)
    for row_index,row in enumerate(backg):
        for col_index,col in enumerate(row):
            # if an X is found then the programme draws a square in a certain position in the screen
            if col == "X":
                pygame.draw.rect(surface,(255,255,255),(col_index*size,row_index*size,100,100))
            # if a P is found then a player class is created with and it passes a certain position in the screen
            # then it adds the player into the player group
            elif col == "P":
                player_sprite = Player((col_index*100,(row_index*100)+25))
                player.add(player_sprite)

    return player
                

            
                
  
        
# for row in enumerate(level):
#     print(row)
#     for col in enumerate(row[1]):
#         print(col)

    

# charateristics of the block
posx = 100
posy = 100
height = 100
width = 100

# creates a pygame window and names it
DISPLAYSURF = pygame.display.set_mode((500,height*len(level)))
pygame.display.set_caption("TEst window")

run = True



player = draw_background(level,DISPLAYSURF,height)

while run:# main game loop
    
    for event in pygame.event.get():# Event handler
        # ends game loop if the top right cross button or the escape key is pressed
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    
    # draws the player on the screen
    player.draw(DISPLAYSURF)

    # update the screen
    pygame.display.update()
    
    # Caps the framerate to 60 Frames per second
    clock.tick(60)
    

pygame.quit()
