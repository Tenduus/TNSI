# Mémo pour l'apprentissage du _**SQL**_

### Notes :
 - Par convention il faut écrire les instructions en **majuscule**
 - Ne pas oublier le `;` à la fin d'une ligne d'instruction

### Créer des tables :

```sql
CREATE TABLE nom_de_la_table (id INTEGER PRIMARY KEY, nom TEXT, nom INTEGER);
```


### Insérer des données :

```sql
INSERT INTO nom_de_la_table VALUES (73, "exemple", 33);`
```

### Interroger les données :

#### Sélection :

- ```sql
    SELECT * FROM nom_de_la_table;
    ``` 
    Permet de tout sélectionner 

- ```sql
    SELECT * FROM nom_de_la_table nom > 20;
    ```
    Filtrer avec condition

- ```sql
    SELECT * FROM nom_de_la_table nom > 20 AND nom ="exemple";
    ```
    Filtrer avec condition multiple

#### Trier les données :

- ```sql
    SELECT * FROM nom_de_la_table WHERE nom > 21 ORDER BY age DESC;
    ``` 
    Permet de trier les données par orde croissant **`ASC`** et décroissant **`DESC`**

### Agréger les données :

- ```sql
    SELECT MAX(nom) FROM nom_de_la_table;
    ```
    Fonction d'agrégation avec les instructions :
    1. `MAX()` pour récupérer la valeur maximum d’une colonne sur un ensemble de ligne.
    2. `MIN()` pour récupérer la valeur minimum d'une colonne sur un ensemble de ligne.
    3. `SUM()` pour calculer la somme sur un ensemble d’enregistrement