from WoW import *

class Jeu:
    def __init__(self, nb_joueurs):
        self._nb_joueurs = nb_joueurs
        
    def __repr__(self):
        return f'{self._nb_joueurs}'
        
