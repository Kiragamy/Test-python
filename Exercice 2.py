# -*-coding:Utf-8 -*
# Créer un nouveau fichier Exercice2.py dans votre projet et configurer le charset en utf-8
# En utilisant des boucles while lorsque le nombre d'itérations n'est pas connu et des boucles for lorsque le nombre d'itérations est connu :
#
# 1. Écrire un algorithme qui demande un entier positif, et le rejette tant que le nombre saisi n’est pas conforme.
# nombre=-1
# while nombre!=int(nombre) or nombre<0:
#     nombre = float(input("Veuillez entrer un nombre entier positif "))
# else:
#     print(int(nombre))

# 2. Écrire un algorithme qui demande 10 entiers, compte le nombre d’entiers positifs saisis, et affiche ce résultat.
# cpt = 0
# for i in range(10):
#     nombre = float(input("Veuillez entrer un nombre entier positif"))
#     if nombre>=0:
#         cpt = cpt+1
# print("le nombre d'entiers positifs saisis est", i )

#(nombre!=int(nombre) or nombre<0:) to sum(nombre)<10

# 3. Écrire un algorithme qui demande des entiers positifs à l’utilisateur, les additionne, et qui s’arrête en affichant le
# résultat dès qu’un entier négatif est saisi.
# somme=0
# nombre=0
# while nombre>=0:
#     nombre = float(input("Veuillez entrer un entier positif "))
#     if nombre<0:
#         print("Le nombre", nombre, "est négatif et non conforme. La somme des nombres saisis est", somme)
#     else:
#         somme = somme + nombre
# 4. Modifier ce dernier algorithme pour afficher la moyenne de la série d’entiers positifs saisis.
# moyenne=0
# somme=0
# nombre=0
# cnt=0
# while nombre>=0:
#     nombre = float(input("Veuillez entrer un entier positif "))
#     if nombre<0:
#         moyenne = (somme) / cnt
#         print("Le nombre", nombre, "est négatif et non conforme. La moyenne des nombres saisis est", moyenne)
#     else:
#         cnt = cnt+1
#         somme=somme+nombre