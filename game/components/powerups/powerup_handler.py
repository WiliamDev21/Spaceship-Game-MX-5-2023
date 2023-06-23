from game.components.powerups.life import Life
from game.components.powerups.shield import Shield


class PowerUpHandler:
    
    def __init__(self):
        self.powerups = []
        self.cont = 0
        self.temp_kills = 0

    def update(self, player, kills):
        if self.cont == 350:
            self.add_powerup(Shield())
            self.cont = 0
        if kills - self.temp_kills == 15:
            self.add_powerup(Life())
            self.temp_kills = kills
        for powerup in self.powerups:
            powerup.update(player)
            if not powerup.is_alive:
                self.remove_powerup(powerup)

        self.cont += 1

    def draw(self,screen):
        for powerup in self.powerups:
            powerup.draw(screen)

    def add_powerup(self,powerup):
        self.powerups.append(powerup)

    def remove_powerup(self,powerup):
        self.powerups.remove(powerup)

    def reset(self):
        self.cont = 0
        self.powerups = []