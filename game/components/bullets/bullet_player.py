import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET, BULLET_PLAYER_TYPE

class BulletPlayer(Bullet):
    WIDTH = 10
    HEIGHT = 20
    SPEED = 10

    def __init__(self, ship):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.type = BULLET_PLAYER_TYPE
        super().__init__(self.image, self.type, ship)

    def update(self, enemy):
        self.rect.y -= self.SPEED
        if self.rect.y <= 0:
            self.is_alive = False
        super().update(enemy)