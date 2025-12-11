### Exercice: Gestion d'une bibliothèque

**Consigne :**
Créez une classe `Livre` avec les attributs titre, auteur et nombre de pages. Ajoutez des méthodes pour :

- Afficher les informations du livre
- Comparer si deux livres ont le même nombre de pages

### Exercice: Système bancaire simple

**Consigne :**
Créez une classe `CompteBancaire` permettant de :

- Créer un compte avec un solde initial
- Déposer de l'argent
- Retirer de l'argent (vérifier qu'il y a assez de fonds)
- Afficher le solde

---

## Projet - Analyseur de pages web

### Énoncé du projet

Créez un système d'analyse de pages web qui permet de :

1. Stocker les informations d'une page (URL, title, meta description, H1, nombre de mots)
2. Construisez plusieurs méthodes:
    - verifier_title(): Vérifie si le title respecte les bonnes pratiques
            (entre 30 et 60 caractères recommandé)
    - verifier_meta_description(): Vérifie si la meta description respecte les bonnes pratiques
            (entre 120 et 160 caractères recommandé)
    - verifier_contenu(): Vérifie si la page a suffisamment de contenu
            (minimum 300 mots recommandé)
    - generer_rapport(): Génère un rapport complet des fonctions précédentes
3. (Optionnel) Essayez de comparer plusieurs pages entre elles via une autre classe utilitaire