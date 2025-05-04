from enum import Enum

class Race(Enum):
    HUMAIN = 'HUMAIN'
    NAIN = 'NAIN'
    ELFE = 'ELFE'
    
    def __str__(self):
        return self.value
