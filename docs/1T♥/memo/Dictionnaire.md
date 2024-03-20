# Dictionnaire

### 1. Créer un dictionnaire

```py
    nom_dico = {clé:val, clé:val}
```
Dans un dictionnaire chaque paire s'écrit sous la forme **clé:valeur**. Chaque clé doit être unqiue dans le dictionnaire. Elle peut être sous la forme d'une chaîne de caractère entre guillemets, une valeur numérique ou un tuple (une sorte de liste non modifiable).

### 2. Accéder aux éléments d'un dictionnaire

```py
    nom_dico[clé]
```

### 3. Tester l'existence d'un clé 

Il est facile de vérifier l'existence d'une clé dans un dictionnaire en écrivant une instruction conditionnelle **if** avec un opérateur **in**.

```py
    if clé in nom_dico:
        action
```

### 4. Ajouter une paire à un dictionnaire 

```py
    nom_dico[clé] = valeur
```
Si l'on écrit la même instruction, mais que la clé existe déjà dans le dictionnaire, la valeur que l'on spécifie remplacera l'ancienne. 

### 5. Enlever un élément d'un dictionnaire 

Il existe trois méthode pour enlever un élément dans un dictionnaire : **pop()**, **popitem()** et **del**

#### Suppression ciblée avec pop()

```py 
    nom_dico.pop(clé)