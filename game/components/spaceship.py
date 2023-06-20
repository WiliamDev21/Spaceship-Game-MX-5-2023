import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT,BULLET_PLAYER_TYPE


class Spaceship:
    WIDHT = 40
    HEIGTH = 60
    X_POS = (SCREEN_WIDTH//2)-WIDHT
    Y_POS = 450

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(
            self.image, (self.WIDHT, self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.life = 50
        self.is_alive = True
        self.FIRE_RATE=7
        self.fire_cont=0

    def update(self, user_input,bullet_handler):
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()
        if user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()
        elif user_input[pygame.K_SPACE]:
            if self.fire_cont % self.FIRE_RATE==0:
                self.shoot(bullet_handler)
        self.fire_cont+=1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10

    def move_up(self):
        if self.rect.top > SCREEN_HEIGHT/2:
            self.rect.y -= 10

    def get_damage(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.is_alive = False

    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)