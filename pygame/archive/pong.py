import pygame, math
# --Global Constant

# -- Color 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50, 255)
YELLOW = (255,255,0)
RED = (255,50,50)
DARKBLUE = (0,0, 150)

# -- Initialize pygame
pygame.init()

# -- Blank Screen
size = (640, 400)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
surface = pygame.display.set_caption("Pong")
# -- Exit game flag set to False
done = False
sun_x = 40
sun_y = 100
sun_flag = True
ballWidth = 20
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1
# -- Manages how fast screen refresh
clock = pygame.time.Clock()

### -- Game loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Endif
    #Next event
    #--Game logic goes after this comment
    x_val += x_direction
    y_val += y_direction
    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    # screen, [red, blue, green], (left, top, width, height))
    pygame.draw.rect(screen,BLACK, (0,0, size[0],size[1]))
    pygame.draw.rect(screen,BLUE,(x_val, y_val,ballWidth,ballWidth))

    # circle(surface, color, center, radius, width)
    pygame.draw.circle(screen,YELLOW,(sun_x,sun_y),40,0)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
    if sun_x > size[0] + 40 or sun_x < -40:
        screen.fill(DARKBLUE)
        pygame.display.update()
        pygame.time.delay(100)
#Endwhile
pygame.quit()