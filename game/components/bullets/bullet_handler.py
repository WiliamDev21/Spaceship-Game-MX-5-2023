from game.components.bullets.laser import Laser
from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE, LASER_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer

class BulletHandler:
    def __init__(self):
        self.bullets = []
    
    def update(self, player, enemies):
        for bullet in self.bullets:
            if not bullet.is_alive:
                self.remove_bullet(bullet)
            else:
                if bullet.type == BULLET_ENEMY_TYPE:
                    bullet.update(player)
                else:
                    for enemy in enemies:
                        bullet.update(enemy)
    
    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
    
    def add_bullet(self, type, ship):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(ship))
        elif type == LASER_TYPE:
            self.bullets.append(Laser(ship))
        else:
            self.bullets.append(BulletPlayer(ship))
    
    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
    
    def reset(self):
        self.bullets = []