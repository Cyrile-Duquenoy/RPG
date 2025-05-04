from enum import Enum
from .classe import Classe

class SpecialAttack(Enum):
    FRAPPE_PUISSANTE = ("FRAPPE_PUISSANTE",
                        Classe.GUERRIER,
                        lambda player: print(f"{player._name} exécute une Frappe Puissante !"))
    
    BOULE_DE_FEU = ("BOULE_DE_FEU",
                    Classe.MAGE,
                    lambda player: print(f"{player._name} exécute une Fboule de feu !"))
    
    def __init__(self, description, classe_associee, effet):
        self.description = description
        self.classe_associee = classe_associee
        self.effet = effet
        
    def __str__(self):
        return self.description

