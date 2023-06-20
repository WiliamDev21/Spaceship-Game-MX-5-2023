import random
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, LEFT, RIGHT,BULLET_ENEMY_TYPE


class Enemy:
    Y_POS_INITIAL = -60
    MOV_X = [RIGHT, LEFT]
    extra_speed=0
    SHOOTING_TIME = 30

    def __init__(self, image,extra_speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = self.Y_POS_INITIAL
        self.mov_x = random.choice(self.MOV_X)
        self.is_alive = True
        self.is_destroyed = False
        self.extra_speed=extra_speed
        self.shooting_time = 0

    def update(self, player_pos,bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.move()
        self.shoot(bullet_handler)
        self.shooting_time += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        pass

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)

    def get_damage(self,damage):
        self.is_alive = False