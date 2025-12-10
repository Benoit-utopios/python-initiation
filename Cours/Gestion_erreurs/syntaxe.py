# Structure d'une base: try / except

try:
    # Code susceptible de provoquer une erreur
    10 / 0
except:
    # Code exécuté en cas d'erreur
    print("Une erreur s'est produite")

# Capture d'une erreur spécifique
try:
    nombre = int(input("Entrez un nombre: "))
except ValueError:
    # Code exécuté en cas d'erreur
    print("Ce n'est pas un nombre valide !")
except ZeroDivisionError:
    print("Division par zéro impossible !")

# Structure complète : try/except/else/finally
try:
    nombre = int(input("Entrez un nombre: "))
    resultat = 100 / nombre
except ValueError:
    # Code exécuté en cas d'erreur
    print("Ce n'est pas un nombre valide !")
except ZeroDivisionError:
    print("Division par zéro impossible !")
else:
    # Execute SI aucune erreur n'est survenue
    print(f"Résultat: {resultat}")
finally:
    # TOUJOURS exécuté (erreur ou pas)
    print("--- Fin du calcul ---")

# Récupérer le message d'erreur
try:
    nombre = int(input("Entrez un nombre: "))
except ValueError as erreur:
    # Code exécuté en cas d'erreur
    print(f"Erreur détectée: {erreur}")

# Lever une erreur
age = int(input("Entrez votre âge: "))

if age < 0:
    raise ValueError("L'âge ne peut pas être négatif")
if age > 150:
    raise ValueError("L'âge semble irréaliste")

print(f"{age}")