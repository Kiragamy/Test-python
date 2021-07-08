# -*-coding:Utf-8 -*

# Créer un fichier feuDeSignalisation.py et configurer l'encodage utf-8

# 1) Définir une classe Feu_De_Signalisation pour décrire son fonctionnement.
class Feu_De_Signalisation:
    "Le principe d'un feu tricolore consiste à devenir vert quand la voie est libre, devenir orange clignotant, devenir orange, puis devenir rouge quand la voie n'est plus libre "

    couleur=["Vert", "Orange", "Rouge", "Orange clignotant"]

    def __init__(self, index=0):
        self.index = index

    def successeur(self):
        if self.index != 3:
            self.index = (self.index+1)%3

    def afficher_etat(self):
        print(self.couleur[self.index])

    def switch_maintenance(self):
        if self.index != 3:
            self.index = 3
        else:
            self.index = 0


recollet = Feu_De_Signalisation()
recollet.afficher_etat()
recollet.successeur()
recollet.afficher_etat()
recollet.successeur()
recollet.afficher_etat()
recollet.switch_maintenance()
recollet.afficher_etat()
recollet.successeur()
recollet.afficher_etat()
recollet.switch_maintenance()
recollet.afficher_etat()
# 2) Le constructeur de la classe ( méthode __init__() ) initialise son état à "vert" par le biais d'un un index pour suivre cet enregistrement.
# 	Cet index sera initialisé à 0, utiliser une liste ["Vert", "Orange", "Rouge", "Orange Clignotant"]

# 3) La méthode successeur doit faire passer le feu d'une couleur à une autre en incrémentant l'index d'enregistrement modulo 3
# La méthode afficher_etat doit afficher l'état du feu de signalisation