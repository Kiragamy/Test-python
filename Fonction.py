# -*-coding:Utf-8 -*
# 1) Créer une fonction qui creer_tableau2d(nb_lignes, nb_colonnes) et renvoi un tableau 2D (liste 2D)
def creer_tableau2d (nb_lignes, nb_colonnes):
    liste=[]
    for i in range(nb_lignes):
        sous_liste=[]
        for j in range(nb_colonnes):
            sous_liste.append("o")
        liste.append(sous_liste)
    return liste
# 2) Créer une fonction initialise_tableau2d(nb_lignes, nb_colonnes, tableau) qui initialise le contenu à '*' pour chacun des éléments
def initialise_tableau2d(size_x, size_y, tableau):
    for x in range(size_x):
        for y in range(size_y):
            tableau[x][y] ="*"
    return tableau
# 3) Créer une fonction affiche_tableau2d(nb_lignes, nb_colonnes, tableau) qui affiche le tableau à l'écran
def affiche_tableau2d(size_x,size_y,tableau):
    for x in range(size_x):
        for y in range(size_y):
            print(tableau[x][y], end=" ")
        print(" ")
    return tableau
print("Exemple de tableau ")
nb_lignes=5
nb_colonne=5
tableau = creer_tableau2d(nb_lignes,nb_colonne)
print(tableau)
tableau = initialise_tableau2d(nb_lignes,nb_colonne,tableau)
print(tableau)
tableau=affiche_tableau2d(nb_lignes,nb_colonne,tableau)
print(tableau)

# 4) Dessiner un rectangle:
# 	4.1) Créer une procédure ligne(x_start, y_start, x_end, y_end) qui va dessiner une ligne depuis les coordonnées (x_start, y_start) à (x_end, y_end)
# 		# nota: penser à vérifier en début de procédure que les conditions
# 		# x_end > x_start et y_end > y_start sont bien respectées (inverser respectivement x_end(/y_end) avec x_start(/y_start) si nécessaire)
# 	     Tester la procédure et vérifier qu'une ligne est bien dessinée
def ligne(x_start, y_start, x_end, y_end, tableau):
    for y in range(y_start, y_end +1):
        for x in range(x_start, x_end + 1):
            tableau[x][y] = "*"
    return tableau

affiche_tableau2d(15,15,(ligne(5,10,5,10, creer_tableau2d(15,15))))






# 	4.2) Créer une procédure rectangle(x, y, l, h, tableau) qui utilise la procédure ligne(...) précédemment conçue pour dessiner un rectangle
# 		Dessiner la ligne du bas en commençant à la position (x,y) jusqu’à (x+l, y)
# 		Dessiner la ligne du haut en commençant à la position (x,y+h) jusqu’à (x+l, y+h)
# 		Dessiner la barre verticale de gauche de (x, y) à (x, y+h)
# 		Dessiner la barre verticale de droite de (x+l, y) à (x+l, y+h)
# 	     Tester la procédure et vérifier qu'un rectangle est bien dessiné