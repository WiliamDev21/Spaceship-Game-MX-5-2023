import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3

class Kamikaze(Enemy):
    WIDHT=50
    HEIGHT=60

    def __init__(self):
        self.image=pygame.transform.scale(ENEMY_3, (self.WIDHT,self.HEIGHT))
        self.speed_y=random.randrange(15,25)
        super().__init__(self.image)

    def move(self):
        self.rect.y += self.speed_y