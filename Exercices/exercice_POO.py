# Exercice 1
class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages

    def afficher_infos(self):
        print(f"{self.titre} par {self.auteur} - {self.nb_pages} pages")

    def comparer_pages(self, autre_livre):
        if self.nb_pages > autre_livre.nb_pages:
            print(f"{self.titre} a plus de pages que {autre_livre.titre}")
        elif self.nb_pages < autre_livre.nb_pages:
            print(f"{self.titre} a moins de pages que {autre_livre.titre}")
        else:
            print(f"Les deux livres ont le même nombre de pages")


# Tests
livre1 = Livre("Le Petit Prince", "Saint-Exupéry", 96)
livre2 = Livre("1984", "Orwell", 328)
livre1.afficher_infos()
livre1.comparer_pages(livre2)


# Exercice 2

# Tests
# compte = CompteBancaire("Alice", 1000)
# compte.deposer(500)
# compte.retirer(200)
# compte.afficher_solde()