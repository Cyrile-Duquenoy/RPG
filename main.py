from RPG.character import (Player,
                           Race,
                           SpecialAttack)

if __name__ == "__main__":
    P1 = Player(name='Player 1')
    print(P1)
    
    P1.classe = 'GUERRIER'
    print(P1)
    
    P1.utiliser_attaque_speciale(SpecialAttack.FRAPPE_PUISSANTE)
    P1.utiliser_attaque_speciale(SpecialAttack.BOULE_DE_FEU)