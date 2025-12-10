# Tuples vide
tuple_vide = ()

# Tuples avec des éléments
coordonnees = (10, 20)
personne = ("Alice", 30, "Paris")

# Tuple avec un seul élément
singleton = (10,)

# Packing
point = 5, 10

# Accès aux éléments

coordonnees = (10, 20, 30)

# Par index
print(coordonnees[0]) # 10
print(coordonnees[-1]) # 30

# Slicing
nombres = (1, 2, 3, 4, 5, 6)
print(nombres[1:4]) # (2, 3, 4)
print(nombres[:3]) # (1, 2, 3)
print(nombres[::2]) # (1, 3, 5)

# Unpacking
x, y, z = coordonnees
# Echange de variables
a, b = 5, 10
a, b = b, a

tuple1 = (1, 2, 3)
tuple2 = (4, 5)
# Concaténation
resultat = tuple1 + tuple2
# Répétition
triple = tuple1*3
# Longueur
len(tuple1)
# Vérification d'appartenance
print(2 in tuple1) # True

# Méthodes
nombres = (1, 2, 3, 2, 4, 2)
print(nombres.count(2)) # 3
print(nombres.index(3)) # 2
