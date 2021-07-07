# -*-coding:Utf-8 -*
# 1) Créer une fonction qui creer_tableau2d(nb_lignes, nb_colonnes) et renvoi un tableau 2D (liste 2D)
def creer_tableau2d (nb_lignes, nb_colonnes)
    liste=[]
    for i in range(nb_lignes):
        sous_liste=[]
        for j in range(nb_colonnes):
            sous_liste.append("*")
    liste.append(sous_liste)
    return liste

# 2) Créer une fonction initialise_tableau2d(nb_lignes, nb_colonnes, tableau) qui initialise le contenu à '*' pour chacun des éléments
# 3) Créer une fonction affiche_tableau2d(nb_lignes, nb_colonnes, tableau) qui affiche le tableau à l'écran