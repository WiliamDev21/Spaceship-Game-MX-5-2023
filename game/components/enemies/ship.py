import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1,RIGHT,LEFT, SCREEN_WIDTH

class Ship(Enemy):
    WIDHT=40
    HEIGHT=60
    SPEED_Y=5
    SPEED_X=2
    INTERVAL=100

    def __init__(self):
        self.image=pygame.transform.scale(ENEMY_1, (self.WIDHT,self.HEIGHT))
        self.cont=0
        super().__init__(self.image)

    def move(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.cont > self.INTERVAL or self.rect.left <= 0:
                self.mov_x = RIGHT
                self.cont = 0
        else:
            self.rect.x += self.SPEED_X
            if self.cont > self.INTERVAL or self.rect.right >= SCREEN_WIDTH:
                self.mov_x = LEFT
                self.cont = 0
        self.cont += 1