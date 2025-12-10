# Set vide
ensemble_vide = set()

# Set avec éléments
nombres = {1, 2, 3, 4, 5}

# A partir d'une liste
liste_avec_doublons = [1, 2, 2, 3, 3, 4, 5]
ensemble = set(liste_avec_doublons)

# Modification des sets
fruits = {"pomme", "banane"}

# Ajout
fruits.add("orange")
print(fruits)

# Ajout plusieurs éléments
fruits.update(["kiwi", "mangue",])

# Supprimer un élément
fruits.remove("banane")

# sans erreurs
fruits.discard("poire")

# Vider le set
fruits.clear()

# Opérations ensemblistes
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
union = A | B

# Intersection
intersection = A & B

# Différence
difference = A - B

# Test d'inclusion
print({1, 2}.issubset(A)) # True
print(A.issuperset({1, 2})) # True
print(A.isdisjoint({10, 11})) # True (aucun élément commun)