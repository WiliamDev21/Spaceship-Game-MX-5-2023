from game.utils.constants import SCREEN_HEIGHT

class Bullet:
    def __init__(self, image, type, ship):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.center = ship.rect.center
        self.is_alive = True

    def update(self, object):
        if self.rect.colliderect(object.rect):
            object.get_damage(10)
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)