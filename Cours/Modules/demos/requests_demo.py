import requests

def verifier_urls(liste_urls):
    """
    Vérifie si des URLs sont accessibles et mesure leur temps de réponse
    """
    for url in liste_urls:
        try:
            response = requests.get(url, timeout=5)
            temps = response.elapsed.total_seconds()
            
            if response.status_code == 200:
                print(f"{url}")
                print(f"   Temps: {temps:.2f}s | Taille: {len(response.content)} octets\n")
            else:
                print(f"{url} - Code: {response.status_code}\n")
                
        except requests.exceptions.Timeout:
            print(f"{url} - Timeout (>5s)\n")
        except requests.exceptions.ConnectionError:
            print(f"{url} - Impossible de se connecter\n")

# Exemple d'utilisation
urls_a_tester = [
    "https://www.python.org",
    "https://www.example.com",
    "https://www.sitenonexistant123456.com"
]

verifier_urls(urls_a_tester)