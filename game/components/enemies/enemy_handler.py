from game.components.enemies.oneshot import Oneshot
from game.components.enemies.ship import Ship
from game.components.enemies.shuttle import Shuttle
from game.components.enemies.kamikaze import Kamikaze
from game.components.enemies.tracker import Tracker


class EnemyHandler():

    def __init__(self):
        self.enemies = []
        self.extra_speed = 0
        self.cont = 1
        self.number_enemy_destroyed = 0

    def update(self, player,bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            self.check_colisions(enemy, player)
            enemy.update(player.rect,bullet_handler)
            if not enemy.is_alive:
                if enemy.is_destroyed:
                    self.number_enemy_destroyed += 1
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if self.cont % 60 == 0:
            self.enemies.append(Shuttle(self.extra_speed))
        if self.cont % 30 == 0:
            self.enemies.append(Ship(self.extra_speed))
        if self.cont % 100 == 0:
            self.enemies.append(Kamikaze(self.extra_speed))
        if self.cont % 500 == 0:
            self.enemies.append(Tracker())
        if self.cont % 300 == 0: #and self.cont > 1000:
            self.enemies.append(Oneshot())
        if self.cont % 400 == 0:
            self.extra_speed += self.cont / 700
            for enemy in self.enemies:
                enemy.extra_speed = self.extra_speed
        self.cont += 1

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def check_colisions(self, enemy, player):
        if enemy.rect.colliderect(player.rect):
            enemy.is_alive = False
            player.get_damage(10)

    def reset(self):
        self.enemies = []
        self.number_enemy_destroyed = 0
        self.extra_speed = 0
        self.cont = 1