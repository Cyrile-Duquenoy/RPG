from enum import Enum

class Weapons(Enum):
    SWORD = 'SWORD'
    BOW = 'BOW'
    
    def __str__(self):
        return self.value
