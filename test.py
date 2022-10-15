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

print(p.rect.top)
