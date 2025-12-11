import sqlite3
from datetime import datetime

# 1. Créer la base de données et la table
conn = sqlite3.connect('mes_positions.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS rankings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mot_cle TEXT,
        position INTEGER,
        url TEXT,
        date TEXT
    )
''')
conn.commit()

# 2. Ajouter des données
def enregistrer_position(mot_cle, position, url):
    """
    Sauvegarde une position pour un mot-clé
    """
    date_actuelle = datetime.now().strftime('%Y-%m-%d')
    
    cursor.execute('''
        INSERT INTO rankings (mot_cle, position, url, date)
        VALUES (?, ?, ?, ?)
    ''', (mot_cle, position, url, date_actuelle))
    
    conn.commit()
    print(f"Position enregistrée: '{mot_cle}' -> Position {position}")

# 3. Consulter les données
def afficher_historique(mot_cle):
    """
    Affiche l'évolution d'une position
    """
    cursor.execute('''
        SELECT date, position, url
        FROM rankings
        WHERE mot_cle = ?
        ORDER BY date DESC
    ''', (mot_cle,))
    
    resultats = cursor.fetchall()
    
    if resultats:
        print(f"\nHistorique pour '{mot_cle}':")
        for date, position, url in resultats:
            print(f"   {date}: Position {position}")
    else:
        print(f"Aucune donnée pour '{mot_cle}'")

# Exemple d'utilisation
enregistrer_position('formation python', 12, 'https://www.example.com/python')
enregistrer_position('apprendre python', 8, 'https://www.example.com/apprendre')
enregistrer_position('formation python', 10, 'https://www.example.com/python')

afficher_historique('formation python')

# Fermer la connexion
conn.close()