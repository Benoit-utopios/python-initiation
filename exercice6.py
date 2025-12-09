# Demander à l'utilisateur de saisir un nombre entier N
N = int(input("Entrez un nombre entier supérieur à 0: "))

# Vérifier que N est bien supérieur à 0
if N <= 0:
    print("Erreur le nombre doit être supérieur à 0")
else:
    # Boucle pour parcourir chaque table de 1 à N
    for table in range (1, N + 1):
        print(f"Table de {table}")
        # Boucle pour calculer et afficher chaque ligne de la table (de 1 à 10)
        for i in range (1, 11):
            resultat = i * table
            print(f"{table} x {i} = {resultat}")
        print()