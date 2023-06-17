from  game.components.enemies.ship import Ship
from  game.components.enemies.shuttle import Shuttle

class EnemyHandler():

    def __init__(self):
        self.enemies=[]
        self.cont=0

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if self.cont == 60:
            self.enemies.append(Shuttle())
            self.cont = 0
        if self.cont % 30 == 0:
            self.enemies.append(Ship())
        self.cont += 1

    def remove_enemy(self,enemy):
        self.enemies.remove(enemy)