# Concaténation
str1 = "chaine 1"
str2 = "chaine 2"
str3 = "str1: " + str1 + ", str2: " + str2
print(str1)
print(str2)
print(str3)

# équivalents
print(str1 + " " + str2)
print(str1, str2)

# Concaténation avec un entier (int)
mon_entier = 12
ma_chaine1 = "J'ai "
ma_chaine2 = " ans"
print(ma_chaine1 + str(mon_entier) + ma_chaine2)

# Chaines formatées
# .format
prenom_enfant = "Titouan"
ma_chaine_formatee = "J'ai {0} ans et je m'appelle {1} (age = {0})".format(mon_entier, prenom_enfant)
print(ma_chaine_formatee)
ma_chaine_formatee2 = f"J'ai {mon_entier} ans et je m'appelle {prenom_enfant} (age = {mon_entier})"
print (ma_chaine_formatee2)

chaine = 'Citation: "Regarde!"'
chaine = 'L\'élève dit: "Regarde"'

# Découpage de chaînes
#         01234567
chaine = "abcdefgh"

# Récupérer un seul caractère avec son indice(index)
print(chaine)
print(chaine[7])
print(chaine[0])
print(chaine[2] + chaine[6])

# Découper une chaine avec un début et une fin
print(chaine[0:4])
print(chaine[:4])
print(chaine[2:4] + chaine[6:])
print(chaine[:])

# Découper avec un pas
print(chaine[::3])

# Découper avec des négatifs
print(chaine[-3:])