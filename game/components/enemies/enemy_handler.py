from  game.components.enemies.ship import Ship
from  game.components.enemies.shuttle import Shuttle
from  game.components.enemies.kamikaze import Kamikaze
from  game.components.enemies.tracker import Tracker

class EnemyHandler():

    def __init__(self):
        self.enemies=[]
        self.cont=1

    def update(self,player):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(player.rect)
            self.check_colisions(enemy,player)
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if self.cont % 60 == 0:
            self.enemies.append(Shuttle())
        if self.cont % 30 == 0:
            self.enemies.append(Ship())
        if self.cont % 100 == 0:
            self.enemies.append(Kamikaze())
        if self.cont % 500 == 0:
            self.enemies.append(Tracker())
        self.cont += 1

    def remove_enemy(self,enemy):
        self.enemies.remove(enemy)

    def check_colisions(self,enemy,player):
        if enemy.rect.colliderect(player.rect):
            enemy.is_alive = False
            player.get_damage(10)