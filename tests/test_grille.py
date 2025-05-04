import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from grille.grille import Grille  # Maintenant Python peut trouver le module Grille

class TestGrille(unittest.TestCase):
    def setUp(self):
        self.grille = Grille(5, 5)

    def test_ajouter_element(self):
        self.grille.ajouter_element(0, 0, "Objet")
        self.assertEqual(self.grille.get_case(0, 0), "Objet")

if __name__ == '__main__':
    unittest.main()


