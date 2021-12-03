import pygame, math, random
# --Global Constant

# -- Color 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50, 255)
YELLOW = (255,255,0)
RED = (255,50,50)
DARKBLUE = (0,0, 150)

class Invader(pygame.sprite.Sprite):
    
    def __init__(self,color, width, height, speed):

        super().__init__()
        self.speed = speed
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,600)
        self.rect.y = random.randint(-50, 0)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= size[1]:
            self.rect.y = 0

class Player(pygame.sprite.Sprite):
    
    def __init__(self,color, width, height):

        super().__init__()
        self.speed = 0
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = size[1]- height

    def update(self):
        self.rect.x += self.speed

    def player_set_speed(self, speed):
        self.speed = speed

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
player = Player(YELLOW, 10, 10)
invader_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
numberOfInvaders = 10
for i in range(numberOfInvaders):
    invader = Invader(WHITE, 5, 5, 1)
    invader_group.add(invader)
    all_sprites_group.add(invader)  
### -- Game loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_set_speed(-3)
            elif event.key == pygame.K_RIGHT:
                player.player_set_speed(3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0)
            
        #Endif
    #Next event
    #--Game logic goes after this comment
    all_sprites_group.update()
    player_hit_group=pygame.sprite.spritecollide(player,invader_group,True)
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