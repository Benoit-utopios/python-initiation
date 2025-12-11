# Ceci est un commentaire
mon_float = 100.5435435 # Ceci est un float
ma_string = "100" # Ceci est un string (chaine de caractères)
mon_bool = True # Ceci est un booléen
greetings_var = "Hello world !"
# Ceci est une fonction
# print(greetings_var)
# saisie_utilisateur = input("Veuillez saisir un nombre à virgule : ")

# print("\n{1}")
# print(f"{float(saisie_utilisateur):^7.2f}")

for element in range(0, 8):
    print(element)

str = "stoP"
print(str.capitalize())

def nom_complet(age,
                prenom="John", 
                nom="Doe",
                ) : 
    return prenom + " " + nom

nom_complet(nom="Toto")