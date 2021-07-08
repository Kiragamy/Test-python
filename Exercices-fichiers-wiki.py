# -*-coding:Utf-8 -*
# Écrivez un script qui compte dans un fichier texte quelconque le nombre de lignes contenant des caractères numériques.

# def comptage_ligne_caractere_numerique(nomfichier):
#     fichier = open(nomfichier, "r")
#     nbre_caractere = 0
#     while 1:
#         txt = fichier.readline()
#         if txt == "":
#             break
#         for character in txt:
#             if character.isdigit():
#                 nbre_caractere = nbre_caractere + 1
#                 break
#     print(nbre_caractere)
#     fichier.close()
#
# comptage_ligne_caractere_numerique("Monfichier")

# Écrivez un script qui compte le nombre de mots contenus dans un fichier texte.

# def comptage_nombre_mots(nomfichier):
#     fichier = open(nomfichier, "r")
#     txt = fichier.read()
#     liste_mots = txt.split()
#     print(len(liste_mots))
#     fichier.close()
# comptage_nombre_mots("Monfichier")

# Écrivez un script qui recopie un fichier texte en veillant à ce que chaque ligne commence par une majuscule.
# def copie_texte_majuscule_ligne(nom_fichier_source,nom_fichier_destination):
#     fichier_source = open(nom_fichier_source, "r")
#     fichier_destination = open(nom_fichier_destination,"w")
#     while 1:
#         txt = fichier_source.readline()
#         if txt == "":
#             break
#         fichier_destination.write(txt.capitalize())
#     fichier_source.close()
#     fichier_destination.close()
#
# copie_texte_majuscule_ligne("Monfichier","Monfichier2")

# Écrivez un script qui recopie un fichier texte en fusionnant (avec la précédente) les lignes qui ne commencent pas par
# une majuscule.
def copie_texte_fusion_ligne(nom_fichier_source,nom_fichier_destination):
    fichier_source = open(nom_fichier_source, "r")
    fichier_destination = open(nom_fichier_destination, "w")
    while 1:
        txt = fichier_source.readline()
        if txt == "":
            break
        if txt[0].isupper() == False:
            fichier_destination.write(txt.join(txt))
        else:
            fichier_destination.write(txt)
    fichier_source.close()
    fichier_destination.close()

copie_texte_fusion_ligne("Monfichier","Monfichier2")