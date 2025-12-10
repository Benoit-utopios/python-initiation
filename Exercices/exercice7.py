# Demander la hauteur du triangle
hauteur = int(input("Entrez la hauteur du triangle: "))
print()

# Version 1
# Boucle pour chaque ligne du triangle
for ligne in range(1, hauteur + 1):
    # Calculer le nombre d'espaces avant les étoiles
    nombre_espaces = hauteur - ligne

    # Calculer le nombre d'étoiles
    nombre_etoiles = 2 * ligne - 1

    # Afficher la ligne: espaces + étoiles
    print(f"{" " * nombre_espaces}{"*" * nombre_etoiles}")

# Version 2
# Boucle pour chaque ligne du triangle
for ligne in range(1, hauteur + 1):

    # Afficher les espaces
    for espace in range(hauteur - ligne):
        print(" ", end="")
    
    # Afficher les étoiles
    for etoile in range(2 * ligne - 1):
        print("*", end="")

    # Aller à la ligne après avoir affiché espaces et étoiles
    print()

# Version 3
# Boucle pour chaque ligne du triangle
for ligne in range(1, hauteur + 1):
    # Calculer le nombre d'étoiles
    nombre_etoiles = 2 * ligne - 1

    # Créer la chaîne d'étoiles
    etoiles = '*' * nombre_etoiles
    largeur_totale = 2 * hauteur - 1
    # Afficher avec formatage
    # print(f"{etoiles:^{largeur_totale}}")
    print(etoiles.center(largeur_totale))



# print("  ", end="")
# etoiles = "*"
# etoiles.center(10)