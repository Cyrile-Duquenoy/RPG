from enum import Enum

class Classe(Enum):
    GUERRIER = 'GUERRIER'
    PALADIN = 'PALADIN'
    CHASSEUR = 'CHASSEUR'
    VOLEUR = 'VOLEUR'
    MAGE = 'MAGE'
    
    def __str__(self):
        return self.value
        
class ClasseBase:
    def attaque_speciale(self, player):
        raise NotImplementedError("Cette classe n'a pas d'attaque spéciale définie.")

class Guerrier(ClasseBase):
    def attaque_speciale(self, player):
        print(f"{player._name} utilise Frappe Puissante !")
        
class MAGE(ClasseBase):
    def attaque_speciale(self, player):
        print(f"{player._name} utilise boule de feu !")

CLASSE_MAPPING = {
    Classe.GUERRIER: Guerrier,
    Classe.MAGE: MAGE
}