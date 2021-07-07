# -*-coding:Utf-8 -*
print("hello")

# #1. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est positif (>= 0) ou non, et affiche
# #“positif” ou “négatif”.
# s=int(input("Veuillez écrire un entier"))
# if s>=0:
#     print("positif")
# else :
#     print("négatif")

# # #2. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictement
# # #négatif, et affiche ce résultat.
# s=int(input("Veuillez écrire un entier"))
# if s>0:
#     print("positif")
# elif s==0:
#         print("nul")
# else :
#         print("négatif")

# #3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction
# #prédéfinie évidemment).
# s=int(input("Veuillez écrire un entier"))
# if s<0:
#     print(s*-1)
# else :
#     print(s)

#4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis
#à l’entier supérieur).
# s=float(input("Veuillez écrire un réel"))
# s_tronque=int(s)
# if s<0:
#     if s_tronque-s >= 0.5:
#        print(int(s)-1)
#     else:
#         print(int(s))
# elif s-s_tronque>=0.5:
#     print(int(s)+1)
# else:
#     print(int(s))

#5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir
#compte des années bissextiles).
# s=int(input("Veuillez écrire un entier entre 1 et 12 (1=janvier ; 2=février ; etc)"))
# if s in [1,3,5,7,8,10,12]:
#     print("31")
# elif s==2:
#     print("28")
# else:
#     print("30")

#6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les
#4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans
#(2000 était une année bissextile).
#s=int(input("Veuillez écrire une année pour vérifier s'il est bissextile"))
# a=int(input("Veuillez écrire un entier représentant une année"))
# if (a%4==0 and a%100!=0) or a%400==0:
#     print("Cette année est bissextile")
# else :
#     print("Cette année n'est pas bissextile")

#7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois)
#et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.
j = int(input("Veuillez écrire un entier entre 1 et 31 qui représente le jour du mois"))
m = int(input("Veuillez écrire un entier entre 1 et 12 (1=janvier ; 2=février ; etc)"))
if m%3==0 and j>=21 and m!=12:
    m=m+1
if m==12 and j>=21:
    m=1
if m in [1,2,3]:
    print("La saison est l'hiver")
elif m in [4,5,6]:
    print("La saison est le printemps")
elif m in [7,8,9]:
    print("La saison est l'été")
else:
    print("La saison est l'automne")