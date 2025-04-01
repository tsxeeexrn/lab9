import pygame, sys, random, time

pygame.init()
FPS = 60
clock = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
SPEED, SCORE, COINS = 3, 0, 0
c1, c2, c3, c4, c5 = False, False, False, False, False

font = pygame.font.SysFont("Verdana", 20)
background = pygame.image.load("AnimatedStreet.png")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("coin.png"), (40, 40))
        self.rect = self.image.get_rect(
            center=(random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40)))

    def reset_position(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect(center=(160, 520))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0: self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH: self.rect.move_ip(5, 0)
        if keys[pygame.K_UP] and self.rect.top > 0: self.rect.move_ip(0, -5)
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT: self.rect.move_ip(0, 5)


P1, E1, C1 = Player(), Enemy(), Coin()
enemies, coins, all_sprites = pygame.sprite.Group(E1), pygame.sprite.Group(C1), pygame.sprite.Group(P1, E1, C1)
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

background_y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT + 1:
            SPEED += 0.1

    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(2)

    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        C1.reset_position()

    if not c1 and COINS >= 3: SPEED += 1; c1 = True
    if not c2 and COINS >= 8: SPEED += 1; c2 = True
    if not c3 and COINS >= 13: SPEED += 1; c3 = True
    if not c4 and COINS >= 18: SPEED += 1; c4 = True
    if not c5 and COINS >= 23: SPEED += 1; c5 = True

    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    screen.blit(font.render(str(SCORE), True, (0, 0, 0)), (10, 10))
    screen.blit(font.render(str(COINS), True, (0, 0, 0)), (370, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        if isinstance(entity, Player) or isinstance(entity, Enemy):
            entity.move()

    pygame.display.update()
    clock.tick(FPS)
