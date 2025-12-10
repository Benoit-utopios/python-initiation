def division_securisee(a, b):
    """
    Divise a par b en gérant les erreurs
    """
    try:
        resultat = a / b
    except ZeroDivisionError:
        print("Division par zéro impossible !")
        return None
    except TypeError:
        print("Les valeurs doivent être des nombres !")
        return None
    else:
        return resultat
    finally:
        print("--- Opération terminée ---")

# Tests
print(division_securisee(10, 2))      # 5.0
print(division_securisee(10, 0))      # None
print(division_securisee(10, "a"))    # None


def demander_nombre():
    """
    Demande un nombre à l'utilisateur jusqu'à ce qu'il soit valide
    """
    while True:
        try:
            nombre = int(input("Entrez un nombre entier : "))
            return nombre  # Sort de la boucle si succès
        except ValueError:
            print("Erreur ! Veuillez entrer un nombre entier valide.")

# Utilisation
nombre_valide = demander_nombre()
print(f"Vous avez entré : {nombre_valide}")
