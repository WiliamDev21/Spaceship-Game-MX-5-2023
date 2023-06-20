
import random
import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_5, LASER_TYPE,SCREEN_HEIGHT, SCREEN_WIDTH

class Oneshot(Enemy):
    WIDHT = 60
    HEIGHT = 50
    POS_X = [0, SCREEN_WIDTH-WIDHT]
    POS_Y = 0
    TIME_MAX = 50
    TIME_WAIT = 20

    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_5, (self.WIDHT, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X[random.randrange(0, 1)]
        self.rect.y = -self.HEIGHT
        self.POS_Y = random.randint(SCREEN_HEIGHT//2,SCREEN_HEIGHT-100)
        self.speed_y = 20
        self.ready = False
        self.timeShooted = 0
        self.timeWaited = 0
        self.is_alive = True


    def update(self, player_pos,bullet_handler):
        if self.rect.y >= self.POS_Y and self.timeShooted < self.TIME_MAX:
            if self.timeWaited >= self.TIME_WAIT:
                if self.timeShooted == 0:
                    self.shoot(bullet_handler)
                self.timeShooted += 1
            self.timeWaited += 1
        else:
            self.move()
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False

    def move(self):
        self.rect.y += self.speed_y
    
    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(LASER_TYPE, self)

        