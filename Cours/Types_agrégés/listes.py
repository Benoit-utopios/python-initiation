# Liste vide
liste_vide = []
autre_liste_vide = list()

# Liste
mixte = [1, "texte", 3.14, True]

# Matrice
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

fruits = ["pomme", "banane", "fraise"]
# Modification d'un élément
fruits[1] = "kiwi"
fruits[1:2] = ["kiwi", "orange"]

# Méthodes de modification

# Ajouter à la fin
fruits.append("orange")
# Insérer à une position
fruits.insert(1, "kiwi")
# Etendre avec une autre liste
fruits.extend(["mangue", "ananas"] )
# Supprimer un élément
fruits.remove("pomme")
# Suppression par index
dernier = fruits.pop(1)

# Vider la liste
fruits.clear()

# Tri (par ordre décroissant)
fruits.sort(reverse=True)

# Copier une liste
fruits.copy()