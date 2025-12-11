import pandas as pd

# Créer des données d'audit
donnees_audit = [
    {'URL': 'https://example.com/page1', 'Titre': 'Page 1', 'H1': 1, 'Temps': 1.2, 'Status': 200},
    {'URL': 'https://example.com/page2', 'Titre': 'Page 2', 'H1': 0, 'Temps': 2.5, 'Status': 200},
    {'URL': 'https://example.com/page3', 'Titre': 'Page 3', 'H1': 2, 'Temps': 0.8, 'Status': 404},
]

# Créer un DataFrame
df = pd.DataFrame(donnees_audit)
# Afficher les données
print("Données d'audit:")
print(df)

# Identifier les problèmes
print("\nPages avec problèmes:")
problemes = df[(df['H1'] != 1) | (df['Status'] != 200) | (df['Temps'] > 2)]
print(problemes[['URL', 'H1', 'Temps', 'Status']])

# Statistiques rapides
print(f"\nStatistiques:")
print(f"Temps de chargement moyen: {df['Temps'].mean():.2f}s")
print(f"Pages avec erreurs: {len(df[df['Status'] != 200])}")

# Exporter en Excel
df.to_excel('audit_seo.xlsx', index=False, sheet_name='Audit')
print("\nRapport exporté vers 'audit_seo.xlsx'")

# Exporter en CSV
df.to_csv('audit_seo.csv', index=False, encoding='utf-8-sig')
print("Rapport exporté vers 'audit_seo.csv'")