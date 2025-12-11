class PageWeb:
    """
    Classe représentant une page web avec ses métadonnées
    """

    def __init__(self, url, title, meta_description, h1, nombre_mots):
        self.url = url
        self.title = title
        self.meta_description = meta_description
        self.h1 = h1
        self.nombre_mots = nombre_mots
        

    def verifier_title(self):
        longueur= len(self.title)
        if 30 <= longueur <= 60:
            return "Titre optimal"
        elif longueur < 30:
            return "Titre trop court"
        else:
            return 'Titre trop long'
        

    def verifier_meta_description(self):
        longueur= len(self.meta_description)
        if 120 <= longueur <= 160:
            return "Titre optimal"
        elif longueur < 120:
            return "Titre trop court"
        else:
            return 'Titre trop long'

    def verifier_contenu(self):
        if self.nombre_mots >= 300:
            return "Contenu suffisant"
        else:
            return "minimum 300mots"

    def generer_rapport(self):
        rapport = {
            "URL": self.url,
            "Title": self.title,
            "Vérification Title": self.verifier_title(),
            "Meta Description": self.meta_description,
            "Vérification Meta Description": self.verifier_meta_description(),
            "Nombre de mots": self.nombre_mots,
            "Vérification Contenu": self.verifier_contenu()
        }
        return rapport
        

class ComparateurPages:
    """
    Classe utilitaire pour comparer plusieurs pages entre elles
    """

    def __init__(self):
        self.pages = []

    def ajouter_page(self, page):
        """
        Ajoute une page à la liste de comparaison
        """
        self.pages.append(page)

    def comparer(self):
        if not self.pages:
            return "Aucune page à comparer"
        
        rapport = f"RAPPORT COMPARATIF"
        for i, page in enumerate(self.pages, 1):
            score = self.calculer_score(page)
            rapport += f"\n{i}. {page.url}\n"
            rapport += f"   Score SEO: {score}\n"
            rapport += f"   Mots: {page.nombre_mots}\n"
        
        return rapport

    def calculer_score(self, page):
        score = 0
        if 30 <= len(page.title) <= 60:
            score += 1
        if 120 <= len(page.meta_description) <= 160:
            score += 1
        if page.nombre_mots >= 300:
            score += 1
        return score

# Création de pages d'exemple
page1 = PageWeb(
    url="https://example.com/seo-guide",
    title="Guide complet du SEO en 2024",
    meta_description="Découvrez notre guide complet du SEO avec toutes les techniques pour améliorer votre référencement naturel et augmenter votre visibilité.",
    h1="Le guide ultime du SEO",
    nombre_mots=450
)

page2 = PageWeb(
    url="https://example.com/python",
    title="Python",
    meta_description="Apprenez Python facilement",
    h1="Tutoriel Python",
    nombre_mots=200
)

page3 = PageWeb(
    url="https://example.com/web-scraping",
    title="Web Scraping avec Python - Tutoriel complet et pratique",
    meta_description="Maîtrisez le web scraping avec Python grâce à notre tutoriel détaillé. Découvrez BeautifulSoup, Requests et les bonnes pratiques pour extraire des données.",
    h1="Web Scraping avec Python",
    nombre_mots=550
)

page4 = PageWeb(
    url="https://example.com/data-science",
    title="Data Science",
    meta_description="Introduction à la Data Science",
    h1="Data Science pour débutants",
    nombre_mots=300
)

# Rapports individuels
print(page1.generer_rapport())
print(page2.generer_rapport())

# Comparaison
comparateur = ComparateurPages()
comparateur.ajouter_page(page1)
comparateur.ajouter_page(page2)
comparateur.ajouter_page(page3)

print(comparateur.comparer())



