from enum import Enum

class Race(Enum):
    HUMAIN = 'HUMAIN'
    NAIN = 'NAIN'
    ELFE_NUIT = 'ELFE_NUIT'
    DRAENAI = 'DRAENAI'
    ORC = 'ORC'
    MORT_VIVANT = 'MORT_VIVANT'
    TAUREN = 'TAUREN'
    TROLL = 'TROLL'
    ELFE_SANG = 'ELFE_SANG'
    GOBELIN = 'GOBELIN'
    
    def __str__(self):
        return self.value
