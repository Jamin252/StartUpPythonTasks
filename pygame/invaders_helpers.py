import pygame, random, math
# --Global Constant

# -- Color 
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,50,50)
VICTORYCONDITION = 100
INVADERSPEED = 1
BULLETCOUNT = 70
INVADERLIVES = 2
NUMOFINVADERS = 10
SIZE = (640, 400)

class Invader(pygame.sprite.Sprite):
    
    def __init__(self, speed):

        super().__init__()
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load("invader.png").convert_alpha(), (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100,500)
        self.rect.y = random.randint(-100, 0)
        self.lives = INVADERLIVES

    def update(self, game):
        oldx = self.rect.x
        self.rect.x += game.invader_group_hspeed
        self.rect.y += self.speed
        if self.rect.y >= SIZE[1]:
            self.respawn(game)
        if any(item.rect.x >= SIZE[0] - 50 or item.rect.x <= 0 for item in game.invader_group):
            self.rect.x = oldx
            game.invader_changeDirection = True

    
    def respawn(self, game):
        self.rect.x = random.randint(0,600)
        self.rect.y = random.randint(-100, 0)
        collide = pygame.sprite.spritecollide(self,game.invader_group,False)
        while len(collide) > 1:
            self.rect.x = random.randint(0,600)
            self.rect.y = random.randint(-100, 0)
            collide = pygame.sprite.spritecollide(self,game.invader_group,False)

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
        self.rect.y = SIZE[1]- height
        self.lives = 5  
        self.bullet_count = BULLETCOUNT
        self.score = 0
        self.reloadTime = False
        self.produce_bullet = False
        self.bulletTemp = 0
        self.bullet_groupP = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x <=0:
            self.rect.x =0
        if self.rect.x >= SIZE[0] - self.width:
            self.rect.x = SIZE[0] -self.width

    def player_set_speed(self, speed):
        self.speed = speed
    
    def change_bullet(self, number):
        self.bullet_count += number

    def getBulletCount(self):
        return self.bullet_count
    
    def keyResponse(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player_set_speed(-5)
            if event.key == pygame.K_RIGHT:
                self.player_set_speed(5)
            if event.key == pygame.K_SPACE:
                self.produce_bullet = True
                self.bulletTemp = 0
            if event.key == pygame.K_r:
                self.reloadTime = pygame.time.get_ticks()
                self.bullet_count = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.player_set_speed(0)
            if event.key == pygame.K_SPACE:
                self.produce_bullet = False
    
    def checkReload(self):
        current_time = pygame.time.get_ticks()
        if type(self.reloadTime) == type(1):
            if current_time - self.reloadTime >= 1400:
                self.bullet_count = 50
                self.reloadTime = False


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


class Scoreboard():

    def __init__(self):
        self.score_coor = (10, 10)
        self.lives_coor = (10, 50)
        self.bullet_coor = (10, 90)
        self.time_coor = (10, 130)
        self.font = pygame.font.Font("freesansbold.ttf", 20)
        self.startTime = pygame.time.get_ticks()
        self.timeNow = 0

    def draw(self,screen,player):
        scoretxt = self.font.render("Score: "+ str(player.score), True, WHITE)
        screen.blit(scoretxt, self.score_coor)
        lifetxt = self.font.render("life: "+ str(player.lives), True, WHITE)
        screen.blit(lifetxt, self.lives_coor) 
        bullettxt = self.font.render("bullets: "+ str(player.bullet_count), True, WHITE)
        screen.blit(bullettxt, self.bullet_coor) 
        timetxt = self.font.render("Time: "+ str(round(self.timeNow/1000, 1)), True, WHITE)
        screen.blit(timetxt, self.time_coor) 


class Game():

    def __init__(self):
        self.size = SIZE
        self.screen = pygame.display.set_mode(self.size)
        self.surface = pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.all_sprites_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.invader_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.scoreBoard = Scoreboard()
        player = Player(YELLOW, 10, 10)
        self.player_group.add(player)
        self.all_sprites_group.add(player)
        self.generate(NUMOFINVADERS)
        self.victory = False
        self.invader_group_hspeed = 1
        self.invader_changeDirection = False
        
        
    def generate(self, numberOfInvaders):
        for i in range(numberOfInvaders):
            invader = Invader(INVADERSPEED)
            collide = pygame.sprite.spritecollide(invader,self.invader_group,False)
            while len(collide) > 0:
                invader.rect.x = random.randint(0,600)
                invader.rect.y = random.randint(-100, 0)
                collide = pygame.sprite.spritecollide(invader,self.invader_group,False)
            self.invader_group.add(invader)
            self.all_sprites_group.add(invader) 
    
    def startScreen(self):
        tempTime = pygame.time.get_ticks()
        timeDiff = pygame.time.get_ticks() - tempTime
        timeTxt = None
        font = pygame.font.Font("freesansbold.ttf", 1000)
        while timeDiff < 4000:
            timeTxt = font.render(str(math.floor(4 - timeDiff/1000)), True, WHITE)
            self.screen.fill(BLACK)
            self.screen.blit(timeTxt,(SIZE[0]/2, SIZE[1]/2))
            pygame.display.flip()
            timeDiff = pygame.time.get_ticks() - tempTime
    
    def setTimeNow(self):
        self.scoreBoard.timeNow = pygame.time.get_ticks() - self.scoreBoard.startTime
    
    def keyResponse(self,event):
        for player in self.player_group:
            player.keyResponse(event)
    
    def logic(self):
        self.produce_bullet()
        self.invader_group.update(self)
        self.checkInvaderDirection()
        self.player_group.update()
        self.bullet_group.update()
        self.bulletInvaderInteraction()
        self.playerInvaderInteraction()
        self.checkReload()
        
    def checkInvaderDirection(self):
        if self.invader_changeDirection:
            self.invader_group_hspeed *= -1
        self.invader_changeDirection = False

    def produce_bullet(self):
        for tempplayer in self.player_group:
            if tempplayer.produce_bullet and tempplayer.getBulletCount() > 0 and tempplayer.bulletTemp % 15 == 0:
                bullet = Bullet(RED, tempplayer.rect.x + 5, tempplayer.rect.y)
                tempplayer.change_bullet(-1)
                tempplayer.bullet_groupP.add(bullet)
                self.bullet_group.add(bullet)
                self.all_sprites_group.add(bullet)
            if tempplayer.produce_bullet:
                tempplayer.bulletTemp += 1
    
    def bulletInvaderInteraction(self):
        for tempPlayer in self.player_group:
            bullet_hit_group = pygame.sprite.groupcollide(tempPlayer.bullet_groupP,self.invader_group,True, False)
            for bullet in bullet_hit_group:
                invader_hit_group=pygame.sprite.spritecollide(bullet,self.invader_group,False)
                for hit in invader_hit_group:
                    hp = hit.damage(-1)
                    if hp <= 0:
                        hit.respawn(self)
                        tempPlayer.score += 1
    
    def playerInvaderInteraction(self):
        for tempPlayer in self.player_group:
            player_hit_group=pygame.sprite.spritecollide(tempPlayer,self.invader_group,False)
            for foo in player_hit_group:
                tempPlayer.lives=tempPlayer.lives-1
                foo.respawn(self)
    
    def checkReload(self):
        for tempPlayer in self.player_group:
            tempPlayer.checkReload()

    def drawScreen(self):
        self.screen.fill(BLACK)

        # -- Draw here
        self.drawSprite()
        self.drawScoreboard()
        pygame.display.flip()
    
    def drawSprite(self):
        self.all_sprites_group.draw(self.screen)
    
    def drawScoreboard(self):
        for player in self.player_group:
            self.scoreBoard.draw(self.screen, player)

    def finishCondition(self):
        if any(player.lives <= 0 or player.score >= VICTORYCONDITION for player in self.player_group):
            if any(player.score >= VICTORYCONDITION for player in self.player_group):
                self.victory = True
            return True
        return False
    
    def finishScreen(self):
        self.screen.fill(BLACK)
        font = pygame.font.Font("freesansbold.ttf", 50)
        resulttxt = font.render("VICTORY" if self.victory else "DEFEAT", True, WHITE)
        self.screen.blit(resulttxt, (SIZE[0]/2-50, SIZE[1]/2)) 
        pygame.display.flip()
        tempTime = pygame.time.get_ticks()
        while pygame.time.get_ticks() - tempTime < 2000:
            pass
    
    def play(self):

        done = False
        while not done:
            self.setTimeNow()
            # -- User input and controls
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                self.keyResponse(event)
                    
                #Endif
            #Next event
            #--Game logic goes after this comment
            self.logic()
            # -- Screen background is BLACK
            self.drawScreen()
            self.clock.tick(60)
            # - The clock ticks over
            done = True if self.finishCondition() else done
        #Endwhile
        self.finishScreen()



def runGame():
    pygame.init()

    game = Game()
    game.play()
    pygame.quit()