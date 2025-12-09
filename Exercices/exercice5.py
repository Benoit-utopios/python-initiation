# # Version 1
# age = int(input("Saisir age: "))
# salaire = int(input("Saisir salaire: "))
# experience = int(input("Saisir experience: "))

# if age <= 29:
#     print("trop jeune")
# elif salaire > 40000:
#     print("Salaire demandé trop élevé")
# elif experience < 5:
#     print("pas assez d'expérience")
# else:
#     print("OK")

# del age
# del salaire
# del experience

# # Version 2
# age = None
# salaire = None
# experience = None

# age = int(input("Quel est votre âge ?: "))
# if age < 30:
#     print("Vous n'êtes pas éligible au poste. Age minimum: 30")
# else:
#     salaire = float(input("Quel est votre prétention salariale ?: "))
#     if salaire > 40000:
#         print("Vous n'êtes pas éligible au poste.")
#     else:
#         experience = int(input("Combien d'années d'expérience avez vous ?"))
#         if experience < 5:
#             print("Vous n'êtes pas éligible au poste")
#         else:
#             print("Félicitations, vous êtes éligible !")

# Version 3
age = int(input("Veuillez entrer votre âge : \n"))
if age < 30 :
    print("Vous n'avez pas l'âge requis pour cette candidature.")
    exit()
salaire = int(input("Salaire demandé \n"))
if salaire > 40000 :
    pass
experience = int(input("Combien d'années d'expérience avez-vous ? \n"))
if experience < 5 :
    print("Vous n'avez pas l'expérience requise pour cette candidature.")
    exit()
print("Vous avez tous les critères pour être embauché(e).")








