# Création du tuple etudiant
etudiant = ("Dupont", "Jean", 20, 14.5)
print(f"Tuple initial : {etudiant}\n")

# Unpacking
nom, prenom, age, moyenne = etudiant

# Affichage
print(f"Nom: {nom}, Prénom: {prenom}, Age: {age}, Moyenne: {moyenne}")


# Création du tuple de 10 notes
notes = (12, 15, 8, 18, 14, 11, 16, 9, 17, 13)
print(f"\nTuple de notes : {notes}\n")

trois_dernieres_notes = notes[-3:]
note_sur_deux = notes[::2]
nombre_de_quinze = notes.count(15)

# Fonction calculer_statistiques()
def calculer_statistiques(notes):
    moyenne = sum(notes) / len(notes)
    mini = min(notes)
    maxi = max(notes)

    return (mini, maxi, moyenne)

min_note, max_note, moyenne_calc = calculer_statistiques(notes)
print(f"Note mini: {min_note} Note maxi: {max_note} Moyenne: {moyenne_calc}")