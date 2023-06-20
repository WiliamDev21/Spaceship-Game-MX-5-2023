import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3,SCREEN_HEIGHT


class Kamikaze(Enemy):
    WIDHT = 50
    HEIGHT = 60

    def __init__(self,extra_speed):
        self.image = pygame.transform.scale(ENEMY_3, (self.WIDHT, self.HEIGHT))
        self.speed_y = random.randrange(20, 25)
        super().__init__(self.image,extra_speed)

    def move(self):
        self.rect.y += self.speed_y+self.extra_speed

    def update(self,player_pos,bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.move()
