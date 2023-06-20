from game.components.enemies.ship import Ship
from game.components.enemies.shuttle import Shuttle
from game.components.enemies.kamikaze import Kamikaze
from game.components.enemies.tracker import Tracker


class EnemyHandler():

    def __init__(self):
        self.enemies = []
        self.extra_speed = 0
        self.cont = 1

    def update(self, player,bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            self.check_colisions(enemy, player)
            enemy.update(player.rect,bullet_handler)
            if not enemy.is_alive:
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
        if self.cont % 700 == 0:
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
