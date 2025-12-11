# Les modules

Les modules sont un mécanisme pour organiser et réutiliser du code. Ils permettent de structurer vos programmes en unités logiques et de partager du code entre différents projets.

## Qu'est ce qu'un module ?

Un module est un fichier .py contenant des définitions et des instructions. Il peut contenir des fonctions, des classes, des variables, du code exécutable.

## Qu'est ce qu'un package ?

Un package est une collection de modules organisés dans un répertoire. Il doit contenir un fichier spécial nommé `__init__.py`

---

## **Requests - Requêtes HTTP en Python**

Requests permet de récupérer le contenu de pages web en quelques lignes. C'est la première étape avant d'analyser ces pages avec BeautifulSoup.

### **Installation**

```python
pip install requests

```

### **Principales méthodes de Requests**

| Méthode/Attribut | Description | Exemple |
| --- | --- | --- |
| `requests.get(url)` | Effectue une requête GET (récupérer des données) | `response = requests.get('https://example.com')` |
| `requests.post(url, data)` | Effectue une requête POST (envoyer des données) | `requests.post('https://api.com', data={'key': 'value'})` |
| `response.status_code` | Code de statut HTTP (200, 404, 500...) | `if response.status_code == 200:` |
| `response.text` | Contenu de la réponse en texte | `html = response.text` |
| `response.content` | Contenu de la réponse en bytes | `taille = len(response.content)` |
| `response.json()` | Parse la réponse JSON en dictionnaire Python | `data = response.json()` |
| `response.headers` | Headers HTTP de la réponse | `content_type = response.headers['Content-Type']` |
| `response.elapsed` | Temps écoulé pour la requête | `temps = response.elapsed.total_seconds()` |
| `timeout=X` | Limite de temps pour la requête (en secondes) | `requests.get(url, timeout=5)` |
| `headers={...}` | Personnaliser les headers de la requête | `requests.get(url, headers={'User-Agent': 'Bot'})` |
| `params={...}` | Ajouter des paramètres à l'URL | `requests.get(url, params={'page': 1, 'limit': 10})` |

---

## **SQLite - Stocker vos données**

SQLite permet de sauvegarder vos données dans un fichier pour les réutiliser plus tard. Idéal pour stocker l'historique de vos audits SEO.

### **Pas d'installation** (inclus dans Python)

```python
import sqlite3

```

### **Principales méthodes de SQLite**

| Méthode | Description | Exemple |
| --- | --- | --- |
| `sqlite3.connect(fichier)` | Crée/ouvre une base de données | `conn = sqlite3.connect('ma_base.db')` |
| `conn.cursor()` | Crée un curseur pour exécuter des requêtes | `cursor = conn.cursor()` |
| `cursor.execute(sql, params)` | Exécute une requête SQL | `cursor.execute('SELECT * FROM table WHERE id = ?', (5,))` |
| `cursor.executemany(sql, liste)` | Exécute une requête pour plusieurs enregistrements | `cursor.executemany('INSERT INTO t VALUES (?)', [(1,), (2,)])` |
| `cursor.fetchone()` | Récupère le premier résultat | `ligne = cursor.fetchone()` |
| `cursor.fetchall()` | Récupère tous les résultats | `lignes = cursor.fetchall()` |
| `cursor.fetchmany(n)` | Récupère n résultats | `lignes = cursor.fetchmany(10)` |
| `conn.commit()` | Sauvegarde les modifications | `conn.commit()` |
| `conn.rollback()` | Annule les modifications non validées | `conn.rollback()` |
| `conn.close()` | Ferme la connexion à la base | `conn.close()` |
| `CREATE TABLE` | Crée une nouvelle table | `CREATE TABLE users (id INTEGER, name TEXT)` |
| `INSERT INTO` | Ajoute des données | `INSERT INTO users VALUES (1, 'Alice')` |
| `SELECT` | Récupère des données | `SELECT * FROM users WHERE age > 18` |
| `UPDATE` | Modifie des données | `UPDATE users SET name = 'Bob' WHERE id = 1` |
| `DELETE` | Supprime des données | `DELETE FROM users WHERE id = 1` |

Utiliser `?` pour sécuriser les requêtes et `commit()` pour sauvegarder

---

## **BeautifulSoup - Extraire des données HTML**

### **Installation**

```python
pip install beautifulsoup4

```

### **Principales méthodes de BeautifulSoup**

