# Dictionnaire vide
dico_vide = {}
autre_dico_vide = dict()

# Dictionnaire avec des éléments
personne = {
    "nom": "Dupont",
    "prenom": "Marie",
    "age": 28,
    "ville": "Paris",
    1: "un",
    (3, 4): "tuple comme clé"
}

coordonnees = dict(x=10, y=20, z=30)

elements = [("a", 1), ("b", 2)]
dico = dict(elements)

# Accès par clé
print(personne["nom"]) # Dupont

# Accès sécurisé avec get()
print(personne.get("ville"))

# Modification d'une valeur
personne["age"] = 44

# Ajout d'une nouvelle paire
personne["email"] = "marie.dupont@caramail.fr"

# Suppression avec récupération de la valeur
age = personne.pop("age")

# Méthodes importantes
# Obtenir toutes les clés
cles = personne.keys()

# Obtenir toutes les valeurs
valeurs = personne.values()

# Obtenir toutes les paires
items = personne.items()

# Vider le dictionnaire
personne.clear()