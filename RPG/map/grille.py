#from materiaux import Materiaux

class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [[None for _ in range(hauteur)] for _ in range(largeur)]  # lignes d'abord
    
    def ajouter_element(self, x, y, element):
        if 0 <= x < self.largeur and 0 <= y < self.hauteur:
            self.grille[y][x] = element  # y = ligne, x = colonne
        else:
            raise ValueError("Coordonnées en dehors de la grille.")
    
    def get_case(self, x, y):
        if 0 <= x < self.largeur and 0 <= y < self.hauteur:
            return self.grille[y][x]
        else:
            raise ValueError("Coordonnées en dehors de la grille.")
    
    def afficher(self):
        for ligne in self.grille:
            print(ligne)




