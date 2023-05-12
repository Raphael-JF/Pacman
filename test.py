def calculer_taille_cellule(taille_fenetre, nb_cases_x, nb_cases_y):
    largeur_fenetre, hauteur_fenetre = taille_fenetre

    taille_cellule_x = largeur_fenetre // nb_cases_x
    taille_cellule_y = hauteur_fenetre // nb_cases_y

    return min(largeur_fenetre // nb_cases_x, hauteur_fenetre // nb_cases_y)

# Exemple d'utilisation
taille_fenetre = (800 , 450)
nb_cases_x = 10
nb_cases_y = 8

taille_cellule = calculer_taille_cellule(taille_fenetre, nb_cases_x, nb_cases_y)
print("Taille de la cellule :", taille_cellule)