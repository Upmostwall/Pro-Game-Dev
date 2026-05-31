import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

screen.fill(white)

class myCircle:
    def __init__(self, color, pos, rad, wid = 0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.scrn = screen

    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

    def grow(self, x):
        self.rad = x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

position = (300, 300)
radius = 50
wid = 2
pygame.draw.circle(screen, red, position, radius, wid)
pygame.display.update()

bluecircle = myCircle(blue, position, radius + 60)
redcircle = myCircle(red, position, radius + 40)
yellowcircle = myCircle(yellow, position, radius, 5)
greencircle = myCircle(green, position, 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bluecircle.draw()
            redcircle.draw()
            yellowcircle.draw()
            greencircle.draw()
            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            bluecircle.grow(2)
            redcircle.grow(2)
            yellowcircle.grow(2)
            greencircle.grow(2)
            pygame.display.update()

        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            blackcircle = myCircle(black, pos, 5)
            blackcircle.draw()
            pygame.display.update()

pygame.quit()