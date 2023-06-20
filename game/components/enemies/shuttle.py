import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2, LEFT, RIGHT, SCREEN_WIDTH


class Shuttle(Enemy):
    WIDHT = 50
    HEIGHT = 50
    SPEED_Y = 6
    SPEED_X = 16

    def __init__(self,extra_speed):
        self.image = pygame.transform.scale(ENEMY_2, (self.WIDHT, self.HEIGHT))
        super().__init__(self.image,extra_speed)

    def move(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X+self.extra_speed
            if self.rect.left <= 0:
                self.mov_x = RIGHT
        else:
            self.rect.x += self.SPEED_X+self.extra_speed
            if self.rect.right >= SCREEN_WIDTH:
                self.mov_x = LEFT
