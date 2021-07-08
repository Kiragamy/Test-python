# -*-coding:Utf-8 -*
# 1) Créer une fonction qui creer_tableau2d(nb_lignes, nb_colonnes) et renvoi un tableau 2D (liste 2D)

def creer_tableau2d(nb_lignes,nb_colonnes):
    # liste = []
    # for i in range(nb_lignes):
    #     liste.append(["*"] * nb_colonnes)
# # return liste
    return [["*"] * nb_colonnes for _ in range(nb_lignes)]

def affiche_tableau_2d(tableau):
    nb_lignes = len(tableau)
    nb_colonnes = len(tableau[0])
    print(f"Nb lignes = {nb_lignes}")
    print(f"Nb colonnes = {nb_colonnes}")


affiche_tableau_2d(creer_tableau2d(5,3))


# 2) Créer une fonction initialise_tableau2d(nb_lignes, nb_colonnes, tableau) qui initialise le contenu à '*' pour chacun des éléments
# 3) Créer une fonction affiche_tableau2d(nb_lignes, nb_colonnes, tableau) qui affiche le tableau à l'écran