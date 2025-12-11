import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
from datetime import datetime

# 1. Liste d'URLs à auditer
urls = [
    'https://www.example.com',
    'https://www.python.org'
]

# 2. Créer la base de données
conn = sqlite3.connect('audit_complet.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pages (
        url TEXT,
        titre TEXT,
        nb_h1 INTEGER,
        temps REAL,
        date TEXT
    )
''')

# 3. Auditer chaque page
for url in urls:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraire les données
    titre = soup.find('title')
    titre_text = titre.text if titre else 'Aucun'
    nb_h1 = len(soup.find_all('h1'))
    temps = response.elapsed.total_seconds()

    # Sauvegarder en base
    cursor.execute('''
        INSERT INTO pages VALUES (?, ?, ?, ?, ?)
    ''', (url, titre_text, nb_h1, temps, datetime.now().strftime('%Y-%m-%d')))

    print(f"{url} audité")

conn.commit()

# 4. Exporter vers Excel
df = pd.read_sql_query('SELECT * FROM pages', conn)
df.to_excel('rapport_final.xlsx', index=False)

print("\nRapport complet généré: rapport_final.xlsx")

conn.close()
