import pygame

map =[[1,1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1], [1,1,0,1,1,1,1,1,0,1], [1,0,0,0,0,0,1,0,0,1],[1,0,1,1,1,0,1,0,0,1],[1,0,1,1,1,0,1,0,0,1], [1,0,1,1,1,0,1,0,0,1], [1,0,0,0,0,0,0,0,0,1], [1,1,1,1,1,1,1,1,1,1]]

class tile(pygame.sprite.Sprite):

    def __init__(self, color, width, height, x_ref, y_ref):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        self.speedx = 0
        self.speedy = 0
        self.oldx = 20
        self.oldy = 20
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy   
    
    def move(self, speed, dir):
        if dir == 0:
            self.speedx = speed
        elif dir == 1:
            self.speedy = speed
        elif dir == 2:
            self.speedx = 0
            self.speedy = 0

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50, 255)
YELLOW = (255,255,0)
RED = (255,50,50)
DARKBLUE = (0,0, 150)

pygame.init()

# -- Blank Screen
size = (640, 400)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
surface = pygame.display.set_caption("Snow")
# -- Exit game flag set to False
done = False
# -- Manages how fast screen refresh
clock = pygame.time.Clock()
pacman = Player()

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(pacman)

wall_list = pygame.sprite.Group()

for y in range(10):
    for x in range(10):
        if map[x][y] == 1:
            my_wall = tile(BLUE, 20, 20, x*20, y * 20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman.move(-1,1)
            elif event.key == pygame.K_RIGHT:
                pacman.move(1,0)
            elif event.key == pygame.K_DOWN:
                pacman.move(1,1)
            elif event.key == pygame.K_LEFT:
                pacman.move(-1,0)
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                pacman.move(0,2)

    all_sprites_list.update()
    player_hit_list = pygame.sprite.spritecollide(pacman, wall_list,False)

    for foo in player_hit_list:
        pacman.move(0, 2)
        pacman.rect.x = pacman.oldx
        pacman.rect.y = pacman.oldy
    pacman.oldx = pacman.rect.x
    pacman.oldy = pacman.rect.y

    
    screen.fill(BLACK)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
#Endwhile
pygame.quit()