| Méthode | Description | Exemple |
| --- | --- | --- |
| `BeautifulSoup(html, 'html.parser')` | Parse un document HTML | `soup = BeautifulSoup(response.content, 'html.parser')` |
| `soup.find(tag)` | Trouve le premier élément correspondant | `titre = soup.find('title')` |
| `soup.find(tag, attrs={})` | Trouve un élément avec des attributs spécifiques | `meta = soup.find('meta', {'name': 'description'})` |
| `soup.find_all(tag)` | Trouve tous les éléments correspondants | `tous_liens = soup.find_all('a')` |
| `soup.find_all(tag, limit=n)` | Trouve les n premiers éléments | `premiers_h2 = soup.find_all('h2', limit=5)` |
| `element.text` | Récupère le texte d'un élément | `texte = titre.text` |
| `element.get_text()` | Récupère le texte avec options de formatage | `texte = element.get_text(strip=True)` |
| `element.get(attr)` | Récupère la valeur d'un attribut | `href = lien.get('href')` |
| `element['attr']` | Accès direct à un attribut (lève erreur si absent) | `href = lien['href']` |
| `soup.select(selector)` | Sélection CSS | `images = soup.select('img.thumbnail')` |
| `soup.select_one(selector)` | Premier élément par sélection CSS | `premier = soup.select_one('div.container')` |
| `element.find_parent(tag)` | Trouve l'élément parent | `parent = element.find_parent('div')` |
| `element.find_next_sibling()` | Trouve l'élément frère suivant | `suivant = element.find_next_sibling()` |
| `element.contents` | Liste des enfants directs | `enfants = div.contents` |
| `element.stripped_strings` | Itérateur sur les textes (sans espaces) | `for texte in div.stripped_strings:` |
- `BeautifulSoup()` pour parser le HTML
- `find()` pour trouver un élément unique
- `find_all()` pour trouver tous les éléments
- `.text` pour obtenir le contenu textuel
- `.get()` pour obtenir un attribut

---

## **Pandas - Exporter en Excel/CSV**

### **Installation**

```python
pip install pandas openpyxl

```

### **Principales méthodes de Pandas**

| Méthode | Description | Exemple |
| --- | --- | --- |
| `pd.DataFrame(data)` | Crée un DataFrame à partir de données | `df = pd.DataFrame([{'nom': 'Alice', 'age': 25}])` |
| `pd.read_csv(fichier)` | Lit un fichier CSV | `df = pd.read_csv('donnees.csv')` |
| `pd.read_excel(fichier)` | Lit un fichier Excel | `df = pd.read_excel('donnees.xlsx')` |
| `pd.read_sql_query(sql, conn)` | Lit depuis une base SQL | `df = pd.read_sql_query('SELECT * FROM t', conn)` |
| `df.head(n)` | Affiche les n premières lignes (défaut: 5) | `df.head(10)` |
| `df.tail(n)` | Affiche les n dernières lignes | `df.tail(3)` |
| `df.info()` | Informations sur le DataFrame | `df.info()` |
| `df.describe()` | Statistiques descriptives | `df.describe()` |
| `df['colonne']` | Accède à une colonne | `ages = df['age']` |
| `df[['col1', 'col2']]` | Sélectionne plusieurs colonnes | `sous_df = df[['nom', 'age']]` |
| `df[condition]` | Filtre les lignes selon une condition | `adultes = df[df['age'] >= 18]` |
| `df.loc[lignes, colonnes]` | Sélection par labels | `df.loc[0:5, ['nom', 'age']]` |
| `df.iloc[lignes, colonnes]` | Sélection par positions | `df.iloc[0:5, 0:2]` |
| `df.sort_values(col)` | Trie par colonne | `df.sort_values('age', ascending=False)` |
| `df.groupby(col)` | Groupe les données | `df.groupby('ville').mean()` |
| `df['col'].mean()` | Calcule la moyenne | `age_moyen = df['age'].mean()` |
| `df['col'].sum()` | Calcule la somme | `total = df['ventes'].sum()` |
| `df['col'].min()` / `.max()` | Valeurs min/max | `age_min = df['age'].min()` |
| `df['col'].count()` | Compte les valeurs non-nulles | `nb_valeurs = df['nom'].count()` |
| `df.to_excel(fichier)` | Exporte en Excel | `df.to_excel('rapport.xlsx', index=False)` |
| `df.to_csv(fichier)` | Exporte en CSV | `df.to_csv('donnees.csv', index=False)` |
| `len(df)` | Nombre de lignes | `nb_lignes = len(df)` |
| `df.dropna()` | Supprime les lignes avec valeurs manquantes | `df_propre = df.dropna()` |
| `df.fillna(valeur)` | Remplace les valeurs manquantes | `df.fillna(0)` |

---