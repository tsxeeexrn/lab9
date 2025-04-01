import pygame

pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

screen.fill(WHITE)
clock = pygame.time.Clock()

drawing = False
color = BLACK
size = 20
shape = "circle"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_e:
                color = WHITE
            elif event.key == pygame.K_UP:
                size += 5
            elif event.key == pygame.K_DOWN:
                size = max(5, size - 5)
            elif event.key == pygame.K_s:
                shape = "square"
            elif event.key == pygame.K_t:
                shape = "triangle"
            elif event.key == pygame.K_y:
                shape = "equilateral"
            elif event.key == pygame.K_h:
                shape = "rhombus"
            elif event.key == pygame.K_c:
                shape = "circle"
            elif event.key == pygame.K_x:
                screen.fill(WHITE)

    if drawing:
        x, y = pygame.mouse.get_pos()
        if shape == "circle":
            pygame.draw.circle(screen, color, (x, y), size)
        elif shape == "square":
            pygame.draw.rect(screen, color, (x - size, y - size, size * 2, size * 2))
        elif shape == "triangle":
            pygame.draw.polygon(screen, color, [(x - size, y + size), (x + size, y + size), (x, y - size)])
        elif shape == "equilateral":
            pygame.draw.polygon(screen, color, [(x, y - size), (x - size, y + size), (x + size, y + size)])
        elif shape == "rhombus":
            pygame.draw.polygon(screen, color, [(x, y - size), (x - size, y), (x, y + size), (x + size, y)])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
