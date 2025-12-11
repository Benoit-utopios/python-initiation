## Exercice pratique - Manipulation de tuples

**Objectif** : Maîtriser les tuples et l'unpacking

**Consignes :**

1. Créez un tuple `etudiant` contenant : nom, prénom, âge, moyenne générale (ex: `("Dupont", "Jean", 20, 14.5)`)
2. Utilisez l'unpacking pour extraire chaque information dans des variables séparées et affichez une phrase descriptive.
3. Créez un tuple de 10 notes (entre 0 et 20) et :
    - Affichez les 3 dernières notes (indices -3, -2, -1)
    - Affichez une note sur deux
    - Comptez combien de fois la note 15 apparaît
4. Écrivez une fonction `calculer_statistiques(notes)` qui retourne un tuple contenant :
    - La note minimale
    - La note maximale
    - La moyenne
    
    Testez avec : `(12, 15, 8, 18, 14, 11, 16, 9, 17, 13)`
    
5. Utilisez l'unpacking pour récupérer directement les statistiques et les afficher.