def calculatrice():
    """
    Calculatrice simple avec gestion d'erreurs
    """
    print("=== CALCULATRICE ===\n")

    try:
        # Saisie des nombres
        nombre1 = float(input("Premier nombre : "))
        nombre2 = float(input("Deuxième nombre : "))

        # Saisie de l'opération
        operation = input("Opération (+, -, *, /) : ")

        # Calcul selon l'opération
        if operation == '+':
            resultat = nombre1 + nombre2
        elif operation == '-':
            resultat = nombre1 - nombre2
        elif operation == '*':
            resultat = nombre1 * nombre2
        elif operation == '/':
            resultat = nombre1 / nombre2
        else:
            raise ValueError("Opération invalide ! Utilisez +, -, * ou /")

        # Affichage du résultat
        print(f"\nRésultat : {nombre1} {operation} {nombre2} = {resultat}")

    except ValueError as erreur:
        print(f"Erreur de saisie : {erreur}")
    except ZeroDivisionError:
        print("Erreur : Division par zéro impossible !")
    except Exception as erreur:
        print(f"Erreur inattendue : {erreur}")
    finally:
        print("\n--- Fin du calcul ---")

# Lancement
calculatrice()

def valider_email(email):
    """
    Valide un email selon plusieurs critères
    Lève une ValueError si l'email est invalide
    Retourne True si l'email est valide
    """
    # Suppression des espaces
    email = email.strip()

    # Vérification : email non vide
    if not email:
        raise ValueError("L'email ne peut pas être vide.")

    # Vérification : longueur minimale
    if len(email) < 6:
        raise ValueError("L'email doit contenir au moins 6 caractères.")

    # Vérification présence d'un seul @
    if email.count('@') != 1:
        raise ValueError("L'email doit contenir exactement un '@'.")

    # Vérification @ pas au début ou à la fin
    if email.startswith('@') or email.endswith('@'):
        raise ValueError("L'email ne peut pas commencer ou finir par '@'.")

    # Séparation avant et après @
    partie_avant, partie_apres = email.split('@')

    # Vérification parties non vides
    if not partie_avant or not partie_apres:
        raise ValueError("L'email doit avoir du texte avant et après '@'.")

    # Vérification présence d'un . après le @
    if '.' not in partie_apres:
        raise ValueError("L'email doit contenir un '.' après le '@'.")

    # Vérification . pas au début ou à la fin de la partie domaine
    if partie_apres.startswith('.') or partie_apres.endswith('.'):
        raise ValueError("Le domaine ne peut pas commencer ou finir par '.'.")

    # Toutes les vérifications passées
    return True

def demander_email():
    """
    Demande un email à l'utilisateur avec validation
    """
    print("=== VALIDATION D'EMAIL ===\n")

    while True:
        try:
            email = input("Entrez votre email : ")
            valider_email(email)
            return email  # Email valide, on sort de la boucle

        except ValueError as erreur:
            print(f"{erreur}")
            print("Veuillez réessayer.\n")

# Test
email = demander_email()
print(f"\nEmail enregistré : {email}")
