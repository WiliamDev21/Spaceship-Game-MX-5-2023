import random
import pygame

from game.utils.constants import SCREEN_HEIGHT


class PowerUp:
    WIDTH = 30
    HEIGHT = 30
    POS_Y = -HEIGHT
    SPEED = 6

    def __init__(self, image):
        self.image = pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_HEIGHT-120)
        self.rect.y = self.POS_Y
        self.is_alive = True
        self.is_taken = False

    def update(self, player):
        self.rect.y += self.SPEED
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        if self.rect.colliderect(player.rect):
            self.is_alive = False
            self.is_taken = True
            player.activate_powerup(self)

    def draw(self,screen):
        screen.blit(self.image,self.rect)
