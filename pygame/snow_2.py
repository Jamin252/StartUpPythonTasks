import pygame, math, random
# --Global Constant

# -- Color 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50, 255)
YELLOW = (255,255,0)
RED = (255,50,50)
DARKBLUE = (0,0, 150)

class Snow(pygame.sprite.Sprite):
    
    def __init__(self,color, width, height, speed):

        super().__init__()
        self.speed = speed
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,600)
        self.rect.y = random.randint(0,400)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= size[1]:
            self.rect.y = 0


# -- Initialize pygame
pygame.init()

# -- Blank Screen
size = (640, 400)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
surface = pygame.display.set_caption("Snow")
# -- Exit game flag set to False
done = False
sun_x = 40
sun_y = 100
sun_flag = True
# -- Manages how fast screen refresh
clock = pygame.time.Clock()
xspeed = 5
snow_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
numberOfFlakes = 50
for i in range(numberOfFlakes):
    my_snow = Snow(WHITE, 5, 5, 1)
    collide = pygame.sprite.spritecollide(my_snow,snow_group,True)
    while len(collide) > 0:
        my_snow.kill()
        my_snow = Snow(WHITE, 5, 5, 1)
        collide = pygame.sprite.spritecollide(my_snow,snow_group,True)
    snow_group.add(my_snow)
    all_sprites_group.add(my_snow)  

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Endif
    #Next event
    #--Game logic goes after this comment
    all_sprites_group.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_group.draw(screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
#Endwhile
pygame.quit()