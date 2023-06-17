from  game.components.enemies.ship import Ship
from  game.components.enemies.shuttle import Shuttle
from  game.components.enemies.kamikaze import Kamikaze

class EnemyHandler():

    def __init__(self):
        self.enemies=[]
        self.cont=1

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
        if self.cont % 60 == 0:
            self.enemies.append(Shuttle())
        if self.cont % 30 == 0:
            self.enemies.append(Ship())
        if self.cont % 100 == 0:
            self.enemies.append(Kamikaze())
        self.cont += 1

    def remove_enemy(self,enemy):
        self.enemies.remove(enemy)