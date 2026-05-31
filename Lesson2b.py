import pygame, random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Circle!")

WHITE = (255, 255, 255)

circlex = 300
circley = 200
radius = 40
circle_color = (0, 128, 255)

running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            
            distance = ((mousex - circlex) ** 2 + (mousey - circley) ** 2) ** 0.5
        
            if distance <= radius:
                circle_color  = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )

    pygame.draw.circle(screen, circle_color, (circlex, circley), radius)
    pygame.display.update()
pygame.quit()