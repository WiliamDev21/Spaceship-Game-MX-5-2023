import pygame
from game.components.powerups.powerup import PowerUp
from game.utils.constants import HEART


class Life(PowerUp):

    def __init__(self):
        self.image = HEART
        super().__init__(self.image)
