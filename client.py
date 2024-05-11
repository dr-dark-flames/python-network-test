from network import Network
from player import *

width = 500
height = 500


pygame.display.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redraw(surface, p1, p2):
    surface.fill((255, 255, 255))
    p1.draw(surface)
    p2.draw(surface)
    pygame.display.update()


def main(surface):
    n = Network()
    p1 = n.get_pos()

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = n.send(p1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        p1.move()
        redraw(surface, p1, p2)


main(win)
pygame.quit()
