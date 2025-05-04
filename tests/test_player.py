import unittest
from player import Player
from race import Race
from classe import Classe
from caracteristiques import Caracteristiques

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        caracteristiques = Caracteristiques(PV=100, PM=50)
        player = Player('Elyris', race=Race.HUMAIN, classe=Classe.PALADIN, caracteristiques=caracteristiques)
        self.assertEqual(player._name, 'Elyris')
        self.assertEqual(player._race, Race.HUMAIN)
        self.assertEqual(player.caracteristiques['PV'], 100)

if __name__ == '__main__':
    unittest.main()


