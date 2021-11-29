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
    
    def __init__(self,color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,600)
        self.rect.y = random.randint(0,400)

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
    my_snow = Snow(WHITE, 5, 5)
    snow_group.add(my_snow)
    all_sprites_group.add(my_snow)  

### -- Game loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Endif
    #Next event
    #--Game logic goes after this comment
    if sun_x >= size[0] + 60:
        sun_x = 0
    sun_x += xspeed
    sun_y = -math.sqrt(abs((size[0]/2 + 60) ** 2 - (sun_x - size[0] / 2) ** 2)) + size[1] / 2
    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    # screen, [red, blue, green], (left, top, width, height))
    all_sprites_group.draw(screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
#Endwhile
pygame.quit()