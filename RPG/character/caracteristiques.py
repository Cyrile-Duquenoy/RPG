class Caracteristiques:
    '''
    Caractéristiques associées aux joueurs
    PV : Point de Vie
    PM : Point de Magie/Mana
    PA : Point d'actions
    '''
    def __init__(self, PV, PM, PA=0):
        self.PV = PV
        self.PM = PM
        self.PA = PA
        self.caracteristiques = {'PV': self.PV, 'PM': self.PM, 'PA': self.PA}
        
    def __str__(self):
        return f"{self.caracteristiques}"

