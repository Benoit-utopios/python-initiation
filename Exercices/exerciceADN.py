def verification_adn(chaine):
    """
    Vérifie si une chaîne d'ADN est valide (ne contient que 'a', 't', 'c', 'g')
    
    :param chaine: La chaine de caractères à vérifier
    :return: True si la chaine est valide, False sinon
    """
    chaine_upper = chaine.upper()

    for lettre in chaine_upper:
        if lettre not in 'ATCG':
            return False
    return bool(chaine_upper)

def saisie_adn(message):
    """
    Invite l'utilisateur à saisir une chaîne d'ADN valide.
    Répète la demande tant que la saisie est invalide
    
    :param message: Le message à afficher à l'utilisateur
    """
    adn_valide = False
    chaine = ""

    while not adn_valide:
        # Demander la saisie
        chaine = input(message).strip()

        # Vérifier la validité de la chaîne
        if verification_adn(chaine):
            adn_valide = True
        else:
            print("Erreur: La chaîne d'ADN fournie est invalide.")
    
    return chaine

def count_sequence(sequence, chaine):
    sequence_range = len(sequence)
    for i in range(chaine, step=sequence_range):
        print(i)


def occurence_sequence(sequence, chaine):
    return chaine.count(sequence)

def pourcentage_sequence(sequence, chaine, occurence):
    return occurence * len(sequence) * 100 / len(chaine)

chaine_principale = saisie_adn("Veuillez saisir la chaîne d'ADN principale: ")
sequence_a_chercher = saisie_adn("Veuillez saisir la séquence d'ADN à chercher: ")
count_sequence(chaine_principale, sequence_a_chercher)

occurence = occurence_sequence(sequence_a_chercher, chaine_principale )
pourcentage = pourcentage_sequence(sequence_a_chercher, chaine_principale, occurence)

print(f"Il y a {round(pourcentage, 2)}% de {sequence_a_chercher} dans la chaine {chaine_principale} ")