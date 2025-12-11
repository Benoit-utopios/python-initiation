import requests
from bs4 import BeautifulSoup

def analyser_page(url):
    """
    Extrait le titre et les principaux éléments SEO d'une page
    """
    # Récupérer la page
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extraire le titre
    titre = soup.find('title')
    print(f"📄 Titre: {titre.text if titre else 'Aucun titre'}")
    
    # Extraire la meta description
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc:
        print(f"Description: {meta_desc.get('content', 'Vide')}")
    
    # Compter les H1
    h1_tags = soup.find_all('h1')
    print(f"\nNombre de H1: {len(h1_tags)}")
    for h1 in h1_tags:
        print(f"   - {h1.text.strip()}")
    
    # Compter les liens
    tous_liens = soup.find_all('a', href=True)
    print(f"\nNombre total de liens: {len(tous_liens)}")
    
    # Afficher les 5 premiers liens
    print("\n   Exemples de liens:")
    for lien in tous_liens[:5]:
        print(f"   - {lien.get('href')}")

# Exemple d'utilisation
analyser_page('https://www.python.org')