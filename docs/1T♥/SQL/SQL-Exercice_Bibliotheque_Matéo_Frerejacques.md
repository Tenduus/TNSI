# Exercice classique : la blibliothèque 

### 1. Quelles sont les anomalies dans le schéma précédent ?

Les domaines n'ont pas été listés lors de la création de la table.

### 2. Clés et contraintes

#### a. 
```sql
ALTER TABLE Emprunt
ADD Emprunt_ID INT PRIMARY KEY;  
```
Ici, on ajoute une clé primaire pour la table Emprunt.

#### b. 
On ajoute ici une contrainte qui permet de vérifier si la date d'emprunt reste inférieur ou égale àla date de retout réel. Cela reverra un booléen. 

#### c. 

Dans cette requête, La contrainte de clé étrangère assure l'intégrité référentielle entre les tables `Emprunt` et `Abonne`. Cela signifie que chaque valeur de la colonne `Abonne_ID` dans la table `Emprunt` doit correspondre à une valeur existante dans la colonne `Abonne_ID` de la table "Abonne".

#### d. 

Ce serait une mauvaise idée car cela voudrait dire qu'il faut renseigner la date de retour réel dés l'emprunt.

### 3.

#### a. 

```sql 
SELECT * FROM Abonne Nom AND Prenom AND ville='Bayonne';
``` 

#### b. 

```sql 
SELECT * FROM Abonne Nom AND Prenom AND CodePostal='64%';
``` 

#### c. 

```sql 
SELECT * FROM Emprunt WHERE DateRetourReel > DateRetourPrevu AND Abonne_ID;
``` 