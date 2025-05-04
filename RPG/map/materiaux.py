from enum import Enum

class Materiaux(Enum):
    WALL = 'WALL'
    ROCK = 'ROCK'
    WATER = 'WATER'
    GRASS = 'GRASS'
    LAVA = 'LAVA'
    
    def __str__(self):
        return self.value

