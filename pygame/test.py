import pygame



pygame.init()


while True:
    screen = pygame.display.set_mode((500,500))
    im = pygame.image.load('spI.png').convert()
    alpha = 128
    im.fill((125,125,125, alpha), None, pygame.BLEND_RGBA_MULT)
    im = pygame.transform.scale(im, (100,100))
    screen.fill((125,125,125))
    
    screen.blit(im, (0, 0))
    pygame.display.flip()