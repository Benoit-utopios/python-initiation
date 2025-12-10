def soustraire(a, b):
    print(f"Je soustrais {a} et {b}")
    return(a-b)

result = soustraire(15, 4)
print("Résultat:", result)

def quelle_heure(heure: str = "12h00" ):
    print(heure)

quelle_heure()

def compter_lettre_a(sequence):
    count = 0
    for letter in sequence:
        if letter == "a":
            count += 1
    return count

print(compter_lettre_a("abba"))
print(compter_lettre_a("mixer"))