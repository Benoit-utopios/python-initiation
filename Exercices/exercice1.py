# Déclaration des variables et assignation utilisateur
nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")
genre = input("Veuillez préciser votre genre (M. ou Mme):")

# Transformation des valeurs
nom = nom.upper()
prenom = prenom.lower()
genre = genre.capitalize()

# Affichage
print(f"Bonjour {genre} {prenom} {nom}")