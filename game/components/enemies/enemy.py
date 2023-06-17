import random
from game.utils.constants import SCREEN_HEIGHT,SCREEN_WIDTH,LEFT,RIGHT

class Enemy:
    Y_POS=-60
    MOV_X=[RIGHT,LEFT]

    def __init__(self,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x = random.randint(0,SCREEN_WIDTH)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.is_alive=True
    
    def update(self):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive=False
        self.move()

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def move(self):
        pass
    