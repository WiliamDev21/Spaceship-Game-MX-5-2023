import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY_TYPE, LASER, SCREEN_WIDTH


class Laser(Bullet):
    WIDTH = SCREEN_WIDTH-60
    HEIGHT = 50


    def __init__(self,ship):
        self.image = LASER
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.type = BULLET_ENEMY_TYPE
        self.timer = 0
        self.rect = self.image.get_rect()
        self.rect.center = ship.rect.center
        self.rect.x = 61
        self.is_alive = True
        self.oneshot = ship
        self.life_time = ship.TIME_MAX

    def update(self, object):
        if self.rect.colliderect(object.rect):
            object.get_damage(object.life)
        if self.timer == self.life_time or not self.oneshot.is_alive:
            self.is_alive = False
        self.timer += 1