import os
import pygame
from game.components.powerups.life import Life
from game.components.powerups.shield import Shield
from game.utils.constants import IMG_DIR, SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT,BULLET_PLAYER_TYPE, SPACESHIP_SHIELD


class Spaceship:
    WIDHT = 40
    HEIGTH = 60
    X_POS = (SCREEN_WIDTH//2)-WIDHT
    Y_POS = 450
    FIRE_RATE=7

    def __init__(self):
        self.image = pygame.transform.scale(
            SPACESHIP, (self.WIDHT, self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.life = 50
        self.is_alive = True
        self.fire_cont=0
        self.is_inmune = False
        self.inmune_cont = 0
        self.inmune_time = 0


    def update(self, user_input,bullet_handler):
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()
        if user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()

        elif user_input[pygame.K_SPACE]:
            if self.fire_cont == self.FIRE_RATE:
                self.shoot(bullet_handler)
                self.fire_cont=0

        if self.fire_cont < self.FIRE_RATE:
            self.fire_cont += 1

        if self.is_inmune:
            self.inmune_cont += 1
            if self.inmune_cont == self.inmune_time:
                self.reset_shield()
                

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10

    def move_up(self):
        if self.rect.top > SCREEN_HEIGHT/2:
            self.rect.y -= 10

    def get_damage(self, damage):
        self.hit_sound = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/hit_sound.mp3'))
        self.hit_sound.play()
        if not self.is_inmune:
            self.life -= damage
        if self.life <= 0:
            self.die_sound = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/die.mp3'))
            self.die_sound.set_volume(1.5)
            self.die_sound.play()
            self.is_alive = False

    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self)

    def activate_powerup(self,powerup):
        if type(powerup) == Shield:
            self.shield_sound = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/shield_sound.mp3'))
            self.shield_sound.play()
            self.is_inmune = True
            self.inmune_time = 100
            self.image = pygame.transform.scale(
            SPACESHIP_SHIELD, (self.WIDHT, self.HEIGTH))
        elif type(powerup) == Life:
            self.life_sound = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/life_sound.mp3'))
            self.life_sound.play()
            self.life += 10

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.life = 50
        self.fire_cont=0
        
    def reset_shield(self):
        self.image = pygame.transform.scale(
            SPACESHIP, (self.WIDHT, self.HEIGTH))
        self.is_inmune = False
        self.inmune_cont = 0
        self.inmune_time = 0