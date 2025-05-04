from .race import Race
from .classe import Classe, CLASSE_MAPPING, ClasseBase
from .caracteristiques import Caracteristiques
from .special_attack import SpecialAttack

class Player:
    def __init__(self, name: str, race: Race = None, classe: Classe = None, caracteristiques: Caracteristiques = None):
        self._name = name
        self._race = race
        self._classe = classe
        self.caracteristiques = caracteristiques if caracteristiques else Caracteristiques(PV=100, PM=50, PA=0)
        self.PV = self.caracteristiques.PV
        self.PM = self.caracteristiques.PM
        self.PA = self.caracteristiques.PA
        self.inventory = {}
        
        # Initialisation de la logique de classe (ex: Guerrier())
        self._classe_logic = CLASSE_MAPPING.get(classe, ClasseBase)
        
    def __str__(self):
        return f"Player(name={self._name}, race={self._race}, class={self._classe}, caracteristiques={self.caracteristiques})"
    
    def __repr__(self):
        return self.__str__()

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        if isinstance(race, str):
            try:
                race = Race[race]
            except KeyError:
                raise ValueError(f"{race} n'est pas une race valide.")
        elif not isinstance(race, Race):
            raise TypeError("race doit être une instance de Race ou un nom valide de Race.")
        self._race = race

    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, classe):
        if isinstance(classe, str):
            try:
                classe = Classe[classe]
            except KeyError:
                raise ValueError(f"{classe} n'est pas une classe valide.")
        elif not isinstance(classe, Classe):
            raise TypeError("classe doit être une instance de Classe ou un nom valide de Classe.")
        self._classe = classe

    def afficher_inventaire(self):
        if not self.inventory:
            print(f"{self._name} n'a rien dans son inventaire.")
        else:
            print(f"Inventaire de {self._name} :")
            for objet, quantite in self.inventory.items():
                print(f"- {objet} x{quantite}")
                
    def ajouter_objet(self, objet, quantite=1):
        if objet in self.inventory:
            self.inventory[objet] += quantite
        else:
            self.inventory[objet] = quantite

    def to_dict(self):
        return {
            "name": self._name,
            "race": str(self._race) if self._race else None,
            "classe": str(self._classe) if self._classe else None,
            "caracteristiques": self.caracteristiques.to_dict(),
            "inventory": {str(k): v for k, v in self.inventory.items()}
        }
    
    def utiliser_attaque_speciale(self, attaque: SpecialAttack):
        if self._classe != attaque.classe_associee:
            raise PermissionError(f"{self._name} ne peut pas utiliser {attaque}. C'est réservé à la classe {attaque.classe_associee}.")
        
        attaque.effet(self)

    

