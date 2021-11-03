import pygame, random,time
# --Global Constant

# -- Color 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50, 255)
YELLOW = (255,255,0)
RED = (255,50,50)
DARKBLUE = (0,0, 150)
RED = (255,0,0)
VICTORYCONDITION = 100
INVADERSPEED = 2

class Invader(pygame.sprite.Sprite):
    
    def __init__(self, speed):

        super().__init__()
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load("invader.png"), (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,600)
        self.rect.y = random.randint(-100, 0)
        self.x =self.rect.x
        self.y = self.rect.y
        self.lives = 2

    def update(self):
        global invader_group, all_sprites_group
        self.rect.y += self.speed
        if self.rect.y >= size[1]:
            self.kill()
            invader_group, all_sprites_group = generate(1, invader_group, all_sprites_group)
    def damage(self, damage):
        self.lives += damage
        return self.lives

class Player(pygame.sprite.Sprite):
    
    def __init__(self,color, width, height):

        super().__init__()
        self.speed = 0
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = size[1]- height
        self.lives = 5  
        self.bullet_count = 70
        self.score = 0
        self.time = False

    def update(self):
        self.rect.x += self.speed
        if self.rect.x <=0:
            self.rect.x =0
        if self.rect.x >= size[0] - self.width:
            self.rect.x = size[0] -self.width

    def player_set_speed(self, speed):
        self.speed = speed
    
    def change_bullet(self, number):
        self.bullet_count += number

    def getBulletCount(self):
        return self.bullet_count
    

class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, xcoor, ycoor):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 2
        self.image = pygame.Surface([2,2])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = xcoor
        self.rect.y = ycoor

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
def generate(numberOfInvaders, invader_group, all_sprites_group):
    for i in range(numberOfInvaders):
        invader = Invader(INVADERSPEED)
        collide = pygame.sprite.spritecollide(invader,invader_group,False)
        while len(collide) > 0:
            invader.rect.x = random.randint(0,600)
            invader.rect.y = random.randint(-100, 0)
            collide = pygame.sprite.spritecollide(invader,invader_group,False)
        invader_group.add(invader)
        all_sprites_group.add(invader) 
    return invader_group, all_sprites_group
# -- Initialize pygame
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
xspeed = 5
player = Player(YELLOW, 10, 10)
invader_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
numberOfInvaders = 10
invader_group, all_sprites_group = generate(numberOfInvaders, invader_group, all_sprites_group)
### -- Game loop
bullet_group = pygame.sprite.Group()
score_coor = (10, 10)
lives_coor = (10, 50)
bullet_coor = (10, 90)

font = pygame.font.Font("freesansbold.ttf", 20)
victory = False
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            if player.score >= 20:
                victory  = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_set_speed(-5)
            elif event.key == pygame.K_RIGHT:
                player.player_set_speed(5)
            elif event.key == pygame.K_UP:
                if player.getBulletCount() >0:
                    bullet = Bullet(RED, player.rect.x + 5, player.rect.y)
                    player.change_bullet(-1)
                    bullet_group.add(bullet)
                    all_sprites_group.add(bullet)
            elif event.key == pygame.K_r:
                player.time = pygame.time.get_ticks()
                player.bullet_count = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0)
            
        #Endif
    #Next event
    #--Game logic goes after this comment
    all_sprites_group.update()
    player_hit_group=pygame.sprite.spritecollide(player,invader_group,False)
    bullet_hit_group = pygame.sprite.groupcollide(bullet_group,invader_group,True, False)
    for bullet in bullet_hit_group:
        invader_hit_group=pygame.sprite.spritecollide(bullet,invader_group,False)
        for hit in invader_hit_group:
            hp = hit.damage(-1)
            if hp <= 0:
                hit.kill()
                invader_group, all_sprites_group = generate(1, invader_group, all_sprites_group)
                player.score += 1
    for foo in player_hit_group:
        player.lives=player.lives-1
        foo.kill()
        invader_group, all_sprites_group = generate(1, invader_group, all_sprites_group) 
    current_time = pygame.time.get_ticks()
    if type(player.time) == type(1):
        if current_time - player.time >= 1400:
            player.bullet_count = 50
            player.time = False

    player.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_group.draw(screen)
    bullet_group.draw(screen)
    screen.blit(player.image, (player.rect.x, player.rect.y))
    scoretxt = font.render("Score: "+ str(player.score), True, WHITE)
    screen.blit(scoretxt, score_coor)
    lifetxt = font.render("life: "+ str(player.lives), True, WHITE)
    screen.blit(lifetxt, lives_coor) 
    bullettxt = font.render("bullets: "+ str(player.bullet_count), True, WHITE)
    screen.blit(bullettxt, bullet_coor) 
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
    if player.lives <= 0 or player.score >= VICTORYCONDITION:
        if player.score >= VICTORYCONDITION:
            victory = True
        done = True
#Endwhile
screen.fill(BLACK)
pygame.font.Font("freesansbold.ttf", 500)
resulttxt = font.render("VICTORY" if victory else "DEFEAT", True, WHITE)
screen.blit(resulttxt, (size[0]/2-50, size[1]/2)) 
pygame.display.flip()
time.sleep(2)
pygame.quit()